# Tools Schema Reference (Best-effort)

- generated_utc: `2026-02-03T16:43:42Z`
- sources:
  - `codex-rs/core/src/tools/spec.rs`
  - `codex-rs/core/src/tools/handlers/plan.rs`
  - `codex-rs/core/src/tools/handlers/apply_patch.rs`
  - `codex-rs/protocol/src/models.rs`

说明：本文件尝试从 Rust 源码中提取 tool schema（JSON Schema 子集）。
若某字段为 `kind=expr` 或 `kind=unparsed`，表示这是源码表达式，未做求值。

- 逐工具语义规格：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/INDEX.md`
- tool_count: `22`
- duplicates_detected: `0`

| Tool | Kind | Required | Params (name:type) | Source |
|---|---|---|---|---|
| `apply_patch` | `freeform` | (n/a) | (n/a) | `codex-rs/core/src/tools/handlers/apply_patch.rs:267` |
| `apply_patch` | `function` | `input` | `input:string` | `codex-rs/core/src/tools/handlers/apply_patch.rs:287` |
| `close_agent` | `function` | `id` | `id:string` | `codex-rs/core/src/tools/spec.rs:645` |
| `exec_command` | `function` | `cmd` | `cmd:string`, `justification:string`, `login:boolean`, `max_output_tokens:number`, `prefix_rule:array`, `sandbox_permissions:string`, `shell:string`, `tty:boolean`, `workdir:string`, `yield_time_ms:number` | `codex-rs/core/src/tools/spec.rs:248` |
| `grep_files` | `function` | `pattern` | `include:string`, `limit:number`, `path:string`, `pattern:string` | `codex-rs/core/src/tools/spec.rs:762` |
| `list_dir` | `function` | `dir_path` | `depth:number`, `dir_path:string`, `limit:number`, `offset:number` | `codex-rs/core/src/tools/spec.rs:911` |
| `list_mcp_resource_templates` | `function` | (none) | `cursor:string`, `server:string` | `codex-rs/core/src/tools/spec.rs:981` |
| `list_mcp_resources` | `function` | (none) | `cursor:string`, `server:string` | `codex-rs/core/src/tools/spec.rs:947` |
| `local_shell` | `local_shell` | (n/a) | (n/a) | `codex-rs/core/src/tools/spec.rs:1300` |
| `read_file` | `function` | `file_path` | `file_path:string`, `indentation:object`, `limit:number`, `mode:string`, `offset:number` | `codex-rs/core/src/tools/spec.rs:865` |
| `read_mcp_resource` | `function` | `server`, `uri` | `server:string`, `uri:string` | `codex-rs/core/src/tools/spec.rs:1015` |
| `request_user_input` | `function` | `questions` | `questions:array` | `codex-rs/core/src/tools/spec.rs:622` |
| `send_input` | `function` | `id`, `message` | `id:string`, `interrupt:boolean`, `message:string` | `codex-rs/core/src/tools/spec.rs:505` |
| `shell` | `function` | `command` | `command:array`, `justification:string`, `prefix_rule:array`, `sandbox_permissions:string`, `timeout_ms:number`, `workdir:string` | `codex-rs/core/src/tools/spec.rs:350` |
| `shell_command` | `function` | `command` | `command:string`, `justification:string`, `login:boolean`, `prefix_rule:array`, `sandbox_permissions:string`, `timeout_ms:number`, `workdir:string` | `codex-rs/core/src/tools/spec.rs:412` |
| `spawn_agent` | `function` | `message` | `agent_type:string`, `message:string` | `codex-rs/core/src/tools/spec.rs:467` |
| `test_sync_tool` | `function` | (none) | `barrier:object`, `sleep_after_ms:number`, `sleep_before_ms:number` | `codex-rs/core/src/tools/spec.rs:713` |
| `update_plan` | `function` | `plan` | `explanation:string`, `plan:array` | `codex-rs/core/src/tools/handlers/plan.rs:45` |
| `view_image` | `function` | `path` | `path:string` | `codex-rs/core/src/tools/spec.rs:433` |
| `wait` | `function` | `ids` | `ids:array`, `timeout_ms:number` | `codex-rs/core/src/tools/spec.rs:540` |
| `web_search` | `web_search` | (n/a) | (n/a) | `codex-rs/core/src/tools/spec.rs:1390` |
| `write_stdin` | `function` | `session_id` | `chars:string`, `max_output_tokens:number`, `session_id:number`, `yield_time_ms:number` | `codex-rs/core/src/tools/spec.rs:295` |

机器可读版本：`workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`
