# `codex-rs/execpolicy-legacy/src/arg_matcher.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3721`
- sha256: `1a53447f7c585c2ef52cc6eb83b866d1658516b93200f693cdad028d52add9a3`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/arg_matcher.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ArgMatcher {`
- `pub fn cardinality(&self) -> ArgMatcherCardinality {`
- `pub fn arg_type(&self) -> ArgType {`
- `pub enum ArgMatcherCardinality {`
- `pub fn is_exact(&self) -> Option<usize> {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:3` `use crate::arg_type::ArgType;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:4` `use crate::starlark::values::ValueLike;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:5` `use allocative::Allocative;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:6` `use derive_more::derive::Display;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:7` `use starlark::any::ProvidesStaticType;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:8` `use starlark::values::AllocValue;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:9` `use starlark::values::Heap;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:10` `use starlark::values::NoSerialize;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:11` `use starlark::values::StarlarkValue;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:12` `use starlark::values::UnpackValue;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:13` `use starlark::values::Value;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:14` `use starlark::values::starlark_value;`
- `use` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:15` `use starlark::values::string::StarlarkStr;`
- `enum` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:20` `pub enum ArgMatcher {`
- `impl` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:50` `impl ArgMatcher {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:51` `pub fn cardinality(&self) -> ArgMatcherCardinality {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:66` `pub fn arg_type(&self) -> ArgType {`
- `enum` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:81` `pub enum ArgMatcherCardinality {`
- `impl` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:87` `impl ArgMatcherCardinality {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:88` `pub fn is_exact(&self) -> Option<usize> {`
- `impl` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:97` `impl<'v> AllocValue<'v> for ArgMatcher {`
- `fn` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:98` `fn alloc_value(self, heap: &'v Heap) -> Value<'v> {`
- `impl` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:104` `impl<'v> StarlarkValue<'v> for ArgMatcher {`
- `type` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:105` `type Canonical = ArgMatcher;`
- `impl` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:108` `impl<'v> UnpackValue<'v> for ArgMatcher {`
- `type` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:109` `type Error = starlark::Error;`
- `fn` `codex-rs/execpolicy-legacy/src/arg_matcher.rs:111` `fn unpack_value_impl(value: Value<'v>) -> starlark::Result<Option<Self>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::arg_type::ArgType;`
- `use crate::starlark::values::ValueLike;`
- `use allocative::Allocative;`
- `use derive_more::derive::Display;`
- `use starlark::any::ProvidesStaticType;`
- `use starlark::values::AllocValue;`
- `use starlark::values::Heap;`
- `use starlark::values::NoSerialize;`
- `use starlark::values::StarlarkValue;`
- `use starlark::values::UnpackValue;`
- `use starlark::values::Value;`
- `use starlark::values::starlark_value;`
- `use starlark::values::string::StarlarkStr;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
