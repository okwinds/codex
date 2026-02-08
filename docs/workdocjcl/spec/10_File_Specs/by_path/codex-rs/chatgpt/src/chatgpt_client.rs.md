# `codex-rs/chatgpt/src/chatgpt_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2005`
- sha256: `3f1df20e7a6f721e41c4a8f140d4b55e69f5e2d8b341c980122769d902c69842`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/chatgpt/src/chatgpt_client.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/chatgpt/src/chatgpt_client.rs:1` `use codex_core::config::Config;`
- `use` `codex-rs/chatgpt/src/chatgpt_client.rs:2` `use codex_core::default_client::create_client;`
- `use` `codex-rs/chatgpt/src/chatgpt_client.rs:4` `use crate::chatgpt_token::get_chatgpt_token_data;`
- `use` `codex-rs/chatgpt/src/chatgpt_client.rs:5` `use crate::chatgpt_token::init_chatgpt_token_from_auth;`
- `use` `codex-rs/chatgpt/src/chatgpt_client.rs:7` `use anyhow::Context;`
- `use` `codex-rs/chatgpt/src/chatgpt_client.rs:8` `use serde::de::DeserializeOwned;`
- `use` `codex-rs/chatgpt/src/chatgpt_client.rs:9` `use std::time::Duration;`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::Config;`
- `use codex_core::default_client::create_client;`
- `use crate::chatgpt_token::get_chatgpt_token_data;`
- `use crate::chatgpt_token::init_chatgpt_token_from_auth;`
- `use anyhow::Context;`
- `use serde::de::DeserializeOwned;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
