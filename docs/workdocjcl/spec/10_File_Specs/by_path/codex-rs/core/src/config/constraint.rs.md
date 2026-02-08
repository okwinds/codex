# `codex-rs/core/src/config/constraint.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7036`
- sha256: `10e4d620d75a68df23db7c168c7e66c356ed698486b78c2b436760bc39c5b6bf`
- generated_utc: `2026-02-08T10:45:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config/constraint.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ConstraintError {`
- `pub fn empty_field(field_name: impl Into<String>) -> Self {`
- `pub struct Constrained<T> {`
- `pub fn new(`
- `pub fn normalized(`
- `pub fn allow_any(initial_value: T) -> Self {`
- `pub fn allow_any_from_default() -> Self`
- `pub fn get(&self) -> &T {`
- `pub fn value(&self) -> T`
- `pub fn can_set(&self, candidate: &T) -> ConstraintResult<()> {`
- `pub fn set(&mut self, value: T) -> ConstraintResult<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config/constraint.rs:1` `use std::fmt;`
- `use` `codex-rs/core/src/config/constraint.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/config/constraint.rs:4` `use crate::config_loader::RequirementSource;`
- `use` `codex-rs/core/src/config/constraint.rs:5` `use thiserror::Error;`
- `enum` `codex-rs/core/src/config/constraint.rs:8` `pub enum ConstraintError {`
- `impl` `codex-rs/core/src/config/constraint.rs:29` `impl ConstraintError {`
- `fn` `codex-rs/core/src/config/constraint.rs:30` `pub fn empty_field(field_name: impl Into<String>) -> Self {`
- `type` `codex-rs/core/src/config/constraint.rs:37` `pub type ConstraintResult<T> = Result<T, ConstraintError>;`
- `impl` `codex-rs/core/src/config/constraint.rs:39` `impl From<ConstraintError> for std::io::Error {`
- `fn` `codex-rs/core/src/config/constraint.rs:40` `fn from(err: ConstraintError) -> Self {`
- `type` `codex-rs/core/src/config/constraint.rs:45` `type ConstraintValidator<T> = dyn Fn(&T) -> ConstraintResult<()> + Send + Sync;`
- `type` `codex-rs/core/src/config/constraint.rs:48` `type ConstraintNormalizer<T> = dyn Fn(T) -> T + Send + Sync;`
- `struct` `codex-rs/core/src/config/constraint.rs:51` `pub struct Constrained<T> {`
- `impl` `codex-rs/core/src/config/constraint.rs:57` `impl<T: Send + Sync> Constrained<T> {`
- `fn` `codex-rs/core/src/config/constraint.rs:58` `pub fn new(`
- `fn` `codex-rs/core/src/config/constraint.rs:72` `pub fn normalized(`
- `fn` `codex-rs/core/src/config/constraint.rs:87` `pub fn allow_any(initial_value: T) -> Self {`
- `fn` `codex-rs/core/src/config/constraint.rs:96` `pub fn allow_any_from_default() -> Self`
- `fn` `codex-rs/core/src/config/constraint.rs:103` `pub fn get(&self) -> &T {`
- `fn` `codex-rs/core/src/config/constraint.rs:107` `pub fn value(&self) -> T`
- `fn` `codex-rs/core/src/config/constraint.rs:114` `pub fn can_set(&self, candidate: &T) -> ConstraintResult<()> {`
- `fn` `codex-rs/core/src/config/constraint.rs:118` `pub fn set(&mut self, value: T) -> ConstraintResult<()> {`
- `impl` `codex-rs/core/src/config/constraint.rs:130` `impl<T> std::ops::Deref for Constrained<T> {`
- `type` `codex-rs/core/src/config/constraint.rs:131` `type Target = T;`
- `fn` `codex-rs/core/src/config/constraint.rs:133` `fn deref(&self) -> &Self::Target {`
- `impl` `codex-rs/core/src/config/constraint.rs:138` `impl<T: fmt::Debug> fmt::Debug for Constrained<T> {`
- `fn` `codex-rs/core/src/config/constraint.rs:139` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `impl` `codex-rs/core/src/config/constraint.rs:146` `impl<T: PartialEq> PartialEq for Constrained<T> {`
- `fn` `codex-rs/core/src/config/constraint.rs:147` `fn eq(&self, other: &Self) -> bool {`
- `use` `codex-rs/core/src/config/constraint.rs:154` `use super::*;`
- `use` `codex-rs/core/src/config/constraint.rs:155` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/config/constraint.rs:157` `fn invalid_value(candidate: impl Into<String>, allowed: impl Into<String>) -> ConstraintError {`
- `fn` `codex-rs/core/src/config/constraint.rs:167` `fn constrained_allow_any_accepts_any_value() {`
- `fn` `codex-rs/core/src/config/constraint.rs:174` `fn constrained_allow_any_default_uses_default_value() {`
- `fn` `codex-rs/core/src/config/constraint.rs:180` `fn constrained_normalizer_applies_on_init_and_set() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config/constraint.rs:191` `fn constrained_new_rejects_invalid_initial_value() {`
- `fn` `codex-rs/core/src/config/constraint.rs:204` `fn constrained_set_rejects_invalid_value_and_leaves_previous() {`
- `fn` `codex-rs/core/src/config/constraint.rs:222` `fn constrained_can_set_allows_probe_without_setting() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt;`
- `use std::sync::Arc;`
- `use crate::config_loader::RequirementSource;`
- `use thiserror::Error;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
