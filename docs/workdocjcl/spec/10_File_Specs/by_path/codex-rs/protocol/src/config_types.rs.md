# `codex-rs/protocol/src/config_types.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9530`
- sha256: `2f381b7c296ee80d35e05cee183d39d88af2b3bca5b48c69ac6182fa0696e28d`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/config_types.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ReasoningSummary {`
- `pub enum Verbosity {`
- `pub enum SandboxMode {`
- `pub enum WindowsSandboxLevel {`
- `pub enum Personality {`
- `pub enum WebSearchMode {`
- `pub enum ForcedLoginMethod {`
- `pub enum TrustLevel {`
- `pub enum AltScreenMode {`
- `pub enum ModeKind {`
- `pub struct CollaborationMode {`
- `pub fn model(&self) -> &str {`
- `pub fn reasoning_effort(&self) -> Option<ReasoningEffort> {`
- `pub fn with_updates(`
- `pub fn apply_mask(&self, mask: &CollaborationModeMask) -> Self {`
- `pub struct Settings {`
- `pub struct CollaborationModeMask {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/config_types.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/config_types.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/config_types.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/config_types.rs:4` `use strum_macros::Display;`
- `use` `codex-rs/protocol/src/config_types.rs:5` `use strum_macros::EnumIter;`
- `use` `codex-rs/protocol/src/config_types.rs:6` `use ts_rs::TS;`
- `use` `codex-rs/protocol/src/config_types.rs:8` `use crate::openai_models::ReasoningEffort;`
- `enum` `codex-rs/protocol/src/config_types.rs:18` `pub enum ReasoningSummary {`
- `enum` `codex-rs/protocol/src/config_types.rs:45` `pub enum Verbosity {`
- `enum` `codex-rs/protocol/src/config_types.rs:57` `pub enum SandboxMode {`
- `enum` `codex-rs/protocol/src/config_types.rs:74` `pub enum WindowsSandboxLevel {`
- `enum` `codex-rs/protocol/src/config_types.rs:98` `pub enum Personality {`
- `enum` `codex-rs/protocol/src/config_types.rs:108` `pub enum WebSearchMode {`
- `enum` `codex-rs/protocol/src/config_types.rs:118` `pub enum ForcedLoginMethod {`
- `enum` `codex-rs/protocol/src/config_types.rs:128` `pub enum TrustLevel {`
- `enum` `codex-rs/protocol/src/config_types.rs:158` `pub enum AltScreenMode {`
- `enum` `codex-rs/protocol/src/config_types.rs:173` `pub enum ModeKind {`
- `struct` `codex-rs/protocol/src/config_types.rs:185` `pub struct CollaborationMode {`
- `impl` `codex-rs/protocol/src/config_types.rs:190` `impl CollaborationMode {`
- `fn` `codex-rs/protocol/src/config_types.rs:192` `fn settings_ref(&self) -> &Settings {`
- `fn` `codex-rs/protocol/src/config_types.rs:196` `pub fn model(&self) -> &str {`
- `fn` `codex-rs/protocol/src/config_types.rs:200` `pub fn reasoning_effort(&self) -> Option<ReasoningEffort> {`
- `fn` `codex-rs/protocol/src/config_types.rs:211` `pub fn with_updates(`
- `fn` `codex-rs/protocol/src/config_types.rs:236` `pub fn apply_mask(&self, mask: &CollaborationModeMask) -> Self {`
- `struct` `codex-rs/protocol/src/config_types.rs:254` `pub struct Settings {`
- `struct` `codex-rs/protocol/src/config_types.rs:263` `pub struct CollaborationModeMask {`
- `use` `codex-rs/protocol/src/config_types.rs:273` `use super::*;`
- `use` `codex-rs/protocol/src/config_types.rs:274` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/protocol/src/config_types.rs:277` `fn apply_mask_can_clear_optional_fields() {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use strum_macros::Display;`
- `use strum_macros::EnumIter;`
- `use ts_rs::TS;`
- `use crate::openai_models::ReasoningEffort;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
