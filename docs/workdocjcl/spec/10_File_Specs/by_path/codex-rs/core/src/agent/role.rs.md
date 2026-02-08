# `codex-rs/core/src/agent/role.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4921`
- sha256: `c1353252a8bd0c1755e4edfa136e1f976c990db8c2c906f664c9d9edbbaa3d87`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/agent/role.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum AgentRole {`
- `pub struct AgentProfile {`
- `pub fn enum_values() -> Vec<String> {`
- `pub fn profile(self) -> AgentProfile {`
- `pub fn apply_to_config(self, config: &mut Config) -> Result<(), String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/agent/role.rs:1` `use crate::config::Config;`
- `use` `codex-rs/core/src/agent/role.rs:2` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/agent/role.rs:3` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/agent/role.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/core/src/agent/role.rs:5` `use serde::Serialize;`
- `const` `codex-rs/core/src/agent/role.rs:8` `const ORCHESTRATOR_PROMPT: &str = include_str!("../../templates/agents/orchestrator.md");`
- `const` `codex-rs/core/src/agent/role.rs:11` `const EXPLORER_MODEL: &str = "gpt-5.2-codex";`
- `const` `codex-rs/core/src/agent/role.rs:14` `const ALL_ROLES: [AgentRole; 3] = [`
- `enum` `codex-rs/core/src/agent/role.rs:25` `pub enum AgentRole {`
- `struct` `codex-rs/core/src/agent/role.rs:38` `pub struct AgentProfile {`
- `impl` `codex-rs/core/src/agent/role.rs:51` `impl AgentRole {`
- `fn` `codex-rs/core/src/agent/role.rs:53` `pub fn enum_values() -> Vec<String> {`
- `fn` `codex-rs/core/src/agent/role.rs:73` `pub fn profile(self) -> AgentProfile {`
- `fn` `codex-rs/core/src/agent/role.rs:112` `pub fn apply_to_config(self, config: &mut Config) -> Result<(), String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::Config;`
- `use crate::protocol::SandboxPolicy;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
