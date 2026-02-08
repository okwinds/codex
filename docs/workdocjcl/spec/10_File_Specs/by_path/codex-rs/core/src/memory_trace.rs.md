# `codex-rs/core/src/memory_trace.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10017`
- sha256: `6cabd7e2be0e17395d85ee8491e3c7b6afe53583eea4ce5782364a7cebce03f8`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/memory_trace.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct BuiltTraceMemory {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/memory_trace.rs:1` `use std::path::Path;`
- `use` `codex-rs/core/src/memory_trace.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/memory_trace.rs:4` `use crate::ModelClient;`
- `use` `codex-rs/core/src/memory_trace.rs:5` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/memory_trace.rs:6` `use crate::error::Result;`
- `use` `codex-rs/core/src/memory_trace.rs:7` `use codex_api::MemoryTrace as ApiMemoryTrace;`
- `use` `codex-rs/core/src/memory_trace.rs:8` `use codex_api::MemoryTraceMetadata as ApiMemoryTraceMetadata;`
- `use` `codex-rs/core/src/memory_trace.rs:9` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/memory_trace.rs:10` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/memory_trace.rs:11` `use codex_protocol::openai_models::ReasoningEffort as ReasoningEffortConfig;`
- `use` `codex-rs/core/src/memory_trace.rs:12` `use serde_json::Map;`
- `use` `codex-rs/core/src/memory_trace.rs:13` `use serde_json::Value;`
- `struct` `codex-rs/core/src/memory_trace.rs:16` `pub struct BuiltTraceMemory {`
- `struct` `codex-rs/core/src/memory_trace.rs:23` `struct PreparedTrace {`
- `fn` `codex-rs/core/src/memory_trace.rs:36` `pub async fn build_memories_from_trace_files(`
- `fn` `codex-rs/core/src/memory_trace.rs:76` `async fn prepare_trace(index: usize, path: &Path) -> Result<PreparedTrace> {`
- `fn` `codex-rs/core/src/memory_trace.rs:95` `async fn load_trace_text(path: &Path) -> Result<String> {`
- `fn` `codex-rs/core/src/memory_trace.rs:100` `fn decode_trace_bytes(raw: &[u8]) -> String {`
- `fn` `codex-rs/core/src/memory_trace.rs:112` `fn load_trace_items(path: &Path, text: &str) -> Result<Vec<Value>> {`
- `fn` `codex-rs/core/src/memory_trace.rs:157` `fn normalize_trace_items(items: Vec<Value>, path: &Path) -> Result<Vec<Value>> {`
- `fn` `codex-rs/core/src/memory_trace.rs:204` `fn is_allowed_trace_item(item: &Map<String, Value>) -> bool {`
- `fn` `codex-rs/core/src/memory_trace.rs:219` `fn build_trace_id(index: usize, path: &Path) -> String {`
- `use` `codex-rs/core/src/memory_trace.rs:230` `use super::*;`
- `use` `codex-rs/core/src/memory_trace.rs:231` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/memory_trace.rs:232` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/memory_trace.rs:235` `fn normalize_trace_items_handles_payload_wrapper_and_message_role_filtering() {`
- `fn` `codex-rs/core/src/memory_trace.rs:271` `fn load_trace_items_supports_jsonl_arrays_and_objects() {`
- `fn` `codex-rs/core/src/memory_trace.rs:285` `async fn load_trace_text_decodes_utf8_sig() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use crate::ModelClient;`
- `use crate::error::CodexErr;`
- `use crate::error::Result;`
- `use codex_api::MemoryTrace as ApiMemoryTrace;`
- `use codex_api::MemoryTraceMetadata as ApiMemoryTraceMetadata;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ReasoningEffort as ReasoningEffortConfig;`
- `use serde_json::Map;`
- `use serde_json::Value;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
