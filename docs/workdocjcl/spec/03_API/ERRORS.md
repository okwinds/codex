# 错误与异常处理（Errors）

Codex CLI 的错误处理分为三类：
1) CLI 进程级别：以 exit code 表达成功/失败
2) UI/交互级别：以事件（`ErrorEvent`/`WarningEvent` 等）在 UI 中展示
3) 网络/API 级别：外部 HTTP 错误、流式中断、限流等，转译为内部 error 并影响 turn 结果

## 1. CLI Exit Codes（复刻约束）
通用原则：
- `0`：成功
- `1`：失败（参数错误、登录失败、网络失败、内部错误等）

示例（登录）：
- ChatGPT 登录禁用但用户尝试：打印提示并 `exit(1)`。
- stdin 是 TTY 但用户使用 `--with-api-key`：打印提示并 `exit(1)`。

## 2. 事件层（Event-based error reporting）
核心引擎输出 event stream，错误相关事件主要包括：
- `ErrorEvent`：不可恢复错误
- `WarningEvent`：可继续但需要用户知晓的风险/降级
- `StreamErrorEvent`：流式解析/传输错误

复刻要求：
- 错误必须与“turn”绑定（能定位到发生在哪个阶段：模型请求/工具执行/审批等）。
- UI 层可以选择如何呈现，但必须保留错误信息的结构与可诊断性。

## 3. 网络/API 错误处理（典型场景）

### 3.1 Auth 错误
- 401/403：凭据无效或权限不足 → 提示用户重新登录或检查 key。
- 读取凭据失败：提示并停止请求（避免空 token 请求）。

### 3.2 限流与重试（provider 参数）
provider 支持 request/stream 的最大重试次数与超时策略（见 `ModelProviderInfo`）：
- `request_max_retries`
- `stream_max_retries`
- `stream_idle_timeout_ms`

### 3.3 流式中断
- SSE/WebSocket 断开或 idle timeout：
  - 若允许重连：按 provider 的策略重试。
  - 若不可恢复：发出 `StreamErrorEvent` 并结束 turn。

## 4. 可观测性（Logging/Monitoring）
- Rust 日志通过 `RUST_LOG` 控制；TUI 默认写入 `~/.codex/log/codex-tui.log`（见 `docs/install.md`）。
- state DB 可存储 logs（`logs` 表），并可按 `thread_id` 查询。
- OTEL 与 analytics/feedback 由 config 控制（见 `ConfigToml.otel/analytics/feedback`）。

## 5. 来源（Source）
- 登录错误与 exit code：`codex-rs/cli/src/login.rs`
- Provider 重试/超时：`codex-rs/core/src/model_provider_info.rs`
- 事件类型：`codex-rs/protocol/src/*.rs`
- 日志与 state DB：`codex-rs/state/src/runtime.rs`
