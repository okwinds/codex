# `codex-rs/tui/src/slash_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5410`
- sha256: `778d17b731af942ff63f6562c5b136bedd4c2dbf7ea44ac4f380683336df2190`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `impl` `codex-rs/tui/src/slash_command.rs:48` `impl SlashCommand {`
- `fn` `codex-rs/tui/src/slash_command.rs:50` `pub fn description(self) -> &'static str {`
- `fn` `codex-rs/tui/src/slash_command.rs:86` `pub fn command(self) -> &'static str {`
- `fn` `codex-rs/tui/src/slash_command.rs:91` `pub fn supports_inline_args(self) -> bool {`
- `fn` `codex-rs/tui/src/slash_command.rs:99` `pub fn available_during_task(self) -> bool {`
- `fn` `codex-rs/tui/src/slash_command.rs:134` `fn is_visible(self) -> bool {`
- `fn` `codex-rs/tui/src/slash_command.rs:143` `pub fn built_in_slash_commands() -> Vec<(&'static str, SlashCommand)> {`

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
- `workdocjcl/spec/06_UI/TUI.md`
