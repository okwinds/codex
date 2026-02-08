# `codex-rs/mcp-server/tests/common/mock_model_server.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1403`
- sha256: `d2cbc2c34d697b19db36829d0b1caa5241635c92b1a777098d2c89a883cc3973`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/tests/common/mock_model_server.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::atomic::AtomicUsize;`
- `use std::sync::atomic::Ordering;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::Respond;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
