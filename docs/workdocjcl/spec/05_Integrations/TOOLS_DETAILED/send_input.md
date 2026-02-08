# Tool: `send_input` (function)

## 0. 目的
向已存在的子 agent 发送消息（可选 interrupt）。

## 1. 暴露/启用条件
仅当 `ToolsConfig.collab_tools == true`：
- push_spec：`create_send_input_tool`
- handler：`builder.register_handler("send_input", CollabHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_send_input_tool`
解析类型：`codex-rs/core/src/tools/handlers/collab.rs::send_input::SendInputArgs`

字段：
- `id`（必填）：agent id（ThreadId 字符串）
- `message`（必填）：消息内容（trim 后不能为空）
- `interrupt`（默认 false）：true 则先中断 agent 当前任务

## 3. 运行时语义
handler：`CollabHandler` → `send_input::handle`

步骤：
1) 解析 `id` → `ThreadId`（非法 → `"invalid agent id ..."`）
2) 校验 message 非空
3) 若 `interrupt=true` → `agent_control.interrupt_agent(receiver_thread_id)`
4) 发 begin 事件：`CollabAgentInteractionBeginEvent`
5) 调用 `agent_control.send_prompt(receiver_thread_id, prompt)`
6) 获取 status（`get_status`），发 end 事件：`CollabAgentInteractionEndEvent`
7) 返回 JSON 字符串：`{"submission_id":"<id>"}`（`SendInputResult`）

## 4. 输出
`ToolOutput::Function { content: <JSON string>, success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_send_input_tool`
- handler：`codex-rs/core/src/tools/handlers/collab.rs`（send_input 模块）

