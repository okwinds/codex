# `codex-rs/execpolicy-legacy/src/policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3426`
- sha256: `01423fc1a0ba01c619880e185e7489aa9c03c02c35c158a6211d158352afa188`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/policy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Policy {`
- `pub fn new(`
- `pub fn check(&self, exec_call: &ExecCall) -> Result<MatchedExec> {`
- `pub fn check_each_good_list_individually(&self) -> Vec<PositiveExampleFailedCheck> {`
- `pub fn check_each_bad_list_individually(&self) -> Vec<NegativeExamplePassedCheck> {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:1` `use multimap::MultiMap;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:2` `use regex_lite::Error as RegexError;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:3` `use regex_lite::Regex;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:5` `use crate::ExecCall;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:6` `use crate::Forbidden;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:7` `use crate::MatchedExec;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:8` `use crate::NegativeExamplePassedCheck;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:9` `use crate::ProgramSpec;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:10` `use crate::error::Error;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:11` `use crate::error::Result;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:12` `use crate::policy_parser::ForbiddenProgramRegex;`
- `use` `codex-rs/execpolicy-legacy/src/policy.rs:13` `use crate::program::PositiveExampleFailedCheck;`
- `struct` `codex-rs/execpolicy-legacy/src/policy.rs:15` `pub struct Policy {`
- `impl` `codex-rs/execpolicy-legacy/src/policy.rs:21` `impl Policy {`
- `fn` `codex-rs/execpolicy-legacy/src/policy.rs:22` `pub fn new(`
- `fn` `codex-rs/execpolicy-legacy/src/policy.rs:44` `pub fn check(&self, exec_call: &ExecCall) -> Result<MatchedExec> {`
- `fn` `codex-rs/execpolicy-legacy/src/policy.rs:88` `pub fn check_each_good_list_individually(&self) -> Vec<PositiveExampleFailedCheck> {`
- `fn` `codex-rs/execpolicy-legacy/src/policy.rs:96` `pub fn check_each_bad_list_individually(&self) -> Vec<NegativeExamplePassedCheck> {`

## Dependencies (auto sample)
### Imports / Includes
- `use multimap::MultiMap;`
- `use regex_lite::Error as RegexError;`
- `use regex_lite::Regex;`
- `use crate::ExecCall;`
- `use crate::Forbidden;`
- `use crate::MatchedExec;`
- `use crate::NegativeExamplePassedCheck;`
- `use crate::ProgramSpec;`
- `use crate::error::Error;`
- `use crate::error::Result;`
- `use crate::policy_parser::ForbiddenProgramRegex;`
- `use crate::program::PositiveExampleFailedCheck;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
