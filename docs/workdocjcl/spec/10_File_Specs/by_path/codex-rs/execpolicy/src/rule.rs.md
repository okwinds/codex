# `codex-rs/execpolicy/src/rule.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4796`
- sha256: `9c5d3a763b82033f6f3a6eb884a61c6c13d883e4ad1ae30a63a86935fb84a662`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/rule.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum PatternToken {`
- `pub fn alternatives(&self) -> &[String] {`
- `pub struct PrefixPattern {`
- `pub fn matches_prefix(&self, cmd: &[String]) -> Option<Vec<String>> {`
- `pub enum RuleMatch {`
- `pub fn decision(&self) -> Decision {`
- `pub struct PrefixRule {`
- `pub trait Rule: Any + Debug + Send + Sync {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/rule.rs:1` `use crate::decision::Decision;`
- `use` `codex-rs/execpolicy/src/rule.rs:2` `use crate::error::Error;`
- `use` `codex-rs/execpolicy/src/rule.rs:3` `use crate::error::Result;`
- `use` `codex-rs/execpolicy/src/rule.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/execpolicy/src/rule.rs:5` `use serde::Serialize;`
- `use` `codex-rs/execpolicy/src/rule.rs:6` `use shlex::try_join;`
- `use` `codex-rs/execpolicy/src/rule.rs:7` `use std::any::Any;`
- `use` `codex-rs/execpolicy/src/rule.rs:8` `use std::fmt::Debug;`
- `use` `codex-rs/execpolicy/src/rule.rs:9` `use std::sync::Arc;`
- `enum` `codex-rs/execpolicy/src/rule.rs:13` `pub enum PatternToken {`
- `impl` `codex-rs/execpolicy/src/rule.rs:18` `impl PatternToken {`
- `fn` `codex-rs/execpolicy/src/rule.rs:19` `fn matches(&self, token: &str) -> bool {`
- `fn` `codex-rs/execpolicy/src/rule.rs:26` `pub fn alternatives(&self) -> &[String] {`
- `struct` `codex-rs/execpolicy/src/rule.rs:37` `pub struct PrefixPattern {`
- `impl` `codex-rs/execpolicy/src/rule.rs:42` `impl PrefixPattern {`
- `fn` `codex-rs/execpolicy/src/rule.rs:43` `pub fn matches_prefix(&self, cmd: &[String]) -> Option<Vec<String>> {`
- `enum` `codex-rs/execpolicy/src/rule.rs:61` `pub enum RuleMatch {`
- `impl` `codex-rs/execpolicy/src/rule.rs:79` `impl RuleMatch {`
- `fn` `codex-rs/execpolicy/src/rule.rs:80` `pub fn decision(&self) -> Decision {`
- `struct` `codex-rs/execpolicy/src/rule.rs:89` `pub struct PrefixRule {`
- `trait` `codex-rs/execpolicy/src/rule.rs:95` `pub trait Rule: Any + Debug + Send + Sync {`
- `fn` `codex-rs/execpolicy/src/rule.rs:96` `fn program(&self) -> &str;`
- `fn` `codex-rs/execpolicy/src/rule.rs:98` `fn matches(&self, cmd: &[String]) -> Option<RuleMatch>;`
- `fn` `codex-rs/execpolicy/src/rule.rs:100` `fn as_any(&self) -> &dyn Any;`
- `type` `codex-rs/execpolicy/src/rule.rs:103` `pub type RuleRef = Arc<dyn Rule>;`
- `impl` `codex-rs/execpolicy/src/rule.rs:105` `impl Rule for PrefixRule {`
- `fn` `codex-rs/execpolicy/src/rule.rs:106` `fn program(&self) -> &str {`
- `fn` `codex-rs/execpolicy/src/rule.rs:110` `fn matches(&self, cmd: &[String]) -> Option<RuleMatch> {`
- `fn` `codex-rs/execpolicy/src/rule.rs:120` `fn as_any(&self) -> &dyn Any {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::decision::Decision;`
- `use crate::error::Error;`
- `use crate::error::Result;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use shlex::try_join;`
- `use std::any::Any;`
- `use std::fmt::Debug;`
- `use std::sync::Arc;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
