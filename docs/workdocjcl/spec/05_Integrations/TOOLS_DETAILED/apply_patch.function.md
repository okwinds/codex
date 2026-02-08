# Tool: `apply_patch` (function)

## 0. 目的（Purpose）
对工作区文件应用补丁（patch），并把结果（包括 diff/错误）回注模型。

本 tool 有两种形态：
- **function 形态**：`ToolSpec::Function(ResponsesApiTool { name:"apply_patch", parameters:{ input:string } })`
- **freeform 形态**：`ToolSpec::Freeform(FreeformTool { name:"apply_patch", format:{ type:"grammar", syntax:"lark", definition:... } })`

本文件覆盖 **function 形态**。

## 1. 暴露/启用条件（Exposed when）
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

当 `ToolsConfig.apply_patch_tool_type == Some(ApplyPatchToolType::Function)`：
- `builder.push_spec(create_apply_patch_json_tool())`
- `builder.register_handler("apply_patch", ApplyPatchHandler)`

> 注意：tool name 恒为 `"apply_patch"`；不同形态由 tool spec 决定。

## 2. 输入（Input arguments）
schema（权威）：`codex-rs/core/src/tools/handlers/apply_patch.rs::create_apply_patch_json_tool`

字段：
- `input`（必填，`String`）：完整的 apply_patch patch 文本（包含 `*** Begin Patch`/`*** End Patch`）

## 3. patch 语法（Grammar / wire format）
语法权威来源：
- Lark grammar：`codex-rs/core/src/tools/handlers/tool_apply_patch.lark`（通过 `include_str!` 注入到 freeform tool 定义）
- 说明文本（人类可读）：`create_apply_patch_json_tool` 的长 description（同 repo 的 tool 使用说明）

## 4. 运行时语义（Runtime semantics）
handler：`codex-rs/core/src/tools/handlers/apply_patch.rs::ApplyPatchHandler`

### 4.1 输入来源
function tool payload：
- `ToolPayload::Function { arguments }` → JSON 解析为 `ApplyPatchToolArgs { input }`

### 4.2 二次校验（安全/可预览）
在真正写文件前，会调用：
- `codex_apply_patch::maybe_parse_apply_patch_verified(&["apply_patch", input], &cwd)`

分支：
- `Body(changes)`：patch 语法正确，得到变更集合（结构化）
- `CorrectnessError(e)`：返回 `RespondToModel("apply_patch verification failed: ...")`
- `ShellParseError(_)`：返回 `RespondToModel("apply_patch handler received invalid patch input")`
- `NotApplyPatch`：返回 `RespondToModel("apply_patch handler received non-apply_patch input")`

### 4.3 应用 patch（两条执行路径）
当得到 `Body(changes)` 后调用：
- `apply_patch::apply_patch(turn, changes).await`

返回 `InternalApplyPatchInvocation`：
1) `Output(item)`：直接产生输出（无需进入 exec/sandbox）
2) `DelegateToExec(apply)`：需要进入 tool orchestrator（含审批/沙箱/差异事件）执行

### 4.4 DelegateToExec 路径（审批/沙箱/事件）
1) 变更转换：
   - `changes = convert_apply_patch_to_protocol(&apply.action)`
2) 收集涉及的绝对路径用于审批 key：
   - `file_paths_for_action(&apply.action)`（包含 move 的目标路径）
3) 事件：
   - `ToolEmitter::apply_patch(changes, apply.auto_approved)` begin/end
4) 组装请求：
   - `ApplyPatchRequest { action, file_paths, changes, exec_approval_requirement, timeout_ms=None, codex_exe=turn.codex_linux_sandbox_exe }`
5) `ToolOrchestrator::run(ApplyPatchRuntime, req, tool_ctx, turn, turn.approval_policy)`

## 5. 输出（Output）
- 成功：`ToolOutput::Function { content: <格式化后的补丁结果>, success: Some(true) }`
- 失败：以 `FunctionCallError` 形式上抛并回注（见 `_COMMON_OUTPUT_ENVELOPE.md`）

## 6. 与其他工具的交互（重要）
`shell` / `shell_command` / `exec_command` 会调用 `intercept_apply_patch`：
- 当模型试图通过执行命令间接运行 apply_patch（比如把 patch 作为命令参数），会拦截并改走本工具流程。

## 7. 代码映射
- handler：`codex-rs/core/src/tools/handlers/apply_patch.rs::ApplyPatchHandler`
- tool spec（function）：`codex-rs/core/src/tools/handlers/apply_patch.rs::create_apply_patch_json_tool`
- tool registry：`codex-rs/core/src/tools/spec.rs::build_specs`
- patch engine：`codex-rs/core/src/apply_patch/*` + `codex-rs/apply-patch/*`
- 公共输出封装：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/_COMMON_OUTPUT_ENVELOPE.md`

