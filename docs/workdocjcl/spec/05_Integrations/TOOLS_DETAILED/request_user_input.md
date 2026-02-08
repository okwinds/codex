# Tool: `request_user_input` (function)

## 0. 目的
让模型向用户提出 1–3 个多选问题，并等待用户选择结果；用于在“计划/协作”模式下做关键决策分支。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

仅当 `ToolsConfig.collaboration_modes_tools == true`：
- `builder.push_spec(create_request_user_input_tool())`
- `builder.register_handler("request_user_input", RequestUserInputHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_request_user_input_tool`
解析类型：`codex_protocol::request_user_input::RequestUserInputArgs`

核心字段：
- `questions`（必填，数组，长度 1–3）：
  - `id`（必填）：stable identifier（snake_case）
  - `header`（必填）：短标题（≤12 chars）
  - `question`（必填）：单句问题
  - `options`（必填）：2–3 个互斥选项（label/description）
    - 注意：实现会强制为每个 question 加一个 “Other”（free-form）选项（见下）

## 3. 运行时语义
handler：`codex-rs/core/src/tools/handlers/request_user_input.rs::RequestUserInputHandler`

### 3.1 模式门槛
仅允许在以下 mode 使用：
- `ModeKind::Plan`
- `ModeKind::PairProgramming`

否则报错：`"request_user_input is unavailable in {mode_name} mode"`

### 3.2 选项合法性
- 要求每个 question 都有 non-empty options（否则报错）

### 3.3 自动添加 Other
对每个 question：
- `question.is_other = true;`

（客户端会基于此添加 free-form “Other” 选项；tool schema 里禁止模型显式提供 Other）

### 3.4 等待用户响应
调用：
- `session.request_user_input(turn, call_id, args).await`

若用户取消/未收到响应：
- 报错 `"request_user_input was cancelled before receiving a response"`

收到响应后：
- 序列化为 JSON 字符串作为 tool output content 返回

## 4. 输出
`ToolOutput::Function { content: <JSON string>, success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_request_user_input_tool`
- handler：`codex-rs/core/src/tools/handlers/request_user_input.rs`

