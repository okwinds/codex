# `codex-rs/state/src/model/thread_metadata.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11312`
- sha256: `8f959c7e05639113d8d03072504e7b0d37ec71f1eb76556e62e752d74fdd1fce`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `struct` `codex-rs/state/src/model/thread_metadata.rs:91` `pub struct ThreadMetadataBuilder {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:120` `impl ThreadMetadataBuilder {`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:122` `pub fn new(`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:146` `pub fn build(&self, default_provider: &str) -> ThreadMetadata {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:179` `impl ThreadMetadata {`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:181` `pub fn diff_fields(&self, other: &Self) -> Vec<&'static str> {`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:235` `fn canonicalize_datetime(dt: DateTime<Utc>) -> DateTime<Utc> {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:259` `impl ThreadRow {`
- `impl` `codex-rs/state/src/model/thread_metadata.rs:282` `impl TryFrom<ThreadRow> for ThreadMetadata {`
- `type` `codex-rs/state/src/model/thread_metadata.rs:283` `type Error = anyhow::Error;`
- `fn` `codex-rs/state/src/model/thread_metadata.rs:285` `fn try_from(row: ThreadRow) -> std::result::Result<Self, Self::Error> {`
- `struct` `codex-rs/state/src/model/thread_metadata.rs:345` `pub struct BackfillStats {`

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
- `workdocjcl/spec/02_Data/ENTITIES.md`
