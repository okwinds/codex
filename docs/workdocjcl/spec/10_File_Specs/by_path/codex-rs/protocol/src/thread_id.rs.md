# `codex-rs/protocol/src/thread_id.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2182`
- sha256: `51b05d825cf7fea7fdced5c97fa4769b72b300d44a1adbfdf3c641eee49edbf7`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/thread_id.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ThreadId {`
- `pub fn new() -> Self {`
- `pub fn from_string(s: &str) -> Result<Self, uuid::Error> {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/thread_id.rs:1` `use std::fmt::Display;`
- `use` `codex-rs/protocol/src/thread_id.rs:3` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/thread_id.rs:4` `use schemars::r#gen::SchemaGenerator;`
- `use` `codex-rs/protocol/src/thread_id.rs:5` `use schemars::schema::Schema;`
- `use` `codex-rs/protocol/src/thread_id.rs:6` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/thread_id.rs:7` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/thread_id.rs:8` `use ts_rs::TS;`
- `use` `codex-rs/protocol/src/thread_id.rs:9` `use uuid::Uuid;`
- `struct` `codex-rs/protocol/src/thread_id.rs:13` `pub struct ThreadId {`
- `impl` `codex-rs/protocol/src/thread_id.rs:17` `impl ThreadId {`
- `fn` `codex-rs/protocol/src/thread_id.rs:18` `pub fn new() -> Self {`
- `fn` `codex-rs/protocol/src/thread_id.rs:24` `pub fn from_string(s: &str) -> Result<Self, uuid::Error> {`
- `impl` `codex-rs/protocol/src/thread_id.rs:31` `impl TryFrom<&str> for ThreadId {`
- `type` `codex-rs/protocol/src/thread_id.rs:32` `type Error = uuid::Error;`
- `fn` `codex-rs/protocol/src/thread_id.rs:34` `fn try_from(value: &str) -> Result<Self, Self::Error> {`
- `impl` `codex-rs/protocol/src/thread_id.rs:39` `impl TryFrom<String> for ThreadId {`
- `type` `codex-rs/protocol/src/thread_id.rs:40` `type Error = uuid::Error;`
- `fn` `codex-rs/protocol/src/thread_id.rs:42` `fn try_from(value: String) -> Result<Self, Self::Error> {`
- `impl` `codex-rs/protocol/src/thread_id.rs:47` `impl From<ThreadId> for String {`
- `fn` `codex-rs/protocol/src/thread_id.rs:48` `fn from(value: ThreadId) -> Self {`
- `impl` `codex-rs/protocol/src/thread_id.rs:53` `impl Default for ThreadId {`
- `fn` `codex-rs/protocol/src/thread_id.rs:54` `fn default() -> Self {`
- `impl` `codex-rs/protocol/src/thread_id.rs:59` `impl Display for ThreadId {`
- `fn` `codex-rs/protocol/src/thread_id.rs:60` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `impl` `codex-rs/protocol/src/thread_id.rs:65` `impl Serialize for ThreadId {`
- `impl` `codex-rs/protocol/src/thread_id.rs:74` `impl<'de> Deserialize<'de> for ThreadId {`
- `impl` `codex-rs/protocol/src/thread_id.rs:85` `impl JsonSchema for ThreadId {`
- `fn` `codex-rs/protocol/src/thread_id.rs:86` `fn schema_name() -> String {`
- `fn` `codex-rs/protocol/src/thread_id.rs:90` `fn json_schema(generator: &mut SchemaGenerator) -> Schema {`
- `use` `codex-rs/protocol/src/thread_id.rs:97` `use super::*;`
- `fn` `codex-rs/protocol/src/thread_id.rs:99` `fn test_thread_id_default_is_not_zeroes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt::Display;`
- `use schemars::JsonSchema;`
- `use schemars::r#gen::SchemaGenerator;`
- `use schemars::schema::Schema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
- `use uuid::Uuid;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
