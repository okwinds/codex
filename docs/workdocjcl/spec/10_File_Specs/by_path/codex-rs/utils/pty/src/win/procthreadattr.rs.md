# `codex-rs/utils/pty/src/win/procthreadattr.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3218`
- sha256: `ada85c9dc97627af2b05992833a0047e238206b65bc48309bca7d36e11d848e5`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/win/procthreadattr.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ProcThreadAttributeList {`
- `pub fn with_capacity(num_attributes: DWORD) -> Result<Self, Error> {`
- `pub fn as_mut_ptr(&mut self) -> LPPROC_THREAD_ATTRIBUTE_LIST {`
- `pub fn set_pty(&mut self, con: HPCON) -> Result<(), Error> {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:21` `use super::psuedocon::HPCON;`
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:22` `use anyhow::ensure;`
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:23` `use anyhow::Error;`
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:24` `use std::io::Error as IoError;`
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:25` `use std::mem;`
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:26` `use std::ptr;`
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:27` `use winapi::shared::minwindef::DWORD;`
- `use` `codex-rs/utils/pty/src/win/procthreadattr.rs:28` `use winapi::um::processthreadsapi::*;`
- `const` `codex-rs/utils/pty/src/win/procthreadattr.rs:30` `const PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE: usize = 0x00020016;`
- `struct` `codex-rs/utils/pty/src/win/procthreadattr.rs:32` `pub struct ProcThreadAttributeList {`
- `impl` `codex-rs/utils/pty/src/win/procthreadattr.rs:36` `impl ProcThreadAttributeList {`
- `fn` `codex-rs/utils/pty/src/win/procthreadattr.rs:37` `pub fn with_capacity(num_attributes: DWORD) -> Result<Self, Error> {`
- `fn` `codex-rs/utils/pty/src/win/procthreadattr.rs:62` `pub fn as_mut_ptr(&mut self) -> LPPROC_THREAD_ATTRIBUTE_LIST {`
- `fn` `codex-rs/utils/pty/src/win/procthreadattr.rs:66` `pub fn set_pty(&mut self, con: HPCON) -> Result<(), Error> {`
- `impl` `codex-rs/utils/pty/src/win/procthreadattr.rs:87` `impl Drop for ProcThreadAttributeList {`
- `fn` `codex-rs/utils/pty/src/win/procthreadattr.rs:88` `fn drop(&mut self) {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::psuedocon::HPCON;`
- `use anyhow::ensure;`
- `use anyhow::Error;`
- `use std::io::Error as IoError;`
- `use std::mem;`
- `use std::ptr;`
- `use winapi::shared::minwindef::DWORD;`
- `use winapi::um::processthreadsapi::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
