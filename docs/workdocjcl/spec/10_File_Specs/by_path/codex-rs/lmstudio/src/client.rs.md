# `codex-rs/lmstudio/src/client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13276`
- sha256: `bfb88a8c75a8fe0375418d2d109ddbc9eed35b2dd34d90fbf5585f5fd3d76fe2`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/lmstudio/src/client.rs` (read)
- env: `HOME`, `USERPROFILE`

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct LMStudioClient {`

## Definitions (auto, per-file)
- `use` `codex-rs/lmstudio/src/client.rs:1` `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use` `codex-rs/lmstudio/src/client.rs:2` `use codex_core::config::Config;`
- `use` `codex-rs/lmstudio/src/client.rs:3` `use std::io;`
- `use` `codex-rs/lmstudio/src/client.rs:4` `use std::path::Path;`
- `struct` `codex-rs/lmstudio/src/client.rs:7` `pub struct LMStudioClient {`
- `const` `codex-rs/lmstudio/src/client.rs:12` `const LMSTUDIO_CONNECTION_ERROR: &str = "LM Studio is not responding. Install from https://lmstudio.ai/download and run 'lms server start'.";`
- `impl` `codex-rs/lmstudio/src/client.rs:14` `impl LMStudioClient {`
- `fn` `codex-rs/lmstudio/src/client.rs:15` `pub async fn try_from_provider(config: &Config) -> std::io::Result<Self> {`
- `fn` `codex-rs/lmstudio/src/client.rs:46` `async fn check_server(&self) -> io::Result<()> {`
- `fn` `codex-rs/lmstudio/src/client.rs:65` `pub async fn load_model(&self, model: &str) -> io::Result<()> {`
- `fn` `codex-rs/lmstudio/src/client.rs:95` `pub async fn fetch_models(&self) -> io::Result<Vec<String>> {`
- `fn` `codex-rs/lmstudio/src/client.rs:127` `fn find_lms() -> std::io::Result<String> {`
- `fn` `codex-rs/lmstudio/src/client.rs:131` `fn find_lms_with_home_dir(home_dir: Option<&str>) -> std::io::Result<String> {`
- `fn` `codex-rs/lmstudio/src/client.rs:168` `pub async fn download_model(&self, model: &str) -> std::io::Result<()> {`
- `fn` `codex-rs/lmstudio/src/client.rs:194` `fn from_host_root(host_root: impl Into<String>) -> Self {`
- `use` `codex-rs/lmstudio/src/client.rs:209` `use super::*;`
- `fn` `codex-rs/lmstudio/src/client.rs:212` `async fn test_fetch_models_happy_path() {`
- `fn` `codex-rs/lmstudio/src/client.rs:244` `async fn test_fetch_models_no_data_array() {`
- `fn` `codex-rs/lmstudio/src/client.rs:275` `async fn test_fetch_models_server_error() {`
- `fn` `codex-rs/lmstudio/src/client.rs:303` `async fn test_check_server_happy_path() {`
- `fn` `codex-rs/lmstudio/src/client.rs:327` `async fn test_check_server_error() {`
- `fn` `codex-rs/lmstudio/src/client.rs:355` `fn test_find_lms() {`
- `fn` `codex-rs/lmstudio/src/client.rs:370` `fn test_find_lms_with_mock_home() {`
- `fn` `codex-rs/lmstudio/src/client.rs:390` `fn test_from_host_root() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use codex_core::config::Config;`
- `use std::io;`
- `use std::path::Path;`
- `use super::*;`
### Referenced env vars
- `HOME`
- `USERPROFILE`

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
