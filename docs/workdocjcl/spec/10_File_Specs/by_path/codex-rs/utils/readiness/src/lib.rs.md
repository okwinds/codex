# `codex-rs/utils/readiness/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9120`
- sha256: `d2a453b548976a981cb26202c86e042ba193da300d2ab03e34cd9bf280cfc17b`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/readiness/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct Token(i32);`
- `pub trait Readiness: Send + Sync + 'static {`
- `pub struct ReadinessFlag {`
- `pub fn new() -> Self {`
- `pub enum ReadinessError {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/readiness/src/lib.rs:3` `use std::collections::HashSet;`
- `use` `codex-rs/utils/readiness/src/lib.rs:4` `use std::fmt;`
- `use` `codex-rs/utils/readiness/src/lib.rs:5` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/utils/readiness/src/lib.rs:6` `use std::sync::atomic::AtomicI32;`
- `use` `codex-rs/utils/readiness/src/lib.rs:7` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/utils/readiness/src/lib.rs:8` `use std::time::Duration;`
- `use` `codex-rs/utils/readiness/src/lib.rs:10` `use tokio::sync::Mutex;`
- `use` `codex-rs/utils/readiness/src/lib.rs:11` `use tokio::sync::watch;`
- `use` `codex-rs/utils/readiness/src/lib.rs:12` `use tokio::time;`
- `struct` `codex-rs/utils/readiness/src/lib.rs:16` `pub struct Token(i32);`
- `const` `codex-rs/utils/readiness/src/lib.rs:18` `const LOCK_TIMEOUT: Duration = Duration::from_millis(1000);`
- `trait` `codex-rs/utils/readiness/src/lib.rs:21` `pub trait Readiness: Send + Sync + 'static {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:25` `fn is_ready(&self) -> bool;`
- `fn` `codex-rs/utils/readiness/src/lib.rs:30` `async fn subscribe(&self) -> Result<Token, errors::ReadinessError>;`
- `fn` `codex-rs/utils/readiness/src/lib.rs:37` `async fn mark_ready(&self, token: Token) -> Result<bool, errors::ReadinessError>;`
- `fn` `codex-rs/utils/readiness/src/lib.rs:40` `async fn wait_ready(&self);`
- `struct` `codex-rs/utils/readiness/src/lib.rs:43` `pub struct ReadinessFlag {`
- `impl` `codex-rs/utils/readiness/src/lib.rs:54` `impl ReadinessFlag {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:56` `pub fn new() -> Self {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:76` `fn load_ready(&self) -> bool {`
- `impl` `codex-rs/utils/readiness/src/lib.rs:81` `impl Default for ReadinessFlag {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:82` `fn default() -> Self {`
- `impl` `codex-rs/utils/readiness/src/lib.rs:87` `impl fmt::Debug for ReadinessFlag {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:88` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `impl` `codex-rs/utils/readiness/src/lib.rs:96` `impl Readiness for ReadinessFlag {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:97` `fn is_ready(&self) -> bool {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:116` `async fn subscribe(&self) -> Result<Token, errors::ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:142` `async fn mark_ready(&self, token: Token) -> Result<bool, errors::ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:168` `async fn wait_ready(&self) {`
- `use` `codex-rs/utils/readiness/src/lib.rs:187` `use thiserror::Error;`
- `enum` `codex-rs/utils/readiness/src/lib.rs:190` `pub enum ReadinessError {`
- `use` `codex-rs/utils/readiness/src/lib.rs:200` `use std::sync::Arc;`
- `use` `codex-rs/utils/readiness/src/lib.rs:201` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/utils/readiness/src/lib.rs:203` `use super::Readiness;`
- `use` `codex-rs/utils/readiness/src/lib.rs:204` `use super::ReadinessFlag;`
- `use` `codex-rs/utils/readiness/src/lib.rs:205` `use super::Token;`
- `use` `codex-rs/utils/readiness/src/lib.rs:206` `use super::errors::ReadinessError;`
- `use` `codex-rs/utils/readiness/src/lib.rs:207` `use assert_matches::assert_matches;`
- `fn` `codex-rs/utils/readiness/src/lib.rs:210` `async fn subscribe_and_mark_ready_roundtrip() -> Result<(), ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:220` `async fn subscribe_after_ready_returns_none() -> Result<(), ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:230` `async fn mark_ready_rejects_unknown_token() -> Result<(), ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:239` `async fn wait_ready_unblocks_after_mark_ready() -> Result<(), ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:256` `async fn mark_ready_twice_uses_single_token() -> Result<(), ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:266` `async fn is_ready_without_subscribers_marks_flag_ready() -> Result<(), ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:279` `async fn subscribe_returns_error_when_lock_is_held() {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:294` `async fn subscribe_skips_zero_token() -> Result<(), ReadinessError> {`
- `fn` `codex-rs/utils/readiness/src/lib.rs:305` `async fn subscribe_avoids_duplicate_tokens() -> Result<(), ReadinessError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashSet;`
- `use std::fmt;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::atomic::AtomicI32;`
- `use std::sync::atomic::Ordering;`
- `use std::time::Duration;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::watch;`
- `use tokio::time;`
- `use thiserror::Error;`
- `use std::sync::Arc;`
- `use std::sync::atomic::Ordering;`
- `use super::Readiness;`
- `use super::ReadinessFlag;`
- `use super::Token;`
- `use super::errors::ReadinessError;`
- `use assert_matches::assert_matches;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
