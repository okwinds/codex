# `codex-rs/state/src/model/log.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1008`
- sha256: `6d1ebfeee86319e98333217f677c45ba05e4e649166d00cdb0d8ecfbfee41275`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/model/log.rs` (read)

### Outputs / Side Effects
- reads/writes SQLite or DB

## Public Surface (auto)
- `pub struct LogEntry {`
- `pub struct LogRow {`
- `pub struct LogQuery {`

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/model/log.rs:1` `use serde::Serialize;`
- `use` `codex-rs/state/src/model/log.rs:2` `use sqlx::FromRow;`
- `struct` `codex-rs/state/src/model/log.rs:5` `pub struct LogEntry {`
- `struct` `codex-rs/state/src/model/log.rs:18` `pub struct LogRow {`
- `struct` `codex-rs/state/src/model/log.rs:31` `pub struct LogQuery {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Serialize;`
- `use sqlx::FromRow;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ENTITIES.md`
