# Tool: `apply_patch` (freeform custom tool)

## 0. 目的（Purpose）
为支持 freeform/grammar 形式 tool call 的模型（例如 GPT-5 系列）提供更强约束的 patch 输入方式：
- 模型直接输出符合 grammar 的 patch 文本（不包 JSON）
- runtime 仍复用 `ApplyPatchHandler` 处理与审批/沙箱逻辑

## 1. 暴露/启用条件（Exposed when）
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

当 `ToolsConfig.apply_patch_tool_type == Some(ApplyPatchToolType::Freeform)`：
- `builder.push_spec(create_apply_patch_freeform_tool())`
- `builder.register_handler("apply_patch", ApplyPatchHandler)`

## 2. 输入（Input）
custom tool call payload：
- `ToolPayload::Custom { input: String }`
- 该 input 即 patch 全文（应满足 grammar）

## 3. Grammar（权威）
- `codex-rs/core/src/tools/handlers/tool_apply_patch.lark`（`APPLY_PATCH_LARK_GRAMMAR`）
- tool spec 构造：`codex-rs/core/src/tools/handlers/apply_patch.rs::create_apply_patch_freeform_tool`

## 4. 运行时语义（Runtime semantics）
与 function 形态一致（见 `apply_patch.function.md`），区别仅在“输入来源”：
- freeform：直接使用 `ToolPayload::Custom.input` 作为 patch_input
- function：先 JSON 解析出 `input`

## 5. 输出
同 function 形态：`ToolOutput::Function { content, success: Some(true) }`

## 6. 代码映射
- handler：`codex-rs/core/src/tools/handlers/apply_patch.rs::ApplyPatchHandler`
- tool spec（freeform）：`codex-rs/core/src/tools/handlers/apply_patch.rs::create_apply_patch_freeform_tool`

