# `codex-rs/feedback/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13527`
- sha256: `0dd3d96b376c395f5838ac8dff3c70878060b78678674f36d629b8abc2fcb903`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/feedback/src/lib.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct CodexFeedback {`
- `pub fn new() -> Self {`
- `pub fn make_writer(&self) -> FeedbackMakeWriter {`
- `pub fn snapshot(&self, session_id: Option<ThreadId>) -> CodexLogSnapshot {`
- `pub struct FeedbackMakeWriter {`
- `pub struct FeedbackWriter {`
- `pub struct CodexLogSnapshot {`
- `pub fn save_to_temp_file(&self) -> io::Result<PathBuf> {`
- `pub fn upload_feedback(`

## Definitions (auto, per-file)
- `use` `codex-rs/feedback/src/lib.rs:1` `use std::collections::BTreeMap;`
- `use` `codex-rs/feedback/src/lib.rs:2` `use std::collections::VecDeque;`
- `use` `codex-rs/feedback/src/lib.rs:3` `use std::collections::btree_map::Entry;`
- `use` `codex-rs/feedback/src/lib.rs:4` `use std::fs;`
- `use` `codex-rs/feedback/src/lib.rs:5` `use std::io::Write;`
- `use` `codex-rs/feedback/src/lib.rs:6` `use std::io::{self};`
- `use` `codex-rs/feedback/src/lib.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/feedback/src/lib.rs:8` `use std::sync::Arc;`
- `use` `codex-rs/feedback/src/lib.rs:9` `use std::sync::Mutex;`
- `use` `codex-rs/feedback/src/lib.rs:10` `use std::time::Duration;`
- `use` `codex-rs/feedback/src/lib.rs:12` `use anyhow::Result;`
- `use` `codex-rs/feedback/src/lib.rs:13` `use anyhow::anyhow;`
- `use` `codex-rs/feedback/src/lib.rs:14` `use codex_protocol::ThreadId;`
- `use` `codex-rs/feedback/src/lib.rs:15` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/feedback/src/lib.rs:16` `use tracing::Event;`
- `use` `codex-rs/feedback/src/lib.rs:17` `use tracing::Level;`
- `use` `codex-rs/feedback/src/lib.rs:18` `use tracing::field::Visit;`
- `use` `codex-rs/feedback/src/lib.rs:19` `use tracing_subscriber::Layer;`
- `use` `codex-rs/feedback/src/lib.rs:20` `use tracing_subscriber::filter::Targets;`
- `use` `codex-rs/feedback/src/lib.rs:21` `use tracing_subscriber::fmt::writer::MakeWriter;`
- `use` `codex-rs/feedback/src/lib.rs:22` `use tracing_subscriber::registry::LookupSpan;`
- `const` `codex-rs/feedback/src/lib.rs:24` `const DEFAULT_MAX_BYTES: usize = 4 * 1024 * 1024; // 4 MiB`
- `const` `codex-rs/feedback/src/lib.rs:25` `const SENTRY_DSN: &str =`
- `const` `codex-rs/feedback/src/lib.rs:27` `const UPLOAD_TIMEOUT_SECS: u64 = 10;`
- `const` `codex-rs/feedback/src/lib.rs:28` `const FEEDBACK_TAGS_TARGET: &str = "feedback_tags";`
- `const` `codex-rs/feedback/src/lib.rs:29` `const MAX_FEEDBACK_TAGS: usize = 64;`
- `struct` `codex-rs/feedback/src/lib.rs:32` `pub struct CodexFeedback {`
- `impl` `codex-rs/feedback/src/lib.rs:36` `impl Default for CodexFeedback {`
- `fn` `codex-rs/feedback/src/lib.rs:37` `fn default() -> Self {`
- `impl` `codex-rs/feedback/src/lib.rs:42` `impl CodexFeedback {`
- `fn` `codex-rs/feedback/src/lib.rs:43` `pub fn new() -> Self {`
- `fn` `codex-rs/feedback/src/lib.rs:53` `pub fn make_writer(&self) -> FeedbackMakeWriter {`
- `fn` `codex-rs/feedback/src/lib.rs:91` `pub fn snapshot(&self, session_id: Option<ThreadId>) -> CodexLogSnapshot {`
- `struct` `codex-rs/feedback/src/lib.rs:110` `struct FeedbackInner {`
- `impl` `codex-rs/feedback/src/lib.rs:115` `impl FeedbackInner {`
- `fn` `codex-rs/feedback/src/lib.rs:116` `fn new(max_bytes: usize) -> Self {`
- `struct` `codex-rs/feedback/src/lib.rs:125` `pub struct FeedbackMakeWriter {`
- `impl` `codex-rs/feedback/src/lib.rs:129` `impl<'a> MakeWriter<'a> for FeedbackMakeWriter {`
- `type` `codex-rs/feedback/src/lib.rs:130` `type Writer = FeedbackWriter;`
- `fn` `codex-rs/feedback/src/lib.rs:132` `fn make_writer(&'a self) -> Self::Writer {`
- `struct` `codex-rs/feedback/src/lib.rs:139` `pub struct FeedbackWriter {`
- `impl` `codex-rs/feedback/src/lib.rs:143` `impl Write for FeedbackWriter {`
- `fn` `codex-rs/feedback/src/lib.rs:144` `fn write(&mut self, buf: &[u8]) -> io::Result<usize> {`
- `fn` `codex-rs/feedback/src/lib.rs:150` `fn flush(&mut self) -> io::Result<()> {`
- `struct` `codex-rs/feedback/src/lib.rs:155` `struct RingBuffer {`
- `impl` `codex-rs/feedback/src/lib.rs:160` `impl RingBuffer {`
- `fn` `codex-rs/feedback/src/lib.rs:161` `fn new(capacity: usize) -> Self {`
- `fn` `codex-rs/feedback/src/lib.rs:168` `fn len(&self) -> usize {`
- `fn` `codex-rs/feedback/src/lib.rs:172` `fn push_bytes(&mut self, data: &[u8]) {`
- `fn` `codex-rs/feedback/src/lib.rs:197` `fn snapshot_bytes(&self) -> Vec<u8> {`
- `struct` `codex-rs/feedback/src/lib.rs:202` `pub struct CodexLogSnapshot {`
- `impl` `codex-rs/feedback/src/lib.rs:208` `impl CodexLogSnapshot {`
- `fn` `codex-rs/feedback/src/lib.rs:213` `pub fn save_to_temp_file(&self) -> io::Result<PathBuf> {`
- `fn` `codex-rs/feedback/src/lib.rs:222` `pub fn upload_feedback(`
- `use` `codex-rs/feedback/src/lib.rs:230` `use std::collections::BTreeMap;`
- `use` `codex-rs/feedback/src/lib.rs:231` `use std::fs;`
- `use` `codex-rs/feedback/src/lib.rs:232` `use std::str::FromStr;`
- `use` `codex-rs/feedback/src/lib.rs:233` `use std::sync::Arc;`
- `use` `codex-rs/feedback/src/lib.rs:235` `use sentry::Client;`
- `use` `codex-rs/feedback/src/lib.rs:236` `use sentry::ClientOptions;`
- `use` `codex-rs/feedback/src/lib.rs:237` `use sentry::protocol::Attachment;`
- `use` `codex-rs/feedback/src/lib.rs:238` `use sentry::protocol::Envelope;`
- `use` `codex-rs/feedback/src/lib.rs:239` `use sentry::protocol::EnvelopeItem;`
- `use` `codex-rs/feedback/src/lib.rs:240` `use sentry::protocol::Event;`
- `use` `codex-rs/feedback/src/lib.rs:241` `use sentry::protocol::Level;`
- `use` `codex-rs/feedback/src/lib.rs:242` `use sentry::transports::DefaultTransportFactory;`
- `use` `codex-rs/feedback/src/lib.rs:243` `use sentry::types::Dsn;`
- `use` `codex-rs/feedback/src/lib.rs:300` `use sentry::protocol::Exception;`
- `use` `codex-rs/feedback/src/lib.rs:301` `use sentry::protocol::Values;`
- `fn` `codex-rs/feedback/src/lib.rs:340` `fn display_classification(classification: &str) -> String {`
- `struct` `codex-rs/feedback/src/lib.rs:350` `struct FeedbackMetadataLayer {`
- `fn` `codex-rs/feedback/src/lib.rs:358` `fn on_event(&self, event: &Event<'_>, _ctx: tracing_subscriber::layer::Context<'_, S>) {`
- `struct` `codex-rs/feedback/src/lib.rs:382` `struct FeedbackTagsVisitor {`
- `impl` `codex-rs/feedback/src/lib.rs:386` `impl Visit for FeedbackTagsVisitor {`
- `fn` `codex-rs/feedback/src/lib.rs:387` `fn record_i64(&mut self, field: &tracing::field::Field, value: i64) {`
- `fn` `codex-rs/feedback/src/lib.rs:392` `fn record_u64(&mut self, field: &tracing::field::Field, value: u64) {`
- `fn` `codex-rs/feedback/src/lib.rs:397` `fn record_bool(&mut self, field: &tracing::field::Field, value: bool) {`
- `fn` `codex-rs/feedback/src/lib.rs:402` `fn record_f64(&mut self, field: &tracing::field::Field, value: f64) {`
- `fn` `codex-rs/feedback/src/lib.rs:407` `fn record_str(&mut self, field: &tracing::field::Field, value: &str) {`
- `fn` `codex-rs/feedback/src/lib.rs:412` `fn record_debug(&mut self, field: &tracing::field::Field, value: &dyn std::fmt::Debug) {`
- `use` `codex-rs/feedback/src/lib.rs:420` `use super::*;`
- `use` `codex-rs/feedback/src/lib.rs:421` `use tracing_subscriber::layer::SubscriberExt;`
- `use` `codex-rs/feedback/src/lib.rs:422` `use tracing_subscriber::util::SubscriberInitExt;`
- `fn` `codex-rs/feedback/src/lib.rs:425` `fn ring_buffer_drops_front_when_full() {`
- `fn` `codex-rs/feedback/src/lib.rs:438` `fn metadata_layer_records_tags_from_feedback_target() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::collections::VecDeque;`
- `use std::collections::btree_map::Entry;`
- `use std::fs;`
- `use std::io::Write;`
- `use std::io::{self};`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::SessionSource;`
- `use tracing::Event;`
- `use tracing::Level;`
- `use tracing::field::Visit;`
- `use tracing_subscriber::Layer;`
- `use tracing_subscriber::filter::Targets;`
- `use tracing_subscriber::fmt::writer::MakeWriter;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
