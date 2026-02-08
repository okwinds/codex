# `codex-rs/windows-sandbox-rs/src/cap.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1941`
- sha256: `cea741b40cf7a450fa11d62db63e9d89891c8ea7c803ff6769f504d83cdf768f`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/cap.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct CapSids {`
- `pub fn cap_sid_file(codex_home: &Path) -> PathBuf {`
- `pub fn load_or_create_cap_sids(codex_home: &Path) -> Result<CapSids> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:1` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:2` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:3` `use rand::rngs::SmallRng;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:4` `use rand::RngCore;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:5` `use rand::SeedableRng;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:6` `use serde::Deserialize;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:7` `use serde::Serialize;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:8` `use std::fs;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:9` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:10` `use std::path::PathBuf;`
- `struct` `codex-rs/windows-sandbox-rs/src/cap.rs:13` `pub struct CapSids {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:18` `pub fn cap_sid_file(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:22` `fn make_random_cap_sid_string() -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:31` `fn persist_caps(path: &Path, caps: &CapSids) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:41` `pub fn load_or_create_cap_sids(codex_home: &Path) -> Result<CapSids> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use rand::rngs::SmallRng;`
- `use rand::RngCore;`
- `use rand::SeedableRng;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::fs;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
