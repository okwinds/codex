# `codex-rs/tui/src/debug_config.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17385`
- sha256: `50c0bd0611d4a476bc02bc3a641914c403eaeee8150760c5d034e05293762397`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/debug_config.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/debug_config.rs:1` `use crate::history_cell::PlainHistoryCell;`
- `use` `codex-rs/tui/src/debug_config.rs:2` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/tui/src/debug_config.rs:3` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/debug_config.rs:4` `use codex_core::config_loader::ConfigLayerStack;`
- `use` `codex-rs/tui/src/debug_config.rs:5` `use codex_core::config_loader::ConfigLayerStackOrdering;`
- `use` `codex-rs/tui/src/debug_config.rs:6` `use codex_core::config_loader::NetworkConstraints;`
- `use` `codex-rs/tui/src/debug_config.rs:7` `use codex_core::config_loader::RequirementSource;`
- `use` `codex-rs/tui/src/debug_config.rs:8` `use codex_core::config_loader::ResidencyRequirement;`
- `use` `codex-rs/tui/src/debug_config.rs:9` `use codex_core::config_loader::SandboxModeRequirement;`
- `use` `codex-rs/tui/src/debug_config.rs:10` `use codex_core::config_loader::WebSearchModeRequirement;`
- `use` `codex-rs/tui/src/debug_config.rs:11` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/debug_config.rs:12` `use ratatui::text::Line;`
- `fn` `codex-rs/tui/src/debug_config.rs:18` `fn render_debug_config_lines(stack: &ConfigLayerStack) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/debug_config.rs:136` `fn requirement_line(`
- `fn` `codex-rs/tui/src/debug_config.rs:147` `fn join_or_empty(values: Vec<String>) -> String {`
- `fn` `codex-rs/tui/src/debug_config.rs:155` `fn normalize_allowed_web_search_modes(`
- `fn` `codex-rs/tui/src/debug_config.rs:169` `fn format_config_layer_source(source: &ConfigLayerSource) -> String {`
- `fn` `codex-rs/tui/src/debug_config.rs:196` `fn format_sandbox_mode_requirement(mode: SandboxModeRequirement) -> String {`
- `fn` `codex-rs/tui/src/debug_config.rs:205` `fn format_residency_requirement(requirement: ResidencyRequirement) -> String {`
- `fn` `codex-rs/tui/src/debug_config.rs:211` `fn format_network_constraints(network: &NetworkConstraints) -> String {`
- `use` `codex-rs/tui/src/debug_config.rs:270` `use super::render_debug_config_lines;`
- `use` `codex-rs/tui/src/debug_config.rs:271` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/tui/src/debug_config.rs:272` `use codex_core::config::Constrained;`
- `use` `codex-rs/tui/src/debug_config.rs:273` `use codex_core::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/tui/src/debug_config.rs:274` `use codex_core::config_loader::ConfigLayerStack;`
- `use` `codex-rs/tui/src/debug_config.rs:275` `use codex_core::config_loader::ConfigRequirements;`
- `use` `codex-rs/tui/src/debug_config.rs:276` `use codex_core::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/tui/src/debug_config.rs:277` `use codex_core::config_loader::ConstrainedWithSource;`
- `use` `codex-rs/tui/src/debug_config.rs:278` `use codex_core::config_loader::McpServerIdentity;`
- `use` `codex-rs/tui/src/debug_config.rs:279` `use codex_core::config_loader::McpServerRequirement;`
- `use` `codex-rs/tui/src/debug_config.rs:280` `use codex_core::config_loader::NetworkConstraints;`
- `use` `codex-rs/tui/src/debug_config.rs:281` `use codex_core::config_loader::RequirementSource;`
- `use` `codex-rs/tui/src/debug_config.rs:282` `use codex_core::config_loader::ResidencyRequirement;`
- `use` `codex-rs/tui/src/debug_config.rs:283` `use codex_core::config_loader::SandboxModeRequirement;`
- `use` `codex-rs/tui/src/debug_config.rs:284` `use codex_core::config_loader::Sourced;`
- `use` `codex-rs/tui/src/debug_config.rs:285` `use codex_core::config_loader::WebSearchModeRequirement;`
- `use` `codex-rs/tui/src/debug_config.rs:286` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/tui/src/debug_config.rs:287` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/tui/src/debug_config.rs:288` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/tui/src/debug_config.rs:289` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/tui/src/debug_config.rs:290` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/debug_config.rs:291` `use std::collections::BTreeMap;`
- `use` `codex-rs/tui/src/debug_config.rs:292` `use toml::Value as TomlValue;`
- `fn` `codex-rs/tui/src/debug_config.rs:294` `fn empty_toml_table() -> TomlValue {`
- `fn` `codex-rs/tui/src/debug_config.rs:298` `fn absolute_path(path: &str) -> AbsolutePathBuf {`
- `fn` `codex-rs/tui/src/debug_config.rs:302` `fn render_to_text(lines: &[Line<'static>]) -> String {`
- `fn` `codex-rs/tui/src/debug_config.rs:316` `fn debug_config_output_lists_all_layers_including_disabled() {`
- `fn` `codex-rs/tui/src/debug_config.rs:357` `fn debug_config_output_lists_requirement_sources() {`
- `fn` `codex-rs/tui/src/debug_config.rs:461` `fn debug_config_output_normalizes_empty_web_search_mode_list() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::history_cell::PlainHistoryCell;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_core::config::Config;`
- `use codex_core::config_loader::ConfigLayerStack;`
- `use codex_core::config_loader::ConfigLayerStackOrdering;`
- `use codex_core::config_loader::NetworkConstraints;`
- `use codex_core::config_loader::RequirementSource;`
- `use codex_core::config_loader::ResidencyRequirement;`
- `use codex_core::config_loader::SandboxModeRequirement;`
- `use codex_core::config_loader::WebSearchModeRequirement;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use super::render_debug_config_lines;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_core::config::Constrained;`
- `use codex_core::config_loader::ConfigLayerEntry;`
- `use codex_core::config_loader::ConfigLayerStack;`
- `use codex_core::config_loader::ConfigRequirements;`
- `use codex_core::config_loader::ConfigRequirementsToml;`
- `use codex_core::config_loader::ConstrainedWithSource;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
