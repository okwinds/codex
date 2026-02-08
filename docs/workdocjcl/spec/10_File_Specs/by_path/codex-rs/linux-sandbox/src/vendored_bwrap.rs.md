# `codex-rs/linux-sandbox/src/vendored_bwrap.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2886`
- sha256: `01927cdbe4aa8ed8f5f7b5fdb0ee21ab91ac2ef15de48d59c41fba9df566b3f8`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/src/vendored_bwrap.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/linux-sandbox/src/vendored_bwrap.rs:9` `use std::ffi::CString;`
- `use` `codex-rs/linux-sandbox/src/vendored_bwrap.rs:10` `use std::os::raw::c_char;`
- `fn` `codex-rs/linux-sandbox/src/vendored_bwrap.rs:13` `fn bwrap_main(argc: libc::c_int, argv: *const *const c_char) -> libc::c_int;`
- `fn` `codex-rs/linux-sandbox/src/vendored_bwrap.rs:16` `fn argv_to_cstrings(argv: &[String]) -> Vec<CString> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::CString;`
- `use std::os::raw::c_char;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
