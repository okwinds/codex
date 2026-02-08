# `codex-rs/app-server-protocol/src/jsonrpc_lite.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2141`
- sha256: `2c76e095a1d5d8260f6e630021f4bb92142405a828525a5b8d33fb05034c0756`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/jsonrpc_lite.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum RequestId {`
- `pub enum JSONRPCMessage {`
- `pub struct JSONRPCRequest {`
- `pub struct JSONRPCNotification {`
- `pub struct JSONRPCResponse {`
- `pub struct JSONRPCError {`
- `pub struct JSONRPCErrorError {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:4` `use schemars::JsonSchema;`
- `use` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:5` `use serde::Deserialize;`
- `use` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:6` `use serde::Serialize;`
- `use` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:7` `use ts_rs::TS;`
- `const` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:9` `pub const JSONRPC_VERSION: &str = "2.0";`
- `enum` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:13` `pub enum RequestId {`
- `type` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:19` `pub type Result = serde_json::Value;`
- `enum` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:24` `pub enum JSONRPCMessage {`
- `struct` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:33` `pub struct JSONRPCRequest {`
- `struct` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:43` `pub struct JSONRPCNotification {`
- `struct` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:52` `pub struct JSONRPCResponse {`
- `struct` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:59` `pub struct JSONRPCError {`
- `struct` `codex-rs/app-server-protocol/src/jsonrpc_lite.rs:65` `pub struct JSONRPCErrorError {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
