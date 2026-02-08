# `codex-rs/codex-api/src/provider.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4890`
- sha256: `ecbb2f929c15c9d3dbd33ca6d1f7d59f86717e6e9daa9514820e7b7744d04081`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/provider.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RetryConfig {`
- `pub fn to_policy(&self) -> RetryPolicy {`
- `pub struct Provider {`
- `pub fn url_for_path(&self, path: &str) -> String {`
- `pub fn build_request(&self, method: Method, path: &str) -> Request {`
- `pub fn is_azure_responses_endpoint(&self) -> bool {`
- `pub fn websocket_url_for_path(&self, path: &str) -> Result<Url, url::ParseError> {`
- `pub fn is_azure_responses_wire_base_url(name: &str, base_url: Option<&str>) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/provider.rs:1` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/provider.rs:2` `use codex_client::RequestCompression;`
- `use` `codex-rs/codex-api/src/provider.rs:3` `use codex_client::RetryOn;`
- `use` `codex-rs/codex-api/src/provider.rs:4` `use codex_client::RetryPolicy;`
- `use` `codex-rs/codex-api/src/provider.rs:5` `use http::Method;`
- `use` `codex-rs/codex-api/src/provider.rs:6` `use http::header::HeaderMap;`
- `use` `codex-rs/codex-api/src/provider.rs:7` `use std::collections::HashMap;`
- `use` `codex-rs/codex-api/src/provider.rs:8` `use std::time::Duration;`
- `use` `codex-rs/codex-api/src/provider.rs:9` `use url::Url;`
- `struct` `codex-rs/codex-api/src/provider.rs:16` `pub struct RetryConfig {`
- `impl` `codex-rs/codex-api/src/provider.rs:24` `impl RetryConfig {`
- `fn` `codex-rs/codex-api/src/provider.rs:25` `pub fn to_policy(&self) -> RetryPolicy {`
- `struct` `codex-rs/codex-api/src/provider.rs:43` `pub struct Provider {`
- `impl` `codex-rs/codex-api/src/provider.rs:52` `impl Provider {`
- `fn` `codex-rs/codex-api/src/provider.rs:53` `pub fn url_for_path(&self, path: &str) -> String {`
- `fn` `codex-rs/codex-api/src/provider.rs:77` `pub fn build_request(&self, method: Method, path: &str) -> Request {`
- `fn` `codex-rs/codex-api/src/provider.rs:88` `pub fn is_azure_responses_endpoint(&self) -> bool {`
- `fn` `codex-rs/codex-api/src/provider.rs:92` `pub fn websocket_url_for_path(&self, path: &str) -> Result<Url, url::ParseError> {`
- `fn` `codex-rs/codex-api/src/provider.rs:106` `pub fn is_azure_responses_wire_base_url(name: &str, base_url: Option<&str>) -> bool {`
- `fn` `codex-rs/codex-api/src/provider.rs:119` `fn matches_azure_responses_base_url(base_url: &str) -> bool {`
- `const` `codex-rs/codex-api/src/provider.rs:120` `const AZURE_MARKERS: [&str; 5] = [`
- `use` `codex-rs/codex-api/src/provider.rs:132` `use super::*;`
- `fn` `codex-rs/codex-api/src/provider.rs:135` `fn detects_azure_responses_base_urls() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_client::Request;`
- `use codex_client::RequestCompression;`
- `use codex_client::RetryOn;`
- `use codex_client::RetryPolicy;`
- `use http::Method;`
- `use http::header::HeaderMap;`
- `use std::collections::HashMap;`
- `use std::time::Duration;`
- `use url::Url;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
