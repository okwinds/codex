# TUI：Chat Composer（输入框/弹窗/粘贴/附件）

本章给出可复刻级（replication-grade）的 “Chat Composer” 规格：它是 TUI 底部输入框的状态机，负责编辑草稿文本、维护附件占位符（text elements）、弹出并驱动命令/文件/技能(mentions)弹窗、处理粘贴与 Windows 非 bracketed paste burst、并在提交/排队时做 prompt 展开与元素重映射。

> 目标：仅凭本文档即可实现一个等价的输入框组件（可以使用不同 TUI 框架/不同 textarea 实现），但必须保持**输入/附件/弹窗/提交语义**与**与 core 的交互事件**一致。

---

## 1. 职责边界（What/Why）

### 1.1 “composer”负责什么
1) 维护用户草稿：多行文本编辑、光标位置、历史 recall（↑/↓）。  
2) 管理“文本元素（TextElement）”：把附件占位符、slash token、large paste placeholder 作为原子元素插入文本（渲染为特殊样式、编辑时当作不可分割单元）。  
3) 管理“附件列表”：本地图片附件（路径 + placeholder 标签），并保证 placeholder 与附件顺序的一致性。  
4) popup 交互：  
   - `/` → slash command / custom prompt popup  
   - `@` → 文件路径搜索 popup  
   - `$` → skills / connectors mentions popup  
5) 在提交/排队时进行：  
   - large paste placeholder 展开  
   - trim 与 text element byte range 重基准（rebase）  
   - `/prompts:` 自定义 prompt 展开（含 args 解析）  
   - 提交前按 placeholder 剪枝附件（避免发送已失效 placeholder 的附件）  

### 1.2 composer 不负责什么
- 不直接调用模型、也不直接执行工具：它只产出 `InputResult`（Submitted/Queued/Command/CommandWithArgs/None）交给上层（`ChatWidget`/`BottomPane`）转换为 core `Submission` 或 slash command 的 UI 行为。
- 不负责“文件搜索”实现：它只通过 `AppEvent::StartFileSearch(query)` 发起搜索请求，异步结果由 `on_file_search_result` 注入并更新 popup。

---

## 2. 数据模型（State）

### 2.1 顶层状态结构（需等价实现）
`ChatComposer` 关键字段语义（并非逐字段复刻 Rust 布局，但必须复刻语义）：

- `textarea`: 文本缓冲 + cursor + text elements（元素区间/placeholder payload）。
- `textarea_state`: 渲染需要的内部状态（滚动/选择等）。
- `active_popup: ActivePopup`：当前显示的 popup（同一时间最多一个）。
  - `None | Command(CommandPopup) | File(FileSearchPopup) | Skill(SkillPopup)`
- `pending_pastes: Vec<(placeholder, full_text)>`：large paste 占位符到真实内容的映射（允许同一 placeholder 文本出现多次时，按出现顺序替换）。
- `large_paste_counters: HashMap<char_count, counter>`：为相同长度的 large paste 生成稳定的 `#2/#3` 后缀。
- `attached_images: Vec<AttachedImage{ placeholder, path }>`：本地图片附件；**不持久化到跨 session history**，仅本次 session local history 可回放。
  - 不变量：placeholder 始终规范为 `[Image #1]..[Image #N]`，与 vec 顺序一致（见 4.3/4.4）。
- `mention_paths: HashMap<name, canonical_path>`：对 `$skill` / `$connector` mention 的“隐藏映射”。用于恢复/回放时将 UI 插入文本（`$name`）解析回具体 skill path / app connector id（见 6.5）。
- `dismissed_file_popup_token: Option<String>`：用户按 `Esc` 主动关闭 file popup 时记录当前 token，防止立即自动重开。
- `dismissed_mention_popup_token: Option<String>`：同上，针对 `$` mentions popup。
- `current_file_query: Option<String>`：记录当前 file popup 对应 query（用于在离开 file token 时发空 query 清空/取消搜索）。
- `history: ChatComposerHistory`：↑/↓ 历史回放状态（见 7）。
- `paste_burst: PasteBurst` + `disable_paste_burst: bool`：非 bracketed paste burst 检测与缓冲（见 5）。
- `config: ChatComposerConfig`：复用场景的功能开关（见 3）。
- 运行上下文：  
  - `is_task_running: bool`（影响 slash command 可用性、Tab/Enter 的 queue/submit 行为）  
  - `input_enabled: bool`（临时只读，渲染 placeholder，禁用 popup）  
  - 其他 footer/提示相关状态（非复刻核心，可按本 repo 语义实现或简化，但不能破坏提交/弹窗语义）。

### 2.2 输出事件（Output）
composer 对上层输出 `InputResult`：
- `Submitted { text, text_elements }`
- `Queued { text, text_elements }`
- `Command(SlashCommand)`：无 args 的内置 slash command
- `CommandWithArgs(SlashCommand, args_text, args_text_elements)`：支持 inline args 的内置 slash command（如 `/review ...`）
- `None`

> 约束：任何 `text_elements` 的 `ByteRange` 都必须相对 `text` 字节偏移（UTF-8 byte offsets），并与 `TextArea` 的元素 payload 一致（见 4/8）。

---

## 3. 功能开关（ChatComposerConfig）

该输入框可被复用到其它 surface（如 request-user-input），因此提供三开关：

- `popups_enabled`：是否允许任何 popup（command/file/skill）出现。  
  - `false` 时 `sync_popups()` 强制 `ActivePopup::None`。
- `slash_commands_enabled`：是否解析并派发 `/...`。  
  - `false` 时：不显示 slash popup、不做 `/prompts:` 展开、不 dispatch slash command（包括 inline args）。
- `image_paste_enabled`：是否允许“粘贴文件路径→自动作为图片附件”。

默认值：三者均为 `true`。另有 `plain_text()` 预设：三者均为 `false`。

---

## 4. 文本元素（TextElement）与附件占位符

### 4.1 TextElement 语义
`TextElement` 是 `(byte_range, placeholder?)`：
- `byte_range`：元素在 `text` 中的 UTF-8 字节区间 `[start, end)`。
- `placeholder`：若该区间代表一个“原子占位符”，则 placeholder 通常等于该区间对应的文本（例如 `[Image #1]` / `[Pasted Content 1200 chars]` / `"/diff"` 的 `/diff` token element）。

TextArea 需要提供以下等价能力（可自行实现）：
- 插入普通文本（按 cursor）
- 插入元素 payload（作为原子 token）
- 将某个 range 标记为 element（用于 `/name` token 提升为 element）
- 删除 element range（按 byte range）
- 枚举 `text_elements()` 与 `element_payloads()`
- `replace_element_payload(old, new)`（用于图片 renumber）

### 4.2 large paste placeholder（大粘贴占位符）
当一次 paste 的字符数（Unicode `chars().count()`）超过阈值 `LARGE_PASTE_CHAR_THRESHOLD = 1000`：
1) 生成 placeholder：`[Pasted Content {char_count} chars]`  
2) 若同 char_count 发生第 N 次，生成：`[Pasted Content {char_count} chars] #{N}`（N 从 2 开始）  
3) 把 placeholder 作为 element 插入 textarea  
4) 把 `(placeholder, full_text)` push 到 `pending_pastes`

注意：
- `pending_pastes` 的替换必须按“同 placeholder 出现顺序”匹配（见 4.5）。
- 在任何“明确 paste 事件”后，需要清理 paste burst 的 Enter suppression（见 5.6）。

### 4.3 图片附件占位符（本地图片）
图片附件以 element 的形式插入文本，并在 `attached_images` 里存储 path：
- placeholder 文本固定由 `local_image_label_text(n)` 生成（协议层约定）：`[Image #n]`。
- `attach_image(path)` 行为：
  1) `n = attached_images.len() + 1`
  2) placeholder = `[Image #n]`
  3) `textarea.insert_element(placeholder)`
  4) `attached_images.push({placeholder, path})`

#### 4.3.1 删除图片占位符后的 renumber
当用户删除了某个图片 element（例如删除 `[Image #1]`），需要：
1) 从 `attached_images` 中移除对应 placeholder 的附件记录
2) 将剩余附件按 vec 顺序重新标号为 `[Image #1]..`  
3) 同步替换 textarea 中旧 placeholder → 新 placeholder（`replace_element_payload`）

此逻辑由：
- `reconcile_deleted_elements`（检测删除哪些 element payload）
- `relabel_attached_images_and_update_placeholders`（执行 renumber + 替换）

### 4.4 外部编辑器返回文本（apply_external_edit）
当上层使用外部编辑器替换草稿文本（如 Ctrl+G）时：
1) 清空 `pending_pastes`（避免 placeholder 与真实文本错配）。  
2) 仅保留那些 placeholder 在新文本中仍出现的图片附件记录，并按“出现次数”消费（同 placeholder 多次出现时只保留匹配次数）。  
3) 重新构建 textarea：扫描新文本中每个 placeholder 的出现位置，把 placeholder 作为 element 插入，其他部分作为普通文本插入。  
4) 对保留的 `attached_images` 执行 renumber（保证 `[Image #1]..` 连续）。  
5) cursor 放到末尾（新 text.len()）。

### 4.5 pending_pastes 的展开算法（expand_pending_pastes）
目的：提交/解析 prompt args 前，必须把 large paste placeholder 展开为真实全文，同时确保其它 element 的 byte ranges 与 rebuilt 文本对齐。

输入：
- `text: &str`（包含 placeholder 字面量）
- `elements: Vec<TextElement>`（相对 `text`）
- `pending_pastes: &[(placeholder, actual)]`

输出：
- `(rebuilt_text, rebuilt_elements)`

算法（必须等价）：
1) 将 `pending_pastes` 按 `placeholder` 分组为 `VecDeque<&str>`（同 placeholder 多次出现时按 FIFO pop）。
2) 将 `elements` 按 `byte_range.start` 排序。
3) 单趟扫描 elements：
   - 先把 `[cursor, elem.start)` 的普通文本 copy 到 rebuilt
   - 取出 elem 对应的 `elem_text = text[start..end]`
   - 若 elem 有 placeholder 且在 `pending_by_placeholder` 中有 replacement：
     - pop_front 得到 `actual`，把 `actual` 直接拼接到 rebuilt（并**丢弃该 element**，即不写入 rebuilt_elements）
   - 否则：
     - 将 elem_text 追加到 rebuilt，并在 rebuilt_elements 中 push 新 element（其 byte range 以 rebuilt 当前长度计算）
4) 追加末尾 `[cursor, text.len)` 普通文本

关键点：
- 只依赖 `elements` 定位 placeholder，而不是 `find` 字符串；这样能保证“元素原子性”下的稳定替换。
- 如果 `pending_pastes` 非空但 `elements` 为空，直接返回原文（本实现选择只在 elements 非空时展开；复刻时保持一致）。

### 4.6 element 删除与 `pending_pastes` / `attached_images` 的一致性
在 `handle_input_basic_with_time` 对 textarea 应用“非 char/enter 的输入”（例如 Backspace/Delete/剪切/替换）后：
- 如果曾经存在 `pending_pastes` 或 `attached_images`，需做一次 element payload 对比：
  - `elements_before = textarea.element_payloads()`
  - 输入后 `elements_after = textarea.element_payloads()`
  - removed = before - after
  - 对每个 removed：
    - `pending_pastes.retain(|(ph, _)| ph != removed)`
    - 若 `attached_images` 中存在该 placeholder，则 remove 并标记 removed_any_image=true
  - 若 removed_any_image，则执行 4.3.1 renumber

---

## 5. Paste（显式 paste + 非 bracketed paste burst）

### 5.1 显式 paste（handle_paste）
`handle_paste(pasted: String)` 是所有粘贴内容的唯一入口（包括 burst flush 触发的“伪 paste”）。

行为：
1) 规范化换行：`\r\n`→`\n`，`\r`→`\n`
2) `char_count = pasted.chars().count()`
3) 分支：
   - `char_count > 1000`：走 4.2 large paste placeholder
   - `char_count > 1` 且 `image_paste_enabled` 且 `handle_paste_image_path(pasted)` 返回 true：
     - 已 attach_image；再额外插入一个 trailing space `" "`（方便继续输入）
   - 否则：直接插入 pasted 文本
4) 清理 paste burst 的 enter suppression：`paste_burst.clear_after_explicit_paste()`
5) `sync_popups()`

### 5.2 粘贴路径自动识别为图片（handle_paste_image_path）
输入：原始 paste 字符串
1) 调用 `normalize_pasted_path`：  
   - 负责去掉引号/前后空白、Windows→WSL 路径转换等（见 `clipboard_paste` 模块）
2) 若无法解析为路径 → false
3) 调用 `image::image_dimensions(&path)`：
   - 成功：attach_image(path)，记录 format，返回 true
   - 失败：返回 false（保留为普通文本粘贴）

### 5.3 非 bracketed paste burst：集成点（composer 侧）
在一些终端/平台（尤其 Windows/crossterm），paste 可能表现为大量 `KeyCode::Char` + `KeyCode::Enter` 的高速序列。为避免：
- 粘贴中误触发快捷键 overlay（`?`）
- 粘贴中途 Enter 被当作 submit
- 先把首字符渲染出来又回滚导致闪烁（flicker）

composer 引入 `PasteBurst` 进行检测与缓冲。复刻关键点：

- 只有 “plain char”（无 Ctrl/Alt） 才进入 burst 判定；其它输入会 flush/clear burst 窗口。
- ASCII 与 non-ASCII 区分：  
  - ASCII：允许短暂 hold 第一个快字符以抑制 flicker  
  - non-ASCII：不 hold 第一个字符（避免 IME 输入感觉丢字），但允许“retro-capture”将已插入前缀抓回到 burst buffer

`PasteBurst` 自身的完整状态机、阈值与 flush/clear 契约见：
- `workdocjcl/spec/06_UI/TUI_PASTE_BURST.md`

### 5.4 `handle_input_basic_with_time` 的顺序约束
该函数是“最低层编辑路径”，所有会 mutate textarea 的 key 都最终走它（popup handler 中 `input => self.handle_input_basic(input)`）。

顺序要求（必须等价）：
1) 先 `handle_paste_burst_flush(now)`（若 due 则 flush 成 paste 或 typed char）
2) 若输入是 Enter 且 burst active，则把 Enter 追加为 `\n` 到 burst buffer（而不是提交/插入 textarea）
3) 若输入是 plain Char：
   - 无 Ctrl/Alt 且 burst 未禁用：
     - non-ASCII：走 `handle_non_ascii_char`（包含 retro-capture 逻辑）
     - ASCII：根据 `paste_burst.on_plain_char` 的 `CharDecision` 进入 buffer / hold / retro-capture / normal insert
4) 若输入不是 plain char（或含 Ctrl/Alt），在应用 textarea mutation 前必须：
   - `if let Some(pasted)=paste_burst.flush_before_modified_input(): handle_paste(pasted)`
   - 然后才能 `textarea.input(key)`
5) 对“非 Char/Enter”的输入（箭头/Backspace 等），在清理 burst window 前再次确保 buffer 不会卡住：
   - 因为 `clear_window_after_non_char()` 会清掉 timing，导致 buffer 无法超时 flush
6) mutation 后：做 4.6 reconcile_deleted_elements
7) 最后：按输入类型更新 burst window（Ctrl/Alt char 清 window；Enter 不清；其它键清 window）

### 5.5 slash context 下的特殊规则（避免命令不可预测）
当处于 slash context（满足任一）：
- `active_popup` 是 Command popup；或
- first line 以 `/` 开头（且 `slash_commands_enabled`）

则 burst 相关的 Enter suppression 要被禁用，以免影响 slash command dispatch 的确定性：
- 在 `handle_submission_with_time` 中：in_slash_context 时不把 Enter 作为 burst newline。
- 在 `handle_input_basic_with_time` 中：同样基于 `in_slash_context` 禁止 `newline_should_insert_instead_of_submit` 的替代插入逻辑。

### 5.6 禁用 paste burst（set_disable_paste_burst）
当从 enabled → disabled：
1) `flush_before_modified_input()` 若返回 Some(pasted) 则走 `handle_paste(pasted)`（保留用户输入与 placeholder 行为一致）
2) `clear_after_explicit_paste()` 清空 Enter suppression/timing，避免状态泄露

---

## 6. Popups：打开/关闭/优先级/交互

### 6.1 popup 总览
三种 popup，且任意时刻最多一个：
- Command popup：slash commands + custom prompts 列表（`ActivePopup::Command`）
- File popup：`@` 文件路径搜索（`ActivePopup::File`）
- Skill popup：`$` mentions（skills + connectors）（`ActivePopup::Skill`）

### 6.2 核心同步入口：`sync_popups()`
每次 `handle_key_event` 处理完一个 key，都必须调用 `sync_popups()`，以便：
- 依据最新 text/cursor 显示/隐藏弹窗
- 更新弹窗 filter/query
- 保证 slash command element（`/name` token element）始终与第一行对齐（见 8）

同步流程（顺序必须一致）：
1) `sync_slash_command_elements()`
2) 若 `popups_enabled == false`：`active_popup=None` 并返回
3) 计算 `file_token = current_at_token(textarea)`（见 6.4）
4) 若正在浏览历史（`history.should_handle_navigation(text,cursor)` 为 true）：
   - 如有 `current_file_query` 则发 `StartFileSearch("")` 并清空
   - `active_popup=None` 并返回（防止 popup 抢焦点）
5) 计算 `mention_token = current_mention_token()`（见 6.5；只有 mentions_enabled 才可能有）
6) `allow_command_popup = slash_commands_enabled && file_token.is_none && mention_token.is_none`
7) 调用 `sync_command_popup(allow_command_popup)`：
   - 若最终 `active_popup` 变为 Command，则：
     - 若 `current_file_query` 存在，发 `StartFileSearch("")` 并清空
     - 清空 dismissed tokens（file/mention）
     - return
8) 若 `mention_token` 存在：
   - 同样确保清空 file search
   - `sync_mention_popup(token)` 并 return
9) 否则清空 dismissed_mention_popup_token
10) 若 `file_token` 存在：`sync_file_search_popup(token)` 并 return
11) 否则：若仍有 `current_file_query`，发 `StartFileSearch("")` 并清空；清空 dismissed_file_popup_token；若当前 popup 是 File/Skill 则关闭。

### 6.3 Command popup（slash/custom prompt）
打开条件（满足全部）：
- `slash_commands_enabled == true`
- caret 在第一行 `/name` token 内（cursor <= first_line_end 且 `slash_command_under_cursor` 命中）
- `looks_like_slash_prefix(name, rest_after_name)` 为 true：
  - builtin prefix 命中，或
  - 对 custom prompt：`fuzzy_match("prompts:<prompt.name>", name)` 命中
- 当前光标不在 `@token` 内（`current_at_token` 为 None；用于优先 file popup）

交互（在 popup 可见时）：
- `Up`/`Ctrl+P`：move_up
- `Down`/`Ctrl+N`：move_down
- `Esc`：关闭 popup，不改动输入
- `Tab`：完成（completion）：
  - 内置命令：将第一行改成 `/{cmd} `（若已以该命令开头则不重写），cursor=末尾  
  - 特殊：若选择的是 `SlashCommand::Skills`，直接清空 textarea 并返回 `InputResult::Command(Skills)`  
  - 自定义 prompt：调用 `prompt_selection_action(mode=Completion)`（见 `TUI_PROMPTS.md`）
    - `Insert{text,cursor}`：直接 set_text_clearing_elements(text)，cursor=target
    - `Submit`：Completion 模式下不发生
- `Enter`：提交/插入（submit-mode 选择）：
  - 优先：若第一行匹配 numeric-style prompt 且提供 positional args，则不看当前 selection，直接展开并 `Submitted`（见 9.2）  
    - 注意：此路径也必须先 expand pending_pastes（但不会调用 `prepare_submission_text`）
    - 并执行 `prune_attached_images_for_submission`，清空 pending_pastes，清空 textarea
  - 否则：基于 selection：
    - Builtin：清空 textarea，返回 `InputResult::Command(cmd)`
    - UserPrompt：调用 `prompt_selection_action(mode=Submit)`：
      - `Submit{text, text_elements}`：prune attachments，清空 textarea，返回 `Submitted`
      - `Insert{text,cursor}`：仅插入文本（不提交）
  - 若无 selection：fallback 到 `handle_key_event_without_popup`（默认换行/提交逻辑）

### 6.4 File popup（`@` token）
触发：`current_at_token` 返回 Some(query)。注意 query **允许为空字符串**：当用户仅输入一个 `@`（token 为 `"@"`）且光标位于该 token 内时，`current_at_token` 会返回 `Some("")`，用于展示“空查询提示”而非直接关闭 popup。

同步行为：
- 若用户之前对同一 query 按 `Esc` 关闭过，则 `dismissed_file_popup_token == Some(query)` 时不重开。
- 发起搜索：`AppEvent::StartFileSearch(query_or_empty)`（query 为空时也会发空串）
- popup 状态：
  - query 为空：`set_empty_prompt()`，显示提示（not waiting）而不是 loading/no matches
  - query 非空：`set_query(query)` → `waiting=true`
  - 异步结果到达时：`on_file_search_result(query, matches)`（仅当当前 token 仍以 query 为前缀时才更新）

交互：
- Up/Down/Ctrl+P/Ctrl+N：移动 selection
- Esc：关闭 popup 且记录 `dismissed_file_popup_token=Some(current_token)`，避免立即重开
- Tab / Enter：
  - 若无 selection：关闭 popup
  - 若 selection 是图片（`.png/.jpg/.jpeg`）：
    - 尝试读取 dimensions；成功则**移除当前 `@token` 文本**（按 whitespace token 边界）并 attach_image(path)，随后插入 trailing space
    - 若读取失败则退化为“插入路径”
  - 非图片：插入路径（`insert_selected_path`）

插入路径规则（`insert_selected_path`）：
- 以 whitespace 为 token 边界，替换当前 token（无论 cursor 在 token 哪一侧）
- 若 path 含 whitespace 且不含双引号 `"`：插入时包裹双引号 `"path with space"`（为了 prompt args 的 shlex 解析把它当成单 token）
- 替换后**追加一个空格**，cursor 放在空格后
- 替换会 `set_text_clearing_elements`：即丢弃现存 elements（这是已知行为；复刻需一致）

### 6.5 Skill/Connector mentions popup（`$` token）
mentions 启用条件（`mentions_enabled`）：
- `skills` 列表存在且非空，或
- `connectors_enabled==true` 且 `connectors_snapshot.connectors` 存在且非空

token 解析：`current_mention_token()` 使用 `current_prefixed_token(prefix='$', allow_empty=true)`：
- lone `$` 会返回 `Some("")`，从而允许 popup 显示“提示/全量列表”。

mentions 列表构造（`mention_items`）：
- Skills：每个 skill 生成一条 `MentionItem`：
  - `display_name`: 优先 interface.display_name，否则 skill.name
  - `description`: interface.short_description 或 skill.short_description 或 skill.description（trim 后为空则 None）
  - `insert_text`: `format!("${skill_name}")`
  - `search_terms`: 若 display_name==skill.name 则 `[skill.name]`，否则 `[skill.name, display_name]`
  - `path`: `skill.path`（用于 record 到 mention_paths）
- Connectors：从 connectors snapshot 中筛 `is_accessible==true` 的 connector：
  - `display_name`: connectors::connector_display_label(connector)
  - `description`: `"Connected - <desc>"` 或 `"Connected"`（desc 来自 connector.description 非空）
  - `slug`: `codex_core::connectors::connector_mention_slug(connector)`
  - `insert_text`: `format!("${slug}")`
  - `search_terms`: `[display_name, connector.id, slug]`
  - `path`: `Some(format!("app://{connector_id}"))`（用于 record）

交互：
- Up/Down/Ctrl+P/Ctrl+N：移动 selection
- Esc：关闭并记录 dismissed token（避免立即重开）
- Tab / Enter：若有 selection，则插入 selected mention，并关闭 popup
  - 插入规则与 file 类似：替换当前 token，追加空格，cursor 后移；并 `set_text_clearing_elements` 丢弃 elements
  - 同时若 mention 有 path，则 `record_mention_path(insert_text, path)`：
    - 从 insert_text 解析 `$name`（只允许 `[A-Za-z0-9_-]+`），存入 `mention_paths[name]=path`

---

## 7. 历史（↑/↓）与与 popup 的互斥

composer 历史为两层合并：
- Persistent history：跨 session，**仅文本**（不含 elements/attachments）
- Local history：仅本 session，记录 `{text, text_elements, local_image_paths}`（可回放图片占位符与 path）

行为约束：
- 当 `history.should_handle_navigation(text,cursor)` 为 true（正在浏览历史）时：
  - `sync_popups` 必须关闭所有 popup，且停止 file search（发空 query）
  - 以避免 popup 抢焦点影响继续 Up/Down

此外，在 `set_text_content_with_mention_paths` 恢复本地历史时，必须：
- `textarea.set_text_with_elements(text, text_elements)`
- 只保留那些 placeholder 在 `text_elements` 中仍存在的 `local_image_paths`（按 `[Image #i]` 匹配）
- 同步 mention_paths（用于后续解析/回放）

---

## 8. Slash token element（`/name` 的“提升为元素”）

目的：当用户输入完成一个合法的 `/name `（后面跟空白）时，将 `/name` 这段范围标记为 element，使其：
- 渲染为独立样式
- 在编辑时以原子 token 处理（删除/移动时更稳定）

同步规则：
- 只作用于第一行
- 只在 `slash_commands_enabled==true` 时启用

算法（`sync_slash_command_elements`）：
1) 取第一行 `first_line`
2) 计算 `desired_range = slash_command_element_range(first_line)`：
   - `parse_slash_name(first_line)` 成功
   - name 不含 `/`
   - `/name` 后第一字符存在且是 whitespace（即用户输入了空格或其它空白，表示命令 token 完整）
   - `is_known_slash_name(name)` 为 true：builtin 或 custom prompt（`prompts:<name>`）
   - 返回 `Some(0..(1+name.len()))`
3) 遍历现有 `textarea.text_elements()` 中所有 placeholder 以 `/` 开头的 element：
   - 若其 range != desired_range，则认为 stale，删除
   - 若与 desired_range 匹配则标记 has_desired=true
4) 若 desired_range 存在且 has_desired=false，则 `textarea.add_element_range(desired_range)`

---

## 9. 提交/排队/命令派发（Enter/Tab）

### 9.1 `handle_key_event_without_popup`
当无 popup 时：
- `Ctrl+D` 且 textarea 为空：返回 `(None,false)`（让上层处理退出语义）
- `Up/Down/Ctrl+P/Ctrl+N`：若 history.should_handle_navigation 为 true 则进入 history recall；否则当作普通输入（交给 textarea）
- `Tab`（无修饰）且 `is_task_running==true`：触发 `handle_submission(should_queue=true)`（即请求“queue”语义）
- `Enter`（无修饰）：  
  - `should_queue = !steer_enabled`  
    - `steer_enabled=false`（默认）：Enter 走 queue（符合“任务运行中先排队”的交互）  
    - `steer_enabled=true`：Enter 立即 submit，Tab 请求 queue（见 footer hint 语义）
- 其它输入：走 `handle_input_basic`（包含 paste burst）

### 9.2 `handle_submission_with_time`
提交的关键分支顺序（必须一致）：
1) 先尝试 bare builtin slash command：
   - 条件：第一行形如 `/name` 且 rest 为空（`parse_slash_name` rest==""）且 name 命中 builtin
   - 成功：清空 textarea，返回 `InputResult::Command(cmd)`
2) 处理 paste burst 的 newline 插入与 suppression（见 5.5/5.6）
3) 保存原草稿快照（用于“提交被抑制/被拒绝”时恢复）
4) 尝试 dispatch inline-args builtin slash command（`try_dispatch_slash_command_with_args`）：
   - 条件：草稿不以空格开头；`parse_slash_name` rest 非空；name 不含 `/`；命中 builtin 且 supports_inline_args
   - 成功：返回 `InputResult::CommandWithArgs(cmd, trimmed_rest, args_elements)`；**不消耗草稿**（仍保留草稿文本；上层接受后再调用 9.4 做最终准备）
5) 调用 `prepare_submission_text(record_history=true)` 得到最终 `text,text_elements`：
   - should_queue==true → `Queued{...}`
   - 否则 → `Submitted{...}`
6) 若 `prepare_submission_text` 返回 None：恢复原草稿快照并返回 None（不丢用户输入）

### 9.3 `prepare_submission_text`（提交准备与错误恢复）
这是“真正会消耗草稿”的路径（成功时会清空/清理 pending_pastes；失败时会恢复草稿）。

步骤：
1) 复制 `original_input`、`original_text_elements`、`original_local_image_paths`、`original_pending_pastes`
2) 若有 pending_pastes：先调用 4.5 展开 placeholder
3) `text = text.trim()`，并调用 `trim_text_elements(expanded_input, trimmed_text, elements)` 重基准
4) 若 `slash_commands_enabled` 且 `parse_slash_name(&text)` 成功：
   - 若 input 原本以空格开头，或 name 含 `/`：视为 plain text（不做“未识别命令”提示）
   - 否则：要求 name 必须是 builtin 或 known prompt：
     - 不满足：插入一条 info history cell：`Unrecognized command '/{name}'. Type "/" for a list ...`
     - 恢复草稿（original_input + original elements + original images + original pending_pastes）并 return None
5) 若 `slash_commands_enabled`：
   - 调用 `expand_custom_prompt(text, text_elements, custom_prompts)`：
     - Ok(None)：不改
     - Ok(Some(expanded))：替换 text 与 elements
     - Err(e)：插入 error history cell（e.user_message），恢复草稿并 return None
6) `prune_attached_images_for_submission`：只保留 expanded 文本中仍存在的 `[Image #i]` placeholder
7) 若最终 `text` 为空且无 attachments：return None（抑制提交）
8) 若 record_history：将 `{text, text_elements, local_image_paths}` 记录为 local submission（用于本 session ↑/↓）
9) 清空 `pending_pastes` 并 return Some(text,elements)

### 9.4 inline-args 命令的“二阶段提交”（prepare_inline_args_submission）
当上层接收了 `InputResult::CommandWithArgs` 并决定执行命令时，需要再次调用该函数获取最终 args（保证 paste placeholder 已展开、trim 已完成，且元素相对 args 重基准）：
1) `prepare_submission_text(record_history)` 得到 prepared_text + prepared_elements（可能触发 prompt 展开；但 inline args 命令一般不是 `/prompts:`）
2) `parse_slash_name(prepared_text)` 得到 `prepared_rest` 与 `prepared_rest_offset`
3) `slash_command_args_elements(prepared_rest, offset, prepared_elements)`：将 element byte ranges 从 full text shift 到 args 相对坐标
4) 对 args 再 trim，并调用 `trim_text_elements(prepared_rest, trimmed_rest, args_elements)`
5) 返回 `(trimmed_rest, args_elements)`

---

## 10. 错误/边界条件（What can go wrong）

- 未识别 slash command：只在 `slash_commands_enabled==true` 且输入不以空格开头且 name 不含 `/` 时提示；否则当普通文本提交。
- custom prompt args 解析失败：必须给出用户可读错误（见 `TUI_PROMPTS.md` 的错误文案），并恢复草稿。
- 图片路径识别失败（读不到 dimensions）：退化为插入路径文本（file popup）或普通文本粘贴（paste）。
- 删除 element 导致 pending_pastes/attachments 不一致：必须执行 reconcile（4.6），否则会出现“提交时引用不存在 placeholder”的错误。
- 历史浏览期间 popup 抢焦点：通过 `sync_popups` 的 browsing_history 分支禁止。

---

## 11. 来源（Source）
- composer 主实现：`codex-rs/tui/src/bottom_pane/chat_composer.rs`
- paste burst 状态机：`codex-rs/tui/src/bottom_pane/paste_burst.rs`（详规见 `workdocjcl/spec/06_UI/TUI_PASTE_BURST.md`）
- command popup：`codex-rs/tui/src/bottom_pane/command_popup.rs`
- file popup：`codex-rs/tui/src/bottom_pane/file_search_popup.rs`
- skill popup：`codex-rs/tui/src/bottom_pane/skill_popup.rs`
- slash command gating：`codex-rs/tui/src/bottom_pane/slash_commands.rs`
- prompt args 解析/展开：`codex-rs/tui/src/bottom_pane/prompt_args.rs`（详见 `workdocjcl/spec/06_UI/TUI_PROMPTS.md`）
- 参考实现笔记（repo 内）：`docs/tui-chat-composer.md`
