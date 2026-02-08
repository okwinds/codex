# `codex-rs/tui/src/app_event_sender.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `891`
- sha256: `5ed1c6b6cbb04e3cc207e5df0322a740a6017936cc6d9588024d9445ed76ca6c`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/app_event_sender.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/app_event_sender.rs:1` `use tokio::sync::mpsc::UnboundedSender;`
- `use` `codex-rs/tui/src/app_event_sender.rs:3` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/app_event_sender.rs:4` `use crate::session_log;`
- `impl` `codex-rs/tui/src/app_event_sender.rs:11` `impl AppEventSender {`

## Dependencies (auto sample)
### Imports / Includes
- `use tokio::sync::mpsc::UnboundedSender;`
- `use crate::app_event::AppEvent;`
- `use crate::session_log;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
