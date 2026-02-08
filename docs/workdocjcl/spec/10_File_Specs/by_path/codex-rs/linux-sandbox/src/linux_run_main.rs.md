# `codex-rs/linux-sandbox/src/linux_run_main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1740`
- sha256: `12efb5f2841007ae7071735b9ab6d0d767826a5b6a7933b0d62c1740cacbbd9b`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/src/linux_run_main.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct LandlockCommand {`
- `pub fn run_main() -> ! {`

## Definitions (auto, per-file)
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:1` `use clap::Parser;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:2` `use std::ffi::CString;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:5` `use crate::landlock::apply_sandbox_policy_to_current_thread;`
- `struct` `codex-rs/linux-sandbox/src/linux_run_main.rs:8` `pub struct LandlockCommand {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:22` `pub fn run_main() -> ! {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Parser;`
- `use std::ffi::CString;`
- `use std::path::PathBuf;`
- `use crate::landlock::apply_sandbox_policy_to_current_thread;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
