# `codex-rs/state/src/model/backfill_state.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2062`
- sha256: `f2921c4f3dd6b7c5f37be8694ce9f3026c8223a787a6985bf1fab3e10761e08f`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/model/backfill_state.rs` (read)

### Outputs / Side Effects
- reads/writes SQLite or DB

## Public Surface (auto)
- `pub struct BackfillState {`
- `pub enum BackfillStatus {`
- `pub fn parse(value: &str) -> Result<Self> {`

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/model/backfill_state.rs:1` `use anyhow::Result;`
- `use` `codex-rs/state/src/model/backfill_state.rs:2` `use chrono::DateTime;`
- `use` `codex-rs/state/src/model/backfill_state.rs:3` `use chrono::Utc;`
- `use` `codex-rs/state/src/model/backfill_state.rs:4` `use sqlx::Row;`
- `use` `codex-rs/state/src/model/backfill_state.rs:5` `use sqlx::sqlite::SqliteRow;`
- `struct` `codex-rs/state/src/model/backfill_state.rs:9` `pub struct BackfillState {`
- `impl` `codex-rs/state/src/model/backfill_state.rs:18` `impl Default for BackfillState {`
- `fn` `codex-rs/state/src/model/backfill_state.rs:19` `fn default() -> Self {`
- `impl` `codex-rs/state/src/model/backfill_state.rs:28` `impl BackfillState {`
- `enum` `codex-rs/state/src/model/backfill_state.rs:45` `pub enum BackfillStatus {`
- `impl` `codex-rs/state/src/model/backfill_state.rs:51` `impl BackfillStatus {`
- `const` `codex-rs/state/src/model/backfill_state.rs:52` `pub const fn as_str(self) -> &'static str {`
- `fn` `codex-rs/state/src/model/backfill_state.rs:60` `pub fn parse(value: &str) -> Result<Self> {`
- `fn` `codex-rs/state/src/model/backfill_state.rs:70` `fn epoch_seconds_to_datetime(secs: i64) -> Result<DateTime<Utc>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use sqlx::Row;`
- `use sqlx::sqlite::SqliteRow;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
