# `codex-rs/protocol/src/openai_models.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `22447`
- sha256: `52821d907c18d1e05982f8f40c56bc8de0b5bcf81150e00dd136897079cb5028`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/openai_models.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ReasoningEffort {`
- `pub enum InputModality {`
- `pub fn default_input_modalities() -> Vec<InputModality> {`
- `pub struct ReasoningEffortPreset {`
- `pub struct ModelUpgrade {`
- `pub struct ModelPreset {`
- `pub enum ModelVisibility {`
- `pub enum ConfigShellToolType {`
- `pub enum ApplyPatchToolType {`
- `pub enum TruncationMode {`
- `pub struct TruncationPolicyConfig {`
- `pub struct ClientVersion(pub i32, pub i32, pub i32);`
- `pub struct ModelInfo {`
- `pub fn auto_compact_token_limit(&self) -> Option<i64> {`
- `pub fn supports_personality(&self) -> bool {`
- `pub fn get_model_instructions(&self, personality: Option<Personality>) -> String {`
- `pub struct ModelMessages {`
- `pub fn get_personality_message(&self, personality: Option<Personality>) -> Option<String> {`
- `pub struct ModelInstructionsVariables {`
- `pub fn is_complete(&self) -> bool {`
- `pub fn get_personality_message(&self, personality: Option<Personality>) -> Option<String> {`
- `pub struct ModelInfoUpgrade {`
- `pub struct ModelsResponse {`
- `pub fn filter_by_auth(models: Vec<ModelPreset>, chatgpt_mode: bool) -> Vec<ModelPreset> {`
- `pub fn merge(`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/openai_models.rs:6` `use std::collections::HashMap;`
- `use` `codex-rs/protocol/src/openai_models.rs:7` `use std::collections::HashSet;`
- `use` `codex-rs/protocol/src/openai_models.rs:9` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/openai_models.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/openai_models.rs:11` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/openai_models.rs:12` `use strum::IntoEnumIterator;`
- `use` `codex-rs/protocol/src/openai_models.rs:13` `use strum_macros::Display;`
- `use` `codex-rs/protocol/src/openai_models.rs:14` `use strum_macros::EnumIter;`
- `use` `codex-rs/protocol/src/openai_models.rs:15` `use tracing::warn;`
- `use` `codex-rs/protocol/src/openai_models.rs:16` `use ts_rs::TS;`
- `use` `codex-rs/protocol/src/openai_models.rs:18` `use crate::config_types::Personality;`
- `use` `codex-rs/protocol/src/openai_models.rs:19` `use crate::config_types::Verbosity;`
- `const` `codex-rs/protocol/src/openai_models.rs:21` `const PERSONALITY_PLACEHOLDER: &str = "{{ personality }}";`
- `enum` `codex-rs/protocol/src/openai_models.rs:41` `pub enum ReasoningEffort {`
- `enum` `codex-rs/protocol/src/openai_models.rs:68` `pub enum InputModality {`
- `fn` `codex-rs/protocol/src/openai_models.rs:79` `pub fn default_input_modalities() -> Vec<InputModality> {`
- `struct` `codex-rs/protocol/src/openai_models.rs:85` `pub struct ReasoningEffortPreset {`
- `struct` `codex-rs/protocol/src/openai_models.rs:93` `pub struct ModelUpgrade {`
- `struct` `codex-rs/protocol/src/openai_models.rs:104` `pub struct ModelPreset {`
- `enum` `codex-rs/protocol/src/openai_models.rs:139` `pub enum ModelVisibility {`
- `enum` `codex-rs/protocol/src/openai_models.rs:162` `pub enum ConfigShellToolType {`
- `enum` `codex-rs/protocol/src/openai_models.rs:172` `pub enum ApplyPatchToolType {`
- `enum` `codex-rs/protocol/src/openai_models.rs:180` `pub enum TruncationMode {`
- `struct` `codex-rs/protocol/src/openai_models.rs:186` `pub struct TruncationPolicyConfig {`
- `impl` `codex-rs/protocol/src/openai_models.rs:191` `impl TruncationPolicyConfig {`
- `const` `codex-rs/protocol/src/openai_models.rs:192` `pub const fn bytes(limit: i64) -> Self {`
- `const` `codex-rs/protocol/src/openai_models.rs:199` `pub const fn tokens(limit: i64) -> Self {`
- `struct` `codex-rs/protocol/src/openai_models.rs:209` `pub struct ClientVersion(pub i32, pub i32, pub i32);`
- `const` `codex-rs/protocol/src/openai_models.rs:211` `const fn default_effective_context_window_percent() -> i64 {`
- `struct` `codex-rs/protocol/src/openai_models.rs:217` `pub struct ModelInfo {`
- `impl` `codex-rs/protocol/src/openai_models.rs:254` `impl ModelInfo {`
- `fn` `codex-rs/protocol/src/openai_models.rs:255` `pub fn auto_compact_token_limit(&self) -> Option<i64> {`
- `fn` `codex-rs/protocol/src/openai_models.rs:262` `pub fn supports_personality(&self) -> bool {`
- `fn` `codex-rs/protocol/src/openai_models.rs:268` `pub fn get_model_instructions(&self, personality: Option<Personality>) -> String {`
- `struct` `codex-rs/protocol/src/openai_models.rs:293` `pub struct ModelMessages {`
- `impl` `codex-rs/protocol/src/openai_models.rs:298` `impl ModelMessages {`
- `fn` `codex-rs/protocol/src/openai_models.rs:299` `fn has_personality_placeholder(&self) -> bool {`
- `fn` `codex-rs/protocol/src/openai_models.rs:306` `fn supports_personality(&self) -> bool {`
- `fn` `codex-rs/protocol/src/openai_models.rs:314` `pub fn get_personality_message(&self, personality: Option<Personality>) -> Option<String> {`
- `struct` `codex-rs/protocol/src/openai_models.rs:322` `pub struct ModelInstructionsVariables {`
- `impl` `codex-rs/protocol/src/openai_models.rs:328` `impl ModelInstructionsVariables {`
- `fn` `codex-rs/protocol/src/openai_models.rs:329` `pub fn is_complete(&self) -> bool {`
- `fn` `codex-rs/protocol/src/openai_models.rs:335` `pub fn get_personality_message(&self, personality: Option<Personality>) -> Option<String> {`
- `struct` `codex-rs/protocol/src/openai_models.rs:349` `pub struct ModelInfoUpgrade {`
- `impl` `codex-rs/protocol/src/openai_models.rs:354` `impl From<&ModelUpgrade> for ModelInfoUpgrade {`
- `fn` `codex-rs/protocol/src/openai_models.rs:355` `fn from(upgrade: &ModelUpgrade) -> Self {`
- `struct` `codex-rs/protocol/src/openai_models.rs:365` `pub struct ModelsResponse {`
- `impl` `codex-rs/protocol/src/openai_models.rs:370` `impl From<ModelInfo> for ModelPreset {`
- `fn` `codex-rs/protocol/src/openai_models.rs:371` `fn from(info: ModelInfo) -> Self {`
- `impl` `codex-rs/protocol/src/openai_models.rs:402` `impl ModelPreset {`
- `fn` `codex-rs/protocol/src/openai_models.rs:406` `pub fn filter_by_auth(models: Vec<ModelPreset>, chatgpt_mode: bool) -> Vec<ModelPreset> {`
- `fn` `codex-rs/protocol/src/openai_models.rs:416` `pub fn merge(`
- `fn` `codex-rs/protocol/src/openai_models.rs:442` `fn reasoning_effort_mapping_from_presets(`
- `fn` `codex-rs/protocol/src/openai_models.rs:459` `fn effort_rank(effort: ReasoningEffort) -> i32 {`
- `fn` `codex-rs/protocol/src/openai_models.rs:470` `fn nearest_effort(target: ReasoningEffort, supported: &[ReasoningEffort]) -> ReasoningEffort {`
- `use` `codex-rs/protocol/src/openai_models.rs:481` `use super::*;`
- `use` `codex-rs/protocol/src/openai_models.rs:482` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/protocol/src/openai_models.rs:484` `fn test_model(spec: Option<ModelMessages>) -> ModelInfo {`
- `fn` `codex-rs/protocol/src/openai_models.rs:512` `fn personality_variables() -> ModelInstructionsVariables {`
- `fn` `codex-rs/protocol/src/openai_models.rs:521` `fn get_model_instructions_uses_template_when_placeholder_present() {`
- `fn` `codex-rs/protocol/src/openai_models.rs:533` `fn get_model_instructions_always_strips_placeholder() {`
- `fn` `codex-rs/protocol/src/openai_models.rs:580` `fn get_model_instructions_falls_back_when_template_is_missing() {`
- `fn` `codex-rs/protocol/src/openai_models.rs:596` `fn get_personality_message_returns_default_when_personality_is_none() {`
- `fn` `codex-rs/protocol/src/openai_models.rs:605` `fn get_personality_message() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use strum::IntoEnumIterator;`
- `use strum_macros::Display;`
- `use strum_macros::EnumIter;`
- `use tracing::warn;`
- `use ts_rs::TS;`
- `use crate::config_types::Personality;`
- `use crate::config_types::Verbosity;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
