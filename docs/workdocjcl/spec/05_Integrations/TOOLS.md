# 内置工具目录（Tool Catalog）

Codex 的核心能力来自“模型调用工具（tool calls）→ 本地 runtime 执行 → 结果回注模型”。本章列出 **核心内置工具**（不包含所有测试/演示用工具），并给出启用条件与实现锚点。

> 权威来源：`codex-rs/core/src/tools/spec.rs`（工具 schema 与名称的最终定义处）。

## 0. 相关规格（Replication-critical）
本文件是“目录级概览”。要达到可复刻，需要同时参考：
- 工具 schema（机器可读）：`docs/workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`
- 工具 schema（人类摘要）：`docs/workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.md`
- 逐工具行为规格（含审批/沙箱/错误路径）：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/INDEX.md`
- 公共输出封装（所有 tool 通用）：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/_COMMON_OUTPUT_ENVELOPE.md`

## 1. 工具启用条件（ToolsConfig）
工具集并非固定；它会受到以下因素影响：
- features（例如 `shell_tool`、`unified_exec`、`apply_patch_freeform`、`collab` 等）
- model capability（`ModelInfo.shell_type`、`ModelInfo.apply_patch_tool_type`、`experimental_supported_tools`）
- web_search mode（config + feature）

## 2. 核心工具（Core tools）

| tool name | 类别 | 用途 | 关键启用条件（简述） |
|---|---|---|---|
| `shell` | tool | 在 shell 中执行命令（实现取决于 shell_type） | `Feature::ShellTool` enabled |
| `shell_command` | tool | 非 PTY 的 shell command 执行（更简单） | 由 model_info/shell_type 决定 |
| `exec_command` | tool | PTY-backed exec（可返回 session id 进行交互） | `Feature::UnifiedExec` 或 model 支持 |
| `write_stdin` | tool | 向已启动的 exec session 写入 stdin | 依赖 exec session 生命周期 |
| `send_input` | tool | 向 agent/子 agent 发送输入（协作/多 agent） | collab/collaboration features |
| `wait` | tool | 等待某异步操作/agent 完成（带 timeout） | collab tools enabled |
| `spawn_agent` | tool | 生成子 agent 执行子任务 | `Feature::Collab` enabled |
| `close_agent` | tool | 关闭子 agent | collab tools enabled |
| `request_user_input` | tool | 询问用户 1-3 个多选问题并等待回答 | UI 支持 request_user_input flow |
| `read_file` | tool | 读取文件内容（受 sandbox/read permissions） | 基础工具 |
| `list_dir` | tool | 列出目录内容 | 基础工具 |
| `grep_files` | tool | 在工作区内搜索文本 | 基础工具 |
| `list_mcp_resources` | tool | 列出 MCP resources | MCP enabled + server connected |
| `list_mcp_resource_templates` | tool | 列出 MCP resource templates | MCP enabled + server connected |
| `read_mcp_resource` | tool | 读取 MCP resource | MCP enabled + server connected |
| `update_plan` | tool | 更新计划（UI 展示计划/进度） | 常用（PLAN_TOOL） |
| `view_image` | tool | 读取本地图片（用于 multimodal） | model 支持图像输入时更常用 |

## 3. apply_patch 工具（重要）
apply_patch 的具体 tool schema 会根据：
- feature `apply_patch_freeform`
- model capability `apply_patch_tool_type`
选择不同形态（function vs freeform）。复刻时必须确保：
- patch 格式与解析严格一致
- apply_patch 的写文件行为受 approvals/sandbox 控制

## 4. Web search 工具（可选）
web search 工具受 `web_search` config 与 feature 影响：
- disabled / cached / live
复刻时至少要保证：
- 当禁用时，不向模型暴露 web search 能力
- 当启用时，产出结构化结果并受 sandbox/network 策略约束

## 5. 来源（Source）
- 工具 schema：`codex-rs/core/src/tools/spec.rs`
- tool router/runtime：`codex-rs/core/src/tools/router.rs`、`codex-rs/core/src/tools/runtimes/`
- apply_patch handlers：`codex-rs/core/src/tools/handlers/apply_patch/*`

## 6. Legacy aliases（兼容性）
运行时会接受但不一定暴露给模型的 tool name：
- `container.exec`：`shell` 的历史别名（同一参数结构 `ShellToolCallParams`）
  - 详见：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/container.exec.md`
