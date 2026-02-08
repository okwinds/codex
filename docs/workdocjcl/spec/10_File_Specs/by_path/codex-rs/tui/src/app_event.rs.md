# `codex-rs/tui/src/app_event.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11348`
- sha256: `f48fff1e5ff5087eb02c79ba1d5bf4deced55013c1931f1c8229b56ee73f7e56`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/app_event.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/app_event.rs:11` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/app_event.rs:13` `use codex_chatgpt::connectors::AppInfo;`
- `use` `codex-rs/tui/src/app_event.rs:14` `use codex_common::approval_presets::ApprovalPreset;`
- `use` `codex-rs/tui/src/app_event.rs:15` `use codex_core::protocol::Event;`
- `use` `codex-rs/tui/src/app_event.rs:16` `use codex_core::protocol::RateLimitSnapshot;`
- `use` `codex-rs/tui/src/app_event.rs:17` `use codex_file_search::FileMatch;`
- `use` `codex-rs/tui/src/app_event.rs:18` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/app_event.rs:19` `use codex_protocol::openai_models::ModelPreset;`
- `use` `codex-rs/tui/src/app_event.rs:21` `use crate::bottom_pane::ApprovalRequest;`
- `use` `codex-rs/tui/src/app_event.rs:22` `use crate::bottom_pane::StatusLineItem;`
- `use` `codex-rs/tui/src/app_event.rs:23` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/app_event.rs:25` `use codex_core::features::Feature;`
- `use` `codex-rs/tui/src/app_event.rs:26` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/tui/src/app_event.rs:27` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/tui/src/app_event.rs:28` `use codex_protocol::config_types::CollaborationModeMask;`
- `use` `codex-rs/tui/src/app_event.rs:29` `use codex_protocol::config_types::Personality;`
- `use` `codex-rs/tui/src/app_event.rs:30` `use codex_protocol::openai_models::ReasoningEffort;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use codex_chatgpt::connectors::AppInfo;`
- `use codex_common::approval_presets::ApprovalPreset;`
- `use codex_core::protocol::Event;`
- `use codex_core::protocol::RateLimitSnapshot;`
- `use codex_file_search::FileMatch;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::openai_models::ModelPreset;`
- `use crate::bottom_pane::ApprovalRequest;`
- `use crate::bottom_pane::StatusLineItem;`
- `use crate::history_cell::HistoryCell;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::CollaborationModeMask;`
- `use codex_protocol::config_types::Personality;`
- `use codex_protocol::openai_models::ReasoningEffort;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
