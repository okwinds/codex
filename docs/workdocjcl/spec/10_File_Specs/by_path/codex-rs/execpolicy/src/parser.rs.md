# `codex-rs/execpolicy/src/parser.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8221`
- sha256: `30cbd9256479de307f105f54c1e91e8dcbb140bd918521a1e5557d32609288a7`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/parser.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PolicyParser {`
- `pub fn new() -> Self {`
- `pub fn parse(&mut self, policy_identifier: &str, policy_file_contents: &str) -> Result<()> {`
- `pub fn build(self) -> crate::policy::Policy {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/parser.rs:1` `use multimap::MultiMap;`
- `use` `codex-rs/execpolicy/src/parser.rs:2` `use shlex;`
- `use` `codex-rs/execpolicy/src/parser.rs:3` `use starlark::any::ProvidesStaticType;`
- `use` `codex-rs/execpolicy/src/parser.rs:4` `use starlark::environment::GlobalsBuilder;`
- `use` `codex-rs/execpolicy/src/parser.rs:5` `use starlark::environment::Module;`
- `use` `codex-rs/execpolicy/src/parser.rs:6` `use starlark::eval::Evaluator;`
- `use` `codex-rs/execpolicy/src/parser.rs:7` `use starlark::starlark_module;`
- `use` `codex-rs/execpolicy/src/parser.rs:8` `use starlark::syntax::AstModule;`
- `use` `codex-rs/execpolicy/src/parser.rs:9` `use starlark::syntax::Dialect;`
- `use` `codex-rs/execpolicy/src/parser.rs:10` `use starlark::values::Value;`
- `use` `codex-rs/execpolicy/src/parser.rs:11` `use starlark::values::list::ListRef;`
- `use` `codex-rs/execpolicy/src/parser.rs:12` `use starlark::values::list::UnpackList;`
- `use` `codex-rs/execpolicy/src/parser.rs:13` `use starlark::values::none::NoneType;`
- `use` `codex-rs/execpolicy/src/parser.rs:14` `use std::cell::RefCell;`
- `use` `codex-rs/execpolicy/src/parser.rs:15` `use std::cell::RefMut;`
- `use` `codex-rs/execpolicy/src/parser.rs:16` `use std::sync::Arc;`
- `use` `codex-rs/execpolicy/src/parser.rs:18` `use crate::decision::Decision;`
- `use` `codex-rs/execpolicy/src/parser.rs:19` `use crate::error::Error;`
- `use` `codex-rs/execpolicy/src/parser.rs:20` `use crate::error::Result;`
- `use` `codex-rs/execpolicy/src/parser.rs:21` `use crate::rule::PatternToken;`
- `use` `codex-rs/execpolicy/src/parser.rs:22` `use crate::rule::PrefixPattern;`
- `use` `codex-rs/execpolicy/src/parser.rs:23` `use crate::rule::PrefixRule;`
- `use` `codex-rs/execpolicy/src/parser.rs:24` `use crate::rule::RuleRef;`
- `use` `codex-rs/execpolicy/src/parser.rs:25` `use crate::rule::validate_match_examples;`
- `use` `codex-rs/execpolicy/src/parser.rs:26` `use crate::rule::validate_not_match_examples;`
- `struct` `codex-rs/execpolicy/src/parser.rs:28` `pub struct PolicyParser {`
- `impl` `codex-rs/execpolicy/src/parser.rs:32` `impl Default for PolicyParser {`
- `fn` `codex-rs/execpolicy/src/parser.rs:33` `fn default() -> Self {`
- `impl` `codex-rs/execpolicy/src/parser.rs:38` `impl PolicyParser {`
- `fn` `codex-rs/execpolicy/src/parser.rs:39` `pub fn new() -> Self {`
- `fn` `codex-rs/execpolicy/src/parser.rs:47` `pub fn parse(&mut self, policy_identifier: &str, policy_file_contents: &str) -> Result<()> {`
- `fn` `codex-rs/execpolicy/src/parser.rs:66` `pub fn build(self) -> crate::policy::Policy {`
- `struct` `codex-rs/execpolicy/src/parser.rs:72` `struct PolicyBuilder {`
- `impl` `codex-rs/execpolicy/src/parser.rs:76` `impl PolicyBuilder {`
- `fn` `codex-rs/execpolicy/src/parser.rs:77` `fn new() -> Self {`
- `fn` `codex-rs/execpolicy/src/parser.rs:83` `fn add_rule(&mut self, rule: RuleRef) {`
- `fn` `codex-rs/execpolicy/src/parser.rs:88` `fn build(self) -> crate::policy::Policy {`
- `fn` `codex-rs/execpolicy/src/parser.rs:158` `fn parse_string_example(raw: &str) -> Result<Vec<String>> {`
- `fn` `codex-rs/execpolicy/src/parser.rs:172` `fn parse_list_example(list: &ListRef) -> Result<Vec<String>> {`
- `fn` `codex-rs/execpolicy/src/parser.rs:209` `fn policy_builtins(builder: &mut GlobalsBuilder) {`

## Dependencies (auto sample)
### Imports / Includes
- `use multimap::MultiMap;`
- `use shlex;`
- `use starlark::any::ProvidesStaticType;`
- `use starlark::environment::GlobalsBuilder;`
- `use starlark::environment::Module;`
- `use starlark::eval::Evaluator;`
- `use starlark::starlark_module;`
- `use starlark::syntax::AstModule;`
- `use starlark::syntax::Dialect;`
- `use starlark::values::Value;`
- `use starlark::values::list::ListRef;`
- `use starlark::values::list::UnpackList;`
- `use starlark::values::none::NoneType;`
- `use std::cell::RefCell;`
- `use std::cell::RefMut;`
- `use std::sync::Arc;`
- `use crate::decision::Decision;`
- `use crate::error::Error;`
- `use crate::error::Result;`
- `use crate::rule::PatternToken;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
