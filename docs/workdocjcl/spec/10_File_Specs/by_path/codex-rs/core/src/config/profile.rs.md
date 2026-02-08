# `codex-rs/core/src/config/profile.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2800`
- sha256: `7542a1b9a48ee8ccba28b590943d69d34aa7b8bc3c1bd3dc270c22ce59b72cc6`
- generated_utc: `2026-02-08T10:45:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config/profile.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ConfigProfile {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config/profile.rs:1` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config/profile.rs:2` `use schemars::JsonSchema;`
- `use` `codex-rs/core/src/config/profile.rs:3` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config/profile.rs:4` `use serde::Serialize;`
- `use` `codex-rs/core/src/config/profile.rs:6` `use crate::config::types::Personality;`
- `use` `codex-rs/core/src/config/profile.rs:7` `use crate::protocol::AskForApproval;`
- `use` `codex-rs/core/src/config/profile.rs:8` `use codex_protocol::config_types::ReasoningSummary;`
- `use` `codex-rs/core/src/config/profile.rs:9` `use codex_protocol::config_types::SandboxMode;`
- `use` `codex-rs/core/src/config/profile.rs:10` `use codex_protocol::config_types::Verbosity;`
- `use` `codex-rs/core/src/config/profile.rs:11` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/core/src/config/profile.rs:12` `use codex_protocol::openai_models::ReasoningEffort;`
- `struct` `codex-rs/core/src/config/profile.rs:18` `pub struct ConfigProfile {`
- `impl` `codex-rs/core/src/config/profile.rs:51` `impl From<ConfigProfile> for codex_app_server_protocol::Profile {`
- `fn` `codex-rs/core/src/config/profile.rs:52` `fn from(config_profile: ConfigProfile) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use crate::config::types::Personality;`
- `use crate::protocol::AskForApproval;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::config_types::SandboxMode;`
- `use codex_protocol::config_types::Verbosity;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use codex_protocol::openai_models::ReasoningEffort;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
