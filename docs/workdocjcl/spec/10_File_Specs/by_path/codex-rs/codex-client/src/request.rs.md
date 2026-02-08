# `codex-rs/codex-client/src/request.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1178`
- sha256: `70a3b377d4793ad6be6dd06c51b00c2c2ca46035612c55d68aa9a29c2f72e8db`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/request.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub enum RequestCompression {`
- `pub struct Request {`
- `pub fn new(method: Method, url: String) -> Self {`
- `pub fn with_compression(mut self, compression: RequestCompression) -> Self {`
- `pub struct Response {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-client/src/request.rs:1` `use bytes::Bytes;`
- `use` `codex-rs/codex-client/src/request.rs:2` `use http::Method;`
- `use` `codex-rs/codex-client/src/request.rs:3` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/codex-client/src/request.rs:4` `use serde::Serialize;`
- `use` `codex-rs/codex-client/src/request.rs:5` `use serde_json::Value;`
- `use` `codex-rs/codex-client/src/request.rs:6` `use std::time::Duration;`
- `enum` `codex-rs/codex-client/src/request.rs:9` `pub enum RequestCompression {`
- `struct` `codex-rs/codex-client/src/request.rs:16` `pub struct Request {`
- `impl` `codex-rs/codex-client/src/request.rs:25` `impl Request {`
- `fn` `codex-rs/codex-client/src/request.rs:26` `pub fn new(method: Method, url: String) -> Self {`
- `fn` `codex-rs/codex-client/src/request.rs:42` `pub fn with_compression(mut self, compression: RequestCompression) -> Self {`
- `struct` `codex-rs/codex-client/src/request.rs:49` `pub struct Response {`

## Dependencies (auto sample)
### Imports / Includes
- `use bytes::Bytes;`
- `use http::Method;`
- `use reqwest::header::HeaderMap;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
