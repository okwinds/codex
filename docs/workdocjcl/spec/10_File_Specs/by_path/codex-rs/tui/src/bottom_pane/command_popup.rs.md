# `codex-rs/tui/src/bottom_pane/command_popup.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `21755`
- sha256: `1676e8b33e2cb92b406ac3ae6c3b233ba702a09a4602d2f53b774e9ac0d3fc7c`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/command_popup.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:1` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:2` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:3` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:5` `use super::popup_consts::MAX_POPUP_ROWS;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:6` `use super::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:7` `use super::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:8` `use super::selection_popup_common::render_rows;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:9` `use super::slash_commands;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:10` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:11` `use crate::render::RectExt;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:12` `use crate::slash_command::SlashCommand;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:13` `use codex_protocol::custom_prompts::CustomPrompt;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:14` `use codex_protocol::custom_prompts::PROMPTS_CMD_PREFIX;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:15` `use std::collections::HashSet;`
- `const` `codex-rs/tui/src/bottom_pane/command_popup.rs:20` `const ALIAS_COMMANDS: &[SlashCommand] = &[SlashCommand::Quit, SlashCommand::Approvals];`
- `impl` `codex-rs/tui/src/bottom_pane/command_popup.rs:45` `impl CommandPopup {`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:115` `use super::selection_popup_common::measure_rows_height;`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:124` `fn filtered(&self) -> Vec<(CommandItem, Option<Vec<usize>>)> {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:191` `fn filtered_items(&self) -> Vec<CommandItem> {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:195` `fn rows_from_matches(`
- `impl` `codex-rs/tui/src/bottom_pane/command_popup.rs:255` `impl WidgetRef for CommandPopup {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:256` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:271` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/command_popup.rs:272` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:275` `fn filter_includes_init_when_typing_prefix() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:295` `fn selecting_init_by_exact_match() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:310` `fn model_is_first_suggestion_for_mo() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:324` `fn filtered_commands_keep_presentation_order_for_prefix() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:340` `fn prompt_discovery_lists_custom_prompts() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:371` `fn prompt_name_collision_with_builtin_is_ignored() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:395` `fn prompt_description_uses_frontmatter_metadata() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:415` `fn prompt_description_falls_back_when_missing() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:432` `fn prefix_filter_limits_matches_for_ac() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:451` `fn quit_hidden_in_empty_filter_but_shown_for_prefix() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:463` `fn collab_command_hidden_when_collaboration_modes_disabled() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:486` `fn collab_command_visible_when_collaboration_modes_enabled() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:505` `fn plan_command_visible_when_collaboration_modes_enabled() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:524` `fn personality_command_hidden_when_disabled() {`
- `fn` `codex-rs/tui/src/bottom_pane/command_popup.rs:551` `fn personality_command_visible_when_enabled() {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::widgets::WidgetRef;`
- `use super::popup_consts::MAX_POPUP_ROWS;`
- `use super::scroll_state::ScrollState;`
- `use super::selection_popup_common::GenericDisplayRow;`
- `use super::selection_popup_common::render_rows;`
- `use super::slash_commands;`
- `use crate::render::Insets;`
- `use crate::render::RectExt;`
- `use crate::slash_command::SlashCommand;`
- `use codex_protocol::custom_prompts::CustomPrompt;`
- `use codex_protocol::custom_prompts::PROMPTS_CMD_PREFIX;`
- `use std::collections::HashSet;`
- `use super::selection_popup_common::measure_rows_height;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
