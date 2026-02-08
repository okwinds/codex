# TUI：Slash Commands（`/...`）复刻级规格

本章目标：复刻 Codex TUI 的“slash command”体系：用户在输入框中以 `/` 开头输入命令，UI 会在**本地**执行对应动作（打开弹窗、提交 `Op`、切换模式、退出等），而不是把它当作普通用户消息提交给模型。

---

## 1. 命令集合（内建 SlashCommand）

定义：`codex-rs/tui/src/slash_command.rs:SlashCommand`

命令字符串：
- 默认使用 `kebab-case`（`#[strum(serialize_all = "kebab-case")]`）
- 特例：`ElevateSandbox` 的命令字符串固定为 `setup-elevated-sandbox`

展示顺序：
- **枚举定义顺序即 popup 展示顺序**（代码注释要求“不要按字母排序”）

可见性（is_visible）：
- `/rollout` 与 `/test-approval` 仅在 `cfg!(debug_assertions)` 下可见

---

## 2. 识别与派发：ChatComposer → ChatWidget

### 2.1 Slash command 解析（`/name <rest>`）
解析函数：`codex-rs/tui/src/bottom_pane/prompt_args.rs:parse_slash_name`

输入：一行文本 `line`
输出：`Option<(name, rest, rest_offset)>`
- 仅当 `line` 以 `/` 开头且 name 非空时返回 Some
- name 读取到第一个空白字符前
- rest 为 name 之后去掉前导空白的剩余部分
- `rest_offset` 是 rest 在原始 line 中的 byte offset（用于 text_elements rebasing）

> `parse_slash_name` 既用于内建 slash commands，也用于 `/prompts:<name>` 的自定义 prompt 解析；自定义 prompts 的参数展开与元素保真细节见 `docs/workdocjcl/spec/06_UI/TUI_PROMPTS.md`。

### 2.2 “裸命令”派发（无 args）
函数：`ChatComposer::try_dispatch_bare_slash_command`

判定条件（必须全部满足）：
- `slash_commands_enabled == true`
- `first_line` 能 `parse_slash_name(first_line)` 得到 `(name, rest, ...)`
- `rest.is_empty()`
- `find_builtin_command(name, ...)` 找到内建命令（受 gating 影响，见 §2.4）
- 若当前 task 正在运行且命令不可用：拒绝并插入错误信息（`reject_slash_command_if_unavailable`）

效果：
- 清空 textarea（`set_text_clearing_elements("")`）
- 返回 `InputResult::Command(cmd)`

### 2.3 “带 inline args 的命令”派发（例如 `/review ...`）
函数：`ChatComposer::try_dispatch_slash_command_with_args`

判定条件（必须全部满足）：
- `slash_commands_enabled == true`
- 输入文本 `text` **不以空格开头**（以空格开头 → 强制当作普通文本）
- `parse_slash_name(&text)` 成功返回 `(name, rest, rest_offset)`
- `rest` 非空
- `name` **不包含 `'/'`**（包含则当作普通文本，避免 `/a/b` 触发命令语义）
- `find_builtin_command(...)` 找到 builtin
- `cmd.supports_inline_args()==true`（目前只有 `/review`、`/rename`、`/plan`）
- 若当前 task 正在运行且命令不可用：拒绝（同上）

效果：
- 生成 `InputResult::CommandWithArgs(cmd, trimmed_rest, args_elements)`
  - `args_elements` 会把全文本的 text elements 映射到 args 区间，并执行 trim

### 2.4 builtin gating（哪些命令会被识别）
内建命令查找：`codex-rs/tui/src/bottom_pane/slash_commands.rs:find_builtin_command`

可见/可用内建命令集合由 `builtins_for_input(...)` 过滤得到：
- 未启用 collaboration modes 时：隐藏 `/collab` 与 `/plan`
- 未启用 connectors（apps）时：隐藏 `/apps`
- 未启用 personality command 时：隐藏 `/personality`
- `allow_elevate_sandbox == false` 时：隐藏 `/setup-elevated-sandbox`

> 复刻注意：composer 的“能否识别某命令”和 popup 的“能否展示某命令”必须一致，因此 gating 被集中在该模块中。

### 2.5 未识别命令的错误提示（提交前校验）
在 `ChatComposer::prepare_submission_text` 中，会对输入做一次“命令存在性校验”：
- 若输入（trim 后）第一行是 `/name...` 且不是“当作普通文本”的情况：
  - 若 name 不是 builtin，也不是已知 custom prompt（`/prompts:<name>`），则：
    - 插入 info event：
      - `Unrecognized command '/{name}'. Type "/" for a list of supported commands.`
    - 恢复用户原输入（包括 text_elements / attachments / cursor），并抑制本次提交（返回 None）

这样可以避免用户误拼写命令后直接提交给模型。

来源：
- `codex-rs/tui/src/bottom_pane/chat_composer.rs:prepare_submission_text`
- 关联：composer 提交/粘贴/附件/弹窗的完整状态机见 `docs/workdocjcl/spec/06_UI/TUI_COMPOSER.md`

---

## 3. ChatWidget 对命令的执行语义（dispatch_command）

入口：
- `ChatWidget::handle_key_event` 收到 `InputResult::Command(cmd)` → `dispatch_command(cmd)`
- 收到 `InputResult::CommandWithArgs(cmd, args, elements)` → `dispatch_command_with_args(cmd, args, elements)`

共同限制：
- 若 `!cmd.available_during_task()` 且当前 `bottom_pane.is_task_running()==true`：
  - 插入错误信息：`'/{cmd}' is disabled while a task is in progress.`
  - `bottom_pane.drain_pending_submission_state()`
  - 返回（不执行命令）

来源：
- `codex-rs/tui/src/slash_command.rs:available_during_task`
- `codex-rs/tui/src/chatwidget.rs:dispatch_command`

---

## 4. 每个命令的行为（复刻级清单）

> 下表描述的是“UI 行为/向 core 发出的 Op 或 AppEvent”。其中打开的 popup/overlay 其内部规格在各自章节描述。

### 4.1 会话/线程生命周期
- `/new` → `AppEvent::NewSession`
- `/resume` → `AppEvent::OpenResumePicker`（见 `docs/workdocjcl/spec/06_UI/TUI_RESUME_PICKER.md`）
- `/fork` → `AppEvent::ForkCurrentSession`
- `/rename`（无 args）→ 打开 rename prompt view（自定义输入框）
- `/rename <name>` → 发送 `Op::SetThreadName { name }`（并插入确认 history cell；name 会 normalize）
- `/quit`、`/exit` → `request_quit_without_confirmation()`
- `/logout` → 执行 `codex_core::auth::logout(...)` 后退出

### 4.2 模式/策略类弹窗
- `/model` → `open_model_popup()`
- `/personality` → `open_personality_popup()`
- `/approvals` → `open_approvals_popup()`
- `/permissions` → `open_permissions_popup()`
- `/experimental` → `open_experimental_popup()`
- `/collab` → `open_collaboration_modes_popup()`（需 collaboration modes enabled）
- `/plan`：
  - 若 collaboration modes disabled：插入 info message 并返回
  - 否则尝试切换到 Plan mask（`set_collaboration_mask(plan_mask)`）
- `/plan <text>`：
  - 先执行 `/plan` 切换模式
  - 若切换后当前模式不是 Plan：停止
  - 否则把 `<text>` 当作用户消息提交（会保留 text elements 与图片占位符语义）

### 4.3 评审/上下文相关
- `/compact` → `Op::Compact`（同时清除 token usage 显示）
- `/review`（无 args）→ 打开 review popup（选择 review target）
- `/review <instructions>` → 发送 `Op::Review { target: Custom { instructions } }`

### 4.4 工具类输出（插入到 transcript）
- `/diff`：
  - 先插入 “diff in progress” 提示
  - 异步计算 `get_git_diff()`，完成后通过 `AppEvent::DiffResult(text)` 回写
- `/mention`：向 composer 插入 `"@"`
- `/skills`：打开 skills 菜单
- `/status`：插入当前 session 状态输出
- `/ps`：插入后台 terminal 列表输出
- `/mcp`：插入 MCP 工具/服务器输出
- `/apps`：插入 connectors/apps 输出

### 4.5 平台特例（Windows）
- `/setup-elevated-sandbox`（仅 windows + degraded 模式 gating 后可见）：
  - 选择 builtin approval preset `"auto"`（找不到则报错）
  - 校验 approval_policy 可设置
  - 发送 `AppEvent::BeginWindowsSandboxElevatedSetup { preset }`

### 4.6 调试命令（debug_assertions）
- `/rollout`：输出当前 rollout path（若不可用则提示）
- `/test-approval`：注入一个合成的 `ApplyPatchApprovalRequestEvent` 以测试审批 UI（exec approval 测试代码目前注释掉）

### 4.7 `/init`（创建 AGENTS.md 的提示）
- 目标路径：`<cwd>/{DEFAULT_PROJECT_DOC_FILENAME}`
- 若文件已存在：插入 info message，避免覆盖
- 否则提交一个内置 prompt（`prompt_for_init_command.md`）作为用户消息，让模型生成内容

来源：
- `codex-rs/tui/src/chatwidget.rs:dispatch_command` / `dispatch_command_with_args`
- `codex-rs/tui/src/slash_command.rs:description/supports_inline_args/available_during_task`
