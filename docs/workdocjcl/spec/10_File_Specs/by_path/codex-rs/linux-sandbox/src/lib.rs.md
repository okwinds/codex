# `codex-rs/linux-sandbox/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `580`
- sha256: `a19dc73ba97e38301779335c7d52c445eb12c34aff9e95de78b17f4fd0ac9842`
- generated_utc: `2026-02-08T10:45:37Z`

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
- `mod` `codex-rs/linux-sandbox/src/lib.rs:7` `mod bwrap;`
- `mod` `codex-rs/linux-sandbox/src/lib.rs:9` `mod landlock;`
- `mod` `codex-rs/linux-sandbox/src/lib.rs:11` `mod linux_run_main;`
- `mod` `codex-rs/linux-sandbox/src/lib.rs:13` `mod vendored_bwrap;`
- `fn` `codex-rs/linux-sandbox/src/lib.rs:16` `pub fn run_main() -> ! {`
- `fn` `codex-rs/linux-sandbox/src/lib.rs:21` `pub fn run_main() -> ! {`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
