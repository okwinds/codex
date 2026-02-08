# `codex-rs/cli/src/mcp_cmd.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `27474`
- sha256: `15db05a620bffb96095132e945c134e366428d4872dac2b33fd11e5ada857e71`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/mcp_cmd.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct McpCli {`
- `pub enum McpSubcommand {`
- `pub struct ListArgs {`
- `pub struct GetArgs {`
- `pub struct AddArgs {`
- `pub struct AddMcpTransportArgs {`
- `pub struct AddMcpStdioArgs {`
- `pub struct AddMcpStreamableHttpArgs {`
- `pub struct RemoveArgs {`
- `pub struct LoginArgs {`
- `pub struct LogoutArgs {`

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/mcp_cmd.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:3` `use anyhow::Context;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:4` `use anyhow::Result;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:5` `use anyhow::anyhow;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:6` `use anyhow::bail;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:7` `use clap::ArgGroup;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:8` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:9` `use codex_common::format_env_display::format_env_display;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:10` `use codex_core::config::Config;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:11` `use codex_core::config::edit::ConfigEditsBuilder;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:12` `use codex_core::config::find_codex_home;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:13` `use codex_core::config::load_global_mcp_servers;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:14` `use codex_core::config::types::McpServerConfig;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:15` `use codex_core::config::types::McpServerTransportConfig;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:16` `use codex_core::mcp::auth::McpOAuthLoginSupport;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:17` `use codex_core::mcp::auth::compute_auth_statuses;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:18` `use codex_core::mcp::auth::oauth_login_support;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:19` `use codex_core::protocol::McpAuthStatus;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:20` `use codex_rmcp_client::delete_oauth_tokens;`
- `use` `codex-rs/cli/src/mcp_cmd.rs:21` `use codex_rmcp_client::perform_oauth_login;`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:31` `pub struct McpCli {`
- `enum` `codex-rs/cli/src/mcp_cmd.rs:40` `pub enum McpSubcommand {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:50` `pub struct ListArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:57` `pub struct GetArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:68` `pub struct AddArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:85` `pub struct AddMcpTransportArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:94` `pub struct AddMcpStdioArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:114` `pub struct AddMcpStreamableHttpArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:130` `pub struct RemoveArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:136` `pub struct LoginArgs {`
- `struct` `codex-rs/cli/src/mcp_cmd.rs:146` `pub struct LogoutArgs {`
- `impl` `codex-rs/cli/src/mcp_cmd.rs:151` `impl McpCli {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:152` `pub async fn run(self) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:183` `async fn run_add(config_overrides: &CliConfigOverrides, add_args: AddArgs) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:289` `async fn run_remove(config_overrides: &CliConfigOverrides, remove_args: RemoveArgs) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:322` `async fn run_login(config_overrides: &CliConfigOverrides, login_args: LoginArgs) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:365` `async fn run_logout(config_overrides: &CliConfigOverrides, logout_args: LogoutArgs) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:395` `async fn run_list(config_overrides: &CliConfigOverrides, list_args: ListArgs) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:645` `async fn run_get(config_overrides: &CliConfigOverrides, get_args: GetArgs) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:804` `fn parse_env_pair(raw: &str) -> Result<(String, String), String> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:819` `fn validate_server_name(name: &str) -> Result<()> {`
- `fn` `codex-rs/cli/src/mcp_cmd.rs:832` `fn format_mcp_status(config: &McpServerConfig) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use anyhow::bail;`
- `use clap::ArgGroup;`
- `use codex_common::CliConfigOverrides;`
- `use codex_common::format_env_display::format_env_display;`
- `use codex_core::config::Config;`
- `use codex_core::config::edit::ConfigEditsBuilder;`
- `use codex_core::config::find_codex_home;`
- `use codex_core::config::load_global_mcp_servers;`
- `use codex_core::config::types::McpServerConfig;`
- `use codex_core::config::types::McpServerTransportConfig;`
- `use codex_core::mcp::auth::McpOAuthLoginSupport;`
- `use codex_core::mcp::auth::compute_auth_statuses;`
- `use codex_core::mcp::auth::oauth_login_support;`
- `use codex_core::protocol::McpAuthStatus;`
- `use codex_rmcp_client::delete_oauth_tokens;`
- `use codex_rmcp_client::perform_oauth_login;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/03_API/CLI.md`
