# `codex-rs/mcp-server/tests/common/responses.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2696`
- sha256: `0a8999cf60ffe06d661f26dcfc2b5232d8b9cc7108a400b6fe0808d91ade91d4`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/tests/common/responses.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub fn create_shell_command_sse_response(`
- `pub fn create_final_assistant_message_sse_response(message: &str) -> anyhow::Result<String> {`
- `pub fn create_apply_patch_sse_response(`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use serde_json::json;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
