# `codex-rs/ollama/src/client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `16263`
- sha256: `3a55e5b712f592f34f6adc8436211d5eddd04f054bda0c29183ef5bf4a66890d`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/ollama/src/client.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub struct OllamaClient {`

## Definitions (auto, per-file)
- `use` `codex-rs/ollama/src/client.rs:1` `use bytes::BytesMut;`
- `use` `codex-rs/ollama/src/client.rs:2` `use futures::StreamExt;`
- `use` `codex-rs/ollama/src/client.rs:3` `use futures::stream::BoxStream;`
- `use` `codex-rs/ollama/src/client.rs:4` `use semver::Version;`
- `use` `codex-rs/ollama/src/client.rs:5` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/ollama/src/client.rs:6` `use std::collections::VecDeque;`
- `use` `codex-rs/ollama/src/client.rs:7` `use std::io;`
- `use` `codex-rs/ollama/src/client.rs:9` `use crate::parser::pull_events_from_value;`
- `use` `codex-rs/ollama/src/client.rs:10` `use crate::pull::PullEvent;`
- `use` `codex-rs/ollama/src/client.rs:11` `use crate::pull::PullProgressReporter;`
- `use` `codex-rs/ollama/src/client.rs:12` `use crate::url::base_url_to_host_root;`
- `use` `codex-rs/ollama/src/client.rs:13` `use crate::url::is_openai_compatible_base_url;`
- `use` `codex-rs/ollama/src/client.rs:14` `use codex_core::ModelProviderInfo;`
- `use` `codex-rs/ollama/src/client.rs:15` `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use` `codex-rs/ollama/src/client.rs:16` `use codex_core::WireApi;`
- `use` `codex-rs/ollama/src/client.rs:17` `use codex_core::config::Config;`
- `const` `codex-rs/ollama/src/client.rs:19` `const OLLAMA_CONNECTION_ERROR: &str = "No running Ollama server detected. Start it with: `ollama serve` (after installing). Install instructions: https://github.com/ollama/ollama?tab=readme-ov-file#ollama";`
- `struct` `codex-rs/ollama/src/client.rs:22` `pub struct OllamaClient {`
- `impl` `codex-rs/ollama/src/client.rs:28` `impl OllamaClient {`
- `fn` `codex-rs/ollama/src/client.rs:32` `pub async fn try_from_oss_provider(config: &Config) -> io::Result<Self> {`
- `fn` `codex-rs/ollama/src/client.rs:50` `async fn try_from_provider_with_base_url(base_url: &str) -> io::Result<Self> {`
- `fn` `codex-rs/ollama/src/client.rs:81` `async fn probe_server(&self) -> io::Result<()> {`
- `fn` `codex-rs/ollama/src/client.rs:104` `pub async fn fetch_models(&self) -> io::Result<Vec<String>> {`
- `fn` `codex-rs/ollama/src/client.rs:130` `pub async fn fetch_version(&self) -> io::Result<Option<Version>> {`
- `fn` `codex-rs/ollama/src/client.rs:157` `pub async fn pull_model_stream(`
- `fn` `codex-rs/ollama/src/client.rs:215` `pub async fn pull_with_reporter(`
- `fn` `codex-rs/ollama/src/client.rs:250` `fn from_host_root(host_root: impl Into<String>) -> Self {`
- `use` `codex-rs/ollama/src/client.rs:265` `use super::*;`
- `use` `codex-rs/ollama/src/client.rs:266` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/ollama/src/client.rs:270` `async fn test_fetch_models_happy_path() {`
- `fn` `codex-rs/ollama/src/client.rs:301` `async fn test_fetch_version() {`
- `fn` `codex-rs/ollama/src/client.rs:337` `async fn test_probe_server_happy_path_openai_compat_and_native() {`
- `fn` `codex-rs/ollama/src/client.rs:374` `async fn test_try_from_oss_provider_ok_when_server_running() {`
- `fn` `codex-rs/ollama/src/client.rs:398` `async fn test_try_from_oss_provider_err_when_server_missing() {`

## Dependencies (auto sample)
### Imports / Includes
- `use bytes::BytesMut;`
- `use futures::StreamExt;`
- `use futures::stream::BoxStream;`
- `use semver::Version;`
- `use serde_json::Value as JsonValue;`
- `use std::collections::VecDeque;`
- `use std::io;`
- `use crate::parser::pull_events_from_value;`
- `use crate::pull::PullEvent;`
- `use crate::pull::PullProgressReporter;`
- `use crate::url::base_url_to_host_root;`
- `use crate::url::is_openai_compatible_base_url;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use codex_core::WireApi;`
- `use codex_core::config::Config;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
