# Tool: `spawn_agent` (function)

## 0. 目的
创建一个子 agent（子线程/子会话）执行一个独立子任务，并返回可用于后续通信的 `agent_id`。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

仅当 `ToolsConfig.collab_tools == true`（feature `Collab` enabled）：
- push_spec：`create_spawn_agent_tool`
- handler：`builder.register_handler("spawn_agent", CollabHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_spawn_agent_tool`
解析类型：`codex-rs/core/src/tools/handlers/collab.rs::spawn::SpawnAgentArgs`

字段：
- `message`（必填）：子任务描述（trim 后不能为空）
- `agent_type`（可选）：agent role（`AgentRole` enum）；缺省 `Default`

## 3. 运行时语义
handler：`codex-rs/core/src/tools/handlers/collab.rs::CollabHandler` → `spawn::handle`

关键步骤：
1) 校验 prompt 非空（空 → `"Empty message can't be sent to an agent"`）
2) 计算 spawn depth：
   - `session_source = turn.client.get_session_source()`
   - `child_depth = next_thread_spawn_depth(&session_source)`
   - 若 `exceeds_thread_spawn_depth_limit(child_depth)` → 拒绝 `"Agent depth limit reached. Solve the task yourself."`
3) 发 begin 事件：`CollabAgentSpawnBeginEvent`
4) 构造子 agent Config（`build_agent_spawn_config`）并应用 role：`agent_role.apply_to_config(&mut config)`
5) 调用 `session.services.agent_control.spawn_agent(config, prompt, Some(SessionSource::SubAgent(...)))`
6) 发 end 事件：`CollabAgentSpawnEndEvent`（包含 new_thread_id + status）
7) 返回 JSON 字符串：`{"agent_id": "<thread_id>"}`（`SpawnAgentResult`）

## 4. 输出
`ToolOutput::Function { content: <JSON string>, success: Some(true) }`

## 5. 错误
典型错误：
- prompt 为空
- spawn depth 超限
- agent_control 不可用 / thread not found / internal died（会被映射为 `RespondToModel` 文本）

## 6. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_spawn_agent_tool`
- handler：`codex-rs/core/src/tools/handlers/collab.rs`（spawn 模块）

