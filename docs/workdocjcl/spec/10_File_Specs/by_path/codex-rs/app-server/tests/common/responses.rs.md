# `codex-rs/app-server/tests/common/responses.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2953`
- sha256: `cee4ef736eadd62d7fbb763a5aa0f5675839fbe8e485382d8601bd3ec2b4ab2c`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/common/responses.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub fn create_shell_command_sse_response(`
- `pub fn create_final_assistant_message_sse_response(message: &str) -> anyhow::Result<String> {`
- `pub fn create_apply_patch_sse_response(`
- `pub fn create_exec_command_sse_response(call_id: &str) -> anyhow::Result<String> {`
- `pub fn create_request_user_input_sse_response(call_id: &str) -> anyhow::Result<String> {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use core_test_support::responses;`
- `use serde_json::json;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
