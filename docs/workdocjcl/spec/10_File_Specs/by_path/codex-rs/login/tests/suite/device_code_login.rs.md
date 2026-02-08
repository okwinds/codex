# `codex-rs/login/tests/suite/device_code_login.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `10188`
- sha256: `364ed06e12a486a10543feed21af3b09b251e01adc727ca8c420f553725a9829`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/login/tests/suite/device_code_login.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use base64::Engine;`
- `use base64::engine::general_purpose::URL_SAFE_NO_PAD;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::auth::load_auth_dot_json;`
- `use codex_login::ServerOptions;`
- `use codex_login::run_device_code_login;`
- `use serde_json::json;`
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicUsize;`
- `use std::sync::atomic::Ordering;`
- `use tempfile::tempdir;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::Request;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
- `use core_test_support::skip_if_no_network;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
