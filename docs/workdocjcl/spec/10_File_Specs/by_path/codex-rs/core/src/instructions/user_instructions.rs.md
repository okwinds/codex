# `codex-rs/core/src/instructions/user_instructions.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5276`
- sha256: `334b5a46c002569874715115ae6bbcb9a3a9864bbe83f99f5dfddb2ae426edcc`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/instructions/user_instructions.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn is_user_instructions(message: &[ContentItem]) -> bool {`
- `pub fn is_skill_instructions(message: &[ContentItem]) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/instructions/user_instructions.rs:1` `use serde::Deserialize;`
- `use` `codex-rs/core/src/instructions/user_instructions.rs:2` `use serde::Serialize;`
- `use` `codex-rs/core/src/instructions/user_instructions.rs:4` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/instructions/user_instructions.rs:5` `use codex_protocol::models::ResponseItem;`
- `const` `codex-rs/core/src/instructions/user_instructions.rs:7` `pub const USER_INSTRUCTIONS_OPEN_TAG_LEGACY: &str = "<user_instructions>";`
- `const` `codex-rs/core/src/instructions/user_instructions.rs:8` `pub const USER_INSTRUCTIONS_PREFIX: &str = "# AGENTS.md instructions for ";`
- `const` `codex-rs/core/src/instructions/user_instructions.rs:9` `pub const SKILL_INSTRUCTIONS_PREFIX: &str = "<skill";`
- `impl` `codex-rs/core/src/instructions/user_instructions.rs:18` `impl UserInstructions {`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:19` `pub fn is_user_instructions(message: &[ContentItem]) -> bool {`
- `impl` `codex-rs/core/src/instructions/user_instructions.rs:29` `impl From<UserInstructions> for ResponseItem {`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:30` `fn from(ui: UserInstructions) -> Self {`
- `impl` `codex-rs/core/src/instructions/user_instructions.rs:55` `impl SkillInstructions {`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:56` `pub fn is_skill_instructions(message: &[ContentItem]) -> bool {`
- `impl` `codex-rs/core/src/instructions/user_instructions.rs:65` `impl From<SkillInstructions> for ResponseItem {`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:66` `fn from(si: SkillInstructions) -> Self {`
- `use` `codex-rs/core/src/instructions/user_instructions.rs:84` `use super::*;`
- `use` `codex-rs/core/src/instructions/user_instructions.rs:85` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:88` `fn test_user_instructions() {`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:112` `fn test_is_user_instructions() {`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:131` `fn test_skill_instructions() {`
- `fn` `codex-rs/core/src/instructions/user_instructions.rs:156` `fn test_is_skill_instructions() {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
