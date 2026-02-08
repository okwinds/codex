# `codex-rs/protocol/src/config_types.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11253`
- sha256: `4b59d40cd255a17b8f3e4f763fcfe288fd6ef82e93fb9f3a16344f24ba231f69`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `enum` `codex-rs/protocol/src/config_types.rs:109` `pub enum WebSearchMode {`
- `enum` `codex-rs/protocol/src/config_types.rs:119` `pub enum ForcedLoginMethod {`
- `enum` `codex-rs/protocol/src/config_types.rs:129` `pub enum TrustLevel {`
- `enum` `codex-rs/protocol/src/config_types.rs:159` `pub enum AltScreenMode {`
- `enum` `codex-rs/protocol/src/config_types.rs:174` `pub enum ModeKind {`
- `const` `codex-rs/protocol/src/config_types.rs:196` `pub const TUI_VISIBLE_COLLABORATION_MODES: [ModeKind; 2] = [ModeKind::Default, ModeKind::Plan];`
- `impl` `codex-rs/protocol/src/config_types.rs:198` `impl ModeKind {`
- `const` `codex-rs/protocol/src/config_types.rs:199` `pub const fn display_name(self) -> &'static str {`
- `const` `codex-rs/protocol/src/config_types.rs:208` `pub const fn is_tui_visible(self) -> bool {`
- `const` `codex-rs/protocol/src/config_types.rs:212` `pub const fn allows_request_user_input(self) -> bool {`
- `struct` `codex-rs/protocol/src/config_types.rs:220` `pub struct CollaborationMode {`
- `impl` `codex-rs/protocol/src/config_types.rs:225` `impl CollaborationMode {`
- `fn` `codex-rs/protocol/src/config_types.rs:227` `fn settings_ref(&self) -> &Settings {`
- `fn` `codex-rs/protocol/src/config_types.rs:231` `pub fn model(&self) -> &str {`
- `fn` `codex-rs/protocol/src/config_types.rs:235` `pub fn reasoning_effort(&self) -> Option<ReasoningEffort> {`
- `fn` `codex-rs/protocol/src/config_types.rs:246` `pub fn with_updates(`
- `fn` `codex-rs/protocol/src/config_types.rs:271` `pub fn apply_mask(&self, mask: &CollaborationModeMask) -> Self {`
- `struct` `codex-rs/protocol/src/config_types.rs:289` `pub struct Settings {`
- `struct` `codex-rs/protocol/src/config_types.rs:298` `pub struct CollaborationModeMask {`
- `use` `codex-rs/protocol/src/config_types.rs:308` `use super::*;`
- `use` `codex-rs/protocol/src/config_types.rs:309` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/protocol/src/config_types.rs:312` `fn apply_mask_can_clear_optional_fields() {`
- `fn` `codex-rs/protocol/src/config_types.rs:341` `fn mode_kind_deserializes_alias_values_to_default() {`
- `fn` `codex-rs/protocol/src/config_types.rs:350` `fn tui_visible_collaboration_modes_match_mode_kind_visibility() {`

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
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
