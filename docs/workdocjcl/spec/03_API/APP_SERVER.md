# App Server（codex app-server）协议复刻级规格

本章目标：在不依赖源码阅读的前提下，复刻 Codex 的 “app-server” 进程对外 IPC 协议，使富客户端（例如 VS Code 扩展）可以通过 stdio 驱动 Codex 的线程/turn、接收流式事件、并处理 approvals/auth/tools/skills 等交互闭环。

范围：
- 传输层：JSONL over stdio（按行 framing）
- 消息层：JSON-RPC 2.0 风格，但 **省略** `"jsonrpc":"2.0"` 字段
- 初始化握手、实验能力（experimentalApi）协商与 gating
- 服务器→客户端请求（approvals、tool request_user_input、external auth refresh）
- 服务器→客户端通知（thread/turn/item deltas 等事件流）
- 全量 method/notification 清单（从 schema 提取，避免遗漏）

不覆盖：
- “core 引擎（codex-core）内部事件语义”本身（见 `docs/workdocjcl/spec/04_Business_Logic/*` 与 `07_Infrastructure/*`）
- 具体 UI（VS Code/TUI）的展示细节

---

## 1. 进程形态与 framing

### 1.1 进程入口
- 命令：`codex app-server`
- 运行方式：独立进程，通过 stdio 与宿主应用双向通信。

### 1.2 Framing：JSONL（1 行 = 1 条消息）
输入（stdin）：
- 服务器按 `lines()` 读取，每一行尝试 `serde_json::from_str::<JSONRPCMessage>(line)` 解析。
- 单行不是合法 JSON 时：记录日志并丢弃（不会回包错误）。

输出（stdout）：
- 服务器将每条 outgoing message 序列化为单行 JSON，并追加 `\n` 写出。
- 写 stdout 失败时：记录错误并退出 writer 任务，进程随 channels 关闭进入收尾。

复刻要求：
- 必须按行读写；不得发送多行 JSON（JSON 内部可以包含 `\n` 转义，但整体必须是单行字符串）。

---

## 2. 消息模型（JSON-RPC-like，但省略 jsonrpc 字段）

### 2.1 RequestId
`id` 支持两种类型：
- string
- integer（i64；schema 视为 number）

### 2.2 四类 wire message
服务器与客户端都可以发送以下对象（un-tagged union，通过字段形状区分）：

1) **Request**（期望响应）
```json
{ "id": 1, "method": "thread/start", "params": { ... } }
```

2) **Notification**（不期望响应）
```json
{ "method": "turn/started", "params": { ... } }
```

3) **Response**（成功响应）
```json
{ "id": 1, "result": { ... } }
```

4) **Error**（失败响应）
```json
{ "id": 1, "error": { "code": -32600, "message": "Not initialized", "data": null } }
```

> 复刻注意：虽然结构接近 JSON-RPC 2.0，但双方既不要求也不发送 `"jsonrpc":"2.0"`。

---

## 3. 初始化握手（Initialize / initialized）

### 3.1 硬门禁：除了 initialize，其它请求在初始化前全部拒绝
规则：
- 在服务器处理完 `initialize` 之前，任何其它 `ClientRequest` 都会返回 error：
  - `code = -32600`
  - `message = "Not initialized"`

### 3.2 initialize 是“一次性”
- 若重复调用 `initialize`：
  - `code = -32600`
  - `message = "Already initialized"`

### 3.3 InitializeParams（协商能力）
客户端必须先发送 `initialize` request，并提供：
- `clientInfo`：`name`（合规日志识别关键字段）、可选 `title`、`version`
- `capabilities.experimentalApi`（可选，默认 false）：是否允许使用实验 API 方法/字段（见 §4）

initialize 的成功 response 形如：
- `result.userAgent`：服务器将用于上游请求的 user agent（含 suffix）。

### 3.4 initialized（客户端通知）
协议中存在 `initialized` notification（客户端→服务器），但当前服务器实现对所有客户端 notifications 的行为是：
- 接收并仅记录日志，不改变状态、不回包。

复刻建议：
- 仍应保留 `initialized` notification 以对齐协议演进；但实现上按“忽略即可”也应兼容。

---

## 4. experimentalApi gating（实验方法/字段控制）

### 4.1 客户端声明
initialize params：
- `capabilities.experimentalApi = true` 表示愿意接收/调用实验 API。

### 4.2 服务器侧拒绝规则
当某个 request（或某些 params 字段）被标记为 experimental，且客户端未开启 experimentalApi：
- 服务器返回 error：
  - `code = -32600`
  - `message = "{reason} requires experimentalApi capability"`

其中 `{reason}` 是稳定的标识符：
- 方法级：`<method>`
- 字段级：`<method>.<field>`

复刻要求：
- 必须实现“方法级 + 字段级”两种 gating（协议层通过 ExperimentalApi trait 提供 reason）。

---

## 5. 错误码（JSON-RPC 标准码子集）

服务器主要使用两类 error code：
- `-32600`：Invalid Request（包含：未初始化、请求体无法解析为 ClientRequest、experimental gating 拒绝等）
- `-32603`：Internal Error（例如 response 序列化失败时回包）

复刻要求：
- code 与 message 文案必须稳定（尤其 `"Not initialized"` / `"Already initialized"`），否则客户端难以做一致的恢复/提示。

---

## 6. Method / Notification 全量清单（schema 提取，保证不遗漏）

本节提供 **“可调用/可接收”的 method 名称全集**。字段级形状以 schema 为准（见 §7）。

### 6.1 Client → Server：requests（55）
初始化与能力协商：
- `initialize`

Legacy conversation API（v1 风格，camelCase method 名）：
- `newConversation`
- `resumeConversation`
- `forkConversation`
- `interruptConversation`
- `archiveConversation`
- `listConversations`
- `getConversationSummary`
- `getUserSavedConfig`
- `sendUserMessage`
- `sendUserTurn`
- `addConversationListener`
- `removeConversationListener`
- `execOneOffCommand`
- `execCommandApproval`（注意：这是 server→client request 名；client→server 是 `command/exec` 等。这里列出的为 ClientRequest method）

Thread/Turn API（v2，slash method 名）：
- `thread/start`
- `thread/resume`
- `thread/fork`
- `thread/archive`
- `thread/unarchive`
- `thread/rollback`
- `thread/name/set`
- `thread/list`
- `thread/loaded/list`
- `thread/read`
- `turn/start`
- `turn/interrupt`

配置/模型/技能/Apps/工具等：
- `config/read`
- `config/value/write`
- `config/batchWrite`
- `configRequirements/read`
- `config/mcpServer/reload`
- `model/list`
- `setDefaultModel`
- `skills/list`
- `skills/config/write`
- `app/list`
- `fuzzyFileSearch`
- `command/exec`
- `review/start`
- `gitDiffToRemote`
- `feedback/upload`
- `mcpServer/oauth/login`
- `mcpServerStatus/list`
- `userInfo`

账号/鉴权：
- `account/read`
- `account/rateLimits/read`
- `account/login/start`
- `account/login/cancel`
- `account/logout`
- `getAuthStatus`
- `getUserAgent`
- `loginApiKey`
- `loginChatGpt`
- `logoutChatGpt`
- `cancelLoginChatGpt`

> 复刻注意：method 名称的大小写与斜杠必须严格一致；schema 中的 method 是单值 enum，因此可以作为权威字典。

### 6.2 Client → Server：notifications（1）
- `initialized`

### 6.3 Server → Client：requests（7）
这类 request 由服务器发起，客户端必须用 `JSONRPCResponse`（或 `JSONRPCError`）回应同 id。

- `execCommandApproval`（legacy）
- `applyPatchApproval`（legacy）
- `item/commandExecution/requestApproval`（v2 approvals）
- `item/fileChange/requestApproval`（v2 approvals）
- `item/tool/requestUserInput`（tool request_user_input）
- `item/tool/call`（dynamic tool 调用桥接）
- `account/chatgptAuthTokens/refresh`（external auth token refresh）

### 6.4 Server → Client：notifications（31）
事件流（线程/turn/item 级 streaming）：
- `thread/started`
- `thread/name/updated`
- `thread/compacted`
- `thread/tokenUsage/updated`
- `turn/started`
- `turn/plan/updated`
- `turn/diff/updated`
- `turn/completed`
- `item/started`
- `item/agentMessage/delta`
- `item/plan/delta`
- `item/reasoning/textDelta`
- `item/reasoning/summaryTextDelta`
- `item/reasoning/summaryPartAdded`
- `item/commandExecution/outputDelta`
- `item/commandExecution/terminalInteraction`
- `item/fileChange/outputDelta`
- `item/mcpToolCall/progress`
- `item/completed`
- `rawResponseItem/completed`
- `sessionConfigured`
- `error`
- `deprecationNotice`
- `windows/worldWritableWarning`

账号/MCP 状态：
- `account/updated`
- `account/rateLimits/updated`
- `account/login/completed`
- `authStatusChange`
- `loginChatGptComplete`
- `mcpServer/oauthLogin/completed`
- `configWarning`

---

## 7. 字段级 schema：如何获得“与当前版本严格一致”的结构定义

app-server 协议的字段级 shape 由 `codex-app-server-protocol` 生成并随版本演进。复刻时必须把 schema 当作权威来源之一：

### 7.1 内置 schema 文件（仓库内）
目录：
- `codex-rs/app-server-protocol/schema/json/*.json`

其中至少包含：
- `ClientRequest.json` / `ClientNotification.json`
- `ServerRequest.json` / `ServerNotification.json`
- `JSONRPC*` 基础类型（`RequestId`、`JSONRPCRequest/Response/Error/Notification`）
- 每个方法的 Params/Response 类型（例如 `ThreadStartParams.json` 等）

### 7.2 运行时导出（推荐给宿主应用生成类型）
`codex app-server` 提供导出命令：
- `codex app-server generate-ts --out DIR`
- `codex app-server generate-json-schema --out DIR`

复刻建议：
- 宿主应用（例如 VS Code）应在构建时 pin 某个 Codex 版本，并用该版本导出 schema/TS types，避免协议漂移。

---

## 8. 关键交互闭环（复刻必须覆盖）

### 8.1 Approvals（exec/apply_patch）桥接
core 侧产生 approvals 事件后，app-server 会向客户端发起 server request：
- legacy：`execCommandApproval` / `applyPatchApproval`
- v2：`item/commandExecution/requestApproval` / `item/fileChange/requestApproval`

客户端必须回包 decision，服务器再把 decision 转回 core 的 `Op::ExecApproval` / `Op::PatchApproval`（或对应 v2 item 的 approval decision）。

复刻注意：
- v2 approvals 中 `item_id` 目前复用 core 的 `call_id`（兼容性约束，客户端需按此关联 UI/日志）。

### 8.2 Tool `request_user_input` 闭环
当 core 发出 `request_user_input` tool call：
- server → client：`item/tool/requestUserInput`
- client → server：以相同 id 的 response 回传用户选择/输入
- server 将其作为 tool output 回注 core（完成 tool call）

### 8.3 External auth token refresh（ChatGPT auth tokens）
当 core 使用外部宿主提供的 ChatGPT tokens（AuthMode=chatgptAuthTokens）并需要 refresh：
- server → client：`account/chatgptAuthTokens/refresh`
- client 回应新的 tokens（response）
- server 仅在内存中使用（不会持久化到磁盘），并对 refresh 设置超时（超时会 cancel 回调并报错）

---

## 9. Source Map（本章关键源码锚点）

- 进程读写与 framing：`codex-rs/app-server/src/lib.rs`
- initialized 门禁与 experimentalApi gating：`codex-rs/app-server/src/message_processor.rs`
- OutgoingMessage（request/notification/response/error）序列化：`codex-rs/app-server/src/outgoing_message.rs`
- JSONRPC 基础类型：`codex-rs/app-server-protocol/src/jsonrpc_lite.rs`
- method 枚举与 schema 生成：`codex-rs/app-server-protocol/src/protocol/common.rs`
- v1/v2 协议类型：`codex-rs/app-server-protocol/src/protocol/v1.rs`、`codex-rs/app-server-protocol/src/protocol/v2.rs`
- event→notification 桥接（approvals/tool deltas 等）：`codex-rs/app-server/src/bespoke_event_handling.rs`

## 来源（Source）
- `codex-rs/app-server/src/lib.rs`
- `codex-rs/app-server/src/message_processor.rs`
- `codex-rs/app-server/src/outgoing_message.rs`
- `codex-rs/app-server/src/bespoke_event_handling.rs`
- `codex-rs/app-server-protocol/src/jsonrpc_lite.rs`
- `codex-rs/app-server-protocol/src/experimental_api.rs`
- `codex-rs/app-server-protocol/src/protocol/common.rs`
- `codex-rs/app-server-protocol/src/protocol/v1.rs`
- `codex-rs/app-server-protocol/src/protocol/v2.rs`
