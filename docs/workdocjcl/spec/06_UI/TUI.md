# UI：终端界面（TUI）

本章描述 Rust 实现的全屏终端 UI（`codex-rs/tui`）。复刻 UI 时可选择不同 UI 框架，但需保持**交互语义**与**事件驱动模型**一致。

## 1. 入口与运行模型
- TUI crate：`codex-rs/tui/`（crate `codex-tui`）
- 对外入口：
  - 作为库：`codex_tui::run_main(cli, ...) -> AppExitInfo`
  - 作为二进制：`codex-rs/tui/src/main.rs`（调用 `run_main`）
  - 通过顶层 CLI：`codex-rs/cli/src/main.rs` 默认进入交互式 TUI

TUI 的核心职责：
- 负责渲染 UI + 捕获用户输入
- 以 Submission 向 core 提交“用户回合/命令/审批结果”
- 订阅 core 输出的事件流（Event stream），将其映射为 UI 状态更新

## 2. CLI 参数（TUI 相关）
TUI 自身的 CLI 参数结构体：
- `codex-rs/tui/src/cli.rs`：`pub struct Cli`

关键行为（从 `run_main` 可见）：
- `--full-auto`：映射为更宽松的 sandbox_mode + 更少审批（具体组合见 `run_main`）
- `--dangerously-bypass-approvals-and-sandbox`：危险模式（禁用 sandbox/approvals）
- `--sandbox-mode`、`--approval-policy`：显式设置 sandbox 与审批策略
- `--search`（legacy）映射到 config override：`web_search="live"`

## 3. UI 主要模块（按代码目录）
该 crate 由多个模块组成，典型复刻建议：
- `app.rs`：顶层 App 状态机（输入事件、渲染、与 core 的交互）
- `chatwidget.rs`：对话视图（渲染 assistant/user 内容、流式输出）
- `public_widgets/composer_input`：输入框（composer）与输入动作（submit/queue）
- `diff_render.rs` / `get_git_diff.rs`：diff 展示与获取
- `resume_picker.rs`：resume/fork 的会话选择 UI
- `onboarding/`：首次运行与登录引导 UI
- `notifications/`：turn 完成通知（脚本/系统通知）
- `session_log.rs`：会话日志记录（受 `CODEX_TUI_RECORD_SESSION` 等 env vars 控制）
- `slash_command.rs`：斜杠命令解析与执行（UI 内命令）
- `bottom_pane/chat_composer.rs`：输入框状态机（草稿/粘贴/附件/弹窗/提交准备）
- `bottom_pane/prompt_args.rs`：`/prompts:` 自定义 prompt 的参数解析与展开（保留 TextElement）
- `bottom_pane/paste_burst.rs`：非 bracketed paste burst 检测状态机（Windows 终端粘贴 key 流）

## 4. 事件驱动与状态同步（复刻要点）
核心原则：
- UI 不直接驱动模型请求/工具执行；它只负责“提交意图”和“展示结果”。
- UI 的所有可见变化应能由事件流推导（允许 UI 有额外本地状态，例如输入框内容、选择器光标等）。

审批（exec/apply_patch/MCP elicitation）是 UI 与 core 交互的关键闭环，复刻时必须保持事件→弹窗→Op 回传语义一致：
- 详见：`docs/workdocjcl/spec/06_UI/TUI_APPROVALS.md`

会话选择（resume/fork picker）属于“复刻系统级能力”，尤其影响 rollout 恢复与 fork 的可用性：
- 详见：`docs/workdocjcl/spec/06_UI/TUI_RESUME_PICKER.md`

Slash commands（`/...`）是 UI 内部命令体系，决定了大量“非模型消息”的交互入口（打开弹窗/切换模式/退出等）：
- 详见：`docs/workdocjcl/spec/06_UI/TUI_SLASH_COMMANDS.md`

输入框（composer）是 TUI 与 core 交互的另一个关键闭环：它把用户输入统一归一为 `InputResult`，并负责 large paste/附件占位符与 `/prompts:` 展开。
- 详见：`docs/workdocjcl/spec/06_UI/TUI_COMPOSER.md`
- `/prompts:` 细节：`docs/workdocjcl/spec/06_UI/TUI_PROMPTS.md`
- 非 bracketed paste burst：`docs/workdocjcl/spec/06_UI/TUI_PASTE_BURST.md`

## 5. 退出语义（Exit）
TUI 返回：
- `AppExitInfo`
- `ExitReason`

复刻要求：
- `Ctrl+C/Ctrl+D` 的退出确认提示（repo 文档提到 ~1s double-press hint）
- 正常结束 vs 错误结束应区分（影响 CLI exit code）

## 6. 来源（Source）
- TUI 入口：`codex-rs/tui/src/lib.rs`、`codex-rs/tui/src/main.rs`
- TUI CLI args：`codex-rs/tui/src/cli.rs`
- 关键模块：`codex-rs/tui/src/app.rs`、`codex-rs/tui/src/chatwidget.rs`、`codex-rs/tui/src/resume_picker.rs`
