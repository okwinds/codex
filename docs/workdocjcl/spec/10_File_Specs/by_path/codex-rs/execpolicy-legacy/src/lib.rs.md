# `codex-rs/execpolicy-legacy/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1130`
- sha256: `4167142c26b093b183306a45d7f8f689c9553be78d919c103e0e40da547ee960`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn get_default_policy() -> starlark::Result<Policy> {`

## Definitions (auto, per-file)
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:6` `mod arg_matcher;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:7` `mod arg_resolver;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:8` `mod arg_type;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:9` `mod error;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:10` `mod exec_call;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:11` `mod execv_checker;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:12` `mod opt;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:13` `mod policy;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:14` `mod policy_parser;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:15` `mod program;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:16` `mod sed_command;`
- `mod` `codex-rs/execpolicy-legacy/src/lib.rs:17` `mod valid_exec;`
- `const` `codex-rs/execpolicy-legacy/src/lib.rs:40` `const DEFAULT_POLICY: &str = include_str!("default.policy");`
- `fn` `codex-rs/execpolicy-legacy/src/lib.rs:42` `pub fn get_default_policy() -> starlark::Result<Policy> {`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
