# 模块地图（Module Map）

本章提供“代码单元 → 职责”的快速索引，帮助复刻者决定要实现哪些模块、以及模块之间的边界如何划分。

## 1. Rust workspace（`codex-rs/`）

### 1.1 复刻优先级（建议）
1) **必须复刻（核心对外行为依赖）**
- `codex-rs/cli/`（crate `codex-cli`）：`codex` 顶层命令与子命令解析。
- `codex-rs/core/`（crate `codex-core`）：turn loop、工具路由、上下文管理、rollout。
- `codex-rs/tui/`（crate `codex-tui`）：交互式体验（若要提供同等 UX）。
- `codex-rs/protocol/`（crate `codex-protocol`）：事件/配置/模型 I/O 类型的“公共契约”。
- `codex-rs/state/`（crate `codex-state`）：state.sqlite（threads/logs/dynamic_tools）。

2) **按需复刻（可替换/可裁剪）**
- `codex-rs/exec/`（crate `codex-exec`）：`codex exec` headless 模式（用于 CI/脚本）。
- `codex-rs/login/`（crate `codex-login`）：登录与凭据管理（可用其他方式实现，但行为要一致）。
- `codex-rs/mcp-server/`（crate `codex-mcp-server`）：`codex mcp-server`（实验性）。
- `codex-rs/execpolicy*`：执行策略文件解析与校验。
- `codex-rs/responses-api-proxy/`：内部 proxy（用于特殊网络/兼容性场景）。

### 1.2 完整 crate 清单（自动生成）
- Rust workspace member 列表：`docs/workdocjcl/inventory/rust_workspace.md`
- Rust crate 元数据（含 description）：`docs/workdocjcl/inventory/rust_crate_metadata.json`

## 2. Node/pnpm workspace

### 2.1 发布包与职责
| 路径 | 包名 | 角色 |
|---|---|---|
| `codex-cli/` | `@openai/codex` | npm 分发包装层（选择并执行平台二进制） |
| `sdk/typescript/` | `@openai/codex-sdk` | TypeScript SDK（可选，但建议保留） |
| `shell-tool-mcp/` | `@openai/codex-shell-tool-mcp` | Shell tool MCP server |
| `codex-rs/responses-api-proxy/npm/` |（见该目录 `package.json`）| responses-api-proxy 的 npm 产物 |

### 2.2 完整 package 清单（自动生成）
- pnpm workspace package 列表：`docs/workdocjcl/inventory/node_workspace.md`

## 3. 复刻的“接口边界”（建议以协议为准）
为了确保复刻一致性，建议把以下内容当作“接口契约”：
- CLI 语法（子命令、flags、默认行为）：以 `codex-rs/cli/src/main.rs`（clap）为准。
- 事件协议（UI/headless 输出）：以 `codex-rs/protocol/` 中的类型为准。
- 配置文件结构：以 `codex-rs/core/src/config/mod.rs` 的 `ConfigToml` 以及生成的 schema 为准（仓库内存在 `codex-rs/core/config.schema.json`）。
- 状态数据库 schema：以 `codex-rs/state/migrations/*.sql` 为准。

## 4. 来源（Source）
- Rust workspace 根：`codex-rs/Cargo.toml`
- pnpm workspace：`pnpm-workspace.yaml`
