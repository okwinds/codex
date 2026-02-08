# `codex-rs/utils/git/src/errors.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1133`
- sha256: `8358361d24a2aea8dc73188ae1b8de3258f549c1f2db028e08b7f6f374c0ec99`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/git/src/errors.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum GitToolingError {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/git/src/errors.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/utils/git/src/errors.rs:2` `use std::process::ExitStatus;`
- `use` `codex-rs/utils/git/src/errors.rs:3` `use std::string::FromUtf8Error;`
- `use` `codex-rs/utils/git/src/errors.rs:5` `use thiserror::Error;`
- `use` `codex-rs/utils/git/src/errors.rs:6` `use walkdir::Error as WalkdirError;`
- `enum` `codex-rs/utils/git/src/errors.rs:10` `pub enum GitToolingError {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::process::ExitStatus;`
- `use std::string::FromUtf8Error;`
- `use thiserror::Error;`
- `use walkdir::Error as WalkdirError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
