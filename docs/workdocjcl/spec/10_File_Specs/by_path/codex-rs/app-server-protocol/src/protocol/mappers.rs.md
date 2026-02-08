# `codex-rs/app-server-protocol/src/protocol/mappers.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `485`
- sha256: `af2b664e1ab8eb9e20ec751018a3c966ac609f5138180f4a4d5ef6ce033bf49d`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/protocol/mappers.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/protocol/mappers.rs:1` `use crate::protocol::v1;`
- `use` `codex-rs/app-server-protocol/src/protocol/mappers.rs:2` `use crate::protocol::v2;`
- `impl` `codex-rs/app-server-protocol/src/protocol/mappers.rs:4` `impl From<v1::ExecOneOffCommandParams> for v2::CommandExecParams {`
- `fn` `codex-rs/app-server-protocol/src/protocol/mappers.rs:5` `fn from(value: v1::ExecOneOffCommandParams) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::protocol::v1;`
- `use crate::protocol::v2;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
