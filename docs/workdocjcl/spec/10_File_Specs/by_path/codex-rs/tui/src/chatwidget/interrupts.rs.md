# `codex-rs/tui/src/chatwidget/interrupts.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3674`
- sha256: `adee0ba769b368245401c25784e1f27c2c4a8e24be1622c8ca41f9eabebc3799`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/chatwidget/interrupts.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:1` `use std::collections::VecDeque;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:3` `use codex_core::protocol::ApplyPatchApprovalRequestEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:4` `use codex_core::protocol::ExecApprovalRequestEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:5` `use codex_core::protocol::ExecCommandBeginEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:6` `use codex_core::protocol::ExecCommandEndEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:7` `use codex_core::protocol::McpToolCallBeginEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:8` `use codex_core::protocol::McpToolCallEndEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:9` `use codex_core::protocol::PatchApplyEndEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:10` `use codex_protocol::approvals::ElicitationRequestEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:11` `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use` `codex-rs/tui/src/chatwidget/interrupts.rs:13` `use super::ChatWidget;`
- `impl` `codex-rs/tui/src/chatwidget/interrupts.rs:33` `impl InterruptManager {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::VecDeque;`
- `use codex_core::protocol::ApplyPatchApprovalRequestEvent;`
- `use codex_core::protocol::ExecApprovalRequestEvent;`
- `use codex_core::protocol::ExecCommandBeginEvent;`
- `use codex_core::protocol::ExecCommandEndEvent;`
- `use codex_core::protocol::McpToolCallBeginEvent;`
- `use codex_core::protocol::McpToolCallEndEvent;`
- `use codex_core::protocol::PatchApplyEndEvent;`
- `use codex_protocol::approvals::ElicitationRequestEvent;`
- `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use super::ChatWidget;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
