# `codex-rs/core/src/mcp/skill_dependencies.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17508`
- sha256: `fa9baeb99d66cdacfb09d7a90a16b557ee584b128ea9576def7d0bec47965fdc`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/mcp/skill_dependencies.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:4` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:5` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:6` `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:7` `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:8` `use codex_protocol::request_user_input::RequestUserInputQuestionOption;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:9` `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:10` `use codex_rmcp_client::perform_oauth_login;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:11` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:12` `use tracing::warn;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:14` `use super::auth::McpOAuthLoginSupport;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:15` `use super::auth::oauth_login_support;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:16` `use super::effective_mcp_servers;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:17` `use crate::codex::Session;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:18` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:19` `use crate::config::Config;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:20` `use crate::config::edit::ConfigEditsBuilder;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:21` `use crate::config::load_global_mcp_servers;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:22` `use crate::config::types::McpServerConfig;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:23` `use crate::config::types::McpServerTransportConfig;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:24` `use crate::default_client::is_first_party_originator;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:25` `use crate::default_client::originator;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:26` `use crate::features::Feature;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:27` `use crate::skills::SkillMetadata;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:28` `use crate::skills::model::SkillToolDependency;`
- `const` `codex-rs/core/src/mcp/skill_dependencies.rs:30` `const SKILL_MCP_DEPENDENCY_PROMPT_ID: &str = "skill_mcp_dependency_install";`
- `const` `codex-rs/core/src/mcp/skill_dependencies.rs:31` `const MCP_DEPENDENCY_OPTION_INSTALL: &str = "Install";`
- `const` `codex-rs/core/src/mcp/skill_dependencies.rs:32` `const MCP_DEPENDENCY_OPTION_SKIP: &str = "Continue anyway";`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:34` `fn is_full_access_mode(turn_context: &TurnContext) -> bool {`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:42` `fn format_missing_mcp_dependencies(missing: &HashMap<String, McpServerConfig>) -> String {`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:48` `async fn filter_prompted_mcp_dependencies(`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:64` `async fn should_install_mcp_dependencies(`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:269` `fn canonical_mcp_key(transport: &str, identifier: &str, fallback: &str) -> String {`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:278` `fn canonical_mcp_server_key(name: &str, config: &McpServerConfig) -> String {`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:289` `fn canonical_mcp_dependency_key(dependency: &SkillToolDependency) -> Result<String, String> {`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:365` `fn mcp_dependency_to_server_config(`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:419` `use super::*;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:420` `use crate::skills::model::SkillDependencies;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:421` `use codex_protocol::protocol::SkillScope;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:422` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/mcp/skill_dependencies.rs:423` `use std::path::PathBuf;`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:425` `fn skill_with_tools(tools: Vec<SkillToolDependency>) -> SkillMetadata {`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:438` `fn collect_missing_respects_canonical_installed_key() {`
- `fn` `codex-rs/core/src/mcp/skill_dependencies.rs:474` `fn collect_missing_dedupes_by_canonical_key_but_preserves_original_name() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use codex_protocol::request_user_input::RequestUserInputQuestionOption;`
- `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use codex_rmcp_client::perform_oauth_login;`
- `use tokio_util::sync::CancellationToken;`
- `use tracing::warn;`
- `use super::auth::McpOAuthLoginSupport;`
- `use super::auth::oauth_login_support;`
- `use super::effective_mcp_servers;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::config::Config;`
- `use crate::config::edit::ConfigEditsBuilder;`
- `use crate::config::load_global_mcp_servers;`
- `use crate::config::types::McpServerConfig;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
