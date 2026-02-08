# `codex-mcp-server`

- path: `codex-rs/mcp-server`
- generated_utc: `2026-02-08T10:45:13Z`
- role: MCP client/server or related support

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-mcp-server` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `codex-arg0`
- `codex-common`
- `codex-core`
- `codex-protocol`
- `codex-utils-json-to-toml`
- `rmcp`
- `schemars`
- `serde`
- `serde_json`
- `shlex`
- `tokio`
- `tracing`
- `tracing-subscriber`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use crate::codex_tool_config::CodexToolCallParam;`
- `pub use crate::codex_tool_config::CodexToolCallReplyParam;`
- `pub use crate::exec_approval::ExecApprovalElicitRequestParams;`
- `pub use crate::exec_approval::ExecApprovalResponse;`
- `pub use crate::patch_approval::PatchApprovalElicitRequestParams;`
- `pub use crate::patch_approval::PatchApprovalResponse;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
