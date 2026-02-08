# 核心基础设施复核（Model API / Prompt 管理 / System Prompts / Tools / Skills）

本文件是“复刻级规格文档”的复核层（review layer）：把 Codex 的核心能力基础设施按**输入/输出/依赖/失败模式/映射关系**逐项审计，并把所有关键契约锚定到 spec 文档与代码实现。

目标读者：
- 需要复刻 Codex 核心能力（而非 UI 像素级细节）的实现者
- 需要对 prompt/skills/tools 这些“不可见但决定行为”的基础设施做完整对齐验证的审计者

---

## 1. Model API 交互（网络层）复核

### 1.1 必须复刻的契约
- provider 配置面：`ModelProviderInfo`（wire_api、headers、query_params、retry、idle_timeout、supports_websockets）
- wire API 选择：Responses vs Chat（不可自动探测）
- streaming 请求：
  - `POST` + `Accept: text/event-stream`
  - 可选 compression（Zstd）
  - headers→事件预注入（RateLimits / ModelsEtag / ServerReasoningIncluded / turn_state）
- Azure Responses 特例：
  - `store` 默认 true
  - `attach_item_ids` 写回 payload
- Chat streaming DONE sentinel 终止规则
- `response.failed` 的 retry delay 文案解析（OpenAI vs Azure 两类模式）

### 1.2 对应规格文档（Spec anchors）
- provider/wire/headers/events/azure：`docs/workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md`
- Responses SSE/WS 事件解析、重试与 WS→HTTP 回退：`docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md`
- provider registry + auth 注入：`docs/workdocjcl/spec/05_Integrations/MODEL_PROVIDERS.md`

### 1.3 代码锚点（Code anchors）
- provider URL 与 Azure 检测：`codex-rs/codex-api/src/provider.rs`
- streaming 请求固定行为：`codex-rs/codex-api/src/endpoint/streaming.rs`
- Responses 请求构造与 Azure store：`codex-rs/codex-api/src/requests/responses.rs`
- Chat 请求构造：`codex-rs/codex-api/src/requests/chat.rs`
- SSE 解析：
  - Responses：`codex-rs/codex-api/src/sse/responses.rs`
  - Chat：`codex-rs/codex-api/src/sse/chat.rs`

### 1.4 典型失败模式（必须对齐）
- provider.wire_api 误配（chat↔responses）：会导致请求 shape 错误（非可恢复）
- 第三方 provider 缺失 `x-codex-*` / `X-Models-Etag` / `x-reasoning-included`：
  - 不应视为错误；只是不产生对应预注入事件
- Chat provider 不发送 `[DONE]` sentinel 且不断开连接：
  - 若不兼容处理，会出现“永不 Completed”卡死
- Azure Responses 未 attach item ids：
  - 可能导致 Azure 端 store/回放语义偏离（需按当前实现复刻）

---

## 2. Prompt 管理（BaseInstructions + initial context）复核

### 2.1 必须复刻的契约
- BaseInstructions 决议优先级：
  1) config override
  2) session_meta（rollout/history）
  3) model_info.get_model_instructions(personality)
- initial context 注入顺序（developer→dev→collab→personality→user→env）
- baked vs injected personality 判定（是否需要额外 personality message）
- compaction 重建时：会重新调用 `build_initial_context` 并过滤 session prefix

### 2.2 对应规格文档
- prompt 组装与注入顺序：`docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`
- rollout/compaction 重建影响：`docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md`

### 2.3 代码锚点
- BaseInstructions 决议与 build_initial_context：`codex-rs/core/src/codex.rs`
- project AGENTS.md 与 skills section 注入：`codex-rs/core/src/project_doc.rs`
- model instructions / personality 模板：`codex-rs/core/src/models_manager/model_info.rs`

### 2.4 复刻边界
- 只要 base instructions 文本与注入顺序一致，即使内部实现语言/结构不同，也可视为“可复刻”。
- 若缺失 prompt 资产原文（仅靠摘要）会导致行为不可复刻（尤其是 prompt 工程的细微约束）。

---

## 3. 系统预置 prompt（verbatim assets）复核

### 3.1 必须复刻的契约
- model slug → base prompt 的选择矩阵必须一致（分支顺序是契约）
- personality/template 资产必须原文一致（模板化 instructions 会影响最终 instructions）

### 3.2 对应规格文档
- 选择矩阵与模板组合：`docs/workdocjcl/spec/04_Business_Logic/SYSTEM_PRESET_PROMPTS.md`
- 资产副本与 sha256：`docs/workdocjcl/spec/04_Business_Logic/PROMPTS/INDEX.md` + `docs/workdocjcl/spec/04_Business_Logic/PROMPTS/MANIFEST.json`

### 3.3 代码锚点（原始来源）
- include_str 资产与 slug 分支：`codex-rs/core/src/models_manager/model_info.rs`
- 源文件位置（原仓库）：`codex-rs/core/*.md`、`codex-rs/core/templates/*`

---

## 4. Tools 调用基础设施复核

### 4.1 必须复刻的契约
- tool schema（名称/参数/输出）必须与运行时工具路由一致
- tool 调用产物必须以 `ResponseItem` 形式进入 history/rollout（可影响 resume/fork/compaction）
- approvals 与 sandbox/execpolicy 的联动必须一致（否则会产生不可复刻的“行为差异”）
- tool outputs 的 envelope（success/error/metadata）必须一致（否则模型与 UI 的反馈回路不同）

### 4.2 对应规格文档
- tool catalog（启用条件/总览）：`docs/workdocjcl/spec/05_Integrations/TOOLS.md`
- tool schema reference：`docs/workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.md`
- per-tool 行为规格（审批/沙箱/错误路径/输出 envelope）：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/INDEX.md`
- approvals/sandbox/execpolicy：`docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`、`docs/workdocjcl/spec/07_Infrastructure/SECURITY_SANDBOX.md`、`docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md`

### 4.3 代码锚点
- tool schema：`codex-rs/core/src/tools/spec.rs`
- tool router/dispatch：`codex-rs/core/src/tools/router.rs`
- handlers：`codex-rs/core/src/tools/handlers/*`

### 4.4 典型失败模式（必须对齐）
- 输出 envelope 不一致：模型可能无法可靠判断 tool 成功/失败，导致后续行为偏离
- approvals 缓存/队列/快捷键语义不一致：会改变工具执行时机与可见性（即使结果相同也会改变 rollout）
- tool call 类型（function vs custom_tool_call vs local_shell_call）误用：会改变 model 侧的 tool-calling 协议与上下文

---

## 5. Skills 使用基础设施复核

### 5.1 必须复刻的契约
- skills roots、扫描深度、symlink 规则、dedupe/sort 规则
- SKILL.md frontmatter 与 agents/openai.yaml 的校验（fail-open 与 warn 语义）
- `$name` / link mention 的消歧与 connector slug 冲突规则
- `<skill>...</skill>` 注入格式（作为 user message 的一部分）
- env_var dependencies：触发 `request_user_input` 并缓存“已提示集合”（session-only）
- system skills 安装与 marker fingerprint（salt `"v1"`）

### 5.2 对应规格文档
- skills 语义总规格：`docs/workdocjcl/spec/05_Integrations/SKILLS.md`
- embedded system skills 资产副本：`docs/workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS.md` + `docs/workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS/MANIFEST.json`

### 5.3 代码锚点
- loader/manager/injection：`codex-rs/core/src/skills/*`
- system skills 安装：`codex-rs/core/src/skills/system.rs`

### 5.4 复刻边界与风险
- skills 内容本身（SKILL.md + scripts/assets）属于“运行时可见提示与工具编排”输入的一部分；缺失会改变模型输出。
- system skills 的实际集合在当前仓库实现中非常小（samples）；复刻时不应擅自扩充，否则行为偏离。

