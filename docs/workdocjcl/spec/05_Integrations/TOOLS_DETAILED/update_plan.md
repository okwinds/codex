# Tool: `update_plan` (function)

## 0. 目的
提供一个结构化方式，让模型向客户端提交“任务计划/进度列表”（TODO/checklist），用于 UI 渲染。

重要说明（来自实现注释）：此 tool 的 **输出本身没有实际用处**；有价值的是输入（plan items），供客户端读/渲染。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

该 tool 总会被加入：
- `builder.push_spec(PLAN_TOOL.clone())`
- `builder.register_handler("update_plan", PlanHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/handlers/plan.rs::PLAN_TOOL`

字段：
- `plan`（必填）：数组，每项：
  - `step`（必填 string）
  - `status`（必填 string）：`pending | in_progress | completed`
- `explanation`（可选 string）：对更新原因/策略的说明

客户端约束（来自 tool 描述）：
- 同一时间最多一个 step 处于 `in_progress`

## 3. 运行时语义
handler：`codex-rs/core/src/tools/handlers/plan.rs::PlanHandler`

步骤：
1) 如果当前 collaboration mode 是 `ModeKind::Plan`：
   - 拒绝：`"update_plan is a TODO/checklist tool and is not allowed in Plan mode"`
2) JSON 解析为 `codex_protocol::plan_tool::UpdatePlanArgs`
3) 发送事件：`session.send_event(turn, EventMsg::PlanUpdate(args))`
4) 返回文本 `"Plan updated"`

## 4. 输出
`ToolOutput::Function { content: "Plan updated", success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/handlers/plan.rs::PLAN_TOOL`
- handler：`codex-rs/core/src/tools/handlers/plan.rs::handle_update_plan`

