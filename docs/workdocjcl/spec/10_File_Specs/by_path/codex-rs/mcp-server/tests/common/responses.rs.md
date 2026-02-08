# `codex-rs/mcp-server/tests/common/responses.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1633`
- sha256: `7b84a751172b4e6830cf13c24d9420a8a1ca3e84ced9f4821acf07bcb6b87c4c`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `use std::path::Path;`
- `use core_test_support::responses;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
