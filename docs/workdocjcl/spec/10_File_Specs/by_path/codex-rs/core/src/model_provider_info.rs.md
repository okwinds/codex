# `codex-rs/core/src/model_provider_info.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `16824`
- sha256: `93eb6b6e9ce44dd2dca80ee56a8b3033b0da498e15f1e704d4e604206850be96`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/model_provider_info.rs` (read)
- env: `CODEX_OSS_BASE_URL`, `CODEX_OSS_PORT`, `OPENAI_BASE_URL`

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum WireApi {`
- `pub struct ModelProviderInfo {`
- `pub fn api_key(&self) -> crate::error::Result<Option<String>> {`
- `pub fn request_max_retries(&self) -> u64 {`
- `pub fn stream_max_retries(&self) -> u64 {`
- `pub fn stream_idle_timeout(&self) -> Duration {`
- `pub fn create_openai_provider() -> ModelProviderInfo {`
- `pub fn is_openai(&self) -> bool {`
- `pub fn built_in_model_providers() -> HashMap<String, ModelProviderInfo> {`
- `pub fn create_oss_provider(default_provider_port: u16, wire_api: WireApi) -> ModelProviderInfo {`
- `pub fn create_oss_provider_with_base_url(base_url: &str, wire_api: WireApi) -> ModelProviderInfo {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/model_provider_info.rs:8` `use crate::auth::AuthMode;`
- `use` `codex-rs/core/src/model_provider_info.rs:9` `use crate::error::EnvVarError;`
- `use` `codex-rs/core/src/model_provider_info.rs:10` `use codex_api::Provider as ApiProvider;`
- `use` `codex-rs/core/src/model_provider_info.rs:11` `use codex_api::provider::RetryConfig as ApiRetryConfig;`
- `use` `codex-rs/core/src/model_provider_info.rs:12` `use http::HeaderMap;`
- `use` `codex-rs/core/src/model_provider_info.rs:13` `use http::header::HeaderName;`
- `use` `codex-rs/core/src/model_provider_info.rs:14` `use http::header::HeaderValue;`
- `use` `codex-rs/core/src/model_provider_info.rs:15` `use schemars::JsonSchema;`
- `use` `codex-rs/core/src/model_provider_info.rs:16` `use serde::Deserialize;`
- `use` `codex-rs/core/src/model_provider_info.rs:17` `use serde::Serialize;`
- `use` `codex-rs/core/src/model_provider_info.rs:18` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/model_provider_info.rs:19` `use std::env::VarError;`
- `use` `codex-rs/core/src/model_provider_info.rs:20` `use std::time::Duration;`
- `const` `codex-rs/core/src/model_provider_info.rs:22` `const DEFAULT_STREAM_IDLE_TIMEOUT_MS: u64 = 300_000;`
- `const` `codex-rs/core/src/model_provider_info.rs:23` `const DEFAULT_STREAM_MAX_RETRIES: u64 = 5;`
- `const` `codex-rs/core/src/model_provider_info.rs:24` `const DEFAULT_REQUEST_MAX_RETRIES: u64 = 4;`
- `const` `codex-rs/core/src/model_provider_info.rs:26` `const MAX_STREAM_MAX_RETRIES: u64 = 100;`
- `const` `codex-rs/core/src/model_provider_info.rs:28` `const MAX_REQUEST_MAX_RETRIES: u64 = 100;`
- `const` `codex-rs/core/src/model_provider_info.rs:30` `const OPENAI_PROVIDER_NAME: &str = "OpenAI";`
- `const` `codex-rs/core/src/model_provider_info.rs:31` `const CHAT_WIRE_API_REMOVED_ERROR: &str = "`wire_api = \"chat\"` is no longer supported.\nHow to fix: set `wire_api = \"responses\"` in your provider config.\nMore info: https://github.com/openai/codex/discussions/7782";`
- `enum` `codex-rs/core/src/model_provider_info.rs:38` `pub enum WireApi {`
- `impl` `codex-rs/core/src/model_provider_info.rs:44` `impl<'de> Deserialize<'de> for WireApi {`
- `struct` `codex-rs/core/src/model_provider_info.rs:61` `pub struct ModelProviderInfo {`
- `impl` `codex-rs/core/src/model_provider_info.rs:117` `impl ModelProviderInfo {`
- `fn` `codex-rs/core/src/model_provider_info.rs:118` `fn build_header_map(&self) -> crate::error::Result<HeaderMap> {`
- `fn` `codex-rs/core/src/model_provider_info.rs:179` `pub fn api_key(&self) -> crate::error::Result<Option<String>> {`
- `fn` `codex-rs/core/src/model_provider_info.rs:203` `pub fn request_max_retries(&self) -> u64 {`
- `fn` `codex-rs/core/src/model_provider_info.rs:210` `pub fn stream_max_retries(&self) -> u64 {`
- `fn` `codex-rs/core/src/model_provider_info.rs:217` `pub fn stream_idle_timeout(&self) -> Duration {`
- `fn` `codex-rs/core/src/model_provider_info.rs:222` `pub fn create_openai_provider() -> ModelProviderInfo {`
- `fn` `codex-rs/core/src/model_provider_info.rs:263` `pub fn is_openai(&self) -> bool {`
- `const` `codex-rs/core/src/model_provider_info.rs:268` `pub const DEFAULT_LMSTUDIO_PORT: u16 = 1234;`
- `const` `codex-rs/core/src/model_provider_info.rs:269` `pub const DEFAULT_OLLAMA_PORT: u16 = 11434;`
- `const` `codex-rs/core/src/model_provider_info.rs:271` `pub const LMSTUDIO_OSS_PROVIDER_ID: &str = "lmstudio";`
- `const` `codex-rs/core/src/model_provider_info.rs:272` `pub const OLLAMA_OSS_PROVIDER_ID: &str = "ollama";`
- `fn` `codex-rs/core/src/model_provider_info.rs:275` `pub fn built_in_model_providers() -> HashMap<String, ModelProviderInfo> {`
- `use` `codex-rs/core/src/model_provider_info.rs:276` `use ModelProviderInfo as P;`
- `fn` `codex-rs/core/src/model_provider_info.rs:298` `pub fn create_oss_provider(default_provider_port: u16, wire_api: WireApi) -> ModelProviderInfo {`
- `fn` `codex-rs/core/src/model_provider_info.rs:318` `pub fn create_oss_provider_with_base_url(base_url: &str, wire_api: WireApi) -> ModelProviderInfo {`
- `use` `codex-rs/core/src/model_provider_info.rs:339` `use super::*;`
- `use` `codex-rs/core/src/model_provider_info.rs:340` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/model_provider_info.rs:343` `fn test_deserialize_ollama_model_provider_toml() {`
- `fn` `codex-rs/core/src/model_provider_info.rs:370` `fn test_deserialize_azure_model_provider_toml() {`
- `fn` `codex-rs/core/src/model_provider_info.rs:401` `fn test_deserialize_example_model_provider_toml() {`
- `fn` `codex-rs/core/src/model_provider_info.rs:435` `fn test_deserialize_chat_wire_api_shows_helpful_error() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthMode;`
- `use crate::error::EnvVarError;`
- `use codex_api::Provider as ApiProvider;`
- `use codex_api::provider::RetryConfig as ApiRetryConfig;`
- `use http::HeaderMap;`
- `use http::header::HeaderName;`
- `use http::header::HeaderValue;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::collections::HashMap;`
- `use std::env::VarError;`
- `use std::time::Duration;`
- `use ModelProviderInfo as P;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- `CODEX_OSS_BASE_URL`
- `CODEX_OSS_PORT`
- `OPENAI_BASE_URL`

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
