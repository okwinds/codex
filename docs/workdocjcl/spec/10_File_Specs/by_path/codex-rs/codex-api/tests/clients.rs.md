# `codex-rs/codex-api/tests/clients.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `9306`
- sha256: `66de5ab35ecf863e6c60a4e64db3cfd8ba89b3b618cd1ea0c3cca5103e0d7667`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/tests/clients.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use async_trait::async_trait;`
- `use bytes::Bytes;`
- `use codex_api::AuthProvider;`
- `use codex_api::ChatClient;`
- `use codex_api::Provider;`
- `use codex_api::ResponsesClient;`
- `use codex_api::ResponsesOptions;`
- `use codex_api::WireApi;`
- `use codex_api::requests::responses::Compression;`
- `use codex_client::HttpTransport;`
- `use codex_client::Request;`
- `use codex_client::Response;`
- `use codex_client::StreamResponse;`
- `use codex_client::TransportError;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
