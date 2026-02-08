# `codex-rs/execpolicy-legacy/src/valid_exec.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2625`
- sha256: `be4fe17f96c2582090e88d6586e3ad52e188eb6988892c7f40fdb81eb5448a44`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/valid_exec.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct ValidExec {`
- `pub fn new(program: &str, args: Vec<MatchedArg>, system_path: &[&str]) -> Self {`
- `pub fn might_write_files(&self) -> bool {`
- `pub struct MatchedArg {`
- `pub fn new(index: usize, r#type: ArgType, value: &str) -> Result<Self> {`
- `pub struct MatchedOpt {`
- `pub fn new(name: &str, value: &str, r#type: ArgType) -> Result<Self> {`
- `pub fn name(&self) -> &str {`
- `pub struct MatchedFlag {`
- `pub fn new(name: &str) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/valid_exec.rs:1` `use crate::arg_type::ArgType;`
- `use` `codex-rs/execpolicy-legacy/src/valid_exec.rs:2` `use crate::error::Result;`
- `use` `codex-rs/execpolicy-legacy/src/valid_exec.rs:3` `use serde::Serialize;`
- `struct` `codex-rs/execpolicy-legacy/src/valid_exec.rs:7` `pub struct ValidExec {`
- `impl` `codex-rs/execpolicy-legacy/src/valid_exec.rs:20` `impl ValidExec {`
- `fn` `codex-rs/execpolicy-legacy/src/valid_exec.rs:21` `pub fn new(program: &str, args: Vec<MatchedArg>, system_path: &[&str]) -> Self {`
- `fn` `codex-rs/execpolicy-legacy/src/valid_exec.rs:33` `pub fn might_write_files(&self) -> bool {`
- `struct` `codex-rs/execpolicy-legacy/src/valid_exec.rs:40` `pub struct MatchedArg {`
- `impl` `codex-rs/execpolicy-legacy/src/valid_exec.rs:46` `impl MatchedArg {`
- `fn` `codex-rs/execpolicy-legacy/src/valid_exec.rs:47` `pub fn new(index: usize, r#type: ArgType, value: &str) -> Result<Self> {`
- `struct` `codex-rs/execpolicy-legacy/src/valid_exec.rs:59` `pub struct MatchedOpt {`
- `impl` `codex-rs/execpolicy-legacy/src/valid_exec.rs:68` `impl MatchedOpt {`
- `fn` `codex-rs/execpolicy-legacy/src/valid_exec.rs:69` `pub fn new(name: &str, value: &str, r#type: ArgType) -> Result<Self> {`
- `fn` `codex-rs/execpolicy-legacy/src/valid_exec.rs:78` `pub fn name(&self) -> &str {`
- `struct` `codex-rs/execpolicy-legacy/src/valid_exec.rs:84` `pub struct MatchedFlag {`
- `impl` `codex-rs/execpolicy-legacy/src/valid_exec.rs:89` `impl MatchedFlag {`
- `fn` `codex-rs/execpolicy-legacy/src/valid_exec.rs:90` `pub fn new(name: &str) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::arg_type::ArgType;`
- `use crate::error::Result;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
