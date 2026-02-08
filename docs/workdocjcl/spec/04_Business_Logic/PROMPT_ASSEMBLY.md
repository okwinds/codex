# Prompt 组装与注入（Prompt Assembly）复刻级规格

本章目标：给出 **可复刻** 的“模型输入（prompt）组装”规范，使实现者在不知道原仓库的前提下，仍能在 *同一配置/同一历史/同一 features* 下构造出语义等价的模型请求（Responses API / Chat API 都适用）。

本章覆盖范围：
- session 初始化时：`base_instructions`（线程级 instructions 字段）如何决议与持久化
- 每个 turn：如何构造 `Prompt`（`instructions` + `input` items + tools）
- developer/user/skills/environment 等“注入项”的顺序与 gating（feature/配置开关）
- personality 注入的“baked vs injected”判定与更新策略
- compaction（上下文压缩）对 prompt 组装的影响点（尤其是 base instructions、initial context 的重建）

不覆盖：
- 工具 schema 与 tool runtime（见 `docs/workdocjcl/spec/05_Integrations/TOOLS.md` 与 `TOOLS_DETAILED/*`）
- approvals/execpolicy 的具体语义（见 `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`、`EXEC_POLICY.md`）
- skills 的发现/启用/mentions 解析（见 `docs/workdocjcl/spec/05_Integrations/SKILLS.md`）

---

## 0. 关键术语与数据结构（必须一致）

### 0.1 BaseInstructions（线程级 instructions）
- 类型：`codex_protocol::models::BaseInstructions { text: String }`
- 语义：对应 Responses API 的 `instructions` 字段；**不**等价于 developer role message。
- 复刻要求：
  - 必须实现 session 级 `base_instructions` 的决议优先级（见 §1）
  - 发送模型请求时必须把 `BaseInstructions.text` 放到 API payload 的 `instructions`

### 0.2 ResponseItem（输入上下文 items）
Codex 使用 Responses 风格的“input items”。它会把 developer/user/environment/工具调用历史统一表示为 `ResponseItem` 并组成 `Prompt.input`。

Prompt 最终由两部分构成：
1) `instructions`（BaseInstructions.text）
2) `input`（ResponseItem 序列：包含权限指令、用户/技能指令、环境信息、历史消息与工具调用等）

### 0.3 DeveloperInstructions（developer role message）
类型：`codex_protocol::models::DeveloperInstructions { text: String }`。

来源分三类：
1) **权限/审批/沙箱策略提示**（permissions instructions）：由 `DeveloperInstructions::from_policy(...)` 生成
2) **用户配置注入**：`config.developer_instructions`
3) **CollaborationMode 注入**：`DeveloperInstructions::from_collaboration_mode(...)`
4) **Personality spec 注入**：`DeveloperInstructions::personality_spec_message(...)`（见 §3）

### 0.4 UserInstructions（AGENTS.md 与用户指令合并）
类型：`crate::instructions::UserInstructions { directory, text }`。

编码形态（非常关键，复刻必须一致）：
```
# AGENTS.md instructions for <directory>

<INSTRUCTIONS>
<contents>
</INSTRUCTIONS>
```
其中 `<contents>` 是多个来源的拼接产物（见 §2）。

### 0.5 SkillInstructions（技能注入项）
类型：`crate::instructions::SkillInstructions { name, path, contents }`。

编码形态（复刻必须一致）：
```
<skill>
<name>...</name>
<path>...</path>
...SKILL.md full contents...
</skill>
```

> 技能如何被选中（`$name`、`[$name](path)`、与 connectors 冲突消歧）不在本章展开，见 `docs/workdocjcl/spec/05_Integrations/SKILLS.md`。

### 0.6 EnvironmentContext（环境上下文）
输入项：`ResponseItem::from(EnvironmentContext::new(Some(cwd), shell))`
- 其中 `EnvironmentContext` 为 core 内部结构（`codex-rs/core/src/environment_context.rs`），会被序列化为 XML：
  - `<environment_context> ... </environment_context>`（tag 常量见 `codex-rs/protocol/src/protocol.rs`）
- 字段语义：
  - `cwd`：当前工作目录（`PathBuf`）
  - `shell`：用户 shell（`Shell`）

该项在每个 turn 都会被注入（见 §2.1、§2.3）。

---

## 1. Session 初始化：BaseInstructions 决议（优先级必须一致）

在创建 `SessionConfiguration` 时，会计算线程级 `base_instructions`。优先级为：
1) `config.base_instructions`（显式 override）
2) `conversation_history.session_meta.base_instructions`（resume/fork thread 时从历史恢复）
3) `model_info.get_model_instructions(config.personality)`（模型默认 instructions；可能包含 personality 模板）

复刻算法（伪代码）：
```text
model_info = models_manager.get_model_info(selected_model, config)
base = if config.base_instructions is Some:
         config.base_instructions
       else if conversation_history has base_instructions:
         conversation_history.base_instructions.text
       else:
         model_info.get_model_instructions(config.personality)
```

复刻注意：
- 第 3 步调用的是 `ModelInfo.get_model_instructions(personality)`，它可能：
  - 若 `model_messages.instructions_template` 存在：用模板替换 `{{ personality }}`（见 §3.1）
  - 若模板缺失但 personality 有值：会 warn 并 fallback 到 `base_instructions`

---

## 2. 每个 Turn：Initial Context 的组装（顺序=语义）

### 2.1 build_initial_context：必须按固定顺序 push items
对于一个 turn，Codex 会先构建一段“initial context”，并作为对话历史的最前缀。

**顺序不可更改**（按 push 顺序）：
1) `DeveloperInstructions::from_policy(...)`（permissions instructions）
2) `turn_context.developer_instructions`（可选，来自 config）
3) `DeveloperInstructions::from_collaboration_mode(...)`（可选）
4) personality spec message（可选，且仅当“需要注入”）
5) `UserInstructions { text: user_instructions, directory: cwd }`（可选）
6) `EnvironmentContext(cwd, shell)`（必有）

复刻伪代码（只表达 ordering 与 gating）：
```text
items = []
items += developer_instructions_from_policy(...)
if turn_context.developer_instructions != None:
  items += developer_instructions(turn_context.developer_instructions)
if collaboration_mode has non-empty developer_instructions:
  items += collab_developer_instructions(...)
if feature Personality enabled and turn_context.personality != None:
  maybe items += personality_spec_message (see §3.2)
if user_instructions != None:
  items += user_instructions_message(cwd, user_instructions)
items += environment_context(cwd, shell)
```

### 2.2 permissions instructions 的语义边界
`DeveloperInstructions::from_policy(...)` 会把下列信息写入 developer role message：
- sandbox mode（DangerFullAccess/ReadOnly/WorkspaceWrite）
- network access（Enabled/Restricted）
- approval policy（Never/UnlessTrusted/OnFailure/OnRequest）
- request_rule（execpolicy allow-prefixes）相关文案（当 feature 开启）
- workspace-write 的 writable_roots（含 cwd）列表

复刻要求：permissions instructions 必须整体包在：
```
<permissions instructions>
...
</permissions instructions>
```
并遵循协议层模板文本（否则模型行为会明显漂移）。

### 2.3 UserInstructions 的来源与拼接（AGENTS + skills section）
`UserInstructions.text` 来自 `get_user_instructions(config, enabled_skills)` 的拼接结果（见 `codex-rs/core/src/project_doc.rs`），顺序如下：
1) `config.user_instructions`（可选）
2) project doc（可选）：从 repo root 到 cwd 的 `AGENTS.override.md`/`AGENTS.md`（见 §2.4）
3) skills section（可选）：把当前启用的 skills 列表渲染为一个“可读清单”（用于告诉模型有哪些技能可被 `$name` 引用）
4) hierarchical agents message（可选）：feature `ChildAgentsMd` 开启时追加

复刻关键点：
- 第 2 步与第 1 步之间要插入固定分隔符：
  - `\n\n--- project-doc ---\n\n`
- skills section 是“列表清单”，而真正的技能内容只在用户显式 mention 后以 `<skill>...</skill>` 形式注入（见 `docs/workdocjcl/spec/05_Integrations/SKILLS.md`）。

### 2.4 Project doc（AGENTS.md）发现规则（repo root → cwd）
project doc 的发现规则为：
1) 从 `cwd` 向上找 `.git`（文件或目录）作为 git root；若找不到，只看 cwd
2) 在 “git root → cwd 的路径链” 上，每一层目录按候选文件名优先级查找：
   - `AGENTS.override.md`（优先）
   - `AGENTS.md`
   - `project_doc_fallback_filenames`（config 可配置追加候选）
3) 每层目录最多取第一个命中的文件；最终把命中的内容按目录顺序拼接
4) 受 `project_doc_max_bytes` 总预算限制：超预算时截断，并 warn

---

## 3. Personality：baked vs injected（必须一致，否则会重复注入）

### 3.1 模型 instructions 模板：`ModelMessages.instructions_template`
当 `ModelInfo.model_messages.instructions_template` 存在时：
- `ModelInfo.get_model_instructions(personality)` 会把模板中的 `{{ personality }}` 替换为：
  - `ModelMessages.instructions_variables` 中对应 personality 的消息（Friendly/Pragmatic/Default）
- 该替换在 **BaseInstructions** 层发生（即 API payload 的 `instructions` 字段）

复刻注意：
- 若 personality 为空：用 `personality_default`（可为空字符串）替换
- 即使 personality 有值，只要模板存在也会走 template 替换（不会 fallback 到 base_instructions）

### 3.2 初始 turn：has_baked_personality 判定
在 `build_initial_context` 中，只有满足以下条件才会注入 personality spec message：
- feature `Personality` enabled
- `turn_context.personality` is Some
- `!has_baked_personality`
- `model_messages.get_personality_message(Some(personality))` 返回非空字符串

其中：
```
has_baked_personality =
  model_info.supports_personality()
  && base_instructions == model_info.get_model_instructions(Some(personality))
```

解释：
- 若模型支持 personality 且 base_instructions 已经等于“带 personality 替换后的 instructions”，则认为 personality 已 baked 到 `instructions` 字段中，避免重复注入。
- 否则把 personality 作为 developer message 注入：
  - `DeveloperInstructions::personality_spec_message(personality_message)`

### 3.3 turn 之间 personality 更新：只在发生变化时注入
当 turn context 的 personality 与前一 turn 不同时，会额外插入一个 personality update item（developer message），用于告诉模型“从现在开始切换人格”。

复刻要求：
- personality update 的注入策略与 §3.2 一致：依赖 `model_messages.get_personality_message`，空消息不注入
- 注入项是 developer role message（`<personality_spec> ... </personality_spec>` 包裹）

---

## 4. Skills 注入与 Prompt 的关系（只定义“组装点”）

Codex 的技能体系有两条进入 prompt 的路径：

1) **技能列表清单**：作为 `UserInstructions.text` 的“skills section”提供给模型，告诉模型有哪些技能可用（不包含 SKILL.md 正文）。
2) **技能正文注入**：当用户输入文本显式 mention skill（`$name` 或 `[$name](path)`）时，core 读取对应 `SKILL.md` 并把全文作为 `SkillInstructions` 追加到 prompt history（role=user，XML 包裹）。

复刻注意：
- 技能正文注入必须发生在“用户输入 turn item”之后（否则模型看不到用户这次 mention 的上下文）。
- 技能正文注入失败（文件不可读等）时：
  - 不应 panic；应产生 warning（并继续执行 turn）。

选择/消歧/启用禁用/依赖提示等详见：`docs/workdocjcl/spec/05_Integrations/SKILLS.md`。

---

## 5. Prompt → API payload：字段映射（Responses/Chat 共用点）

### 5.1 core Prompt 结构
`crate::client_common::Prompt` 是 core 内部的“单 turn 请求结构”：
- `base_instructions: BaseInstructions` → API payload `instructions`
- `input: Vec<ResponseItem>` → API payload `input`
- `tools: Vec<ToolSpec>` → API payload `tools`
- `parallel_tool_calls: bool` → API payload `parallel_tool_calls`
- `output_schema: Option<Value>` → API payload `output_schema`

### 5.2 API Prompt 适配：`build_api_prompt(...)`
Responses API 请求的核心映射规则（伪代码）：
```text
ApiPrompt.instructions = prompt.base_instructions.text
ApiPrompt.input = prompt.get_formatted_input()
ApiPrompt.tools = tools_json
ApiPrompt.parallel_tool_calls = prompt.parallel_tool_calls
ApiPrompt.output_schema = prompt.output_schema
```

### 5.3 Freeform apply_patch 与 tool output reserialize（重要细节）
当 prompt.tools 中出现 **Freeform** 形态的 `apply_patch` 工具时：
- `prompt.get_formatted_input()` 会对历史中的 shell/tool outputs 做一次“结构化文本重写”（避免 JSON 再序列化导致格式破坏）。

复刻要求：
- 该重写只在 freeform apply_patch present 时发生
- 其目的是保证模型能把 tool output 作为“可读结构化文本”消费（尤其是 apply_patch 的 patch 格式）

---

## 6. Compaction（上下文压缩）对 prompt 的影响点

当触发自动/手动 compaction 时：
1) 会构造一个新的 turn，把“compaction prompt”作为 `UserInput::Text` 注入（该 prompt 来自 `turn_context.compact_prompt()`）
2) compaction turn 的 `Prompt.base_instructions` 仍来自 `sess.get_base_instructions()`（即线程级 BaseInstructions）
3) compaction 完成后，会重建 history：
   - 取 `sess.build_initial_context(turn_context)` 作为新 history 前缀
   - 将旧历史的 user messages 折叠为 summary（加上固定 `SUMMARY_PREFIX`）
   - 追加 ghost snapshots（如存在）

复刻要点：
- compaction 后 initial context 的顺序必须与 §2 一致
- `UserInstructions` 与 `EnvironmentContext` 会在 compaction 后的新 history 中再次出现（因为 history 是重建的）

---

## 7. Source Map（本章关键源码锚点）

复刻实现时应至少对齐下列源码的行为与顺序：
- BaseInstructions 决议：`codex-rs/core/src/codex.rs`（session spawn 逻辑）
- initial context 注入顺序：`codex-rs/core/src/codex.rs#build_initial_context`
- project doc 发现/拼接：`codex-rs/core/src/project_doc.rs`
- UserInstructions/SkillInstructions 编码：`codex-rs/core/src/instructions/user_instructions.rs`
- DeveloperInstructions permissions/personality/collab：`codex-rs/protocol/src/models.rs`
- model instructions template 与 personality variables：`codex-rs/protocol/src/openai_models.rs`、`codex-rs/core/src/models_manager/model_info.rs`
- Prompt → API payload：`codex-rs/core/src/client_common.rs`、`codex-rs/core/src/client.rs`
- compaction history 重建：`codex-rs/core/src/compact.rs`

## 来源（Source）
- `codex-rs/core/src/codex.rs#record_initial_history`
- `codex-rs/core/src/codex.rs#seed_initial_context_if_needed`
- `codex-rs/core/src/codex.rs#build_initial_context`
- `codex-rs/core/src/project_doc.rs#get_user_instructions`
- `codex-rs/core/src/instructions/user_instructions.rs`
- `codex-rs/core/src/environment_context.rs`
- `codex-rs/protocol/src/models.rs#BaseInstructions`
- `codex-rs/protocol/src/models.rs#DeveloperInstructions`
- `codex-rs/protocol/src/protocol.rs`
- `codex-rs/core/src/client_common.rs#Prompt`
- `codex-rs/core/src/client.rs#build_api_prompt`
- `codex-rs/core/src/compact.rs`
