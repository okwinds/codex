# `codex-rs/execpolicy-legacy/src/program.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8021`
- sha256: `dcee6735e11085fa2ed4092b157604cbaa435e38b7353e3bc997b4ca5104d598`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/program.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ProgramSpec {`
- `pub fn new(`
- `pub enum MatchedExec {`
- `pub enum Forbidden {`
- `pub fn check(&self, exec_call: &ExecCall) -> Result<MatchedExec> {`
- `pub fn verify_should_match_list(&self) -> Vec<PositiveExampleFailedCheck> {`
- `pub fn verify_should_not_match_list(&self) -> Vec<NegativeExamplePassedCheck> {`
- `pub struct PositiveExampleFailedCheck {`
- `pub struct NegativeExamplePassedCheck {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/program.rs:1` `use serde::Serialize;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:2` `use std::collections::HashMap;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:3` `use std::collections::HashSet;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:5` `use crate::ArgType;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:6` `use crate::ExecCall;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:7` `use crate::arg_matcher::ArgMatcher;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:8` `use crate::arg_resolver::PositionalArg;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:9` `use crate::arg_resolver::resolve_observed_args_with_patterns;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:10` `use crate::error::Error;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:11` `use crate::error::Result;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:12` `use crate::opt::Opt;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:13` `use crate::opt::OptMeta;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:14` `use crate::valid_exec::MatchedFlag;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:15` `use crate::valid_exec::MatchedOpt;`
- `use` `codex-rs/execpolicy-legacy/src/program.rs:16` `use crate::valid_exec::ValidExec;`
- `struct` `codex-rs/execpolicy-legacy/src/program.rs:19` `pub struct ProgramSpec {`
- `impl` `codex-rs/execpolicy-legacy/src/program.rs:32` `impl ProgramSpec {`
- `fn` `codex-rs/execpolicy-legacy/src/program.rs:33` `pub fn new(`
- `enum` `codex-rs/execpolicy-legacy/src/program.rs:70` `pub enum MatchedExec {`
- `enum` `codex-rs/execpolicy-legacy/src/program.rs:76` `pub enum Forbidden {`
- `impl` `codex-rs/execpolicy-legacy/src/program.rs:90` `impl ProgramSpec {`
- `fn` `codex-rs/execpolicy-legacy/src/program.rs:94` `pub fn check(&self, exec_call: &ExecCall) -> Result<MatchedExec> {`
- `fn` `codex-rs/execpolicy-legacy/src/program.rs:197` `pub fn verify_should_match_list(&self) -> Vec<PositiveExampleFailedCheck> {`
- `fn` `codex-rs/execpolicy-legacy/src/program.rs:218` `pub fn verify_should_not_match_list(&self) -> Vec<NegativeExamplePassedCheck> {`
- `struct` `codex-rs/execpolicy-legacy/src/program.rs:237` `pub struct PositiveExampleFailedCheck {`
- `struct` `codex-rs/execpolicy-legacy/src/program.rs:244` `pub struct NegativeExamplePassedCheck {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Serialize;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use crate::ArgType;`
- `use crate::ExecCall;`
- `use crate::arg_matcher::ArgMatcher;`
- `use crate::arg_resolver::PositionalArg;`
- `use crate::arg_resolver::resolve_observed_args_with_patterns;`
- `use crate::error::Error;`
- `use crate::error::Result;`
- `use crate::opt::Opt;`
- `use crate::opt::OptMeta;`
- `use crate::valid_exec::MatchedFlag;`
- `use crate::valid_exec::MatchedOpt;`
- `use crate::valid_exec::ValidExec;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
