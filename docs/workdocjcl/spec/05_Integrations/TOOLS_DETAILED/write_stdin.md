# Tool: `write_stdin` (function)

## 0. 目的（Purpose）
向 `exec_command` 启动的 PTY 会话写入 stdin，并获取最近输出。

## 1. 暴露/启用条件
与 `exec_command` 相同：`ToolsConfig.shell_type == UnifiedExec` 时暴露并注册 handler。
见：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/exec_command.md`

## 2. 输入（Input arguments）
权威解析类型：`codex-rs/core/src/tools/handlers/unified_exec.rs::WriteStdinArgs`

字段：
- `session_id`（必填，`i32`）：要写入的 exec session id（同 `exec_command` 输出里显示的 session id）
- `chars`（可选，默认空字符串）：写入的字符序列（允许空字符串用于“轮询输出”）
- `yield_time_ms`（可选，默认 250）：等待输出时间片
- `max_output_tokens`（可选）：输出 token 上限

> 结构化 schema 参考：`workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`（条目：`name=write_stdin kind=function`）

## 3. 运行时语义
handler：`codex-rs/core/src/tools/handlers/unified_exec.rs::UnifiedExecHandler`

### 3.1 执行
1) `WriteStdinArgs` 解析
2) 调用 `manager.write_stdin(WriteStdinRequest { process_id: session_id.to_string(), input: chars, yield_time_ms, max_output_tokens })`
3) 发送事件 `EventMsg::TerminalInteraction(TerminalInteractionEvent { call_id, process_id, stdin })`
4) 用 `format_response` 把 `UnifiedExecResponse` 转成文本返回

## 4. 输出
`ToolOutput::Function { content: format_response(...), success: Some(true) }`

## 5. 代码映射
- handler：`codex-rs/core/src/tools/handlers/unified_exec.rs`
- 事件：`codex-rs/core/src/protocol/*`（`TerminalInteractionEvent`）

