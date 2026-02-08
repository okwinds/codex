# CLI 接口（Command Line Interface）

本章定义 Codex 的 **对外接口契约**：`codex` 命令行语法、子命令与关键参数语义。复刻时应以本章为准，实现同等 CLI 行为。

## 1. 总体语法（Grammar）

CLI 入口采用 clap 派生，`bin_name` 固定为 `codex`（即使实际二进制名含平台 triple）。

```
codex [OPTIONS] [PROMPT]
codex [OPTIONS] <COMMAND> [ARGS]
```

当未指定 `<COMMAND>` 时：把参数转交给交互式 TUI（默认体验）。

## 2. 顶层选项（Top-level Options）
顶层 CLI 结构（简化）：
- `CliConfigOverrides`：`-c/--config key=value`（可多次）对 `config.toml` 做覆盖
- `FeatureToggles`：与 feature/experimental 相关的 flags（见 `codex-rs/cli/src/main.rs`）
- `TuiCli`：交互式 UI 的 options（由 `codex-tui` crate 定义）

### 2.1 `-c/--config key=value`（配置覆盖）
- 输入：字符串 `key=value`，`key` 支持 dotted path（例如 `shell_environment_policy.inherit=all`）
- value 解析规则：
  - 优先尝试按 TOML literal 解析（数字/数组/inline table 等）
  - 若解析失败，则作为字符串（并去除包裹引号）
- 输出：覆盖后的 TOML 配置树

## 3. 子命令（Subcommands）

> 说明：以下子命令名以 `codex-rs/cli/src/main.rs` 的 `enum Subcommand` 为准。

| 子命令 | 说明 | 复刻要点 |
|---|---|---|
| `exec`（alias `e`） | 非交互运行 Codex | stdout/stderr 行为、退出码、输入（prompt/stdin） |
| `review` | 非交互 code review | review 输出格式与输入约束 |
| `login` | 登录 | 支持 chatgpt/device-code/api-key(stdin) |
| `logout` | 清理凭据 | 删除 file/keyring 中的保存 |
| `mcp` | 管理 MCP servers（实验） | config.toml 的 `mcp_servers` CRUD 与显示 |
| `mcp-server` | 运行 Codex MCP server（实验） | stdio transport；协议兼容 |
| `app-server` | 运行 app server 或相关工具（实验） | 主要供内部/桌面端 |
| `completion` | 生成 shell completions | 支持 bash/zsh/fish 等（clap_complete） |
| `sandbox`（alias `debug`） | 运行平台沙箱命令 | macOS/ Linux/ Windows 三套 wrapper |
| `apply`（alias `a`） | 应用最新 diff 到 git working tree | 与 agent 输出 diff 的格式耦合 |
| `resume` | 恢复历史会话 | picker/--last/--all 行为一致 |
| `fork` | 分叉历史会话 | picker/--last/--all 行为一致 |
| `cloud` / `cloud-tasks` | 浏览 cloud tasks | 依赖 Cloud API；可选复刻 |
| `features` | 查看 feature flags | 输出应包含 key/stage/default 等 |

## 4. `sandbox` 子命令（平台沙箱）
语法（概念）：
- macOS：`codex sandbox macos [--full-auto] [--log-denials] [COMMAND]...`
- Linux：`codex sandbox linux [--full-auto] [COMMAND]...`
- Windows：`codex sandbox windows [--full-auto] [COMMAND]...`

复刻要求：
- “full-auto”语义：是否放宽写入范围、是否仍禁用网络等（与产品安全模型一致）
- 需要与主程序的 sandbox_mode 对齐（不要出现两套不一致策略）

## 5. 来源（Source）
- CLI 入口与子命令：`codex-rs/cli/src/main.rs`
- `-c/--config` 覆盖解析：`codex-rs/common/src/config_override.rs`
