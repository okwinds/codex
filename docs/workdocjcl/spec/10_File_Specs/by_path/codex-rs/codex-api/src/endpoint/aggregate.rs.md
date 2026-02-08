# `codex-rs/codex-api/src/endpoint/aggregate.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6417`
- sha256: `854764a269963902ea3c2f2908ab0316080aeb75a4eee9992dde8e2ce5beff8f`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/aggregate.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct AggregatedStream {`
- `pub trait AggregateStreamExt {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:1` `use crate::common::ResponseEvent;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:2` `use crate::common::ResponseStream;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:3` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:4` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:5` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:6` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:7` `use futures::Stream;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:8` `use std::collections::VecDeque;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:9` `use std::pin::Pin;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:10` `use std::task::Context;`
- `use` `codex-rs/codex-api/src/endpoint/aggregate.rs:11` `use std::task::Poll;`
- `struct` `codex-rs/codex-api/src/endpoint/aggregate.rs:14` `pub struct AggregatedStream {`
- `impl` `codex-rs/codex-api/src/endpoint/aggregate.rs:21` `impl Stream for AggregatedStream {`
- `type` `codex-rs/codex-api/src/endpoint/aggregate.rs:22` `type Item = Result<ResponseEvent, ApiError>;`
- `fn` `codex-rs/codex-api/src/endpoint/aggregate.rs:24` `fn poll_next(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {`
- `trait` `codex-rs/codex-api/src/endpoint/aggregate.rs:138` `pub trait AggregateStreamExt {`
- `fn` `codex-rs/codex-api/src/endpoint/aggregate.rs:139` `fn aggregate(self) -> AggregatedStream;`
- `impl` `codex-rs/codex-api/src/endpoint/aggregate.rs:142` `impl AggregateStreamExt for ResponseStream {`
- `fn` `codex-rs/codex-api/src/endpoint/aggregate.rs:143` `fn aggregate(self) -> AggregatedStream {`
- `impl` `codex-rs/codex-api/src/endpoint/aggregate.rs:148` `impl AggregatedStream {`
- `fn` `codex-rs/codex-api/src/endpoint/aggregate.rs:149` `fn new(inner: ResponseStream) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::common::ResponseEvent;`
- `use crate::common::ResponseStream;`
- `use crate::error::ApiError;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ReasoningItemContent;`
- `use codex_protocol::models::ResponseItem;`
- `use futures::Stream;`
- `use std::collections::VecDeque;`
- `use std::pin::Pin;`
- `use std::task::Context;`
- `use std::task::Poll;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
