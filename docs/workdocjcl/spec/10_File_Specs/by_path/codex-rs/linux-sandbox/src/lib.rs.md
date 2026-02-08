# `codex-rs/linux-sandbox/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `341`
- sha256: `ada8eee3fec6d86228c80486d75c9d888fdc917466142c9d17e4958330386c19`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn run_main() -> ! {`
- `pub fn run_main() -> ! {`

## Definitions (auto, per-file)
- `mod` `codex-rs/linux-sandbox/src/lib.rs:2` `mod landlock;`
- `mod` `codex-rs/linux-sandbox/src/lib.rs:4` `mod linux_run_main;`
- `mod` `codex-rs/linux-sandbox/src/lib.rs:6` `mod mounts;`
- `fn` `codex-rs/linux-sandbox/src/lib.rs:9` `pub fn run_main() -> ! {`
- `fn` `codex-rs/linux-sandbox/src/lib.rs:14` `pub fn run_main() -> ! {`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
