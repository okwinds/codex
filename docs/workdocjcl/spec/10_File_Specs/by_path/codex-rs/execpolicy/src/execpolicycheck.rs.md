# `codex-rs/execpolicy/src/execpolicycheck.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2479`
- sha256: `bc60e70d19f747600cced785d542c0510e5f836082b30cc22d61dcbdd4a40b36`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/execpolicycheck.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct ExecPolicyCheckCommand {`
- `pub fn run(&self) -> Result<()> {`
- `pub fn format_matches_json(matched_rules: &[RuleMatch], pretty: bool) -> Result<String> {`
- `pub fn load_policies(policy_paths: &[PathBuf]) -> Result<Policy> {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:1` `use std::fs;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:4` `use anyhow::Context;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:5` `use anyhow::Result;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:6` `use clap::Parser;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:7` `use serde::Serialize;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:9` `use crate::Decision;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:10` `use crate::Policy;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:11` `use crate::PolicyParser;`
- `use` `codex-rs/execpolicy/src/execpolicycheck.rs:12` `use crate::RuleMatch;`
- `struct` `codex-rs/execpolicy/src/execpolicycheck.rs:16` `pub struct ExecPolicyCheckCommand {`
- `impl` `codex-rs/execpolicy/src/execpolicycheck.rs:35` `impl ExecPolicyCheckCommand {`
- `fn` `codex-rs/execpolicy/src/execpolicycheck.rs:37` `pub fn run(&self) -> Result<()> {`
- `fn` `codex-rs/execpolicy/src/execpolicycheck.rs:48` `pub fn format_matches_json(matched_rules: &[RuleMatch], pretty: bool) -> Result<String> {`
- `fn` `codex-rs/execpolicy/src/execpolicycheck.rs:61` `pub fn load_policies(policy_paths: &[PathBuf]) -> Result<Policy> {`
- `struct` `codex-rs/execpolicy/src/execpolicycheck.rs:78` `struct ExecPolicyCheckOutput<'a> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs;`
- `use std::path::PathBuf;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use clap::Parser;`
- `use serde::Serialize;`
- `use crate::Decision;`
- `use crate::Policy;`
- `use crate::PolicyParser;`
- `use crate::RuleMatch;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
