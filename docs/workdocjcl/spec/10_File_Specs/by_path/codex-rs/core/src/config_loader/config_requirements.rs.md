# `codex-rs/core/src/config_loader/config_requirements.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `28220`
- sha256: `95d5d0212c8f638f119b57622c417602cc7d08d4215e8c0f778477a7fa09bbf6`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/config_requirements.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum RequirementSource {`
- `pub struct ConfigRequirements {`
- `pub enum McpServerIdentity {`
- `pub struct McpServerRequirement {`
- `pub struct ConfigRequirementsToml {`
- `pub struct Sourced<T> {`
- `pub fn new(value: T, source: RequirementSource) -> Self {`
- `pub struct ConfigRequirementsWithSources {`
- `pub fn merge_unset_fields(&mut self, source: RequirementSource, other: ConfigRequirementsToml) {`
- `pub fn into_toml(self) -> ConfigRequirementsToml {`
- `pub enum SandboxModeRequirement {`
- `pub enum ResidencyRequirement {`
- `pub fn is_empty(&self) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:1` `use codex_protocol::config_types::SandboxMode;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:2` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:3` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:4` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:5` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:6` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:7` `use std::fmt;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:9` `use super::requirements_exec_policy::RequirementsExecPolicy;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:10` `use super::requirements_exec_policy::RequirementsExecPolicyToml;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:11` `use crate::config::Constrained;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:12` `use crate::config::ConstraintError;`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:15` `pub enum RequirementSource {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:24` `impl fmt::Display for RequirementSource {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:25` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:50` `pub struct ConfigRequirements {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:58` `impl Default for ConfigRequirements {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:59` `fn default() -> Self {`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:72` `pub enum McpServerIdentity {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:78` `pub struct McpServerRequirement {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:84` `pub struct ConfigRequirementsToml {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:95` `pub struct Sourced<T> {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:100` `impl<T> Sourced<T> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:101` `pub fn new(value: T, source: RequirementSource) -> Self {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:106` `impl<T> std::ops::Deref for Sourced<T> {`
- `type` `codex-rs/core/src/config_loader/config_requirements.rs:107` `type Target = T;`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:109` `fn deref(&self) -> &Self::Target {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:115` `pub struct ConfigRequirementsWithSources {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:123` `impl ConfigRequirementsWithSources {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:124` `pub fn merge_unset_fields(&mut self, source: RequirementSource, other: ConfigRequirementsToml) {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:158` `pub fn into_toml(self) -> ConfigRequirementsToml {`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:179` `pub enum SandboxModeRequirement {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:193` `impl From<SandboxMode> for SandboxModeRequirement {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:194` `fn from(mode: SandboxMode) -> Self {`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:205` `pub enum ResidencyRequirement {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:209` `impl ConfigRequirementsToml {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:210` `pub fn is_empty(&self) -> bool {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:219` `impl TryFrom<ConfigRequirementsWithSources> for ConfigRequirements {`
- `type` `codex-rs/core/src/config_loader/config_requirements.rs:220` `type Error = ConstraintError;`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:222` `fn try_from(toml: ConfigRequirementsWithSources) -> Result<Self, Self::Error> {`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:349` `use super::*;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:350` `use anyhow::Result;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:351` `use codex_execpolicy::Decision;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:352` `use codex_execpolicy::Evaluation;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:353` `use codex_execpolicy::RuleMatch;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:354` `use codex_protocol::protocol::NetworkAccess;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:355` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:356` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:357` `use toml::from_str;`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:359` `fn tokens(cmd: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:363` `fn with_unknown_source(toml: ConfigRequirementsToml) -> ConfigRequirementsWithSources {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:384` `fn merge_unset_fields_copies_every_field_and_sets_sources() {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:424` `fn merge_unset_fields_fills_missing_values() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:455` `fn merge_unset_fields_does_not_overwrite_existing_values() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:493` `fn constraint_error_includes_requirement_source() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:540` `fn constraint_error_includes_cloud_requirements_source() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:567` `fn deserialize_allowed_approval_policies() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:622` `fn deserialize_allowed_sandbox_modes() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:676` `fn deserialize_mcp_server_requirements() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:715` `fn deserialize_exec_policy_requirements() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:744` `fn exec_policy_error_includes_requirement_source() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::config_types::SandboxMode;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use serde::Deserialize;`
- `use std::collections::BTreeMap;`
- `use std::fmt;`
- `use super::requirements_exec_policy::RequirementsExecPolicy;`
- `use super::requirements_exec_policy::RequirementsExecPolicyToml;`
- `use crate::config::Constrained;`
- `use crate::config::ConstraintError;`
- `use super::*;`
- `use anyhow::Result;`
- `use codex_execpolicy::Decision;`
- `use codex_execpolicy::Evaluation;`
- `use codex_execpolicy::RuleMatch;`
- `use codex_protocol::protocol::NetworkAccess;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use pretty_assertions::assert_eq;`
- `use toml::from_str;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
