# `codex-rs/execpolicy/src/policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5521`
- sha256: `71e4d9b003cb9d64da810f6e825fcf87530104772969b591a5c46bee191f4885`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/policy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Policy {`
- `pub fn new(rules_by_program: MultiMap<String, RuleRef>) -> Self {`
- `pub fn empty() -> Self {`
- `pub fn rules(&self) -> &MultiMap<String, RuleRef> {`
- `pub fn get_allowed_prefixes(&self) -> Vec<Vec<String>> {`
- `pub fn add_prefix_rule(&mut self, prefix: &[String], decision: Decision) -> Result<()> {`
- `pub fn matches_for_command(`
- `pub struct Evaluation {`
- `pub fn is_match(&self) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/policy.rs:1` `use crate::decision::Decision;`
- `use` `codex-rs/execpolicy/src/policy.rs:2` `use crate::error::Error;`
- `use` `codex-rs/execpolicy/src/policy.rs:3` `use crate::error::Result;`
- `use` `codex-rs/execpolicy/src/policy.rs:4` `use crate::rule::PatternToken;`
- `use` `codex-rs/execpolicy/src/policy.rs:5` `use crate::rule::PrefixPattern;`
- `use` `codex-rs/execpolicy/src/policy.rs:6` `use crate::rule::PrefixRule;`
- `use` `codex-rs/execpolicy/src/policy.rs:7` `use crate::rule::RuleMatch;`
- `use` `codex-rs/execpolicy/src/policy.rs:8` `use crate::rule::RuleRef;`
- `use` `codex-rs/execpolicy/src/policy.rs:9` `use multimap::MultiMap;`
- `use` `codex-rs/execpolicy/src/policy.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/execpolicy/src/policy.rs:11` `use serde::Serialize;`
- `use` `codex-rs/execpolicy/src/policy.rs:12` `use std::sync::Arc;`
- `type` `codex-rs/execpolicy/src/policy.rs:14` `type HeuristicsFallback<'a> = Option<&'a dyn Fn(&[String]) -> Decision>;`
- `struct` `codex-rs/execpolicy/src/policy.rs:17` `pub struct Policy {`
- `impl` `codex-rs/execpolicy/src/policy.rs:21` `impl Policy {`
- `fn` `codex-rs/execpolicy/src/policy.rs:22` `pub fn new(rules_by_program: MultiMap<String, RuleRef>) -> Self {`
- `fn` `codex-rs/execpolicy/src/policy.rs:26` `pub fn empty() -> Self {`
- `fn` `codex-rs/execpolicy/src/policy.rs:30` `pub fn rules(&self) -> &MultiMap<String, RuleRef> {`
- `fn` `codex-rs/execpolicy/src/policy.rs:34` `pub fn get_allowed_prefixes(&self) -> Vec<Vec<String>> {`
- `fn` `codex-rs/execpolicy/src/policy.rs:58` `pub fn add_prefix_rule(&mut self, prefix: &[String], decision: Decision) -> Result<()> {`
- `fn` `codex-rs/execpolicy/src/policy.rs:116` `pub fn matches_for_command(`
- `fn` `codex-rs/execpolicy/src/policy.rs:143` `fn render_pattern_token(token: &PatternToken) -> String {`
- `struct` `codex-rs/execpolicy/src/policy.rs:152` `pub struct Evaluation {`
- `impl` `codex-rs/execpolicy/src/policy.rs:158` `impl Evaluation {`
- `fn` `codex-rs/execpolicy/src/policy.rs:159` `pub fn is_match(&self) -> bool {`
- `fn` `codex-rs/execpolicy/src/policy.rs:166` `fn from_matches(matched_rules: Vec<RuleMatch>) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::decision::Decision;`
- `use crate::error::Error;`
- `use crate::error::Result;`
- `use crate::rule::PatternToken;`
- `use crate::rule::PrefixPattern;`
- `use crate::rule::PrefixRule;`
- `use crate::rule::RuleMatch;`
- `use crate::rule::RuleRef;`
- `use multimap::MultiMap;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::sync::Arc;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
