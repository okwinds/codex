# `codex-rs/state/src/model/thread_memory.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1491`
- sha256: `8c8cbd2e005f1c4203e767d90d931f04fd5b33ed41730b5b3c3d27e9ea158302`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/model/thread_memory.rs` (read)

### Outputs / Side Effects
- reads/writes SQLite or DB

## Public Surface (auto)
- `pub struct ThreadMemory {`

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/model/thread_memory.rs:1` `use anyhow::Result;`
- `use` `codex-rs/state/src/model/thread_memory.rs:2` `use chrono::DateTime;`
- `use` `codex-rs/state/src/model/thread_memory.rs:3` `use chrono::Utc;`
- `use` `codex-rs/state/src/model/thread_memory.rs:4` `use codex_protocol::ThreadId;`
- `use` `codex-rs/state/src/model/thread_memory.rs:5` `use sqlx::Row;`
- `use` `codex-rs/state/src/model/thread_memory.rs:6` `use sqlx::sqlite::SqliteRow;`
- `struct` `codex-rs/state/src/model/thread_memory.rs:10` `pub struct ThreadMemory {`
- `impl` `codex-rs/state/src/model/thread_memory.rs:25` `impl ThreadMemoryRow {`
- `impl` `codex-rs/state/src/model/thread_memory.rs:36` `impl TryFrom<ThreadMemoryRow> for ThreadMemory {`
- `type` `codex-rs/state/src/model/thread_memory.rs:37` `type Error = anyhow::Error;`
- `fn` `codex-rs/state/src/model/thread_memory.rs:39` `fn try_from(row: ThreadMemoryRow) -> std::result::Result<Self, Self::Error> {`
- `fn` `codex-rs/state/src/model/thread_memory.rs:49` `fn epoch_seconds_to_datetime(secs: i64) -> Result<DateTime<Utc>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_protocol::ThreadId;`
- `use sqlx::Row;`
- `use sqlx::sqlite::SqliteRow;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
