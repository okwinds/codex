# `codex-rs/state/src/model/thread_metadata.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11933`
- sha256: `47562cded35cb06cd6a1d68644c82083cfe162f8d906d9cc74464e32855a1e56`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/model/thread_metadata.rs` (read)

### Outputs / Side Effects
- reads/writes SQLite or DB

## Public Surface (auto)
- `pub enum SortKey {`
- `pub struct Anchor {`
- `pub struct ThreadsPage {`
- `pub struct ExtractionOutcome {`
- `pub struct ThreadMetadata {`
- `pub struct ThreadMetadataBuilder {`
- `pub fn new(`
- `pub fn build(&self, default_provider: &str) -> ThreadMetadata {`
- `pub fn diff_fields(&self, other: &Self) -> Vec<&'static str> {`
- `pub struct BackfillStats {`

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/model/thread_metadata.rs:1` `use anyhow::Result;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:2` `use chrono::DateTime;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:3` `use chrono::Timelike;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:4` `use chrono::Utc;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:5` `use codex_protocol::ThreadId;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:6` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:7` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:8` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:9` `use sqlx::Row;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:10` `use sqlx::sqlite::SqliteRow;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:11` `use std::path::PathBuf;`
- `use` `codex-rs/state/src/model/thread_metadata.rs:12` `use uuid::Uuid;`
- `enum` `codex-rs/state/src/model/thread_metadata.rs:16` `pub enum SortKey {`
- `struct` `codex-rs/state/src/model/thread_metadata.rs:25` `pub struct Anchor {`
- `struct` `codex-rs/state/src/model/thread_metadata.rs:34` `pub struct ThreadsPage {`
- `struct` `codex-rs/state/src/model/thread_metadata.rs:45` `pub struct ExtractionOutcome {`
- `struct` `codex-rs/state/src/model/thread_metadata.rs:54` `pub struct ThreadMetadata {`
- `struct` `codex-rs/state/src/model/thread_metadata.rs:93` `pub struct ThreadMetadataBuilder {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:124` `impl ThreadMetadataBuilder {`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:126` `pub fn new(`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:151` `pub fn build(&self, default_provider: &str) -> ThreadMetadata {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:185` `impl ThreadMetadata {`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:187` `pub fn diff_fields(&self, other: &Self) -> Vec<&'static str> {`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:244` `fn canonicalize_datetime(dt: DateTime<Utc>) -> DateTime<Utc> {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:269` `impl ThreadRow {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:293` `impl TryFrom<ThreadRow> for ThreadMetadata {`
- `type` `codex-rs/state/src/model/thread_metadata.rs:294` `type Error = anyhow::Error;`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:296` `fn try_from(row: ThreadRow) -> std::result::Result<Self, Self::Error> {`
- `struct` `codex-rs/state/src/model/thread_metadata.rs:358` `pub struct BackfillStats {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use chrono::DateTime;`
- `use chrono::Timelike;`
- `use chrono::Utc;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::protocol::SessionSource;`
- `use sqlx::Row;`
- `use sqlx::sqlite::SqliteRow;`
- `use std::path::PathBuf;`
- `use uuid::Uuid;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
