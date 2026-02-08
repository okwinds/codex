# `codex-rs/core/tests/suite/rmcp_client.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `38583`
- sha256: `ed947ed4da7baf073a64fe305d6a4aaecd431a525869fbd43e56266706cce59d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/rmcp_client.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::ffi::OsStr;`
- `use std::ffi::OsString;`
- `use std::fs;`
- `use std::net::TcpListener;`
- `use std::path::Path;`
- `use std::time::Duration;`
- `use std::time::SystemTime;`
- `use std::time::UNIX_EPOCH;`
- `use codex_core::config::types::McpServerConfig;`
- `use codex_core::config::types::McpServerTransportConfig;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::McpInvocation;`
- `use codex_core::protocol::McpToolCallBeginEvent;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::user_input::UserInput;`
- `use codex_utils_cargo_bin::cargo_bin;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
