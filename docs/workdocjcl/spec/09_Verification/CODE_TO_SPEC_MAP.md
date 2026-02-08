# 代码到规格文档映射（Code → Spec Map）

本文件用于“随时核对代码与规格文档的映射关系”。原则：
- **关键入口/关键契约** 必须在某个 spec 文档中被明确描述。
- **文件存在性清单** 用于避免遗漏：
  - repo-only（无遗漏基线）：`docs/workdocjcl/inventory/file_manifest_repo.txt`
  - 全量（含 `workdocjcl/` 生成物）：`docs/workdocjcl/inventory/file_manifest.txt`
  - 语义/行为仍以本映射表与各章节 spec 为准。

## 1. 顶层入口与分发
| 代码位置 | 责任 | 规格文档 |
|---|---|---|
| `README.md` | 用户安装/入口说明 | `docs/workdocjcl/spec/00_Overview/PROJECT.md` |
| `codex-cli/package.json` | npm 包元数据 | `docs/workdocjcl/spec/07_Infrastructure/PACKAGING.md` |
| `codex-cli/bin/codex.js` | Node wrapper：平台探测/执行/信号转发 | `docs/workdocjcl/spec/07_Infrastructure/PACKAGING.md`、`docs/workdocjcl/spec/04_Business_Logic/RULES.md` |

## 2. Rust CLI 多工具入口
| 代码位置 | 责任 | 规格文档 |
|---|---|---|
| `codex-rs/cli/src/main.rs` | `codex` 子命令、参数解析与分发 | `docs/workdocjcl/spec/03_API/CLI.md`、`docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md` |
| `codex-rs/common/src/config_override.rs` | `-c key=value` 覆盖解析 | `docs/workdocjcl/spec/03_API/CLI.md`、`docs/workdocjcl/spec/08_Testing/UNIT_SPECS.md` |
| `codex-rs/cli/src/login.rs` | login/logout/status 与 stdin API key | `docs/workdocjcl/spec/03_API/AUTHENTICATION.md`、`docs/workdocjcl/spec/04_Business_Logic/RULES.md` |
| `codex-rs/app-server/src/main.rs` | `codex app-server`：stdio JSONL server 入口（rich clients） | `docs/workdocjcl/spec/03_API/APP_SERVER.md` |

## 3. Core engine（turn loop / tools / events）
| 代码位置 | 责任 | 规格文档 |
|---|---|---|
| `codex-rs/core/src/codex.rs` | `Codex`：Submission/Event 抽象与 turn loop 主流程 | `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`、`docs/workdocjcl/spec/04_Business_Logic/WORKFLOWS.md` |
| `codex-rs/protocol/src/protocol.rs` | `AgentStatus`、事件类型、错误枚举等 | `docs/workdocjcl/spec/04_Business_Logic/STATE_MACHINES.md`、`docs/workdocjcl/spec/03_API/ERRORS.md` |
| `codex-rs/protocol/src/models.rs` | Base/Developer instructions、permissions 文案、EnvironmentContext 等 prompt primitives | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`、`docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md` |
| `codex-rs/protocol/src/openai_models.rs` | `ModelInfo`、`ModelMessages`（instructions_template + personality variables） | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`、`docs/workdocjcl/spec/05_Integrations/MODEL_PROVIDERS.md` |
| `codex-rs/core/src/config/mod.rs` | `ConfigToml` 与 config loader | `docs/workdocjcl/spec/01_Configuration/ENVIRONMENT.md`、`docs/workdocjcl/spec/01_Configuration/FEATURE_FLAGS.md` |
| `codex-rs/core/config.schema.json` | config.toml 的权威 JSON Schema | `docs/workdocjcl/spec/01_Configuration/CONFIG_TOML.md` |
| `codex-rs/core/src/features.rs` | features registry 与 defaults | `docs/workdocjcl/spec/01_Configuration/FEATURE_FLAGS.md` |
| `codex-rs/core/src/project_doc.rs` | AGENTS.md 发现/拼接 + skills section/hierarchical agents message 注入 | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md` |
| `codex-rs/core/src/instructions/user_instructions.rs` | `UserInstructions`/`SkillInstructions` 的 XML 包裹与编码格式 | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`、`docs/workdocjcl/spec/05_Integrations/SKILLS.md` |
| `codex-rs/core/src/models_manager/model_info.rs` | 内置 `prompt.md`/模型 instructions 模板与 personality 文本来源 | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`、`docs/workdocjcl/spec/04_Business_Logic/SYSTEM_PRESET_PROMPTS.md`、`docs/workdocjcl/spec/04_Business_Logic/PROMPTS/INDEX.md`、`docs/workdocjcl/spec/05_Integrations/MODEL_PROVIDERS.md` |
| `codex-rs/core/src/client_common.rs` | core `Prompt` 类型（instructions/input/tools/output_schema） | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md` |
| `codex-rs/core/src/client.rs` | Prompt → API payload 适配（instructions 字段、tool outputs reserialize） | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS.md` |
| `codex-rs/core/src/client.rs` | Responses streaming：SSE/WS 选择、增量 append、request options（reasoning/text/compression） | `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md`、`docs/workdocjcl/spec/05_Integrations/MODEL_PROVIDERS.md` |
| `codex-rs/core/src/model_provider_info.rs` | **Chat wire 已移除**：`wire_api = "chat"` 配置解析时直接报错；以及 `ollama-chat` legacy provider 移除 | `docs/workdocjcl/spec/05_Integrations/CHAT_WIRE_MAPPING.md`、`docs/workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md` |
| `codex-rs/core/src/compact.rs` | compaction turn：摘要 prompt、history 重建、初始上下文再注入 | `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`、`docs/workdocjcl/spec/04_Business_Logic/WORKFLOWS.md` |
| `codex-rs/core/src/client.rs` | Responses WS→HTTP 回退状态（一次性禁用 websockets；例如 `UPGRADE_REQUIRED` 后降级） | `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md` |
| `codex-rs/core/src/api_bridge.rs` | ApiError → CodexErr（retryable delay/401/429 等） | `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md`、`docs/workdocjcl/spec/03_API/ERRORS.md` |
| `codex-rs/core/src/exec_policy.rs` | execpolicy 加载/合并、未匹配 fallback、审批需求生成、amendment 更新 | `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md`、`docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`、`docs/workdocjcl/spec/07_Infrastructure/COMMAND_SAFETY.md` |
| `codex-rs/core/src/config_loader/requirements_exec_policy.rs` | requirements.toml → execpolicy（仅 prompt/forbidden） | `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md` |
| `codex-rs/execpolicy/*` | execpolicy 语言（Starlark builtin）、Policy/Evaluation、amend 写入 | `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md` |
| `codex-rs/core/src/command_safety/is_safe_command.rs` | 已知安全命令启发式（safe allowlist + flag 限制） | `docs/workdocjcl/spec/07_Infrastructure/COMMAND_SAFETY.md` |
| `codex-rs/core/src/command_safety/is_dangerous_command.rs` | 可能危险命令启发式（git/rm/sudo 等） | `docs/workdocjcl/spec/07_Infrastructure/COMMAND_SAFETY.md` |
| `codex-rs/core/src/bash.rs` | `bash/zsh -lc` 脚本拆解（word-only 子集） | `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md`、`docs/workdocjcl/spec/07_Infrastructure/COMMAND_SAFETY.md` |
| `codex-rs/core/src/tools/orchestrator.rs` | 审批→沙箱→执行→sandbox deny 重试的统一编排 | `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md` |
| `codex-rs/core/src/tools/sandboxing.rs` | ApprovalStore/with_cached_approval/ExecApprovalRequirement 等审批底座 | `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md` |
| `codex-rs/protocol/src/approvals.rs` | exec/apply_patch 等审批事件 + execpolicy amendment | `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`、`docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md` |
| `codex-rs/core/src/skills/loader.rs` | skills roots/扫描/frontmatter/agents/openai.yaml 解析 | `docs/workdocjcl/spec/05_Integrations/SKILLS.md` |
| `codex-rs/core/src/skills/system.rs` | embedded system skills 写入 `CODEX_HOME/skills/.system`（marker 指纹） | `docs/workdocjcl/spec/05_Integrations/SKILLS.md`、`docs/workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS.md` |
| `codex-rs/core/src/skills/manager.rs` | per-cwd cache、user-layer-only enabled/disabled 语义 | `docs/workdocjcl/spec/05_Integrations/SKILLS.md` |
| `codex-rs/core/src/skills/injection.rs` | `$name`/`[$name](path)` mentions 解析、消歧、注入读取 | `docs/workdocjcl/spec/05_Integrations/SKILLS.md` |
| `codex-rs/core/src/skills/env_var_dependencies.rs` | env_var 依赖收集与 `request_user_input` 提示（session-only） | `docs/workdocjcl/spec/05_Integrations/SKILLS.md` |
| `codex-rs/core/src/skills/render.rs` | skills section 文案（注入到 UserInstructions） | `docs/workdocjcl/spec/05_Integrations/SKILLS.md`、`docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md` |
| `codex-rs/app-server/src/lib.rs` | app-server：stdio JSONL read/write、task wiring、线程监听自动 attach | `docs/workdocjcl/spec/03_API/APP_SERVER.md` |
| `codex-rs/app-server/src/message_processor.rs` | app-server：initialize 门禁、experimentalApi gating、config API 分流 | `docs/workdocjcl/spec/03_API/APP_SERVER.md` |
| `codex-rs/app-server/src/outgoing_message.rs` | app-server：OutgoingMessage（request/notification/response/error）与回调管理 | `docs/workdocjcl/spec/03_API/APP_SERVER.md` |
| `codex-rs/app-server/src/bespoke_event_handling.rs` | app-server：core events → app-server notifications/requests（approvals/tool) | `docs/workdocjcl/spec/03_API/APP_SERVER.md`、`docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md` |
| `codex-rs/app-server-protocol/src/jsonrpc_lite.rs` | app-server 协议：JSONRPC message shapes（无 jsonrpc 字段） | `docs/workdocjcl/spec/03_API/APP_SERVER.md` |
| `codex-rs/app-server-protocol/src/protocol/*` | app-server 协议：ClientRequest/ServerNotification 等 method 与 schema 导出 | `docs/workdocjcl/spec/03_API/APP_SERVER.md` |
| `codex-rs/codex-api/src/sse/responses.rs` | Responses SSE：headers→事件、event type 解析、idle timeout、response.failed 分类 | `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md` |
| `codex-rs/codex-api/src/endpoint/responses_websocket.rs` | Responses WebSocket：connect headers(turn_state)、ping/pong、event type 解析与 Completed 终止 | `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md` |
| `codex-rs/codex-api/src/common.rs` | Responses streaming 公共事件类型（ResponseEvent/ResponsesWsRequest） | `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md` |
| `codex-rs/codex-api/src/provider.rs` | Provider：base_url/path/query_params 拼接、Azure endpoint 检测、WS URL 推导 | `docs/workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md` |
| `codex-rs/codex-api/src/endpoint/responses.rs` | ResponsesClient：ResponsesOptions（reasoning/include/text/store_override/compression/turn_state） | `docs/workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md`、`docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md` |
| `codex-rs/codex-api/src/endpoint/aggregate.rs` | `AggregatedStream`：对上层提供“聚合视图”（把 SSE deltas 聚合为更稳定的事件形状） | `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md` |
| `codex-rs/codex-api/src/requests/responses.rs` | Responses 请求体：store 默认与 Azure attach_item_ids | `docs/workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md` |
| `codex-rs/codex-api/src/rate_limits.rs` | Codex bespoke rate-limit/credits headers → RateLimitSnapshot | `docs/workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md` |

## 4. 状态与持久化（state.sqlite）
| 代码位置 | 责任 | 规格文档 |
|---|---|---|
| `codex-rs/state/migrations/*.sql` | schema 真实来源 | `docs/workdocjcl/spec/02_Data/ENTITIES.md`、`docs/workdocjcl/spec/02_Data/MIGRATIONS.md` |
| `codex-rs/state/src/runtime.rs` | `StateRuntime`：DB init/query/insert | `docs/workdocjcl/spec/02_Data/ENTITIES.md`、`docs/workdocjcl/spec/02_Data/RELATIONSHIPS.md` |
| `codex-rs/protocol/src/protocol.rs` | rollout JSONL 类型（RolloutLine/RolloutItem） | `docs/workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`、`docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md` |
| `codex-rs/core/src/rollout/recorder.rs` | rollout 写入 + 加载历史（resume） | `docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md` |
| `codex-rs/core/src/rollout/policy.rs` | rollout 持久化过滤（哪些 RolloutItem/EventMsg/ResponseItem 会写入） | `docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md` |
| `codex-rs/core/src/rollout/truncation.rs` | fork 截断（用户 turn 边界 + rollback 标记） | `docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md` |
| `codex-rs/core/src/thread_manager.rs` | resume/fork thread 的历史选择与 spawn | `docs/workdocjcl/spec/04_Business_Logic/WORKFLOWS.md`、`docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md` |
| `codex-rs/core/src/codex.rs` | rollout 回放重建（reconstruct/seed initial context/token_info） | `docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md`、`docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md` |
| `codex-rs/state/src/extract.rs` | rollout → ThreadMetadata 抽取规则 | `docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md` |

## 5. 模型提供方与网络集成
| 代码位置 | 责任 | 规格文档 |
|---|---|---|
| `codex-rs/core/src/model_provider_info.rs` | providers registry、wire_api、重试/超时、env headers | `docs/workdocjcl/spec/05_Integrations/MODEL_PROVIDERS.md`、`docs/workdocjcl/spec/01_Configuration/ENVIRONMENT.md` |
| `codex-rs/responses-api-proxy/` | 本地严格代理（内部用途） | `docs/workdocjcl/spec/03_API/ENDPOINTS.md` |
| `codex-rs/core/src/tools/spec.rs` | tool schema（名称/参数/输出、启用条件） | `docs/workdocjcl/spec/05_Integrations/TOOLS.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/INDEX.md` |
| `codex-rs/core/src/tools/router.rs` | tool call 解析/dispatch/失败封装 | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/_COMMON_OUTPUT_ENVELOPE.md` |
| `codex-rs/core/src/tools/handlers/shell.rs` | `shell`/`shell_command`/`container.exec`/`local_shell` 执行与审批 | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/shell.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/shell_command.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/container.exec.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/local_shell.md` |
| `codex-rs/core/src/tools/handlers/unified_exec.rs` | `exec_command`/`write_stdin`（PTY 会话） | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/exec_command.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/write_stdin.md` |
| `codex-rs/core/src/tools/handlers/apply_patch.rs` | `apply_patch`（function/freeform）+ intercept | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/apply_patch.function.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/apply_patch.freeform.md` |
| `codex-rs/core/src/tools/handlers/read_file.rs` | `read_file`（slice/indentation） | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/read_file.md` |
| `codex-rs/core/src/tools/handlers/list_dir.rs` | `list_dir` | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/list_dir.md` |
| `codex-rs/core/src/tools/handlers/grep_files.rs` | `grep_files`（rg 搜索） | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/grep_files.md` |
| `codex-rs/core/src/tools/handlers/view_image.rs` | `view_image` | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/view_image.md` |
| `codex-rs/core/src/tools/handlers/plan.rs` | `update_plan`（TODO/checklist） | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/update_plan.md` |
| `codex-rs/core/src/tools/handlers/request_user_input.rs` | `request_user_input` | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/request_user_input.md` |
| `codex-rs/core/src/tools/handlers/collab.rs` | `spawn_agent`/`send_input`/`wait`/`close_agent` | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/spawn_agent.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/send_input.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/wait.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/close_agent.md` |
| `codex-rs/core/src/tools/handlers/mcp_resource.rs` | `list_mcp_resources`/`list_mcp_resource_templates`/`read_mcp_resource` | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/list_mcp_resources.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/list_mcp_resource_templates.md`、`docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/read_mcp_resource.md` |
| `codex-rs/core/src/tools/handlers/test_sync.rs` | `test_sync_tool`（测试同步/屏障） | `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/test_sync_tool.md` |

## 6. MCP 集成
| 代码位置 | 责任 | 规格文档 |
|---|---|---|
| `codex-rs/core/src/config/types.rs` | `McpServerConfig`、transport config | `docs/workdocjcl/spec/05_Integrations/MCP.md` |
| `codex-rs/mcp-server/` | `codex mcp-server`（stdio MCP server） | `docs/workdocjcl/spec/05_Integrations/MCP.md` |
| `shell-tool-mcp/` | Node MCP server（shell tool） | `docs/workdocjcl/spec/00_Overview/PROJECT.md`、`docs/workdocjcl/spec/08_Testing/INTEGRATION_SPECS.md` |

## 7. UI（TUI）
| 代码位置 | 责任 | 规格文档 |
|---|---|---|
| `codex-rs/tui/src/lib.rs` | TUI 主入口 `run_main` | `docs/workdocjcl/spec/06_UI/TUI.md` |
| `codex-rs/tui/src/app.rs` | App 状态机 | `docs/workdocjcl/spec/06_UI/TUI.md` |
| `codex-rs/tui/src/app_backtrack.rs` | Backtrack（Esc/Enter）与 overlay 路由/退出语义 | `docs/workdocjcl/spec/06_UI/TUI_KEYBINDINGS.md` |
| `codex-rs/tui/src/chatwidget.rs` | 对话/流式渲染 | `docs/workdocjcl/spec/06_UI/TUI.md` |
| `codex-rs/tui/src/slash_command.rs` | SlashCommand 枚举、描述、task gating 与展示顺序 | `docs/workdocjcl/spec/06_UI/TUI_SLASH_COMMANDS.md` |
| `codex-rs/tui/src/bottom_pane/slash_commands.rs` | slash 命令 gating + builtin 查找（composer/popup 共享） | `docs/workdocjcl/spec/06_UI/TUI_SLASH_COMMANDS.md` |
| `codex-rs/tui/src/bottom_pane/chat_composer.rs` | 输入框状态机（草稿/粘贴/附件/弹窗/提交准备） | `docs/workdocjcl/spec/06_UI/TUI_COMPOSER.md` |
| `codex-rs/tui/src/bottom_pane/paste_burst.rs` | 非 bracketed paste burst 检测状态机（Windows 终端 key 流粘贴） | `docs/workdocjcl/spec/06_UI/TUI_PASTE_BURST.md`、`docs/workdocjcl/spec/06_UI/TUI_COMPOSER.md` |
| `codex-rs/tui/src/bottom_pane/command_popup.rs` | slash/custom prompt 弹窗（筛选/选中/渲染） | `docs/workdocjcl/spec/06_UI/TUI_COMPOSER.md`、`docs/workdocjcl/spec/06_UI/TUI_PROMPTS.md` |
| `codex-rs/tui/src/bottom_pane/file_search_popup.rs` | `@` 文件搜索弹窗（等待/结果/选择） | `docs/workdocjcl/spec/06_UI/TUI_COMPOSER.md` |
| `codex-rs/tui/src/bottom_pane/skill_popup.rs` | `$` mentions 弹窗（skills/connectors） | `docs/workdocjcl/spec/06_UI/TUI_COMPOSER.md` |
| `codex-rs/tui/src/bottom_pane/prompt_args.rs` | `/prompts:` 参数解析与展开（保留 TextElement） | `docs/workdocjcl/spec/06_UI/TUI_PROMPTS.md` |
| `codex-rs/tui/src/bottom_pane/approval_overlay.rs` | 审批弹窗（exec/apply_patch/MCP），快捷键与队列 | `docs/workdocjcl/spec/06_UI/TUI_APPROVALS.md` |
| `codex-rs/tui/src/bottom_pane/mod.rs` | bottom pane 弹窗栈与审批请求入口 | `docs/workdocjcl/spec/06_UI/TUI_APPROVALS.md` |
| `codex-rs/tui/src/pager_overlay.rs` | 全屏 pager overlays（含审批 Ctrl+A 全屏查看退出语义） | `docs/workdocjcl/spec/06_UI/TUI_APPROVALS.md` |
| `codex-rs/tui/src/exec_command.rs` | 命令渲染（strip `bash -lc` + shlex escaping） | `docs/workdocjcl/spec/06_UI/TUI_APPROVALS.md` |
| `codex-rs/tui/src/resume_picker.rs` | Alt-screen session picker（resume/fork，分页与搜索） | `docs/workdocjcl/spec/06_UI/TUI_RESUME_PICKER.md` |

## 8. 全量清单（存在性覆盖）
- repo-only 文件清单：`docs/workdocjcl/inventory/file_manifest_repo.txt`
- 全量文件清单：`docs/workdocjcl/inventory/file_manifest.txt`
- Rust workspace：`docs/workdocjcl/inventory/rust_workspace.md`
- Node workspace：`docs/workdocjcl/inventory/node_workspace.md`
