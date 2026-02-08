# `codex-rs/codex-client/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `755`
- sha256: `e68f3eba929b886883e429cfd75dd152122675857ba66580d752398be65a61c5`
- generated_utc: `2026-02-08T10:45:22Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/codex-client/src/lib.rs:1` `mod default_client;`
- `mod` `codex-rs/codex-client/src/lib.rs:2` `mod error;`
- `mod` `codex-rs/codex-client/src/lib.rs:3` `mod request;`
- `mod` `codex-rs/codex-client/src/lib.rs:4` `mod retry;`
- `mod` `codex-rs/codex-client/src/lib.rs:5` `mod sse;`
- `mod` `codex-rs/codex-client/src/lib.rs:6` `mod telemetry;`
- `mod` `codex-rs/codex-client/src/lib.rs:7` `mod transport;`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
