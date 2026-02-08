# Tool: `close_agent` (function)

## 0. 目的
关闭（shutdown）一个子 agent，并返回其最后 status。

## 1. 暴露/启用条件
仅当 `ToolsConfig.collab_tools == true`：
- push_spec：`create_close_agent_tool`
- handler：`builder.register_handler("close_agent", CollabHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_close_agent_tool`
解析类型：`codex-rs/core/src/tools/handlers/collab.rs::CloseAgentArgs`

字段：
- `id`（必填）：agent id（ThreadId 字符串）

## 3. 运行时语义
handler：`CollabHandler` → `close_agent::handle`

步骤：
1) 发 begin 事件：`CollabCloseBeginEvent`
2) 订阅 status：`agent_control.subscribe_status(agent_id)`
   - 若失败：发 end 事件并返回错误
3) 若当前 status 不是 `AgentStatus::Shutdown`：
   - 调用 `agent_control.shutdown_agent(agent_id)`
4) 发 end 事件：`CollabCloseEndEvent`（包含 status）
5) 返回 JSON 字符串：`{"status": <AgentStatus>}`（`CloseAgentResult`）

## 4. 输出
`ToolOutput::Function { content: <JSON string>, success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_close_agent_tool`
- handler：`codex-rs/core/src/tools/handlers/collab.rs`（close_agent 模块）

