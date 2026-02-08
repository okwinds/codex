# `codex-rs/core/src/api_bridge.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8522`
- sha256: `79f2785c08398bb3647585d58e730d9227f307da3fecb95837365e072233493f`
- generated_utc: `2026-02-08T10:45:26Z`

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
- `const` `codex-rs/core/src/api_bridge.rs:118` `const MODEL_CAP_MODEL_HEADER: &str = "x-codex-model-cap-model";`
- `const` `codex-rs/core/src/api_bridge.rs:119` `const MODEL_CAP_RESET_AFTER_HEADER: &str = "x-codex-model-cap-reset-after-seconds";`
- `const` `codex-rs/core/src/api_bridge.rs:120` `const REQUEST_ID_HEADER: &str = "x-request-id";`
- `const` `codex-rs/core/src/api_bridge.rs:121` `const OAI_REQUEST_ID_HEADER: &str = "x-oai-request-id";`
- `const` `codex-rs/core/src/api_bridge.rs:122` `const CF_RAY_HEADER: &str = "cf-ray";`
- `use` `codex-rs/core/src/api_bridge.rs:126` `use super::*;`
- `use` `codex-rs/core/src/api_bridge.rs:127` `use codex_api::TransportError;`
- `use` `codex-rs/core/src/api_bridge.rs:128` `use http::HeaderMap;`
- `use` `codex-rs/core/src/api_bridge.rs:129` `use http::StatusCode;`
- `fn` `codex-rs/core/src/api_bridge.rs:132` `fn map_api_error_maps_model_cap_headers() {`
- `fn` `codex-rs/core/src/api_bridge.rs:157` `fn extract_request_tracking_id(headers: Option<&HeaderMap>) -> Option<String> {`
- `fn` `codex-rs/core/src/api_bridge.rs:161` `fn extract_request_id(headers: Option<&HeaderMap>) -> Option<String> {`
- `fn` `codex-rs/core/src/api_bridge.rs:166` `fn extract_header(headers: Option<&HeaderMap>, name: &str) -> Option<String> {`
- `struct` `codex-rs/core/src/api_bridge.rs:207` `struct UsageErrorResponse {`
- `struct` `codex-rs/core/src/api_bridge.rs:212` `struct UsageErrorBody {`
- `impl` `codex-rs/core/src/api_bridge.rs:225` `impl ApiAuthProvider for CoreAuthProvider {`
- `fn` `codex-rs/core/src/api_bridge.rs:226` `fn bearer_token(&self) -> Option<String> {`
- `fn` `codex-rs/core/src/api_bridge.rs:230` `fn account_id(&self) -> Option<String> {`

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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
