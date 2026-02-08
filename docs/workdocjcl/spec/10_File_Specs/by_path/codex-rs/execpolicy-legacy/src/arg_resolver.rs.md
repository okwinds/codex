# `codex-rs/execpolicy-legacy/src/arg_resolver.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7087`
- sha256: `13d7cc58bd0e4537f8cad8120f44b5fa0106da2aa46e23ce9d62825ad3661b4c`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/arg_resolver.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PositionalArg {`
- `pub fn resolve_observed_args_with_patterns(`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:1` `use serde::Serialize;`
- `use` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:3` `use crate::arg_matcher::ArgMatcher;`
- `use` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:4` `use crate::arg_matcher::ArgMatcherCardinality;`
- `use` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:5` `use crate::error::Error;`
- `use` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:6` `use crate::error::Result;`
- `use` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:7` `use crate::valid_exec::MatchedArg;`
- `struct` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:10` `pub struct PositionalArg {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:15` `pub fn resolve_observed_args_with_patterns(`
- `struct` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:148` `struct ParitionedArgs {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_resolver.rs:156` `fn partition_args(program: &str, arg_patterns: &Vec<ArgMatcher>) -> Result<ParitionedArgs> {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Serialize;`
- `use crate::arg_matcher::ArgMatcher;`
- `use crate::arg_matcher::ArgMatcherCardinality;`
- `use crate::error::Error;`
- `use crate::error::Result;`
- `use crate::valid_exec::MatchedArg;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
