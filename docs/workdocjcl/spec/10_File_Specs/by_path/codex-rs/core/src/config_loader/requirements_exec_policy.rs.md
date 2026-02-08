# `codex-rs/core/src/config_loader/requirements_exec_policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8177`
- sha256: `dade0fed186ea70edc5c074dba08aaa437be5c03268f72ae3a69cfb72d22e55d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/requirements_exec_policy.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn new(policy: Policy) -> Self {`
- `pub struct RequirementsExecPolicyToml {`
- `pub struct RequirementsExecPolicyPrefixRuleToml {`
- `pub struct RequirementsExecPolicyPatternTokenToml {`
- `pub enum RequirementsExecPolicyDecisionToml {`
- `pub enum RequirementsExecPolicyParseError {`
- `pub fn to_policy(&self) -> Result<Policy, RequirementsExecPolicyParseError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:1` `use codex_execpolicy::Decision;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:2` `use codex_execpolicy::Policy;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:3` `use codex_execpolicy::rule::PatternToken;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:4` `use codex_execpolicy::rule::PrefixPattern;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:5` `use codex_execpolicy::rule::PrefixRule;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:6` `use codex_execpolicy::rule::RuleRef;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:7` `use multimap::MultiMap;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:8` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:9` `use std::sync::Arc;`
- `use` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:10` `use thiserror::Error;`
- `impl` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:17` `impl RequirementsExecPolicy {`
- `fn` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:18` `pub fn new(policy: Policy) -> Self {`
- `impl` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:23` `impl PartialEq for RequirementsExecPolicy {`
- `fn` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:24` `fn eq(&self, other: &Self) -> bool {`
- `impl` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:31` `impl AsRef<Policy> for RequirementsExecPolicy {`
- `fn` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:32` `fn as_ref(&self) -> &Policy {`
- `fn` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:37` `fn policy_fingerprint(policy: &Policy) -> Vec<String> {`
- `struct` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:50` `pub struct RequirementsExecPolicyToml {`
- `struct` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:58` `pub struct RequirementsExecPolicyPrefixRuleToml {`
- `struct` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:70` `pub struct RequirementsExecPolicyPatternTokenToml {`
- `enum` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:77` `pub enum RequirementsExecPolicyDecisionToml {`
- `impl` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:83` `impl RequirementsExecPolicyDecisionToml {`
- `fn` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:84` `fn as_decision(self) -> Decision {`
- `enum` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:94` `pub enum RequirementsExecPolicyParseError {`
- `impl` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:122` `impl RequirementsExecPolicyToml {`
- `fn` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:125` `pub fn to_policy(&self) -> Result<Policy, RequirementsExecPolicyParseError> {`
- `fn` `codex-rs/core/src/config_loader/requirements_exec_policy.rs:192` `fn parse_pattern_token(`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_execpolicy::Decision;`
- `use codex_execpolicy::Policy;`
- `use codex_execpolicy::rule::PatternToken;`
- `use codex_execpolicy::rule::PrefixPattern;`
- `use codex_execpolicy::rule::PrefixRule;`
- `use codex_execpolicy::rule::RuleRef;`
- `use multimap::MultiMap;`
- `use serde::Deserialize;`
- `use std::sync::Arc;`
- `use thiserror::Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
