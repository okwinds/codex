# `codex-rs/rmcp-client/src/utils.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5908`
- sha256: `c834efd68cca34d448b9d4081826f059a89efab2e7d7d81760d07dfd9120a905`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/utils.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/utils.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/utils.rs:2` `use std::env;`
- `use` `codex-rs/rmcp-client/src/utils.rs:3` `use std::time::Duration;`
- `use` `codex-rs/rmcp-client/src/utils.rs:5` `use anyhow::Context;`
- `use` `codex-rs/rmcp-client/src/utils.rs:6` `use anyhow::Result;`
- `use` `codex-rs/rmcp-client/src/utils.rs:7` `use anyhow::anyhow;`
- `use` `codex-rs/rmcp-client/src/utils.rs:8` `use reqwest::ClientBuilder;`
- `use` `codex-rs/rmcp-client/src/utils.rs:9` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/rmcp-client/src/utils.rs:10` `use reqwest::header::HeaderName;`
- `use` `codex-rs/rmcp-client/src/utils.rs:11` `use reqwest::header::HeaderValue;`
- `use` `codex-rs/rmcp-client/src/utils.rs:12` `use rmcp::service::ServiceError;`
- `use` `codex-rs/rmcp-client/src/utils.rs:13` `use tokio::time;`
- `use` `codex-rs/rmcp-client/src/utils.rs:163` `use super::*;`
- `use` `codex-rs/rmcp-client/src/utils.rs:164` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/rmcp-client/src/utils.rs:166` `use serial_test::serial;`
- `use` `codex-rs/rmcp-client/src/utils.rs:167` `use std::ffi::OsString;`
- `struct` `codex-rs/rmcp-client/src/utils.rs:169` `struct EnvVarGuard {`
- `impl` `codex-rs/rmcp-client/src/utils.rs:174` `impl EnvVarGuard {`
- `fn` `codex-rs/rmcp-client/src/utils.rs:175` `fn set(key: &str, value: &str) -> Self {`
- `impl` `codex-rs/rmcp-client/src/utils.rs:187` `impl Drop for EnvVarGuard {`
- `fn` `codex-rs/rmcp-client/src/utils.rs:188` `fn drop(&mut self) {`
- `fn` `codex-rs/rmcp-client/src/utils.rs:202` `async fn create_env_honors_overrides() {`
- `fn` `codex-rs/rmcp-client/src/utils.rs:211` `fn create_env_includes_additional_whitelisted_variables() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::env;`
- `use std::time::Duration;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use reqwest::ClientBuilder;`
- `use reqwest::header::HeaderMap;`
- `use reqwest::header::HeaderName;`
- `use reqwest::header::HeaderValue;`
- `use rmcp::service::ServiceError;`
- `use tokio::time;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use serial_test::serial;`
- `use std::ffi::OsString;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
