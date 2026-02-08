# `codex-rs/core/src/api_bridge.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8039`
- sha256: `190585482b22eded06cfd530bf3acf475c940e96e2e6f867f1c49dc507a46b7b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/api_bridge.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/api_bridge.rs:1` `use chrono::DateTime;`
- `use` `codex-rs/core/src/api_bridge.rs:2` `use chrono::Utc;`
- `use` `codex-rs/core/src/api_bridge.rs:3` `use codex_api::AuthProvider as ApiAuthProvider;`
- `use` `codex-rs/core/src/api_bridge.rs:4` `use codex_api::TransportError;`
- `use` `codex-rs/core/src/api_bridge.rs:5` `use codex_api::error::ApiError;`
- `use` `codex-rs/core/src/api_bridge.rs:6` `use codex_api::rate_limits::parse_promo_message;`
- `use` `codex-rs/core/src/api_bridge.rs:7` `use codex_api::rate_limits::parse_rate_limit;`
- `use` `codex-rs/core/src/api_bridge.rs:8` `use http::HeaderMap;`
- `use` `codex-rs/core/src/api_bridge.rs:9` `use serde::Deserialize;`
- `use` `codex-rs/core/src/api_bridge.rs:11` `use crate::auth::CodexAuth;`
- `use` `codex-rs/core/src/api_bridge.rs:12` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/api_bridge.rs:13` `use crate::error::ModelCapError;`
- `use` `codex-rs/core/src/api_bridge.rs:14` `use crate::error::RetryLimitReachedError;`
- `use` `codex-rs/core/src/api_bridge.rs:15` `use crate::error::UnexpectedResponseError;`
- `use` `codex-rs/core/src/api_bridge.rs:16` `use crate::error::UsageLimitReachedError;`
- `use` `codex-rs/core/src/api_bridge.rs:17` `use crate::model_provider_info::ModelProviderInfo;`
- `use` `codex-rs/core/src/api_bridge.rs:18` `use crate::token_data::PlanType;`
- `const` `codex-rs/core/src/api_bridge.rs:116` `const MODEL_CAP_MODEL_HEADER: &str = "x-codex-model-cap-model";`
- `const` `codex-rs/core/src/api_bridge.rs:117` `const MODEL_CAP_RESET_AFTER_HEADER: &str = "x-codex-model-cap-reset-after-seconds";`
- `use` `codex-rs/core/src/api_bridge.rs:121` `use super::*;`
- `use` `codex-rs/core/src/api_bridge.rs:122` `use codex_api::TransportError;`
- `use` `codex-rs/core/src/api_bridge.rs:123` `use http::HeaderMap;`
- `use` `codex-rs/core/src/api_bridge.rs:124` `use http::StatusCode;`
- `fn` `codex-rs/core/src/api_bridge.rs:127` `fn map_api_error_maps_model_cap_headers() {`
- `fn` `codex-rs/core/src/api_bridge.rs:152` `fn extract_request_id(headers: Option<&HeaderMap>) -> Option<String> {`
- `struct` `codex-rs/core/src/api_bridge.rs:197` `struct UsageErrorResponse {`
- `struct` `codex-rs/core/src/api_bridge.rs:202` `struct UsageErrorBody {`
- `impl` `codex-rs/core/src/api_bridge.rs:215` `impl ApiAuthProvider for CoreAuthProvider {`
- `fn` `codex-rs/core/src/api_bridge.rs:216` `fn bearer_token(&self) -> Option<String> {`
- `fn` `codex-rs/core/src/api_bridge.rs:220` `fn account_id(&self) -> Option<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_api::AuthProvider as ApiAuthProvider;`
- `use codex_api::TransportError;`
- `use codex_api::error::ApiError;`
- `use codex_api::rate_limits::parse_promo_message;`
- `use codex_api::rate_limits::parse_rate_limit;`
- `use http::HeaderMap;`
- `use serde::Deserialize;`
- `use crate::auth::CodexAuth;`
- `use crate::error::CodexErr;`
- `use crate::error::ModelCapError;`
- `use crate::error::RetryLimitReachedError;`
- `use crate::error::UnexpectedResponseError;`
- `use crate::error::UsageLimitReachedError;`
- `use crate::model_provider_info::ModelProviderInfo;`
- `use crate::token_data::PlanType;`
- `use super::*;`
- `use codex_api::TransportError;`
- `use http::HeaderMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
