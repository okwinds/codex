# TUI：Custom Prompts（/prompts:…）与参数展开（Prompt Args）

本章描述 TUI 侧“自定义 prompts”的解析、补全与展开规则。目标是让复刻实现能够：
- 在输入框中以 `/prompts:<name> ...` 形式调用保存的 prompt；
- 在提交时将 prompt 模板展开成最终文本；
- 在展开过程中**保持 TextElement（附件占位符等）的 byte range 语义**；
- 在 slash popup 中对 prompts 做补全/选择，并支持 numeric-style 的“自动提交”。

> 注：这里的 “custom prompts” 来自协议层 `CustomPrompt`（name/path/content/description/argument_hint），通常由 core/CLI 从本地 prompts 目录加载并下发到 UI。UI 仅负责使用它们，不负责持久化格式本身。

---

## 1. 基本概念与命令形状

### 1.1 命令前缀
- 常量：`PROMPTS_CMD_PREFIX`（当前为 `"prompts"`）
- 自定义 prompt 的调用必须以 **带冒号的前缀**：`/prompts:<prompt_name>`
  - 例如：`/prompts:review`、`/prompts:my-prompt USER=Alice`
  - 不带冒号的 `/prompts ...` 不属于 custom prompt 调用（UI 侧不会把它当作 custom prompt 展开）。

### 1.2 prompt 模板中的两类占位符
1) **命名占位符（named placeholders）**  
   - 形如：`$USER`、`$BRANCH`  
   - 正则：`$[A-Z][A-Z0-9_]*`  
   - 特殊 token：`$ARGUMENTS` 不属于命名占位符集合（见 4.2）。
2) **数字占位符（numeric placeholders）**  
   - `$1..$9`（最多 9 个）  
   - `$ARGUMENTS`（把 positional args 以空格连接）  

### 1.3 “转义”规则（$$…）
如果占位符前面紧挨着一个 `$`（即模板里出现 `$$USER`），则该 `$USER` 被视为字面量，不参与替换：
- `prompt_argument_names("literal $$USER") == []`
- 展开时 `$$USER` 保持原样（不会变成 `$` + 替换值）。

---

## 2. `/name <rest>` 解析（parse_slash_name）

### 2.1 输入与输出
输入：一行字符串 `line`。  
输出：`Option<(name, rest_after_name, rest_offset)>`，其中：
- `name`：`/` 后直到遇到空白为止的 token（允许包含 `:` 等字符，但后续规则会限制）。
- `rest_after_name`：name 之后的剩余内容，做 `trim_start()` 后的结果。
- `rest_offset`：`rest_after_name` 在原 `line` 中的 UTF-8 byte 起始偏移（保证 `line[rest_offset..] == rest_after_name`）。

### 2.2 算法（需等价）
1) 若 `line` 不以 `/` 开头 → None  
2) `stripped = line[1..]`  
3) 在 `stripped` 中找到第一个 whitespace 的位置作为 `name_end`；若不存在则 `name_end = stripped.len()`  
4) `name = stripped[..name_end]`；若 `name` 为空 → None  
5) `rest_untrimmed = stripped[name_end..]`  
6) `rest = rest_untrimmed.trim_start()`  
7) `rest_offset = 1 + name_end + (rest_untrimmed.len() - rest.len())`  

---

## 3. 解析参数：shlex + TextElement 保真（parse_tokens_with_elements）

### 3.1 目标
prompt args 解析使用 shlex 语义（支持双引号包裹包含空格的值），但 composer 的 `TextElement`（例如 `[Image #1]`）可能包含空格，不能被 shlex 拆成多个 token。

因此必须在 tokenize 前把 element ranges 替换为“不会被拆分的 sentinel”，tokenize 后再把 sentinel 还原并重建 element byte ranges（相对 token）。

### 3.2 sentinel 替换（replace_text_elements_with_sentinels）
输入：
- `rest: &str`（要 token 化的文本片段）
- `elements: &[TextElement]`（其 byte ranges 相对 rest）

输出：
- `rest_for_shlex: String`
- `replacements: Vec<ElementReplacement { sentinel, text, placeholder }>`

规则：
1) elements 按 start 排序
2) 逐个 element：
   - 生成 sentinel：`__CODEX_ELEM_{idx}__`，若 rest 中已包含该子串则不断追加 `_` 直到不冲突
   - 将 `[start,end)` 替换为 sentinel
   - 记录 replacement：
     - `text = rest[start..end]`
     - `placeholder = elem.placeholder(rest)`（如果存在）
3) 拼接形成 `rest_for_shlex`

### 3.3 token 还原（apply_replacements_to_token）
shlex 输出 token 字符串后，必须按 replacement 集合做以下处理：
- 扫描 token 内最早出现的 sentinel（可能多个），以“从左到右、每次取最早 sentinel”的方式替换
- 对每个被替换的 sentinel：
  - 把 replacement.text 插入到输出 out
  - 并在 out 的相应区间建立一个 `TextElement(ByteRange{start,end}, placeholder)`
    - start/end 是相对“该 token 的输出字符串 out”的 byte offset
    - placeholder 为 replacement.placeholder

> 结果：`PromptArg { text: token_text, text_elements: Vec<TextElement> }`，其中元素范围相对 token。

---

## 4. 两种参数模式

### 4.1 命名参数（key=value）
当模板包含命名占位符（`prompt_argument_names(content)` 非空）时，调用必须提供 `key=value` 形式的输入。

解析函数：`parse_prompt_inputs(rest, text_elements_relative_to_rest) -> Result<HashMap<String, PromptArg>, PromptArgsError>`

规则：
- `rest` 为空/全空白：返回空 map
- 使用 3.1 的 shlex + elements sentinel tokenization 得到 token 列表
- 每个 token 必须包含 `'='`：
  - 否则错误：`MissingAssignment { token }`
- `key` 不能为空：
  - 否则错误：`MissingKey { token }`
- token 为 `key=value`：必须把 token 中 element byte ranges 映射到 value-only 坐标：
  - `value_start = len("key=")`  
  - 对 token.text_elements：将每个 element range 左移 `value_start`（小于等于 offset 的元素被丢弃）
  - 得到 `PromptArg { text: value, text_elements: value_elements }`

错误文案（必须等价，便于复刻 UI 提示）：
- MissingAssignment：提示“expected key=value … quote values with spaces”
- MissingKey：提示“expected a name before '=' …”

### 4.2 数字参数（positional）
当模板不包含命名占位符时（`prompt_argument_names(content)` 为空），UI 会把 rest 视为 positional args（仍用 shlex，支持 quoted tokens），并支持：
- `$1..$9`：分别替换为 args[0..8]（不存在则替换为空）
- `$ARGUMENTS`：把所有 args 以单空格连接

positional args 解析入口：
- `parse_positional_args(rest, text_elements_relative_to_rest) -> Vec<PromptArg>`

`$ARGUMENTS` 的元素保真规则：
- 连接时在 args 之间插入一个 `' '` 字符
- 每个 arg 的 `text_elements` 需要按 out 当前长度做 offset 平移

---

## 5. prompt 展开（expand_custom_prompt）

### 5.1 入口语义
`expand_custom_prompt(text, text_elements_relative_to_text, custom_prompts) -> Result<Option<PromptExpansion>, PromptExpansionError>`

返回：
- `Ok(None)`：不是 `/prompts:` 形式，或 prompt name 不存在（保持原文不变）
- `Ok(Some(PromptExpansion{text, text_elements}))`：成功展开
- `Err(PromptExpansionError::...)`：需要对用户输出错误消息，并**不消耗草稿**（由 composer 负责恢复草稿，见 `TUI_COMPOSER.md` 9.3）

### 5.2 仅处理 `/prompts:<name>`
1) `parse_slash_name(text)`，若失败 → Ok(None)
2) `name` 必须以 `format!("{PROMPTS_CMD_PREFIX}:")` 开头；否则 Ok(None)
3) `prompt_name = name 去掉 "prompts:" 前缀`
4) 在 `custom_prompts` 中查找 `p.name == prompt_name`：
   - 不存在 → Ok(None)

### 5.3 rest 的 elements 截取与 shift
`text_elements` 是相对 full text 的；但 args 解析只关心 rest 部分，因此需：
- 对每个 element：左移 `rest_offset`
- 截断到 `rest` 长度（start/end 不能越界）
- 丢弃空区间
得到 `local_elements`（相对 rest）

### 5.4 命名占位符分支
若 `required = prompt_argument_names(prompt.content)` 非空：
1) `inputs = parse_prompt_inputs(rest, local_elements)`；错误映射为 `PromptExpansionError::Args { command: "/{name}", error }`
2) `missing = required - inputs.keys()`；若非空 → `PromptExpansionError::MissingArgs { command:"/{name}", missing }`
3) 执行替换：`expand_named_placeholders_with_elements(prompt.content, inputs)`
   - 对每个 `$KEY`（遵循 $$ 逃逸规则）：
     - 若 inputs 含 KEY：把 arg.text 拼接到 out，并把 arg.text_elements 平移到 out 的对应区间
     - 否则：保持 `$KEY` 字面量
4) 返回 `PromptExpansion`

### 5.5 numeric/positional 分支
否则（无命名占位符）：
1) `pos_args = parse_positional_args(rest, local_elements)`
2) 返回 `expand_numeric_placeholders(prompt.content, pos_args)`

`expand_numeric_placeholders` 规则：
- 扫描模板字符串中每个 `$`：
  - `$$` → 输出字面量 `"$$"`，前进 2
  - `$[1-9]` → 若 args[idx] 存在则插入该 arg（含 elements），前进 2
  - `$ARGUMENTS` → 若 args 非空则插入 join 结果，前进 `1 + len("ARGUMENTS")`
  - 其它 `$` → 输出单个 `$`（不展开），前进 1

---

## 6. numeric-style prompt 的“自动提交”与补全文本生成

### 6.1 判断模板是否包含 numeric placeholders
`prompt_has_numeric_placeholders(content)`：
- 只要包含 `$ARGUMENTS` 或出现任意 `$1..$9` 即为 true

### 6.2 从第一行提取 positional args（extract_positional_args_for_prompt_line）
输入：
- `line`：第一行（可能有前导空白）
- `prompt_name`
- `text_elements`：相对整个 line 的 elements

规则：
1) `trimmed = line.trim_start()`；`trim_offset = line.len() - trimmed.len()`
2) `parse_slash_name(trimmed)`；要求 name 形如 `prompts:<prompt_name>`（必须带冒号前缀）
3) `args_str = rest.trim_start().trim_end()`；为空则返回空 vec
4) `args_offset = trim_offset + rest_offset + (rest.len() - rest_trimmed_start.len())`
5) 将 full-line elements 左移 `args_offset`，并截断到 `args_str` 长度，得到 local_elements
6) `parse_positional_args(args_str, local_elements)` 返回 args

### 6.3 auto-submit 展开（expand_if_numeric_with_positional_args）
返回 Some(expanded) 的条件（必须全部满足）：
- 模板没有命名占位符（`prompt_argument_names(content)` 为空）
- 模板包含 numeric placeholders（6.1）
- 第一行确实提供了 positional args（6.2 得到 args 非空）

输出：
- `expand_numeric_placeholders(content, args)`

### 6.4 补全文本生成（prompt_command_with_arg_placeholders）
当用户在 slash popup 中选中一个 prompt，需要生成可编辑的“调用命令文本”：

- 若 prompt 有命名 args：生成
  - `/{PROMPTS_CMD_PREFIX}:{name} ARG1=\"\" ARG2=\"\" ...`
  - cursor 定位在第一个 `""` 内（即最后一个双引号之前一位）
- 若 prompt 只有 numeric placeholders：生成 `/{PROMPTS_CMD_PREFIX}:{name} `（末尾带空格，便于继续输入 args）
- 若 prompt 无任何 placeholders：生成 `/{PROMPTS_CMD_PREFIX}:{name}`（无尾随空格）

---

## 7. 与 composer / popup 的集成点（必须一致）

### 7.1 提交时的展开位置
composer 的 `prepare_submission_text` 在完成 pending paste 展开与 trim 后（且 `slash_commands_enabled==true`）调用 `expand_custom_prompt`：
- 失败：向 history 插入 error cell，恢复草稿，抑制提交
- 成功：替换 text 与 elements，并在之后 `prune_attached_images_for_submission`

### 7.2 slash popup 的 Enter 自动提交（numeric prompt）
当 command popup 可见且用户按 Enter：
1) 先把 pending_pastes 展开（但不走 full `prepare_submission_text`）
2) 若第一行本身就是 `/prompts:<name> ...` 且该 prompt 是 numeric-style 且提供了 args：
   - 直接展开并立刻返回 `InputResult::Submitted{expanded}`
   - 剪枝 attachments（按 expanded text/elements）
   - 清空 pending_pastes 与 textarea
3) 否则按 selection 执行：
   - prompt 无 args：可直接 `Submitted{prompt.content}`
   - prompt 有 args：只插入补全文本（Insert 模式），等待用户继续输入

### 7.3 slash token element 的“已知命令”判定包含 prompts
composer 在 `is_known_slash_name(name)` 中把 `prompts:<prompt>` 视为已知 slash name：
- name 形如 `"prompts:<prompt_name>"`
- 且 `custom_prompts` 中存在同名 prompt
从而 `/prompts:xxx ` 也会被提升为 slash token element（见 `TUI_COMPOSER.md` 8）。

### 7.4 Command popup 的搜索规则包含两种风格
Command popup 会把每个 prompt 的“显示名”视作 `prompts:<name>`，并支持：
- 用户输入 `name` 也能匹配 `/prompts:name`（通过 `push_match` 同时比较 display 与 name）
- 用户输入 `prompts:name` 也能匹配

---

## 8. 来源（Source）
- prompt args 核心：`codex-rs/tui/src/bottom_pane/prompt_args.rs`
- command popup（展示与筛选）：`codex-rs/tui/src/bottom_pane/command_popup.rs`
- composer 提交集成：`codex-rs/tui/src/bottom_pane/chat_composer.rs`
- custom prompt 数据类型：`codex-rs/protocol/src/custom_prompts.rs`（定义 `CustomPrompt`、`PROMPTS_CMD_PREFIX`）

