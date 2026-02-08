# `codex-rs/cli/src/login.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10226`
- sha256: `c0d01e37a1a9f2a7edd71de68e0db5007db581a71397dee38b025b106f78f68f`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/login.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn read_api_key_from_stdin() -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/login.rs:1` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/cli/src/login.rs:2` `use codex_core::CodexAuth;`
- `use` `codex-rs/cli/src/login.rs:3` `use codex_core::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/cli/src/login.rs:4` `use codex_core::auth::AuthMode;`
- `use` `codex-rs/cli/src/login.rs:5` `use codex_core::auth::CLIENT_ID;`
- `use` `codex-rs/cli/src/login.rs:6` `use codex_core::auth::login_with_api_key;`
- `use` `codex-rs/cli/src/login.rs:7` `use codex_core::auth::logout;`
- `use` `codex-rs/cli/src/login.rs:8` `use codex_core::config::Config;`
- `use` `codex-rs/cli/src/login.rs:9` `use codex_login::ServerOptions;`
- `use` `codex-rs/cli/src/login.rs:10` `use codex_login::run_device_code_login;`
- `use` `codex-rs/cli/src/login.rs:11` `use codex_login::run_login_server;`
- `use` `codex-rs/cli/src/login.rs:12` `use codex_protocol::config_types::ForcedLoginMethod;`
- `use` `codex-rs/cli/src/login.rs:13` `use std::io::IsTerminal;`
- `use` `codex-rs/cli/src/login.rs:14` `use std::io::Read;`
- `use` `codex-rs/cli/src/login.rs:15` `use std::path::PathBuf;`
- `const` `codex-rs/cli/src/login.rs:17` `const CHATGPT_LOGIN_DISABLED_MESSAGE: &str =`
- `const` `codex-rs/cli/src/login.rs:19` `const API_KEY_LOGIN_DISABLED_MESSAGE: &str =`
- `const` `codex-rs/cli/src/login.rs:21` `const LOGIN_SUCCESS_MESSAGE: &str = "Successfully logged in";`
- `fn` `codex-rs/cli/src/login.rs:23` `fn print_login_server_start(actual_port: u16, auth_url: &str) {`
- `fn` `codex-rs/cli/src/login.rs:29` `pub async fn login_with_chatgpt(`
- `fn` `codex-rs/cli/src/login.rs:47` `pub async fn run_login_with_chatgpt(cli_config_overrides: CliConfigOverrides) -> ! {`
- `fn` `codex-rs/cli/src/login.rs:75` `pub async fn run_login_with_api_key(`
- `fn` `codex-rs/cli/src/login.rs:102` `pub fn read_api_key_from_stdin() -> String {`
- `fn` `codex-rs/cli/src/login.rs:130` `pub async fn run_login_with_device_code(`
- `fn` `codex-rs/cli/src/login.rs:166` `pub async fn run_login_with_device_code_fallback_to_browser(`
- `fn` `codex-rs/cli/src/login.rs:224` `pub async fn run_login_status(cli_config_overrides: CliConfigOverrides) -> ! {`
- `fn` `codex-rs/cli/src/login.rs:255` `pub async fn run_logout(cli_config_overrides: CliConfigOverrides) -> ! {`
- `fn` `codex-rs/cli/src/login.rs:274` `async fn load_config_or_exit(cli_config_overrides: CliConfigOverrides) -> Config {`
- `fn` `codex-rs/cli/src/login.rs:292` `fn safe_format_key(key: &str) -> String {`
- `use` `codex-rs/cli/src/login.rs:303` `use super::safe_format_key;`
- `fn` `codex-rs/cli/src/login.rs:306` `fn formats_long_key() {`
- `fn` `codex-rs/cli/src/login.rs:312` `fn short_key_returns_stars() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_common::CliConfigOverrides;`
- `use codex_core::CodexAuth;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::auth::AuthMode;`
- `use codex_core::auth::CLIENT_ID;`
- `use codex_core::auth::login_with_api_key;`
- `use codex_core::auth::logout;`
- `use codex_core::config::Config;`
- `use codex_login::ServerOptions;`
- `use codex_login::run_device_code_login;`
- `use codex_login::run_login_server;`
- `use codex_protocol::config_types::ForcedLoginMethod;`
- `use std::io::IsTerminal;`
- `use std::io::Read;`
- `use std::path::PathBuf;`
- `use super::safe_format_key;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/03_API/CLI.md`
