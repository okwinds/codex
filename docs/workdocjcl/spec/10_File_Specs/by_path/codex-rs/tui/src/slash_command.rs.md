# `codex-rs/tui/src/slash_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5722`
- sha256: `12f155e2b8e7b4259b4773937183d004fe201934960c3bb200694b83964cc271`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/slash_command.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum SlashCommand {`
- `pub fn description(self) -> &'static str {`
- `pub fn command(self) -> &'static str {`
- `pub fn supports_inline_args(self) -> bool {`
- `pub fn available_during_task(self) -> bool {`
- `pub fn built_in_slash_commands() -> Vec<(&'static str, SlashCommand)> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/slash_command.rs:1` `use strum::IntoEnumIterator;`
- `use` `codex-rs/tui/src/slash_command.rs:2` `use strum_macros::AsRefStr;`
- `use` `codex-rs/tui/src/slash_command.rs:3` `use strum_macros::EnumIter;`
- `use` `codex-rs/tui/src/slash_command.rs:4` `use strum_macros::EnumString;`
- `use` `codex-rs/tui/src/slash_command.rs:5` `use strum_macros::IntoStaticStr;`
- `enum` `codex-rs/tui/src/slash_command.rs:12` `pub enum SlashCommand {`
- `impl` `codex-rs/tui/src/slash_command.rs:50` `impl SlashCommand {`
- `fn` `codex-rs/tui/src/slash_command.rs:52` `pub fn description(self) -> &'static str {`
- `fn` `codex-rs/tui/src/slash_command.rs:90` `pub fn command(self) -> &'static str {`
- `fn` `codex-rs/tui/src/slash_command.rs:95` `pub fn supports_inline_args(self) -> bool {`
- `fn` `codex-rs/tui/src/slash_command.rs:103` `pub fn available_during_task(self) -> bool {`
- `fn` `codex-rs/tui/src/slash_command.rs:140` `fn is_visible(self) -> bool {`
- `fn` `codex-rs/tui/src/slash_command.rs:149` `pub fn built_in_slash_commands() -> Vec<(&'static str, SlashCommand)> {`

## Dependencies (auto sample)
### Imports / Includes
- `use strum::IntoEnumIterator;`
- `use strum_macros::AsRefStr;`
- `use strum_macros::EnumIter;`
- `use strum_macros::EnumString;`
- `use strum_macros::IntoStaticStr;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
