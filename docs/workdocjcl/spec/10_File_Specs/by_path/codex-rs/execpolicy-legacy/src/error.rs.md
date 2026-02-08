# `codex-rs/execpolicy-legacy/src/error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2128`
- sha256: `efe9722a28290818f60f38f8f0110af4abce86d78c7fe27ead422cdb2515d230`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/error.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum Error {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/error.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/execpolicy-legacy/src/error.rs:3` `use serde::Serialize;`
- `use` `codex-rs/execpolicy-legacy/src/error.rs:5` `use crate::arg_matcher::ArgMatcher;`
- `use` `codex-rs/execpolicy-legacy/src/error.rs:6` `use crate::arg_resolver::PositionalArg;`
- `use` `codex-rs/execpolicy-legacy/src/error.rs:7` `use serde_with::DisplayFromStr;`
- `use` `codex-rs/execpolicy-legacy/src/error.rs:8` `use serde_with::serde_as;`
- `type` `codex-rs/execpolicy-legacy/src/error.rs:10` `pub type Result<T> = std::result::Result<T, Error>;`
- `enum` `codex-rs/execpolicy-legacy/src/error.rs:15` `pub enum Error {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use serde::Serialize;`
- `use crate::arg_matcher::ArgMatcher;`
- `use crate::arg_resolver::PositionalArg;`
- `use serde_with::DisplayFromStr;`
- `use serde_with::serde_as;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
