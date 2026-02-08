# `codex-rs/app-server/tests/common/auth_fixtures.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5372`
- sha256: `162fd7df947bce0f3933e970d506b40cadac826f5094d29b31b99333eae941c8`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/common/auth_fixtures.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct ChatGptAuthFixture {`
- `pub fn new(access_token: impl Into<String>) -> Self {`
- `pub fn refresh_token(mut self, refresh_token: impl Into<String>) -> Self {`
- `pub fn account_id(mut self, account_id: impl Into<String>) -> Self {`
- `pub fn plan_type(mut self, plan_type: impl Into<String>) -> Self {`
- `pub fn chatgpt_user_id(mut self, chatgpt_user_id: impl Into<String>) -> Self {`
- `pub fn chatgpt_account_id(mut self, chatgpt_account_id: impl Into<String>) -> Self {`
- `pub fn email(mut self, email: impl Into<String>) -> Self {`
- `pub fn last_refresh(mut self, last_refresh: Option<DateTime<Utc>>) -> Self {`
- `pub fn claims(mut self, claims: ChatGptIdTokenClaims) -> Self {`
- `pub struct ChatGptIdTokenClaims {`
- `pub fn new() -> Self {`
- `pub fn email(mut self, email: impl Into<String>) -> Self {`
- `pub fn plan_type(mut self, plan_type: impl Into<String>) -> Self {`
- `pub fn chatgpt_user_id(mut self, chatgpt_user_id: impl Into<String>) -> Self {`
- `pub fn chatgpt_account_id(mut self, chatgpt_account_id: impl Into<String>) -> Self {`
- `pub fn encode_id_token(claims: &ChatGptIdTokenClaims) -> Result<String> {`
- `pub fn write_chatgpt_auth(`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use base64::Engine;`
- `use base64::engine::general_purpose::URL_SAFE_NO_PAD;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::auth::AuthDotJson;`
- `use codex_core::auth::save_auth;`
- `use codex_core::token_data::TokenData;`
- `use codex_core::token_data::parse_id_token;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
