# `codex-rs/protocol/src/message_history.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `252`
- sha256: `997e939050137d59e704bb0d5cb0868141584d46df8a6454635fbe9337c8cfc1`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/message_history.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct HistoryEntry {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/message_history.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/message_history.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/message_history.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/message_history.rs:4` `use ts_rs::TS;`
- `struct` `codex-rs/protocol/src/message_history.rs:7` `pub struct HistoryEntry {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
