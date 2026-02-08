# `codex-rs/tui/src/app_event.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10913`
- sha256: `5f40db7d343730265a8747eb92fb2cf9cd3965bb984f55ff29e088c353133e24`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `use` `codex-rs/tui/src/app_event.rs:22` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/app_event.rs:24` `use codex_core::features::Feature;`
- `use` `codex-rs/tui/src/app_event.rs:25` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/tui/src/app_event.rs:26` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/tui/src/app_event.rs:27` `use codex_protocol::config_types::CollaborationModeMask;`
- `use` `codex-rs/tui/src/app_event.rs:28` `use codex_protocol::config_types::Personality;`
- `use` `codex-rs/tui/src/app_event.rs:29` `use codex_protocol::openai_models::ReasoningEffort;`

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
- `workdocjcl/spec/06_UI/TUI.md`
