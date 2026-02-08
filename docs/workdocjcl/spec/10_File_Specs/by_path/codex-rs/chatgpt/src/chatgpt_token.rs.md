# `codex-rs/chatgpt/src/chatgpt_token.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1002`
- sha256: `633a8b8f153655424f9953bb609bb09668476d03e8315faeb4f6fcba7a692948`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/chatgpt/src/chatgpt_token.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn get_chatgpt_token_data() -> Option<TokenData> {`
- `pub fn set_chatgpt_token_data(value: TokenData) {`

## Definitions (auto, per-file)
- `use` `codex-rs/chatgpt/src/chatgpt_token.rs:1` `use codex_core::AuthManager;`
- `use` `codex-rs/chatgpt/src/chatgpt_token.rs:2` `use std::path::Path;`
- `use` `codex-rs/chatgpt/src/chatgpt_token.rs:3` `use std::sync::LazyLock;`
- `use` `codex-rs/chatgpt/src/chatgpt_token.rs:4` `use std::sync::RwLock;`
- `use` `codex-rs/chatgpt/src/chatgpt_token.rs:6` `use codex_core::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/chatgpt/src/chatgpt_token.rs:7` `use codex_core::token_data::TokenData;`
- `static` `codex-rs/chatgpt/src/chatgpt_token.rs:9` `static CHATGPT_TOKEN: LazyLock<RwLock<Option<TokenData>>> = LazyLock::new(|| RwLock::new(None));`
- `fn` `codex-rs/chatgpt/src/chatgpt_token.rs:11` `pub fn get_chatgpt_token_data() -> Option<TokenData> {`
- `fn` `codex-rs/chatgpt/src/chatgpt_token.rs:15` `pub fn set_chatgpt_token_data(value: TokenData) {`
- `fn` `codex-rs/chatgpt/src/chatgpt_token.rs:22` `pub async fn init_chatgpt_token_from_auth(`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::AuthManager;`
- `use std::path::Path;`
- `use std::sync::LazyLock;`
- `use std::sync::RwLock;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::token_data::TokenData;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
