# `codex-rs/tui/src/chatwidget/skills.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13861`
- sha256: `5a78f2855a8954b1830bb5fe61fa9c3405d8f492ab39848bb47a8a40fe1d15c8`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/chatwidget/skills.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/chatwidget/skills.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:3` `use std::path::Path;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:6` `use super::ChatWidget;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:7` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:8` `use crate::bottom_pane::SelectionItem;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:9` `use crate::bottom_pane::SelectionViewParams;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:10` `use crate::bottom_pane::SkillsToggleItem;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:11` `use crate::bottom_pane::SkillsToggleView;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:12` `use crate::bottom_pane::popup_consts::standard_popup_hint_line;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:13` `use crate::skills_helpers::skill_description;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:14` `use crate::skills_helpers::skill_display_name;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:15` `use codex_chatgpt::connectors::AppInfo;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:16` `use codex_core::connectors::connector_mention_slug;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:17` `use codex_core::protocol::ListSkillsResponseEvent;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:18` `use codex_core::protocol::SkillMetadata as ProtocolSkillMetadata;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:19` `use codex_core::protocol::SkillsListEntry;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:20` `use codex_core::skills::model::SkillDependencies;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:21` `use codex_core::skills::model::SkillInterface;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:22` `use codex_core::skills::model::SkillMetadata;`
- `use` `codex-rs/tui/src/chatwidget/skills.rs:23` `use codex_core::skills::model::SkillToolDependency;`
- `impl` `codex-rs/tui/src/chatwidget/skills.rs:25` `impl ChatWidget {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:146` `fn skills_for_cwd(cwd: &Path, skills_entries: &[SkillsListEntry]) -> Vec<ProtocolSkillMetadata> {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:154` `fn enabled_skills_for_mentions(skills: &[ProtocolSkillMetadata]) -> Vec<SkillMetadata> {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:162` `fn protocol_skill_to_core(skill: &ProtocolSkillMetadata) -> SkillMetadata {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:197` `fn normalize_skill_config_path(path: &Path) -> PathBuf {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:297` `fn extract_tool_mentions_from_text(text: &str) -> ToolMentions {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:412` `fn is_common_env_var(name: &str) -> bool {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:430` `fn is_mention_name_char(byte: u8) -> bool {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:434` `fn is_skill_path(path: &str) -> bool {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:438` `fn normalize_skill_path(path: &str) -> &str {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:442` `fn app_id_from_path(path: &str) -> Option<&str> {`
- `fn` `codex-rs/tui/src/chatwidget/skills.rs:447` `fn is_app_or_mcp_path(path: &str) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use super::ChatWidget;`
- `use crate::app_event::AppEvent;`
- `use crate::bottom_pane::SelectionItem;`
- `use crate::bottom_pane::SelectionViewParams;`
- `use crate::bottom_pane::SkillsToggleItem;`
- `use crate::bottom_pane::SkillsToggleView;`
- `use crate::bottom_pane::popup_consts::standard_popup_hint_line;`
- `use crate::skills_helpers::skill_description;`
- `use crate::skills_helpers::skill_display_name;`
- `use codex_chatgpt::connectors::AppInfo;`
- `use codex_core::connectors::connector_mention_slug;`
- `use codex_core::protocol::ListSkillsResponseEvent;`
- `use codex_core::protocol::SkillMetadata as ProtocolSkillMetadata;`
- `use codex_core::protocol::SkillsListEntry;`
- `use codex_core::skills::model::SkillDependencies;`
- `use codex_core::skills::model::SkillInterface;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
