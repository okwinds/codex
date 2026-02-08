# `codex-rs/core/tests/common/streaming_sse.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `25291`
- sha256: `e98833d79000b39342cae84a64eb465c500293500db1bd94d3e55bb4c112208a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/common/streaming_sse.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct StreamingSseChunk {`
- `pub struct StreamingSseServer {`
- `pub fn uri(&self) -> &str {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::VecDeque;`
- `use std::sync::Arc;`
- `use std::time::SystemTime;`
- `use std::time::UNIX_EPOCH;`
- `use tokio::io::AsyncReadExt;`
- `use tokio::io::AsyncWriteExt;`
- `use tokio::net::TcpListener;`
- `use tokio::sync::Mutex as TokioMutex;`
- `use tokio::sync::oneshot;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use reqwest::StatusCode;`
- `use tokio::net::TcpStream;`
- `use tokio::time::Duration;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
