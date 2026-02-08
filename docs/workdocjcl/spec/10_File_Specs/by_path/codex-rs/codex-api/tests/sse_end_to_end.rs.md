# `codex-rs/codex-api/tests/sse_end_to_end.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6633`
- sha256: `12f2b3d7ece83b6dd35dcee1dafa723e0714c6dfe5110cf68a577348830ab71b`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/tests/sse_end_to_end.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use async_trait::async_trait;`
- `use bytes::Bytes;`
- `use codex_api::AggregateStreamExt;`
- `use codex_api::AuthProvider;`
- `use codex_api::Provider;`
- `use codex_api::ResponseEvent;`
- `use codex_api::ResponsesClient;`
- `use codex_api::requests::responses::Compression;`
- `use codex_client::HttpTransport;`
- `use codex_client::Request;`
- `use codex_client::Response;`
- `use codex_client::StreamResponse;`
- `use codex_client::TransportError;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use futures::StreamExt;`
- `use http::HeaderMap;`
- `use http::StatusCode;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
