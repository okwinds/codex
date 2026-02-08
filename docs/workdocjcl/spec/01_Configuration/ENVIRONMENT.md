# 环境变量（Environment Variables）

本章目标是“可复刻”：列出 Codex CLI 直接或间接依赖的环境变量，并说明其默认行为与实现位置。

> 说明：本仓库支持“配置文件中声明 env var 名称”（例如 provider 的 `env_key`、HTTP header 的 `env_http_headers`）。因此，**可被读取的 env var 名称集合在理论上是开放的**。本章分两部分：
> 1) **代码中直接读取/引用的 env vars**（来自扫描，见 `workdocjcl/inventory/env_vars_detected.txt`）
> 2) **配置驱动的 env vars**（名称由 config.toml 指定，无法静态穷举）

## 1. Codex 配置目录与文件布局（核心）

### 1.1 `CODEX_HOME`（关键）
- 类型：路径（string）
- 默认：`~/.codex`
- 行为：
  - 若设置 `CODEX_HOME`：必须存在且为目录；会被 canonicalize；否则启动失败。
  - 若未设置：不强制目录存在（部分路径会在运行时被创建）。
- 来源：
  - `codex-rs/utils/home-dir/src/lib.rs`（`find_codex_home()`）
  - `codex-rs/core/src/config/mod.rs`（`find_codex_home()` 透传）

### 1.2 `~/.codex` 下的重要文件（复刻应保留）
- `config.toml`：主配置文件（`ConfigToml`）
- `state.sqlite`：SQLite state DB（threads/logs/dynamic_tools）
- `log/…`：日志目录（TUI 默认写 `codex-tui.log`）
- `history.jsonl`：历史记录（受 `history` 配置控制）
- 其他：auth/credentials、rollouts、技能/缓存等（随版本演进）

## 2. 必需变量（Required）

### 2.1 使用 API key 登录（可选路径，但在该模式下为必需）
- `OPENAI_API_KEY`：
  - 类型：string（secret）
  - 用途：OpenAI API Bearer token
  - 获取：OpenAI 平台 / 组织内部发放
  - 典型用法：`printenv OPENAI_API_KEY | codex login --with-api-key`
  - 来源：`codex-rs/core/src/auth.rs`、`codex-rs/cli/src/login.rs`、`codex-rs/responses-api-proxy/`

> 说明：若使用“Sign in with ChatGPT”等 OAuth/设备码登录方式，可能不需要 `OPENAI_API_KEY`；但仍需要有效的凭据存储（见 `ConfigToml.cli_auth_credentials_store`）。

## 3. 常用可选变量（Optional, user-facing）

| 变量 | 类型 | 默认 | 用途/行为 | 主要来源（示例） |
|---|---|---|---|---|
| `OPENAI_BASE_URL` | string(URL) | `https://api.openai.com/v1`（默认值在 TUI 与 provider 中体现） | 覆盖内置 OpenAI provider 的 base_url（可指向 proxy/mock） | `codex-rs/core/src/model_provider_info.rs`、`codex-rs/tui/src/chatwidget.rs` |
| `OPENAI_ORGANIZATION` | string | unset | 若设置，会作为 HTTP header `OpenAI-Organization` 注入（通过 provider `env_http_headers`） | `codex-rs/core/src/model_provider_info.rs` |
| `OPENAI_PROJECT` | string | unset | 若设置，会作为 HTTP header `OpenAI-Project` 注入 | `codex-rs/core/src/model_provider_info.rs` |
| `RUST_LOG` | string |（不同子命令默认值不同） | 控制 Rust 日志级别；TUI 默认写 log 文件 | `docs/install.md`、`codex-rs/tui/`、`codex-rs/exec/` |
| `NO_COLOR` | string | unset | 若设置，禁用彩色输出（遵循生态约定） | 多处（终端输出） |
| `EDITOR` / `VISUAL` | string | unset | 选择外部编辑器（如编辑 config） | 多处（编辑/打开器） |

### 3.1 OSS provider（实验性）
| 变量 | 类型 | 默认 | 用途/行为 | 来源 |
|---|---|---|---|---|
| `CODEX_OSS_BASE_URL` | string(URL) | `http://localhost:<port>/v1` | 设置内置 OSS provider base_url（实验性） | `codex-rs/core/src/model_provider_info.rs` |
| `CODEX_OSS_PORT` | int(u16) | 11434(Ollama)/1234(LM Studio) 等 | 当 `CODEX_OSS_BASE_URL` 未设置时，用端口拼 base_url | `codex-rs/core/src/model_provider_info.rs` |

### 3.2 TUI 行为调试/记录（多为开发/诊断用途）
| 变量 | 类型 | 默认 | 用途/行为 | 来源 |
|---|---|---|---|---|
| `CODEX_TUI_RECORD_SESSION` | bool(string) | `false` | 开启会话日志记录（实现细节见 session_log） | `codex-rs/tui/src/session_log.rs` |
| `CODEX_TUI_SESSION_LOG_PATH` | string(path) | 自动生成 | 指定会话日志输出路径 | `codex-rs/tui/src/session_log.rs` |
| `CODEX_TUI_ROUNDED` | bool(string) | unset | 控制 UI 圆角/样式（用于云任务 UI 等） | `codex-rs/cloud-tasks/src/ui.rs` |

### 3.3 Cloud tasks（实验性/内部特性）
| 变量 | 类型 | 默认 | 用途/行为 | 来源 |
|---|---|---|---|---|
| `CODEX_CLOUD_TASKS_MODE` | string | 依实现 | Cloud tasks 模式选择 | `codex-rs/cloud-tasks/src/lib.rs` |
| `CODEX_CLOUD_TASKS_BASE_URL` | string(URL) | `https://chatgpt.com/backend-api` | Cloud tasks backend base URL | `codex-rs/cloud-tasks/src/lib.rs` |
| `CODEX_CLOUD_TASKS_FORCE_INTERNAL` | bool(string) | unset | 强制走内部通道/行为（内部用途） | `codex-rs/cloud-tasks/src/lib.rs` |

## 4. 分发/包装层相关变量（npm wrapper）
这些变量由 `codex-cli/bin/codex.js` 注入，用于提示“如何更新/管理安装”：
- `CODEX_MANAGED_BY_NPM=1` 或 `CODEX_MANAGED_BY_BUN=1`
- 来源：`codex-cli/bin/codex.js`

## 5. 测试/诊断/平台适配变量（不建议用户依赖）
以下变量更多用于测试工具、平台探测或内部调试；复刻时应保留其行为，但不必作为稳定对外接口承诺。

| 变量 | 用途概述 | 示例来源 |
|---|---|---|
| `MCP_STREAMABLE_HTTP_BIND_ADDR` / `BIND_ADDR` | 测试 MCP streamable HTTP server 绑定地址 | `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs` |
| `MCP_EXPECT_BEARER` | 测试 server 要求 bearer token | 同上 |
| `MCP_TEST_IMAGE_DATA_URL` | 测试用图片 data URL | 测试代码 |
| `SBX_DEBUG` | 沙箱调试开关 | 平台 sandbox 相关代码 |
| `CODEX_STARTING_DIFF` | cloud-tasks-client 读取初始 diff（测试/调试） | `codex-rs/cloud-tasks-client/src/http.rs` |
| `CODEX_THREAD_ID` | 线程/会话测试注入 | 测试代码 |
| `CODEX_APPLY_GIT_CFG` | apply/patch 流程中与 git 配置相关 | 相关 crate |

## 6. 配置驱动的 env vars（无法穷举）
以下场景会导致“读取的 env var 名称可由用户配置决定”：
- `model_providers.<id>.env_key`：指定 provider API key env var（例如 Azure 的 `AZURE_OPENAI_API_KEY`）。
- `model_providers.<id>.env_http_headers`：指定从 env 读取 header 值（例如 `OPENAI_ORGANIZATION`、`OPENAI_PROJECT`）。
- `mcp_servers.<name>.transport.*`：MCP server 可能依赖 `bearer_token_env_var` 等。

因此复刻时必须实现：
- 在解析 config 后，根据 config 中出现的 env var 名称去读取 `process env` 并按语义注入（请求 header / token / credential 等）。

## 7. 参考清单（自动生成）
- 代码直读变量清单：`workdocjcl/inventory/env_vars_detected.txt`
- 变量位置采样：`workdocjcl/inventory/env_var_usages.md`

## 8. 来源（Source）
- `CODEX_HOME`：`codex-rs/utils/home-dir/src/lib.rs`
- OpenAI provider base_url 与 env headers：`codex-rs/core/src/model_provider_info.rs`
- 登录与 API key：`codex-rs/core/src/auth.rs`、`codex-rs/cli/src/login.rs`
- TUI session log env vars：`codex-rs/tui/src/session_log.rs`
- npm wrapper env vars：`codex-cli/bin/codex.js`
