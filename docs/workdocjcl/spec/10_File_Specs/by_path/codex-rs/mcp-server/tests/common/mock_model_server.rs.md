# `codex-rs/mcp-server/tests/common/mock_model_server.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1382`
- sha256: `f0dc4fa935d352a49d5e5df9a532730896998fd294c0f47bb22b2a0fd495c61b`
- generated_utc: `2026-02-08T10:45:38Z`

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
