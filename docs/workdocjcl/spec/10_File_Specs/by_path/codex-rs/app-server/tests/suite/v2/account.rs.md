# `codex-rs/app-server/tests/suite/v2/account.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `40061`
- sha256: `247f5aef2d62462b36f69109c79165d4a29a310fc6bee0f9160c7030bcc113f4`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/account.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use anyhow::bail;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use app_test_support::ChatGptAuthFixture;`
- `use app_test_support::ChatGptIdTokenClaims;`
- `use app_test_support::encode_id_token;`
- `use app_test_support::write_chatgpt_auth;`
- `use app_test_support::write_models_cache;`
- `use codex_app_server_protocol::Account;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_app_server_protocol::CancelLoginAccountParams;`
- `use codex_app_server_protocol::CancelLoginAccountResponse;`
- `use codex_app_server_protocol::CancelLoginAccountStatus;`
- `use codex_app_server_protocol::ChatgptAuthTokensRefreshReason;`
- `use codex_app_server_protocol::ChatgptAuthTokensRefreshResponse;`
- `use codex_app_server_protocol::GetAccountParams;`
- `use codex_app_server_protocol::GetAccountResponse;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCErrorError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
