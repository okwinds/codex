# `codex-rs/core/tests/suite/auth_refresh.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `19487`
- sha256: `8eeb280522781ebeeaa95ae85cf04c150776ee8435acfb77b6f826510dbced9a`
- generated_utc: `2026-02-08T10:45:35Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/auth_refresh.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use base64::Engine;`
- `use chrono::Duration;`
- `use chrono::Utc;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_core::AuthManager;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::auth::AuthDotJson;`
- `use codex_core::auth::REFRESH_TOKEN_URL_OVERRIDE_ENV_VAR;`
- `use codex_core::auth::RefreshTokenError;`
- `use codex_core::auth::load_auth_dot_json;`
- `use codex_core::auth::save_auth;`
- `use codex_core::error::RefreshTokenFailedReason;`
- `use codex_core::token_data::IdTokenInfo;`
- `use codex_core::token_data::TokenData;`
- `use core_test_support::skip_if_no_network;`
- `use pretty_assertions::assert_eq;`
- `use serde::Serialize;`
- `use serde_json::Value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
