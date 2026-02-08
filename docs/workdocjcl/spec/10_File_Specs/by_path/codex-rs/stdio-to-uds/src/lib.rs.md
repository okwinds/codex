# `codex-rs/stdio-to-uds/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1444`
- sha256: `7ff5926854ce4731a921a4ee3a225fd8be4922bae2bef6904c524532413c2715`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/stdio-to-uds/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn run(socket_path: &Path) -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/stdio-to-uds/src/lib.rs:3` `use std::io;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:4` `use std::io::Write;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:5` `use std::net::Shutdown;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:6` `use std::path::Path;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:7` `use std::thread;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:9` `use anyhow::Context;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:10` `use anyhow::anyhow;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:13` `use std::os::unix::net::UnixStream;`
- `use` `codex-rs/stdio-to-uds/src/lib.rs:16` `use uds_windows::UnixStream;`
- `fn` `codex-rs/stdio-to-uds/src/lib.rs:20` `pub fn run(socket_path: &Path) -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::io::Write;`
- `use std::net::Shutdown;`
- `use std::path::Path;`
- `use std::thread;`
- `use anyhow::Context;`
- `use anyhow::anyhow;`
- `use std::os::unix::net::UnixStream;`
- `use uds_windows::UnixStream;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
