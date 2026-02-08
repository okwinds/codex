# 集成：MCP（Model Context Protocol）

本章描述 Codex 如何作为 **MCP client** 连接外部 MCP servers，以及（实验性）如何作为 MCP server 被其他客户端调用。

## 1. MCP 的角色
- MCP client：Codex 启动时连接外部工具服务，把其 tools/resources 暴露给模型作为可调用工具。
- MCP server（实验）：`codex mcp-server` 让其他 MCP clients 把 Codex 本身当作一个工具调用。

## 2. 配置入口：`config.toml` → `mcp_servers`
配置类型位于 `ConfigToml.mcp_servers`（map：server name → `McpServerConfig`）。

### 2.1 MCP server config 共同字段
| 字段 | 类型 | 默认 | 说明 |
|---|---|---|---|
| `enabled` | bool | true | 是否初始化该 server |
| `startup_timeout_sec` | duration | unset | 初始化 + 初次 list_tools 超时 |
| `tool_timeout_sec` | duration | unset | 默认 tool 调用超时 |
| `enabled_tools` | [string] | unset | allow-list，仅注册这些工具 |
| `disabled_tools` | [string] | unset | deny-list，最终从工具集中移除 |
| `scopes` | [string] | unset | OAuth scopes（当 transport 需要 OAuth） |

### 2.2 transport: stdio
输入形态（Raw config）：
- `command`: string（必填）
- `args`: [string]
- `env`: map[string]string（直接注入 env）
- `env_vars`: [string]（从当前进程继承这些 env var）
- `cwd`: path（可选）

复刻要点：
- `command` + `args` 形成子进程
- stdio 作为 MCP transport（协议层由 rmcp 实现）
- 需要明确处理“哪些 env 能继承、哪些需要显式列出”（防止泄露敏感 env）

### 2.3 transport: streamable_http
输入形态（Raw config）：
- `url`: string（必填）
- `bearer_token_env_var`: string（可选）
- `http_headers`: map[string]string（可选）
- `env_http_headers`: map[string]string（header value 从 env var 取；空则不注入）

复刻要点：
- 在 HTTP 请求中注入 bearer token（如果配置了 env var）
- 支持 OAuth callback（见 3）

## 3. MCP OAuth（凭据存储与 callback server）
相关配置：
- `mcp_oauth_credentials_store`：`auto` / `keyring` / `file`
- `mcp_oauth_callback_port`：固定 callback 端口（unset 则使用 OS ephemeral port）

复刻要求：
- 当 MCP server 需要 OAuth 时，客户端必须能启动本地 callback server 接受 redirect，并持久化凭据。
- 必须能在重启后复用已保存的 OAuth credentials。

## 4. “缺失依赖”自动提示（可选）
feature：`skill_mcp_dependency_install`
- 当某些 skill/mcp 依赖缺失时，Codex 可提示用户安装（行为取决于 feature 与平台限制）。

## 5. Codex 作为 MCP server（实验）
- 入口：`codex mcp-server`
- transport：stdio
- 对外能力：把 Codex 的某些功能暴露为 MCP tools（具体 tool 集随版本演进）

## 6. 来源（Source）
- 配置类型：`codex-rs/core/src/config/types.rs#McpServerConfig`、`codex-rs/core/src/config/types.rs#McpServerTransportConfig`
- config.toml schema：`codex-rs/core/config.schema.json`
- MCP client：`codex-rs/rmcp-client/`、`codex-rs/core/src/mcp*`
- MCP server：`codex-rs/mcp-server/`
