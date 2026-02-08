# Tool: `web_search` (tool type: `web_search`)

## 0. 目的
向 OpenAI Responses API 声明启用 `type="web_search"` 工具，让模型可以触发“外部网页搜索”（cached 或 live）。

本工具不是本地 function tool：
- 本仓库不会在本地执行搜索命令
- 搜索结果由 provider/模型侧产生，并以 Responses API 的 item/event 形态回传

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

由 `ToolsConfig.web_search_mode` 控制：
- `Some(Cached)` → `ToolSpec::WebSearch { external_web_access: Some(false) }`
- `Some(Live)` → `ToolSpec::WebSearch { external_web_access: Some(true) }`
- `Disabled/None` → 不暴露 web_search tool

> 该 tool spec 没有 JSON schema（不是 function），仅包含 `external_web_access` 配置。

## 2. 运行时语义
### 2.1 tool list 暴露
`ToolRouter::specs()` 会把 `ToolSpec::WebSearch` 序列化进 tools 列表，交给 provider。

### 2.2 结果处理
本仓库的 turn loop 会照常处理 provider 返回的 response items；但不需要（也不能）像 function tool 那样 dispatch 到本地 handler。

## 3. 代码映射
- 暴露点：`codex-rs/core/src/tools/spec.rs::build_specs`
- tool router：`codex-rs/core/src/tools/router.rs`

