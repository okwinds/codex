# `codex-rs/exec/src/event_processor.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1283`
- sha256: `f47fe650ef1976128965a3ef7f6127494ffa79a135ff64372f774793b4b58867`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/src/event_processor.rs` (read)

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec/src/event_processor.rs:1` `use std::path::Path;`
- `use` `codex-rs/exec/src/event_processor.rs:3` `use codex_core::config::Config;`
- `use` `codex-rs/exec/src/event_processor.rs:4` `use codex_core::protocol::Event;`
- `use` `codex-rs/exec/src/event_processor.rs:5` `use codex_core::protocol::SessionConfiguredEvent;`
- `fn` `codex-rs/exec/src/event_processor.rs:15` `fn print_config_summary(`
- `fn` `codex-rs/exec/src/event_processor.rs:23` `fn process_event(&mut self, event: Event) -> CodexStatus;`
- `fn` `codex-rs/exec/src/event_processor.rs:25` `fn print_final_output(&mut self) {}`
- `fn` `codex-rs/exec/src/event_processor.rs:39` `fn write_last_message_file(contents: &str, last_message_path: Option<&Path>) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use codex_core::config::Config;`
- `use codex_core::protocol::Event;`
- `use codex_core::protocol::SessionConfiguredEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
