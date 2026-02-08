# `codex-rs/utils/pty/src/win/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5531`
- sha256: `7e68b9290d3e33c5c9daea973f80c6a6528ece627c6192de1d3bba45bbd97585`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/win/mod.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct WinChild {`
- `pub struct WinChildKiller {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/win/mod.rs:21` `use anyhow::Context as _;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:22` `use filedescriptor::OwnedHandle;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:23` `use portable_pty::Child;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:24` `use portable_pty::ChildKiller;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:25` `use portable_pty::ExitStatus;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:26` `use std::io::Error as IoError;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:27` `use std::io::Result as IoResult;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:28` `use std::os::windows::io::AsRawHandle;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:29` `use std::pin::Pin;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:30` `use std::sync::Mutex;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:31` `use std::task::Context;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:32` `use std::task::Poll;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:33` `use winapi::shared::minwindef::DWORD;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:34` `use winapi::um::minwinbase::STILL_ACTIVE;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:35` `use winapi::um::processthreadsapi::*;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:36` `use winapi::um::synchapi::WaitForSingleObject;`
- `use` `codex-rs/utils/pty/src/win/mod.rs:37` `use winapi::um::winbase::INFINITE;`
- `mod` `codex-rs/utils/pty/src/win/mod.rs:39` `pub mod conpty;`
- `mod` `codex-rs/utils/pty/src/win/mod.rs:40` `mod procthreadattr;`
- `mod` `codex-rs/utils/pty/src/win/mod.rs:41` `mod psuedocon;`
- `struct` `codex-rs/utils/pty/src/win/mod.rs:47` `pub struct WinChild {`
- `impl` `codex-rs/utils/pty/src/win/mod.rs:51` `impl WinChild {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:52` `fn is_complete(&mut self) -> IoResult<Option<ExitStatus>> {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:67` `fn do_kill(&mut self) -> IoResult<()> {`
- `impl` `codex-rs/utils/pty/src/win/mod.rs:79` `impl ChildKiller for WinChild {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:80` `fn kill(&mut self) -> IoResult<()> {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:85` `fn clone_killer(&self) -> Box<dyn ChildKiller + Send + Sync> {`
- `struct` `codex-rs/utils/pty/src/win/mod.rs:92` `pub struct WinChildKiller {`
- `impl` `codex-rs/utils/pty/src/win/mod.rs:96` `impl ChildKiller for WinChildKiller {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:97` `fn kill(&mut self) -> IoResult<()> {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:107` `fn clone_killer(&self) -> Box<dyn ChildKiller + Send + Sync> {`
- `impl` `codex-rs/utils/pty/src/win/mod.rs:113` `impl Child for WinChild {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:114` `fn try_wait(&mut self) -> IoResult<Option<ExitStatus>> {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:118` `fn wait(&mut self) -> IoResult<ExitStatus> {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:135` `fn process_id(&self) -> Option<u32> {`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:144` `fn as_raw_handle(&self) -> Option<std::os::windows::io::RawHandle> {`
- `impl` `codex-rs/utils/pty/src/win/mod.rs:150` `impl std::future::Future for WinChild {`
- `type` `codex-rs/utils/pty/src/win/mod.rs:151` `type Output = anyhow::Result<ExitStatus>;`
- `fn` `codex-rs/utils/pty/src/win/mod.rs:153` `fn poll(mut self: Pin<&mut Self>, cx: &mut Context) -> Poll<anyhow::Result<ExitStatus>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context as _;`
- `use filedescriptor::OwnedHandle;`
- `use portable_pty::Child;`
- `use portable_pty::ChildKiller;`
- `use portable_pty::ExitStatus;`
- `use std::io::Error as IoError;`
- `use std::io::Result as IoResult;`
- `use std::os::windows::io::AsRawHandle;`
- `use std::pin::Pin;`
- `use std::sync::Mutex;`
- `use std::task::Context;`
- `use std::task::Poll;`
- `use winapi::shared::minwindef::DWORD;`
- `use winapi::um::minwinbase::STILL_ACTIVE;`
- `use winapi::um::processthreadsapi::*;`
- `use winapi::um::synchapi::WaitForSingleObject;`
- `use winapi::um::winbase::INFINITE;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
