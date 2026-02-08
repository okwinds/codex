# Tool: `exec_command` (function, PTY-backed)

## 0. 目的（Purpose）
在 PTY（伪终端）中运行命令，支持：
- 输出分块/交互式会话（返回 session id / process id）
- 后续通过 `write_stdin` 向会话写入 stdin 并获取新输出

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

当 `ToolsConfig.shell_type == UnifiedExec`：
- `builder.push_spec(create_exec_command_tool(request_rule_enabled))`
- `builder.push_spec(create_write_stdin_tool())`
- `builder.register_handler("exec_command", UnifiedExecHandler)`
- `builder.register_handler("write_stdin", UnifiedExecHandler)`

## 2. 输入（Input arguments）
权威 schema：`codex-rs/core/src/tools/spec.rs::create_exec_command_tool`
权威解析类型：`codex-rs/core/src/tools/handlers/unified_exec.rs::ExecCommandArgs`

字段：
- `cmd`（必填，`String`）：要执行的命令字符串（会被转换为 argv）
- `workdir`（可选）：工作目录（空字符串会被过滤为 None）
- `shell`（可选）：模型指定的 shell 路径或别名（会影响 argv 生成）
- `login`（可选，默认 true）：是否使用 login shell 语义
- `tty`（可选，默认 false）：是否分配 TTY（true→打开 PTY 并可交互）
- `yield_time_ms`（可选，默认 10000）：等待输出的时间片（毫秒）
- `max_output_tokens`（可选）：输出 token 上限（超出截断）
- `sandbox_permissions` / `justification` / `prefix_rule`：
  - 与 `shell` 同语义
  - `prefix_rule` 仅在 feature `RequestRule` 启用时保留（否则丢弃）

> 结构化 schema 参考：`workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`（条目：`name=exec_command kind=function`）

## 3. 运行时语义（Runtime semantics）
handler：`codex-rs/core/src/tools/handlers/unified_exec.rs::UnifiedExecHandler`

### 3.1 命令 argv 生成
`get_command(args, session.user_shell())`：
- 若 `args.shell` 存在：使用 `get_shell_by_model_provided_path(PathBuf::from(shell_str))` 构造 shell（并设置空 snapshot receiver）
- 否则使用 session 的用户 shell
- 最终调用 `shell.derive_exec_args(&args.cmd, args.login)` 得到 argv

### 3.2 审批策略硬门槛
与 `shell` 一致：
- 若请求 `sandbox_permissions=RequireEscalated` 且 `turn.approval_policy != OnRequest` → 直接拒绝
- 被拒绝时会释放已分配的 process_id

### 3.3 apply_patch 拦截
在真正执行前，对生成的 argv + cwd 做 `intercept_apply_patch`：
- 若检测到 apply_patch：改走 apply_patch 处理，并提前释放 process_id

### 3.4 执行与会话
1) `process_id = manager.allocate_process_id()`
2) 组装 `ExecCommandRequest { command, process_id, yield_time_ms, max_output_tokens, workdir, tty, sandbox_permissions, justification, prefix_rule }`
3) 调用 `manager.exec_command(request, context).await` 得到 `UnifiedExecResponse`

### 3.5 输出格式化
`format_response(&UnifiedExecResponse)` 输出文本包含（按顺序）：
- Chunk ID（若非空）
- Wall time
- exit code（若已退出）
- session id / process id（若仍在运行）
- Original token count（若存在）
- Output: + stdout/stderr 聚合输出

## 4. 输出（Output）
返回 `ToolOutput::Function { content: format_response(...), success: Some(true) }`

## 5. 代码映射
- tool schema：`codex-rs/core/src/tools/spec.rs::create_exec_command_tool`
- handler：`codex-rs/core/src/tools/handlers/unified_exec.rs::UnifiedExecHandler`
- manager/runtime：`codex-rs/core/src/unified_exec/*`

