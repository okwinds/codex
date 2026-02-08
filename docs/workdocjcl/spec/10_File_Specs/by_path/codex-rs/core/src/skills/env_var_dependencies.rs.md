# `codex-rs/core/src/skills/env_var_dependencies.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4867`
- sha256: `86accbe9461daa9d71ac5acd948bf4487370aa41af3b4b351f11f3184452658d`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/env_var_dependencies.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:3` `use std::env;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:6` `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:7` `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:8` `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:9` `use tracing::warn;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:11` `use crate::codex::Session;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:12` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/skills/env_var_dependencies.rs:13` `use crate::skills::SkillMetadata;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::env;`
- `use std::sync::Arc;`
- `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use tracing::warn;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::skills::SkillMetadata;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
