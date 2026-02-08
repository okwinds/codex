# `codex-rs/core/src/skills/injection.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `26232`
- sha256: `86867b370bdf8074c4264d9a13d4a5497a7a016e43a5ab35dafc23a5be133932`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/injection.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/injection.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/skills/injection.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/skills/injection.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/skills/injection.rs:5` `use crate::analytics_client::AnalyticsEventsClient;`
- `use` `codex-rs/core/src/skills/injection.rs:6` `use crate::analytics_client::SkillInvocation;`
- `use` `codex-rs/core/src/skills/injection.rs:7` `use crate::analytics_client::TrackEventsContext;`
- `use` `codex-rs/core/src/skills/injection.rs:8` `use crate::instructions::SkillInstructions;`
- `use` `codex-rs/core/src/skills/injection.rs:9` `use crate::skills::SkillMetadata;`
- `use` `codex-rs/core/src/skills/injection.rs:10` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/skills/injection.rs:11` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/skills/injection.rs:12` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/skills/injection.rs:13` `use tokio::fs;`
- `fn` `codex-rs/core/src/skills/injection.rs:69` `fn emit_skill_injected_metric(otel: Option<&OtelManager>, skill: &SkillMetadata, status: &str) {`
- `struct` `codex-rs/core/src/skills/injection.rs:146` `struct SkillSelectionContext<'a> {`
- `impl` `codex-rs/core/src/skills/injection.rs:159` `impl<'a> ToolMentions<'a> {`
- `fn` `codex-rs/core/src/skills/injection.rs:160` `fn is_empty(&self) -> bool {`
- `const` `codex-rs/core/src/skills/injection.rs:181` `const APP_PATH_PREFIX: &str = "app://";`
- `const` `codex-rs/core/src/skills/injection.rs:182` `const MCP_PATH_PREFIX: &str = "mcp://";`
- `const` `codex-rs/core/src/skills/injection.rs:183` `const SKILL_PATH_PREFIX: &str = "skill://";`
- `const` `codex-rs/core/src/skills/injection.rs:184` `const SKILL_FILENAME: &str = "SKILL.md";`
- `fn` `codex-rs/core/src/skills/injection.rs:198` `fn is_skill_filename(path: &str) -> bool {`
- `fn` `codex-rs/core/src/skills/injection.rs:279` `fn select_skills_from_mentions(`
- `fn` `codex-rs/core/src/skills/injection.rs:408` `fn is_common_env_var(name: &str) -> bool {`
- `fn` `codex-rs/core/src/skills/injection.rs:427` `fn text_mentions_skill(text: &str, skill_name: &str) -> bool {`
- `fn` `codex-rs/core/src/skills/injection.rs:458` `fn is_mention_name_char(byte: u8) -> bool {`
- `use` `codex-rs/core/src/skills/injection.rs:464` `use super::*;`
- `use` `codex-rs/core/src/skills/injection.rs:465` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/skills/injection.rs:466` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/skills/injection.rs:467` `use std::collections::HashSet;`
- `fn` `codex-rs/core/src/skills/injection.rs:469` `fn make_skill(name: &str, path: &str) -> SkillMetadata {`
- `fn` `codex-rs/core/src/skills/injection.rs:485` `fn assert_mentions(text: &str, expected_names: &[&str], expected_paths: &[&str]) {`
- `fn` `codex-rs/core/src/skills/injection.rs:491` `fn build_skill_name_counts(`
- `fn` `codex-rs/core/src/skills/injection.rs:505` `fn collect_mentions(`
- `fn` `codex-rs/core/src/skills/injection.rs:522` `fn text_mentions_skill_requires_exact_boundary() {`
- `fn` `codex-rs/core/src/skills/injection.rs:546` `fn text_mentions_skill_handles_end_boundary_and_near_misses() {`
- `fn` `codex-rs/core/src/skills/injection.rs:556` `fn text_mentions_skill_handles_many_dollars_without_looping() {`
- `fn` `codex-rs/core/src/skills/injection.rs:563` `fn extract_tool_mentions_handles_plain_and_linked_mentions() {`
- `fn` `codex-rs/core/src/skills/injection.rs:572` `fn extract_tool_mentions_skips_common_env_vars() {`
- `fn` `codex-rs/core/src/skills/injection.rs:579` `fn extract_tool_mentions_requires_link_syntax() {`
- `fn` `codex-rs/core/src/skills/injection.rs:586` `fn extract_tool_mentions_trims_linked_paths_and_allows_spacing() {`
- `fn` `codex-rs/core/src/skills/injection.rs:591` `fn extract_tool_mentions_stops_at_non_name_chars() {`
- `fn` `codex-rs/core/src/skills/injection.rs:600` `fn collect_explicit_skill_mentions_text_respects_skill_order() {`
- `fn` `codex-rs/core/src/skills/injection.rs:617` `fn collect_explicit_skill_mentions_prioritizes_structured_inputs() {`
- `fn` `codex-rs/core/src/skills/injection.rs:639` `fn collect_explicit_skill_mentions_skips_invalid_structured_and_blocks_plain_fallback() {`
- `fn` `codex-rs/core/src/skills/injection.rs:660` `fn collect_explicit_skill_mentions_skips_disabled_structured_and_blocks_plain_fallback() {`
- `fn` `codex-rs/core/src/skills/injection.rs:682` `fn collect_explicit_skill_mentions_dedupes_by_path() {`
- `fn` `codex-rs/core/src/skills/injection.rs:697` `fn collect_explicit_skill_mentions_skips_ambiguous_name() {`
- `fn` `codex-rs/core/src/skills/injection.rs:713` `fn collect_explicit_skill_mentions_prefers_linked_path_over_name() {`
- `fn` `codex-rs/core/src/skills/injection.rs:729` `fn collect_explicit_skill_mentions_skips_plain_name_when_connector_matches() {`
- `fn` `codex-rs/core/src/skills/injection.rs:744` `fn collect_explicit_skill_mentions_allows_explicit_path_with_connector_conflict() {`
- `fn` `codex-rs/core/src/skills/injection.rs:759` `fn collect_explicit_skill_mentions_skips_when_linked_path_disabled() {`
- `fn` `codex-rs/core/src/skills/injection.rs:776` `fn collect_explicit_skill_mentions_prefers_resource_path() {`
- `fn` `codex-rs/core/src/skills/injection.rs:792` `fn collect_explicit_skill_mentions_skips_missing_path_with_no_fallback() {`
- `fn` `codex-rs/core/src/skills/injection.rs:808` `fn collect_explicit_skill_mentions_skips_missing_path_without_fallback() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::PathBuf;`
- `use crate::analytics_client::AnalyticsEventsClient;`
- `use crate::analytics_client::SkillInvocation;`
- `use crate::analytics_client::TrackEventsContext;`
- `use crate::instructions::SkillInstructions;`
- `use crate::skills::SkillMetadata;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::user_input::UserInput;`
- `use tokio::fs;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
