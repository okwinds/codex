# `codex-rs/login/src/device_code_auth.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7019`
- sha256: `1efa889611169b4788141e3bfcd53dd64be5a1bae9c801bda8f99f38418356a5`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/login/src/device_code_auth.rs` (read)

### Outputs / Side Effects
- performs network I/O
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct DeviceCode {`

## Definitions (auto, per-file)
- `use` `codex-rs/login/src/device_code_auth.rs:1` `use reqwest::StatusCode;`
- `use` `codex-rs/login/src/device_code_auth.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/login/src/device_code_auth.rs:3` `use serde::Serialize;`
- `use` `codex-rs/login/src/device_code_auth.rs:4` `use serde::de::Deserializer;`
- `use` `codex-rs/login/src/device_code_auth.rs:5` `use serde::de::{self};`
- `use` `codex-rs/login/src/device_code_auth.rs:6` `use std::time::Duration;`
- `use` `codex-rs/login/src/device_code_auth.rs:7` `use std::time::Instant;`
- `use` `codex-rs/login/src/device_code_auth.rs:9` `use crate::pkce::PkceCodes;`
- `use` `codex-rs/login/src/device_code_auth.rs:10` `use crate::server::ServerOptions;`
- `use` `codex-rs/login/src/device_code_auth.rs:11` `use std::io;`
- `const` `codex-rs/login/src/device_code_auth.rs:13` `const ANSI_BLUE: &str = "\x1b[94m";`
- `const` `codex-rs/login/src/device_code_auth.rs:14` `const ANSI_GRAY: &str = "\x1b[90m";`
- `const` `codex-rs/login/src/device_code_auth.rs:15` `const ANSI_RESET: &str = "\x1b[0m";`
- `struct` `codex-rs/login/src/device_code_auth.rs:18` `pub struct DeviceCode {`
- `struct` `codex-rs/login/src/device_code_auth.rs:26` `struct UserCodeResp {`
- `struct` `codex-rs/login/src/device_code_auth.rs:35` `struct UserCodeReq {`
- `struct` `codex-rs/login/src/device_code_auth.rs:40` `struct TokenPollReq {`
- `struct` `codex-rs/login/src/device_code_auth.rs:56` `struct CodeSuccessResp {`
- `fn` `codex-rs/login/src/device_code_auth.rs:63` `async fn request_user_code(`
- `fn` `codex-rs/login/src/device_code_auth.rs:100` `async fn poll_for_token(`
- `fn` `codex-rs/login/src/device_code_auth.rs:149` `fn print_device_code_prompt(verification_url: &str, code: &str) {`
- `fn` `codex-rs/login/src/device_code_auth.rs:160` `pub async fn request_device_code(opts: &ServerOptions) -> std::io::Result<DeviceCode> {`
- `fn` `codex-rs/login/src/device_code_auth.rs:174` `pub async fn complete_device_code_login(`
- `fn` `codex-rs/login/src/device_code_auth.rs:226` `pub async fn run_device_code_login(opts: ServerOptions) -> std::io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use reqwest::StatusCode;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde::de::Deserializer;`
- `use serde::de::{self};`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use crate::pkce::PkceCodes;`
- `use crate::server::ServerOptions;`
- `use std::io;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
