# `codex-rs/tui/src/status/helpers.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6144`
- sha256: `805bd62578ea0f0bf8adf3f695aa22d7f99b79d94ad5e8b9eb4a173016cbc838`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/status/helpers.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/status/helpers.rs:1` `use crate::exec_command::relativize_to_home;`
- `use` `codex-rs/tui/src/status/helpers.rs:2` `use crate::text_formatting;`
- `use` `codex-rs/tui/src/status/helpers.rs:3` `use chrono::DateTime;`
- `use` `codex-rs/tui/src/status/helpers.rs:4` `use chrono::Local;`
- `use` `codex-rs/tui/src/status/helpers.rs:5` `use codex_core::AuthManager;`
- `use` `codex-rs/tui/src/status/helpers.rs:6` `use codex_core::CodexAuth;`
- `use` `codex-rs/tui/src/status/helpers.rs:7` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/status/helpers.rs:8` `use codex_core::project_doc::discover_project_doc_paths;`
- `use` `codex-rs/tui/src/status/helpers.rs:9` `use codex_protocol::account::PlanType;`
- `use` `codex-rs/tui/src/status/helpers.rs:10` `use std::path::Path;`
- `use` `codex-rs/tui/src/status/helpers.rs:11` `use unicode_width::UnicodeWidthStr;`
- `use` `codex-rs/tui/src/status/helpers.rs:13` `use super::account::StatusAccountDisplay;`
- `fn` `codex-rs/tui/src/status/helpers.rs:15` `fn normalize_agents_display_path(path: &Path) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec_command::relativize_to_home;`
- `use crate::text_formatting;`
- `use chrono::DateTime;`
- `use chrono::Local;`
- `use codex_core::AuthManager;`
- `use codex_core::CodexAuth;`
- `use codex_core::config::Config;`
- `use codex_core::project_doc::discover_project_doc_paths;`
- `use codex_protocol::account::PlanType;`
- `use std::path::Path;`
- `use unicode_width::UnicodeWidthStr;`
- `use super::account::StatusAccountDisplay;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
