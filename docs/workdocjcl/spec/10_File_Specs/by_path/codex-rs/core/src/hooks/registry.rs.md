# `codex-rs/core/src/hooks/registry.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10754`
- sha256: `0345ec17dd9c75c3afbd7b7604f8d9b513de32e345e5b021c44398c4d081d561`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/hooks/registry.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/hooks/registry.rs:1` `use tokio::process::Command;`
- `use` `codex-rs/core/src/hooks/registry.rs:3` `use super::types::Hook;`
- `use` `codex-rs/core/src/hooks/registry.rs:4` `use super::types::HookEvent;`
- `use` `codex-rs/core/src/hooks/registry.rs:5` `use super::types::HookOutcome;`
- `use` `codex-rs/core/src/hooks/registry.rs:6` `use super::types::HookPayload;`
- `use` `codex-rs/core/src/hooks/registry.rs:7` `use super::user_notification::notify_hook;`
- `use` `codex-rs/core/src/hooks/registry.rs:8` `use crate::config::Config;`
- `fn` `codex-rs/core/src/hooks/registry.rs:15` `fn get_notify_hook(config: &Config) -> Option<Hook> {`
- `impl` `codex-rs/core/src/hooks/registry.rs:25` `impl Hooks {`
- `fn` `codex-rs/core/src/hooks/registry.rs:34` `fn hooks_for_event(&self, hook_event: &HookEvent) -> &[Hook] {`
- `use` `codex-rs/core/src/hooks/registry.rs:63` `use std::fs;`
- `use` `codex-rs/core/src/hooks/registry.rs:64` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/hooks/registry.rs:65` `use std::process::Stdio;`
- `use` `codex-rs/core/src/hooks/registry.rs:66` `use std::sync::Arc;`
- `use` `codex-rs/core/src/hooks/registry.rs:67` `use std::sync::atomic::AtomicUsize;`
- `use` `codex-rs/core/src/hooks/registry.rs:68` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/core/src/hooks/registry.rs:69` `use std::time::Duration;`
- `use` `codex-rs/core/src/hooks/registry.rs:71` `use anyhow::Result;`
- `use` `codex-rs/core/src/hooks/registry.rs:72` `use chrono::TimeZone;`
- `use` `codex-rs/core/src/hooks/registry.rs:73` `use chrono::Utc;`
- `use` `codex-rs/core/src/hooks/registry.rs:74` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/hooks/registry.rs:75` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/hooks/registry.rs:76` `use serde_json::to_string;`
- `use` `codex-rs/core/src/hooks/registry.rs:77` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/hooks/registry.rs:78` `use tokio::time::timeout;`
- `use` `codex-rs/core/src/hooks/registry.rs:80` `use crate::config::test_config;`
- `use` `codex-rs/core/src/hooks/registry.rs:82` `use super::super::types::Hook;`
- `use` `codex-rs/core/src/hooks/registry.rs:83` `use super::super::types::HookEvent;`
- `use` `codex-rs/core/src/hooks/registry.rs:84` `use super::super::types::HookEventAfterAgent;`
- `use` `codex-rs/core/src/hooks/registry.rs:85` `use super::super::types::HookOutcome;`
- `use` `codex-rs/core/src/hooks/registry.rs:86` `use super::super::types::HookPayload;`
- `use` `codex-rs/core/src/hooks/registry.rs:87` `use super::Hooks;`
- `use` `codex-rs/core/src/hooks/registry.rs:88` `use super::command_from_argv;`
- `use` `codex-rs/core/src/hooks/registry.rs:89` `use super::get_notify_hook;`
- `const` `codex-rs/core/src/hooks/registry.rs:91` `const CWD: &str = "/tmp";`
- `const` `codex-rs/core/src/hooks/registry.rs:92` `const INPUT_MESSAGE: &str = "hello";`
- `fn` `codex-rs/core/src/hooks/registry.rs:94` `fn hook_payload(label: &str) -> HookPayload {`
- `fn` `codex-rs/core/src/hooks/registry.rs:113` `fn counting_hook(calls: &Arc<AtomicUsize>, outcome: HookOutcome) -> Hook {`
- `fn` `codex-rs/core/src/hooks/registry.rs:126` `fn hooks_for_after_agent(hooks: Vec<Hook>) -> Hooks {`
- `fn` `codex-rs/core/src/hooks/registry.rs:131` `fn command_from_argv_returns_none_for_empty_args() {`
- `fn` `codex-rs/core/src/hooks/registry.rs:137` `async fn command_from_argv_builds_command() -> Result<()> {`
- `fn` `codex-rs/core/src/hooks/registry.rs:157` `fn get_notify_hook_requires_program_name() {`
- `fn` `codex-rs/core/src/hooks/registry.rs:171` `async fn dispatch_executes_hook() {`
- `fn` `codex-rs/core/src/hooks/registry.rs:180` `async fn default_hook_is_noop_and_continues() {`
- `fn` `codex-rs/core/src/hooks/registry.rs:187` `async fn dispatch_executes_multiple_hooks_for_same_event() {`
- `fn` `codex-rs/core/src/hooks/registry.rs:199` `async fn dispatch_stops_when_hook_returns_stop() {`
- `fn` `codex-rs/core/src/hooks/registry.rs:212` `async fn hook_executes_program_with_payload_argument_unix() -> Result<()> {`
- `fn` `codex-rs/core/src/hooks/registry.rs:260` `async fn hook_executes_program_with_payload_argument_windows() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use tokio::process::Command;`
- `use super::types::Hook;`
- `use super::types::HookEvent;`
- `use super::types::HookOutcome;`
- `use super::types::HookPayload;`
- `use super::user_notification::notify_hook;`
- `use crate::config::Config;`
- `use std::fs;`
- `use std::path::PathBuf;`
- `use std::process::Stdio;`
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicUsize;`
- `use std::sync::atomic::Ordering;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use chrono::TimeZone;`
- `use chrono::Utc;`
- `use codex_protocol::ThreadId;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::to_string;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
