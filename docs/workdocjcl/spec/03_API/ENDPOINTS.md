# 外部接口目录（Endpoints & Interfaces）

Codex CLI 本质上是“本地客户端”，不是传统 Web API 服务。但仓库中仍存在需要复刻的接口边界：
- 对外网络接口（OpenAI/ChatGPT 等）
- 本地辅助服务接口（登录 server、responses-api-proxy 等）
- IPC/协议（MCP stdio、内部 event stream 等）

本章按“接口类型”列出端点/协议，并标注认证方式与来源代码位置。

## 1. OpenAI API（客户端调用）

### 1.1 Responses API
- Endpoint：`POST /v1/responses`
- 传输：HTTP + 流式（SSE/WebSocket，具体取决于 provider 与 feature）
- 认证：`Authorization: Bearer <token>`（token 来源于登录/凭据系统；也可来自 `OPENAI_API_KEY`）
- 主要用途：发送模型输入（prompt + tools + context），接收 streaming output items / tool calls。

> 复刻要点：
> - 需要实现“流式事件解析”与“工具调用 item 的处理”，并把解析结果转成内部 event stream。
> - 需要支持 provider base_url 覆盖（`OPENAI_BASE_URL` 或 config.toml provider override）。

### 1.2 Models（可选/依实现）
Codex 在部分场景下需要模型列表与能力信息（例如 UI 选择模型）。具体端点与缓存策略取决于 provider 实现与 feature（例如 `remote_models`）。

## 2. ChatGPT / Cloud endpoints（客户端调用）
仓库包含与 ChatGPT 登录/Cloud tasks 相关的实现。其外部 HTTP 端点属于产品后端 API，版本可能演进；复刻时更关键的是“客户端行为契约”：
- 登录：本地 login server / device-code flow
- Cloud tasks：基于 `CODEX_CLOUD_TASKS_BASE_URL` 的 API 访问

## 3. 本地登录服务（browser-based login server）
- 角色：在本机启动一个 HTTP server，打开浏览器到 auth URL，完成 OAuth/授权后把凭据写入 `CODEX_HOME`。
- 绑定地址：`http://localhost:<port>`（端口由 OS 分配；会在 stdout/stderr 输出提示）
- 认证：通过外部浏览器交互完成

## 4. responses-api-proxy（本地 HTTP 服务，内部用途）
仓库包含一个“严格代理”，其目标是：
- 仅转发 `POST /v1/responses` 到 OpenAI API，并注入 `Authorization: Bearer $OPENAI_API_KEY`。
- 默认拒绝其他路径（403）
- 可选支持 `GET /shutdown`（当启用 `--http-shutdown` 时）

> 复刻要点：这是一个安全边界组件（隔离 unprivileged 用户无法读取 key 的场景）。

## 5. MCP（Model Context Protocol）

### 5.1 Codex 作为 MCP client（常态）
- Codex 启动时可连接一组 MCP servers（由 config.toml 的 `mcp_servers` 配置决定）。
- 通过 MCP 的 `call_tool` / `list_tools` / `read_resource` 等能力把外部工具与资源纳入 agent 工具集。

### 5.2 Codex 作为 MCP server（实验性）
- 入口：`codex mcp-server`（stdio transport）
- 对外：其他 MCP clients 可把 Codex 当作一个 tool 使用

## 6. 来源（Source）
- OpenAI provider base_url/env headers：`codex-rs/core/src/model_provider_info.rs`
- Rust CLI 子命令：`codex-rs/cli/src/main.rs`
- 登录：`codex-rs/cli/src/login.rs`、`codex-rs/login/`
- responses-api-proxy：`codex-rs/responses-api-proxy/`（含 README 与实现）
- MCP：`codex-rs/mcp-server/`、`codex-rs/rmcp-client/`、`codex-rs/core/src/mcp*`

## 7. App Server（本地 IPC，富客户端）
- 入口：`codex app-server`
- 传输：stdio JSONL（JSON-RPC-like，省略 `"jsonrpc":"2.0"` 字段）
- 用途：VS Code 扩展等富客户端通过 thread/turn/item API 驱动 Codex，并接收 streaming notifications，处理 approvals/auth/tool requests。

复刻规格见：`workdocjcl/spec/03_API/APP_SERVER.md`
