# `codex-rs/tui/src/update_action.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3250`
- sha256: `b2df56c498ac4c36ead14bb4203a3e43d0defee5e83fad8b25aac71f2f2affd8`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/update_action.rs` (read)
- env: `CODEX_MANAGED_BY_BUN`, `CODEX_MANAGED_BY_NPM`

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum UpdateAction {`
- `pub fn command_args(self) -> (&'static str, &'static [&'static str]) {`
- `pub fn command_str(self) -> String {`

## Definitions (auto, per-file)
- `enum` `codex-rs/tui/src/update_action.rs:3` `pub enum UpdateAction {`
- `impl` `codex-rs/tui/src/update_action.rs:12` `impl UpdateAction {`
- `fn` `codex-rs/tui/src/update_action.rs:14` `pub fn command_args(self) -> (&'static str, &'static [&'static str]) {`
- `fn` `codex-rs/tui/src/update_action.rs:23` `pub fn command_str(self) -> String {`
- `fn` `codex-rs/tui/src/update_action.rs:45` `fn detect_update_action(`
- `use` `codex-rs/tui/src/update_action.rs:66` `use super::*;`
- `fn` `codex-rs/tui/src/update_action.rs:69` `fn detects_update_action_without_env_mutation() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::*;`
### Referenced env vars
- `CODEX_MANAGED_BY_BUN`
- `CODEX_MANAGED_BY_NPM`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
