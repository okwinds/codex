# Tool: `view_image` (function)

## 0. 目的
把本地图片文件作为“用户消息中的 image content items”注入到当前会话，使模型获得该图片的视觉输入（multimodal）。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

该 tool 会被无条件加入，且支持并行：
- `builder.push_spec_with_parallel_support(create_view_image_tool(), true)`
- `builder.register_handler("view_image", ViewImageHandler)`

tool name 常量：
- `codex-rs/protocol/src/models.rs::VIEW_IMAGE_TOOL_NAME = "view_image"`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_view_image_tool`
解析类型：`codex-rs/core/src/tools/handlers/view_image.rs::ViewImageArgs`

字段：
- `path`（必填）：本地图片路径（允许相对；运行时会 resolve）

## 3. 运行时语义
handler：`codex-rs/core/src/tools/handlers/view_image.rs::ViewImageHandler`

步骤：
1) `path` → `abs_path = turn.resolve_path(Some(path))`
2) `tokio::fs::metadata(abs_path)`：
   - 不存在/不可访问 → `"unable to locate image at `<abs>`: ..."`
   - 非文件 → `"image path `<abs>` is not a file"`
3) 生成 content items：
   - `local_image_content_items_with_label_number(&abs_path, None)`
4) 构造并注入一条 user message：
   - `ResponseInputItem::Message { role:"user", content:<image items> }`
   - `session.inject_response_items(vec![input]).await`
   - 若无 active task：报错 `"unable to attach image (no active task)"`
5) 发送事件：`EventMsg::ViewImageToolCall(ViewImageToolCallEvent { call_id, path })`
6) 返回文本：`"attached local image path"`

## 4. 输出
`ToolOutput::Function { content: "attached local image path", success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_view_image_tool`
- handler：`codex-rs/core/src/tools/handlers/view_image.rs`

