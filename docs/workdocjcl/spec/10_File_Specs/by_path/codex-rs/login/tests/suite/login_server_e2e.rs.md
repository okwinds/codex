# `codex-rs/login/tests/suite/login_server_e2e.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `11402`
- sha256: `09d23f1f95b6e806827533340fdfb08cffc7d62f3a70086fddbec2718f003431`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/login/tests/suite/login_server_e2e.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::net::SocketAddr;`
- `use std::net::TcpListener;`
- `use std::thread;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use base64::Engine;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_login::ServerOptions;`
- `use codex_login::run_login_server;`
- `use core_test_support::skip_if_no_network;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
