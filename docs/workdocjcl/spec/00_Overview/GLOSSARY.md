# 术语表（Glossary）

本术语表用于确保“规格文档 ↔ 代码实现”用词一致，便于复刻。

## 领域术语（Domain Terms）

| 术语 | 定义 | 在项目中的用法 |
|---|---|---|
| Codex CLI | 在本地终端运行的 coding agent 产品 | 用户运行 `codex` 获取交互式或非交互式体验 |
| Agent | 以模型为核心，结合工具调用完成任务的系统 | `codex-rs/core` 中的 turn loop、tools、approvals |
| Turn | 一轮交互：用户输入 → 模型输出（含工具调用）→ 工具执行/审批 → 模型继续 | `codex-rs/core/src/codex.rs` 事件与状态机 |
| Thread / Session | 一段连续对话与其状态（可恢复/分叉） | CLI 的 `resume`/`fork`；state DB 的 `threads` 表 |
| Rollout | 会话的事件记录（用于回放/恢复/索引） | `codex-rs/core` 的 rollout recorder；state 负责抽取元数据 |
| Approval mode | 审批策略：决定哪些操作需要用户确认 | CLI flags / config.toml；协议中 `AskForApproval` |
| Sandbox mode | 沙箱策略：决定命令执行时的隔离强度与可写范围 | `--sandbox` / config.toml；Seatbelt/Landlock/Windows token |
| Tool | 模型可调用的“可执行能力”，如 shell、apply_patch | `codex-rs/core` tool router + runtime |
| Dynamic Tool | 运行时注入的 tool（例如来自 MCP server 或从会话状态恢复） | `thread_dynamic_tools` 表；`codex_protocol::dynamic_tools` |
| Execpolicy | 命令执行策略文件，用于限制/允许具体命令 | `docs/execpolicy.md`；`codex-rs/execpolicy*` crates |
| MCP | Model Context Protocol（工具/资源协议） | 作为 client 连接外部 MCP servers；也可作为 server 提供工具 |

## 技术术语（Technical Terms）

| 术语 | 定义 |
|---|---|
| Responses API | OpenAI 的响应式模型 API（流式输出、tool calls 等） |
| SSE | Server-Sent Events，用于流式传输事件 |
| WebSocket | 双向实时通讯；在部分 Responses 传输里可用 |
| Seatbelt | macOS sandbox-exec 机制，用于限制子进程权限与网络 |
| Landlock | Linux 下的文件系统访问控制机制（配合 seccomp 等） |
| Restricted token | Windows 受限令牌执行模型（隔离/权限降低） |
| JSONL | 每行一个 JSON 对象的日志/事件记录格式 |
| SQLite | 轻量本地关系数据库，本项目用于 state DB（`state.sqlite`） |

## 缩写（Abbreviations）

| 缩写 | 全称 |
|---|---|
| TUI | Terminal User Interface |
| CLI | Command Line Interface |
| OSS | Open Source Software（此处也指本地模型/自托管 provider 相关） |
| OTEL | OpenTelemetry |

## 来源（Source）
- 核心抽象（Turn/Thread/Rollout/Tool 等）：`codex-rs/core/src/codex.rs`、`codex-rs/protocol/`
- Sandbox/Approval 相关类型：`codex-rs/protocol/` 与 `codex-rs/core/src/config/mod.rs`
- State DB 术语：`codex-rs/state/migrations/*.sql`
