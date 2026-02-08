# `codex-rs/utils/pty/src/win/conpty.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4328`
- sha256: `1ecad7df63d20b2943481d622852eac868c085f9ac3b84dc7f6abe36e0665b26`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/win/conpty.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ConPtySystem {}`
- `pub fn resize(`
- `pub struct ConPtyMasterPty {`
- `pub struct ConPtySlavePty {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/win/conpty.rs:21` `use crate::win::psuedocon::PsuedoCon;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:22` `use anyhow::Error;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:23` `use filedescriptor::FileDescriptor;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:24` `use filedescriptor::Pipe;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:25` `use portable_pty::cmdbuilder::CommandBuilder;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:26` `use portable_pty::Child;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:27` `use portable_pty::MasterPty;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:28` `use portable_pty::PtyPair;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:29` `use portable_pty::PtySize;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:30` `use portable_pty::PtySystem;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:31` `use portable_pty::SlavePty;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:32` `use std::sync::Arc;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:33` `use std::sync::Mutex;`
- `use` `codex-rs/utils/pty/src/win/conpty.rs:34` `use winapi::um::wincon::COORD;`
- `struct` `codex-rs/utils/pty/src/win/conpty.rs:37` `pub struct ConPtySystem {}`
- `impl` `codex-rs/utils/pty/src/win/conpty.rs:39` `impl PtySystem for ConPtySystem {`
- `fn` `codex-rs/utils/pty/src/win/conpty.rs:40` `fn openpty(&self, size: PtySize) -> anyhow::Result<PtyPair> {`
- `struct` `codex-rs/utils/pty/src/win/conpty.rs:73` `struct Inner {`
- `impl` `codex-rs/utils/pty/src/win/conpty.rs:80` `impl Inner {`
- `fn` `codex-rs/utils/pty/src/win/conpty.rs:81` `pub fn resize(`
- `struct` `codex-rs/utils/pty/src/win/conpty.rs:103` `pub struct ConPtyMasterPty {`
- `struct` `codex-rs/utils/pty/src/win/conpty.rs:107` `pub struct ConPtySlavePty {`
- `impl` `codex-rs/utils/pty/src/win/conpty.rs:111` `impl MasterPty for ConPtyMasterPty {`
- `fn` `codex-rs/utils/pty/src/win/conpty.rs:112` `fn resize(&self, size: PtySize) -> anyhow::Result<()> {`
- `fn` `codex-rs/utils/pty/src/win/conpty.rs:117` `fn get_size(&self) -> Result<PtySize, Error> {`
- `fn` `codex-rs/utils/pty/src/win/conpty.rs:122` `fn try_clone_reader(&self) -> anyhow::Result<Box<dyn std::io::Read + Send>> {`
- `fn` `codex-rs/utils/pty/src/win/conpty.rs:126` `fn take_writer(&self) -> anyhow::Result<Box<dyn std::io::Write + Send>> {`
- `impl` `codex-rs/utils/pty/src/win/conpty.rs:138` `impl SlavePty for ConPtySlavePty {`
- `fn` `codex-rs/utils/pty/src/win/conpty.rs:139` `fn spawn_command(&self, cmd: CommandBuilder) -> anyhow::Result<Box<dyn Child + Send + Sync>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::win::psuedocon::PsuedoCon;`
- `use anyhow::Error;`
- `use filedescriptor::FileDescriptor;`
- `use filedescriptor::Pipe;`
- `use portable_pty::cmdbuilder::CommandBuilder;`
- `use portable_pty::Child;`
- `use portable_pty::MasterPty;`
- `use portable_pty::PtyPair;`
- `use portable_pty::PtySize;`
- `use portable_pty::PtySystem;`
- `use portable_pty::SlavePty;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use winapi::um::wincon::COORD;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
