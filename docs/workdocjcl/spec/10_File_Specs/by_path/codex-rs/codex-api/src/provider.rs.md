# `codex-rs/codex-api/src/provider.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5398`
- sha256: `8f50bc983ab3e7f136b34c824ca82578a88c084f7299cca5e096614b607e1d50`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/provider.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum WireApi {`
- `pub struct RetryConfig {`
- `pub fn to_policy(&self) -> RetryPolicy {`
- `pub struct Provider {`
- `pub fn url_for_path(&self, path: &str) -> String {`
- `pub fn build_request(&self, method: Method, path: &str) -> Request {`
- `pub fn is_azure_responses_endpoint(&self) -> bool {`
- `pub fn websocket_url_for_path(&self, path: &str) -> Result<Url, url::ParseError> {`
- `pub fn is_azure_responses_wire_base_url(wire: WireApi, name: &str, base_url: Option<&str>) -> bool {`

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
- `enum` `codex-rs/codex-api/src/provider.rs:13` `pub enum WireApi {`
- `struct` `codex-rs/codex-api/src/provider.rs:24` `pub struct RetryConfig {`
- `impl` `codex-rs/codex-api/src/provider.rs:32` `impl RetryConfig {`
- `fn` `codex-rs/codex-api/src/provider.rs:33` `pub fn to_policy(&self) -> RetryPolicy {`
- `struct` `codex-rs/codex-api/src/provider.rs:51` `pub struct Provider {`
- `impl` `codex-rs/codex-api/src/provider.rs:61` `impl Provider {`
- `fn` `codex-rs/codex-api/src/provider.rs:62` `pub fn url_for_path(&self, path: &str) -> String {`
- `fn` `codex-rs/codex-api/src/provider.rs:86` `pub fn build_request(&self, method: Method, path: &str) -> Request {`
- `fn` `codex-rs/codex-api/src/provider.rs:97` `pub fn is_azure_responses_endpoint(&self) -> bool {`
- `fn` `codex-rs/codex-api/src/provider.rs:101` `pub fn websocket_url_for_path(&self, path: &str) -> Result<Url, url::ParseError> {`
- `fn` `codex-rs/codex-api/src/provider.rs:115` `pub fn is_azure_responses_wire_base_url(wire: WireApi, name: &str, base_url: Option<&str>) -> bool {`
- `fn` `codex-rs/codex-api/src/provider.rs:132` `fn matches_azure_responses_base_url(base_url: &str) -> bool {`
- `const` `codex-rs/codex-api/src/provider.rs:133` `const AZURE_MARKERS: [&str; 5] = [`
- `use` `codex-rs/codex-api/src/provider.rs:145` `use super::*;`
- `fn` `codex-rs/codex-api/src/provider.rs:148` `fn detects_azure_responses_base_urls() {`

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
