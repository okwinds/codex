# `codex-rs/execpolicy-legacy/src/policy_parser.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7628`
- sha256: `3bbff34e5fbd284a8c58bd021d9755d5fdc4c2353de5b3444c1424122756e098`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/policy_parser.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PolicyParser {`
- `pub fn new(policy_source: &str, unparsed_policy: &str) -> Self {`
- `pub fn parse(&self) -> starlark::Result<Policy> {`
- `pub struct ForbiddenProgramRegex {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:3` `use crate::Opt;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:4` `use crate::Policy;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:5` `use crate::ProgramSpec;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:6` `use crate::arg_matcher::ArgMatcher;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:7` `use crate::opt::OptMeta;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:8` `use log::info;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:9` `use multimap::MultiMap;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:10` `use regex_lite::Regex;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:11` `use starlark::any::ProvidesStaticType;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:12` `use starlark::environment::GlobalsBuilder;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:13` `use starlark::environment::LibraryExtension;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:14` `use starlark::environment::Module;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:15` `use starlark::eval::Evaluator;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:16` `use starlark::syntax::AstModule;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:17` `use starlark::syntax::Dialect;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:18` `use starlark::values::Heap;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:19` `use starlark::values::list::UnpackList;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:20` `use starlark::values::none::NoneType;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:21` `use std::cell::RefCell;`
- `use` `codex-rs/execpolicy-legacy/src/policy_parser.rs:22` `use std::collections::HashMap;`
- `struct` `codex-rs/execpolicy-legacy/src/policy_parser.rs:24` `pub struct PolicyParser {`
- `impl` `codex-rs/execpolicy-legacy/src/policy_parser.rs:29` `impl PolicyParser {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:30` `pub fn new(policy_source: &str, unparsed_policy: &str) -> Self {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:37` `pub fn parse(&self) -> starlark::Result<Policy> {`
- `struct` `codex-rs/execpolicy-legacy/src/policy_parser.rs:75` `pub struct ForbiddenProgramRegex {`
- `struct` `codex-rs/execpolicy-legacy/src/policy_parser.rs:81` `struct PolicyBuilder {`
- `impl` `codex-rs/execpolicy-legacy/src/policy_parser.rs:87` `impl PolicyBuilder {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:88` `fn new() -> Self {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:96` `fn build(self) -> Result<Policy, regex_lite::Error> {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:103` `fn add_program_spec(&self, program_spec: ProgramSpec) {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:110` `fn add_forbidden_substrings(&self, substrings: &[String]) {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:115` `fn add_forbidden_program_regex(&self, regex: Regex, reason: String) {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:122` `fn policy_builtins(builder: &mut GlobalsBuilder) {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:183` `fn forbid_substrings(`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:198` `fn forbid_program_regex(`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:215` `fn opt(name: String, r#type: ArgMatcher, required: Option<bool>) -> anyhow::Result<Opt> {`
- `fn` `codex-rs/execpolicy-legacy/src/policy_parser.rs:223` `fn flag(name: String) -> anyhow::Result<Opt> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::Opt;`
- `use crate::Policy;`
- `use crate::ProgramSpec;`
- `use crate::arg_matcher::ArgMatcher;`
- `use crate::opt::OptMeta;`
- `use log::info;`
- `use multimap::MultiMap;`
- `use regex_lite::Regex;`
- `use starlark::any::ProvidesStaticType;`
- `use starlark::environment::GlobalsBuilder;`
- `use starlark::environment::LibraryExtension;`
- `use starlark::environment::Module;`
- `use starlark::eval::Evaluator;`
- `use starlark::syntax::AstModule;`
- `use starlark::syntax::Dialect;`
- `use starlark::values::Heap;`
- `use starlark::values::list::UnpackList;`
- `use starlark::values::none::NoneType;`
- `use std::cell::RefCell;`
- `use std::collections::HashMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
