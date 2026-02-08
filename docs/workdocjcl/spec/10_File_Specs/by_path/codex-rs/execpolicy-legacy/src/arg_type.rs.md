# `codex-rs/execpolicy-legacy/src/arg_type.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2863`
- sha256: `5b513db22a55bb8a0dd3042319074aa1f197643b0a8ae955561f646f06ae6f3a`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/arg_type.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ArgType {`
- `pub fn validate(&self, value: &str) -> Result<()> {`
- `pub fn might_write_file(&self) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:3` `use crate::error::Error;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:4` `use crate::error::Result;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:5` `use crate::sed_command::parse_sed_command;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:6` `use allocative::Allocative;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:7` `use derive_more::derive::Display;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:8` `use serde::Serialize;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:9` `use starlark::any::ProvidesStaticType;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:10` `use starlark::values::StarlarkValue;`
- `use` `codex-rs/execpolicy-legacy/src/arg_type.rs:11` `use starlark::values::starlark_value;`
- `enum` `codex-rs/execpolicy-legacy/src/arg_type.rs:15` `pub enum ArgType {`
- `impl` `codex-rs/execpolicy-legacy/src/arg_type.rs:31` `impl ArgType {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_type.rs:32` `pub fn validate(&self, value: &str) -> Result<()> {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_type.rs:72` `pub fn might_write_file(&self) -> bool {`
- `impl` `codex-rs/execpolicy-legacy/src/arg_type.rs:85` `impl<'v> StarlarkValue<'v> for ArgType {`
- `type` `codex-rs/execpolicy-legacy/src/arg_type.rs:86` `type Canonical = ArgType;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::Error;`
- `use crate::error::Result;`
- `use crate::sed_command::parse_sed_command;`
- `use allocative::Allocative;`
- `use derive_more::derive::Display;`
- `use serde::Serialize;`
- `use starlark::any::ProvidesStaticType;`
- `use starlark::values::StarlarkValue;`
- `use starlark::values::starlark_value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
