# Tools Detailed Specs（逐工具规格）

本目录以“可复刻”为目标，为每个内置 tool 给出：
- **输入 schema**（来自 `TOOLS_SCHEMA_REFERENCE.json`）
- **启用/暴露条件**（来自 `codex-rs/core/src/tools/spec.rs::build_specs`）
- **运行时语义**（对应 handler 的决策树、审批/沙箱交互、输出封装、错误路径）
- **代码映射锚点**（便于随时核对“代码 ↔ 文档”）

> 机器可读 schema 总表：`docs/workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`  
> 入口：`codex-rs/core/src/tools/spec.rs` + `codex-rs/core/src/tools/router.rs`

## 1) Function tools（模型发起 JSON 参数的 function call）
- `apply_patch`（function 形态）：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/apply_patch.function.md`
- `close_agent`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/close_agent.md`
- `exec_command`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/exec_command.md`
- `grep_files`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/grep_files.md`
- `list_dir`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/list_dir.md`
- `list_mcp_resources`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/list_mcp_resources.md`
- `list_mcp_resource_templates`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/list_mcp_resource_templates.md`
- `read_file`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/read_file.md`
- `read_mcp_resource`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/read_mcp_resource.md`
- `request_user_input`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/request_user_input.md`
- `send_input`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/send_input.md`
- `shell`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/shell.md`
- `shell_command`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/shell_command.md`
- `spawn_agent`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/spawn_agent.md`
- `test_sync_tool`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/test_sync_tool.md`
- `update_plan`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/update_plan.md`
- `view_image`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/view_image.md`
- `wait`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/wait.md`
- `write_stdin`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/write_stdin.md`

## 2) Custom tools（freeform）
- `apply_patch`（freeform 形态）：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/apply_patch.freeform.md`

## 3) Non-function tool types
- `local_shell`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/local_shell.md`
- `web_search`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/web_search.md`

## 4) Legacy / alias tool names（运行时接受但可能不暴露给模型）
- `container.exec`：`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/container.exec.md`

