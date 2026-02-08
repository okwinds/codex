# `codex-rs/utils/pty/src/win/psuedocon.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11627`
- sha256: `614d8f9f641bed1552463d11a3742be094e4b69a7d7fef72f4bac072566713c3`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/win/psuedocon.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn CreatePseudoConsole(`
- `pub fn ResizePseudoConsole(hpc: HPCON, size: COORD) -> HRESULT,`
- `pub fn ClosePseudoConsole(hpc: HPCON),`
- `pub fn RtlGetVersion(`
- `pub fn conpty_supported() -> bool {`
- `pub struct PsuedoCon {`
- `pub fn new(size: COORD, input: FileDescriptor, output: FileDescriptor) -> Result<Self, Error> {`
- `pub fn resize(&self, size: COORD) -> Result<(), Error> {`
- `pub fn spawn_command(&self, cmd: CommandBuilder) -> anyhow::Result<WinChild> {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:22` `use super::WinChild;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:23` `use crate::win::procthreadattr::ProcThreadAttributeList;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:24` `use anyhow::bail;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:25` `use anyhow::ensure;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:26` `use anyhow::Error;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:27` `use filedescriptor::FileDescriptor;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:28` `use filedescriptor::OwnedHandle;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:29` `use lazy_static::lazy_static;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:30` `use portable_pty::cmdbuilder::CommandBuilder;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:31` `use shared_library::shared_library;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:32` `use std::env;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:33` `use std::ffi::OsStr;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:34` `use std::ffi::OsString;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:35` `use std::io::Error as IoError;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:36` `use std::mem;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:37` `use std::os::windows::ffi::OsStrExt;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:38` `use std::os::windows::ffi::OsStringExt;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:39` `use std::os::windows::io::AsRawHandle;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:40` `use std::os::windows::io::FromRawHandle;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:41` `use std::path::Path;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:42` `use std::ptr;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:43` `use std::sync::Mutex;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:44` `use winapi::shared::minwindef::DWORD;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:45` `use winapi::shared::ntdef::NTSTATUS;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:46` `use winapi::shared::ntstatus::STATUS_SUCCESS;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:47` `use winapi::shared::winerror::HRESULT;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:48` `use winapi::shared::winerror::S_OK;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:49` `use winapi::um::handleapi::*;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:50` `use winapi::um::processthreadsapi::*;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:51` `use winapi::um::winbase::CREATE_UNICODE_ENVIRONMENT;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:52` `use winapi::um::winbase::EXTENDED_STARTUPINFO_PRESENT;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:53` `use winapi::um::winbase::STARTF_USESTDHANDLES;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:54` `use winapi::um::winbase::STARTUPINFOEXW;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:55` `use winapi::um::wincon::COORD;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:56` `use winapi::um::winnt::HANDLE;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:57` `use winapi::um::winnt::OSVERSIONINFOW;`
- `type` `codex-rs/utils/pty/src/win/psuedocon.rs:59` `pub type HPCON = HANDLE;`
- `const` `codex-rs/utils/pty/src/win/psuedocon.rs:61` `pub const PSEUDOCONSOLE_RESIZE_QUIRK: DWORD = 0x2;`
- `const` `codex-rs/utils/pty/src/win/psuedocon.rs:63` `pub const PSEUDOCONSOLE_PASSTHROUGH_MODE: DWORD = 0x8;`
- `const` `codex-rs/utils/pty/src/win/psuedocon.rs:67` `const MIN_CONPTY_BUILD: u32 = 17_763;`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:70` `pub fn CreatePseudoConsole(`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:77` `pub fn ResizePseudoConsole(hpc: HPCON, size: COORD) -> HRESULT,`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:78` `pub fn ClosePseudoConsole(hpc: HPCON),`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:82` `pub fn RtlGetVersion(`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:87` `fn load_conpty() -> ConPtyFuncs {`
- `static` `codex-rs/utils/pty/src/win/psuedocon.rs:100` `static ref CONPTY: ConPtyFuncs = load_conpty();`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:103` `pub fn conpty_supported() -> bool {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:107` `fn windows_build_number() -> Option<u32> {`
- `struct` `codex-rs/utils/pty/src/win/psuedocon.rs:119` `pub struct PsuedoCon {`
- `impl` `codex-rs/utils/pty/src/win/psuedocon.rs:126` `impl Drop for PsuedoCon {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:127` `fn drop(&mut self) {`
- `impl` `codex-rs/utils/pty/src/win/psuedocon.rs:132` `impl PsuedoCon {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:133` `pub fn new(size: COORD, input: FileDescriptor, output: FileDescriptor) -> Result<Self, Error> {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:151` `pub fn resize(&self, size: COORD) -> Result<(), Error> {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:163` `pub fn spawn_command(&self, cmd: CommandBuilder) -> anyhow::Result<WinChild> {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:218` `fn resolve_current_directory(cmd: &CommandBuilder) -> Option<Vec<u16>> {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:241` `fn build_environment_block(cmd: &CommandBuilder) -> Vec<u16> {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:253` `fn build_cmdline(cmd: &CommandBuilder) -> anyhow::Result<(Vec<u16>, Vec<u16>)> {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:284` `fn search_path(cmd: &CommandBuilder, exe: &OsStr) -> OsString {`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:308` `fn append_quoted(arg: &OsStr, cmdline: &mut Vec<u16>) {`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:355` `use super::windows_build_number;`
- `use` `codex-rs/utils/pty/src/win/psuedocon.rs:356` `use super::MIN_CONPTY_BUILD;`
- `fn` `codex-rs/utils/pty/src/win/psuedocon.rs:359` `fn windows_build_number_returns_value() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::WinChild;`
- `use crate::win::procthreadattr::ProcThreadAttributeList;`
- `use anyhow::bail;`
- `use anyhow::ensure;`
- `use anyhow::Error;`
- `use filedescriptor::FileDescriptor;`
- `use filedescriptor::OwnedHandle;`
- `use lazy_static::lazy_static;`
- `use portable_pty::cmdbuilder::CommandBuilder;`
- `use shared_library::shared_library;`
- `use std::env;`
- `use std::ffi::OsStr;`
- `use std::ffi::OsString;`
- `use std::io::Error as IoError;`
- `use std::mem;`
- `use std::os::windows::ffi::OsStrExt;`
- `use std::os::windows::ffi::OsStringExt;`
- `use std::os::windows::io::AsRawHandle;`
- `use std::os::windows::io::FromRawHandle;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
