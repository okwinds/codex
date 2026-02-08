# `codex-rs/core/src/config_loader/config_requirements.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `43229`
- sha256: `84510e18dd66ef6a79f71c2d8becf5349a2413f5543e21bb734133346e0230a1`
- generated_utc: `2026-02-08T10:45:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/config_requirements.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum RequirementSource {`
- `pub struct ConstrainedWithSource<T> {`
- `pub fn new(value: Constrained<T>, source: Option<RequirementSource>) -> Self {`
- `pub struct ConfigRequirements {`
- `pub fn exec_policy_source(&self) -> Option<&RequirementSource> {`
- `pub enum McpServerIdentity {`
- `pub struct McpServerRequirement {`
- `pub struct NetworkRequirementsToml {`
- `pub struct NetworkConstraints {`
- `pub enum WebSearchModeRequirement {`
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
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:2` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:3` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:4` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:5` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:6` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:7` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:8` `use std::fmt;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:10` `use super::requirements_exec_policy::RequirementsExecPolicy;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:11` `use super::requirements_exec_policy::RequirementsExecPolicyToml;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:12` `use crate::config::Constrained;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:13` `use crate::config::ConstraintError;`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:16` `pub enum RequirementSource {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:25` `impl fmt::Display for RequirementSource {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:26` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:49` `pub struct ConstrainedWithSource<T> {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:54` `impl<T> ConstrainedWithSource<T> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:55` `pub fn new(value: Constrained<T>, source: Option<RequirementSource>) -> Self {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:60` `impl<T> std::ops::Deref for ConstrainedWithSource<T> {`
- `type` `codex-rs/core/src/config_loader/config_requirements.rs:61` `type Target = Constrained<T>;`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:63` `fn deref(&self) -> &Self::Target {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:68` `impl<T> std::ops::DerefMut for ConstrainedWithSource<T> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:69` `fn deref_mut(&mut self) -> &mut Self::Target {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:77` `pub struct ConfigRequirements {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:88` `impl Default for ConfigRequirements {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:89` `fn default() -> Self {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:111` `impl ConfigRequirements {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:112` `pub fn exec_policy_source(&self) -> Option<&RequirementSource> {`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:119` `pub enum McpServerIdentity {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:125` `pub struct McpServerRequirement {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:130` `pub struct NetworkRequirementsToml {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:145` `pub struct NetworkConstraints {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:158` `impl From<NetworkRequirementsToml> for NetworkConstraints {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:159` `fn from(value: NetworkRequirementsToml) -> Self {`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:189` `pub enum WebSearchModeRequirement {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:195` `impl From<WebSearchMode> for WebSearchModeRequirement {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:196` `fn from(mode: WebSearchMode) -> Self {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:205` `impl From<WebSearchModeRequirement> for WebSearchMode {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:206` `fn from(mode: WebSearchModeRequirement) -> Self {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:215` `impl fmt::Display for WebSearchModeRequirement {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:216` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:227` `pub struct ConfigRequirementsToml {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:241` `pub struct Sourced<T> {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:246` `impl<T> Sourced<T> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:247` `pub fn new(value: T, source: RequirementSource) -> Self {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:252` `impl<T> std::ops::Deref for Sourced<T> {`
- `type` `codex-rs/core/src/config_loader/config_requirements.rs:253` `type Target = T;`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:255` `fn deref(&self) -> &Self::Target {`
- `struct` `codex-rs/core/src/config_loader/config_requirements.rs:261` `pub struct ConfigRequirementsWithSources {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:271` `impl ConfigRequirementsWithSources {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:272` `pub fn merge_unset_fields(&mut self, source: RequirementSource, other: ConfigRequirementsToml) {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:308` `pub fn into_toml(self) -> ConfigRequirementsToml {`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:333` `pub enum SandboxModeRequirement {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:347` `impl From<SandboxMode> for SandboxModeRequirement {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:348` `fn from(mode: SandboxMode) -> Self {`
- `enum` `codex-rs/core/src/config_loader/config_requirements.rs:359` `pub enum ResidencyRequirement {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:363` `impl ConfigRequirementsToml {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:364` `pub fn is_empty(&self) -> bool {`
- `impl` `codex-rs/core/src/config_loader/config_requirements.rs:375` `impl TryFrom<ConfigRequirementsWithSources> for ConfigRequirements {`
- `type` `codex-rs/core/src/config_loader/config_requirements.rs:376` `type Error = ConstraintError;`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:378` `fn try_from(toml: ConfigRequirementsWithSources) -> Result<Self, Self::Error> {`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:561` `use super::*;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:562` `use anyhow::Result;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:563` `use codex_execpolicy::Decision;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:564` `use codex_execpolicy::Evaluation;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:565` `use codex_execpolicy::RuleMatch;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:566` `use codex_protocol::protocol::NetworkAccess;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:567` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:568` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config_loader/config_requirements.rs:569` `use toml::from_str;`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:571` `fn tokens(cmd: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:575` `fn with_unknown_source(toml: ConfigRequirementsToml) -> ConfigRequirementsWithSources {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:601` `fn merge_unset_fields_copies_every_field_and_sets_sources() {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:652` `fn merge_unset_fields_fills_missing_values() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:685` `fn merge_unset_fields_does_not_overwrite_existing_values() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:725` `fn constraint_error_includes_requirement_source() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:772` `fn constraint_error_includes_cloud_requirements_source() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:799` `fn constrained_fields_store_requirement_source() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:832` `fn deserialize_allowed_approval_policies() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:887` `fn deserialize_allowed_sandbox_modes() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:941` `fn deserialize_allowed_web_search_modes() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:975` `fn allowed_web_search_modes_allows_disabled() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:1005` `fn allowed_web_search_modes_empty_restricts_to_disabled() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:1035` `fn network_requirements_are_preserved_as_constraints_with_source() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:1079` `fn deserialize_mcp_server_requirements() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:1118` `fn deserialize_exec_policy_requirements() -> Result<()> {`
- `fn` `codex-rs/core/src/config_loader/config_requirements.rs:1147` `fn exec_policy_error_includes_requirement_source() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::config_types::SandboxMode;`
- `use codex_protocol::config_types::WebSearchMode;`
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
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
