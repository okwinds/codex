# `codex-rs/core/src/token_data.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8419`
- sha256: `864f41fad5b76ba2795e98e9d40469760818ea5475ec3ae5b06653344d668f7d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/token_data.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct TokenData {`
- `pub struct IdTokenInfo {`
- `pub fn get_chatgpt_plan_type(&self) -> Option<String> {`
- `pub fn is_workspace_account(&self) -> bool {`
- `pub enum IdTokenInfoError {`
- `pub fn parse_id_token(id_token: &str) -> Result<IdTokenInfo, IdTokenInfoError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/token_data.rs:1` `use base64::Engine;`
- `use` `codex-rs/core/src/token_data.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/core/src/token_data.rs:3` `use serde::Serialize;`
- `use` `codex-rs/core/src/token_data.rs:4` `use thiserror::Error;`
- `struct` `codex-rs/core/src/token_data.rs:7` `pub struct TokenData {`
- `struct` `codex-rs/core/src/token_data.rs:25` `pub struct IdTokenInfo {`
- `impl` `codex-rs/core/src/token_data.rs:38` `impl IdTokenInfo {`
- `fn` `codex-rs/core/src/token_data.rs:39` `pub fn get_chatgpt_plan_type(&self) -> Option<String> {`
- `fn` `codex-rs/core/src/token_data.rs:46` `pub fn is_workspace_account(&self) -> bool {`
- `struct` `codex-rs/core/src/token_data.rs:77` `struct IdClaims {`
- `struct` `codex-rs/core/src/token_data.rs:87` `struct ProfileClaims {`
- `struct` `codex-rs/core/src/token_data.rs:93` `struct AuthClaims {`
- `enum` `codex-rs/core/src/token_data.rs:105` `pub enum IdTokenInfoError {`
- `fn` `codex-rs/core/src/token_data.rs:114` `pub fn parse_id_token(id_token: &str) -> Result<IdTokenInfo, IdTokenInfoError> {`
- `use` `codex-rs/core/src/token_data.rs:163` `use super::*;`
- `use` `codex-rs/core/src/token_data.rs:164` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/token_data.rs:165` `use serde::Serialize;`
- `fn` `codex-rs/core/src/token_data.rs:168` `fn id_token_info_parses_email_and_plan() {`
- `struct` `codex-rs/core/src/token_data.rs:170` `struct Header {`
- `fn` `codex-rs/core/src/token_data.rs:185` `fn b64url_no_pad(bytes: &[u8]) -> String {`
- `fn` `codex-rs/core/src/token_data.rs:200` `fn id_token_info_parses_go_plan() {`
- `struct` `codex-rs/core/src/token_data.rs:202` `struct Header {`
- `fn` `codex-rs/core/src/token_data.rs:217` `fn b64url_no_pad(bytes: &[u8]) -> String {`
- `fn` `codex-rs/core/src/token_data.rs:232` `fn id_token_info_handles_missing_fields() {`
- `struct` `codex-rs/core/src/token_data.rs:234` `struct Header {`
- `fn` `codex-rs/core/src/token_data.rs:244` `fn b64url_no_pad(bytes: &[u8]) -> String {`
- `fn` `codex-rs/core/src/token_data.rs:259` `fn workspace_account_detection_matches_workspace_plans() {`

## Dependencies (auto sample)
### Imports / Includes
- `use base64::Engine;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use thiserror::Error;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
