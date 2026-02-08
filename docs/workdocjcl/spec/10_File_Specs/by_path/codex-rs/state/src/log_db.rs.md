# `codex-rs/state/src/log_db.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8527`
- sha256: `640828a5b1db7ac3fe474db289d9adf230fe13318ab17152fbb2fdbc82a48606`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/log_db.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct LogDbLayer {`
- `pub fn start(state_db: std::sync::Arc<StateRuntime>) -> LogDbLayer {`

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/log_db.rs:21` `use chrono::Duration as ChronoDuration;`
- `use` `codex-rs/state/src/log_db.rs:22` `use chrono::Utc;`
- `use` `codex-rs/state/src/log_db.rs:23` `use std::time::Duration;`
- `use` `codex-rs/state/src/log_db.rs:24` `use std::time::SystemTime;`
- `use` `codex-rs/state/src/log_db.rs:25` `use std::time::UNIX_EPOCH;`
- `use` `codex-rs/state/src/log_db.rs:27` `use tokio::sync::mpsc;`
- `use` `codex-rs/state/src/log_db.rs:28` `use tracing::Event;`
- `use` `codex-rs/state/src/log_db.rs:29` `use tracing::field::Field;`
- `use` `codex-rs/state/src/log_db.rs:30` `use tracing::field::Visit;`
- `use` `codex-rs/state/src/log_db.rs:31` `use tracing::span::Attributes;`
- `use` `codex-rs/state/src/log_db.rs:32` `use tracing::span::Id;`
- `use` `codex-rs/state/src/log_db.rs:33` `use tracing::span::Record;`
- `use` `codex-rs/state/src/log_db.rs:34` `use tracing_subscriber::Layer;`
- `use` `codex-rs/state/src/log_db.rs:35` `use tracing_subscriber::registry::LookupSpan;`
- `use` `codex-rs/state/src/log_db.rs:37` `use crate::LogEntry;`
- `use` `codex-rs/state/src/log_db.rs:38` `use crate::StateRuntime;`
- `const` `codex-rs/state/src/log_db.rs:40` `const LOG_QUEUE_CAPACITY: usize = 512;`
- `const` `codex-rs/state/src/log_db.rs:41` `const LOG_BATCH_SIZE: usize = 64;`
- `const` `codex-rs/state/src/log_db.rs:42` `const LOG_FLUSH_INTERVAL: Duration = Duration::from_millis(250);`
- `const` `codex-rs/state/src/log_db.rs:43` `const LOG_RETENTION_DAYS: i64 = 90;`
- `struct` `codex-rs/state/src/log_db.rs:45` `pub struct LogDbLayer {`
- `fn` `codex-rs/state/src/log_db.rs:49` `pub fn start(state_db: std::sync::Arc<StateRuntime>) -> LogDbLayer {`
- `fn` `codex-rs/state/src/log_db.rs:61` `fn on_new_span(`
- `fn` `codex-rs/state/src/log_db.rs:77` `fn on_record(`
- `fn` `codex-rs/state/src/log_db.rs:102` `fn on_event(&self, event: &Event<'_>, ctx: tracing_subscriber::layer::Context<'_, S>) {`
- `struct` `codex-rs/state/src/log_db.rs:131` `struct SpanLogContext {`
- `struct` `codex-rs/state/src/log_db.rs:136` `struct SpanFieldVisitor {`
- `impl` `codex-rs/state/src/log_db.rs:140` `impl SpanFieldVisitor {`
- `fn` `codex-rs/state/src/log_db.rs:141` `fn record_field(&mut self, field: &Field, value: String) {`
- `impl` `codex-rs/state/src/log_db.rs:148` `impl Visit for SpanFieldVisitor {`
- `fn` `codex-rs/state/src/log_db.rs:149` `fn record_i64(&mut self, field: &Field, value: i64) {`
- `fn` `codex-rs/state/src/log_db.rs:153` `fn record_u64(&mut self, field: &Field, value: u64) {`
- `fn` `codex-rs/state/src/log_db.rs:157` `fn record_bool(&mut self, field: &Field, value: bool) {`
- `fn` `codex-rs/state/src/log_db.rs:161` `fn record_f64(&mut self, field: &Field, value: f64) {`
- `fn` `codex-rs/state/src/log_db.rs:165` `fn record_str(&mut self, field: &Field, value: &str) {`
- `fn` `codex-rs/state/src/log_db.rs:169` `fn record_error(&mut self, field: &Field, value: &(dyn std::error::Error + 'static)) {`
- `fn` `codex-rs/state/src/log_db.rs:173` `fn record_debug(&mut self, field: &Field, value: &dyn std::fmt::Debug) {`
- `fn` `codex-rs/state/src/log_db.rs:199` `async fn run_inserter(`
- `fn` `codex-rs/state/src/log_db.rs:228` `async fn flush(state_db: &std::sync::Arc<StateRuntime>, buffer: &mut Vec<LogEntry>) {`
- `fn` `codex-rs/state/src/log_db.rs:236` `async fn run_retention_cleanup(state_db: std::sync::Arc<StateRuntime>) {`
- `struct` `codex-rs/state/src/log_db.rs:245` `struct MessageVisitor {`
- `impl` `codex-rs/state/src/log_db.rs:250` `impl MessageVisitor {`
- `fn` `codex-rs/state/src/log_db.rs:251` `fn record_field(&mut self, field: &Field, value: String) {`
- `impl` `codex-rs/state/src/log_db.rs:261` `impl Visit for MessageVisitor {`
- `fn` `codex-rs/state/src/log_db.rs:262` `fn record_i64(&mut self, field: &Field, value: i64) {`
- `fn` `codex-rs/state/src/log_db.rs:266` `fn record_u64(&mut self, field: &Field, value: u64) {`
- `fn` `codex-rs/state/src/log_db.rs:270` `fn record_bool(&mut self, field: &Field, value: bool) {`
- `fn` `codex-rs/state/src/log_db.rs:274` `fn record_f64(&mut self, field: &Field, value: f64) {`
- `fn` `codex-rs/state/src/log_db.rs:278` `fn record_str(&mut self, field: &Field, value: &str) {`
- `fn` `codex-rs/state/src/log_db.rs:282` `fn record_error(&mut self, field: &Field, value: &(dyn std::error::Error + 'static)) {`
- `fn` `codex-rs/state/src/log_db.rs:286` `fn record_debug(&mut self, field: &Field, value: &dyn std::fmt::Debug) {`

## Dependencies (auto sample)
### Imports / Includes
- `use chrono::Duration as ChronoDuration;`
- `use chrono::Utc;`
- `use std::time::Duration;`
- `use std::time::SystemTime;`
- `use std::time::UNIX_EPOCH;`
- `use tokio::sync::mpsc;`
- `use tracing::Event;`
- `use tracing::field::Field;`
- `use tracing::field::Visit;`
- `use tracing::span::Attributes;`
- `use tracing::span::Id;`
- `use tracing::span::Record;`
- `use tracing_subscriber::Layer;`
- `use tracing_subscriber::registry::LookupSpan;`
- `use crate::LogEntry;`
- `use crate::StateRuntime;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ENTITIES.md`
