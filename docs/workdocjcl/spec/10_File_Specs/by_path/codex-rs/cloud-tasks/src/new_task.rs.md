# `codex-rs/cloud-tasks/src/new_task.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `808`
- sha256: `1d373bc40210879b81dce60292a4bc553d5461ddb42a2d8c4f41cb6aab43073b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/new_task.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct NewTaskPage {`
- `pub fn new(env_id: Option<String>, best_of_n: usize) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks/src/new_task.rs:1` `use codex_tui::ComposerInput;`
- `struct` `codex-rs/cloud-tasks/src/new_task.rs:3` `pub struct NewTaskPage {`
- `impl` `codex-rs/cloud-tasks/src/new_task.rs:10` `impl NewTaskPage {`
- `fn` `codex-rs/cloud-tasks/src/new_task.rs:11` `pub fn new(env_id: Option<String>, best_of_n: usize) -> Self {`
- `impl` `codex-rs/cloud-tasks/src/new_task.rs:31` `impl Default for NewTaskPage {`
- `fn` `codex-rs/cloud-tasks/src/new_task.rs:32` `fn default() -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_tui::ComposerInput;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
