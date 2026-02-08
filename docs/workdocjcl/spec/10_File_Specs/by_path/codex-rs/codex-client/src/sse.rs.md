# `codex-rs/codex-client/src/sse.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1552`
- sha256: `2c43d61b62621a141aee5b0a8f742bbf70f1be08f0d27255ea38c54e4a06e774`
- generated_utc: `2026-02-08T10:45:22Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/sse.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn sse_stream(`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-client/src/sse.rs:1` `use crate::error::StreamError;`
- `use` `codex-rs/codex-client/src/sse.rs:2` `use crate::transport::ByteStream;`
- `use` `codex-rs/codex-client/src/sse.rs:3` `use eventsource_stream::Eventsource;`
- `use` `codex-rs/codex-client/src/sse.rs:4` `use futures::StreamExt;`
- `use` `codex-rs/codex-client/src/sse.rs:5` `use tokio::sync::mpsc;`
- `use` `codex-rs/codex-client/src/sse.rs:6` `use tokio::time::Duration;`
- `use` `codex-rs/codex-client/src/sse.rs:7` `use tokio::time::timeout;`
- `fn` `codex-rs/codex-client/src/sse.rs:12` `pub fn sse_stream(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::StreamError;`
- `use crate::transport::ByteStream;`
- `use eventsource_stream::Eventsource;`
- `use futures::StreamExt;`
- `use tokio::sync::mpsc;`
- `use tokio::time::Duration;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
