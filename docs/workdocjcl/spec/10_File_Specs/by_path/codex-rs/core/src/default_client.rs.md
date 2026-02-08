# `codex-rs/core/src/default_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11298`
- sha256: `4572f6dd6987885ba33f43c0c7b92e7dcd551d68e512175af07269abd88d8b1b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/default_client.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub struct Originator {`
- `pub enum SetOriginatorError {`
- `pub fn set_default_originator(value: String) -> Result<(), SetOriginatorError> {`
- `pub fn set_default_client_residency_requirement(enforce_residency: Option<ResidencyRequirement>) {`
- `pub fn originator() -> Originator {`
- `pub fn is_first_party_originator(originator_value: &str) -> bool {`
- `pub fn get_codex_user_agent() -> String {`
- `pub fn create_client() -> CodexHttpClient {`
- `pub fn build_reqwest_client() -> reqwest::Client {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/default_client.rs:1` `use crate::config_loader::ResidencyRequirement;`
- `use` `codex-rs/core/src/default_client.rs:2` `use crate::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use` `codex-rs/core/src/default_client.rs:3` `use codex_client::CodexHttpClient;`
- `use` `codex-rs/core/src/default_client.rs:5` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/core/src/default_client.rs:6` `use reqwest::header::HeaderValue;`
- `use` `codex-rs/core/src/default_client.rs:7` `use std::sync::LazyLock;`
- `use` `codex-rs/core/src/default_client.rs:8` `use std::sync::Mutex;`
- `use` `codex-rs/core/src/default_client.rs:9` `use std::sync::RwLock;`
- `static` `codex-rs/core/src/default_client.rs:26` `pub static USER_AGENT_SUFFIX: LazyLock<Mutex<Option<String>>> = LazyLock::new(|| Mutex::new(None));`
- `const` `codex-rs/core/src/default_client.rs:27` `pub const DEFAULT_ORIGINATOR: &str = "codex_cli_rs";`
- `const` `codex-rs/core/src/default_client.rs:28` `pub const CODEX_INTERNAL_ORIGINATOR_OVERRIDE_ENV_VAR: &str = "CODEX_INTERNAL_ORIGINATOR_OVERRIDE";`
- `const` `codex-rs/core/src/default_client.rs:29` `pub const RESIDENCY_HEADER_NAME: &str = "x-openai-internal-codex-residency";`
- `struct` `codex-rs/core/src/default_client.rs:32` `pub struct Originator {`
- `static` `codex-rs/core/src/default_client.rs:36` `static ORIGINATOR: LazyLock<RwLock<Option<Originator>>> = LazyLock::new(|| RwLock::new(None));`
- `static` `codex-rs/core/src/default_client.rs:37` `static REQUIREMENTS_RESIDENCY: LazyLock<RwLock<Option<ResidencyRequirement>>> =`
- `enum` `codex-rs/core/src/default_client.rs:41` `pub enum SetOriginatorError {`
- `fn` `codex-rs/core/src/default_client.rs:46` `fn get_originator_value(provided: Option<String>) -> Originator {`
- `fn` `codex-rs/core/src/default_client.rs:67` `pub fn set_default_originator(value: String) -> Result<(), SetOriginatorError> {`
- `fn` `codex-rs/core/src/default_client.rs:82` `pub fn set_default_client_residency_requirement(enforce_residency: Option<ResidencyRequirement>) {`
- `fn` `codex-rs/core/src/default_client.rs:90` `pub fn originator() -> Originator {`
- `fn` `codex-rs/core/src/default_client.rs:111` `pub fn is_first_party_originator(originator_value: &str) -> bool {`
- `fn` `codex-rs/core/src/default_client.rs:117` `pub fn get_codex_user_agent() -> String {`
- `fn` `codex-rs/core/src/default_client.rs:148` `fn sanitize_user_agent(candidate: String, fallback: &str) -> String {`
- `fn` `codex-rs/core/src/default_client.rs:176` `pub fn create_client() -> CodexHttpClient {`
- `fn` `codex-rs/core/src/default_client.rs:181` `pub fn build_reqwest_client() -> reqwest::Client {`
- `fn` `codex-rs/core/src/default_client.rs:206` `fn is_sandboxed() -> bool {`
- `use` `codex-rs/core/src/default_client.rs:212` `use super::*;`
- `use` `codex-rs/core/src/default_client.rs:213` `use core_test_support::skip_if_no_network;`
- `use` `codex-rs/core/src/default_client.rs:214` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/default_client.rs:217` `fn test_get_codex_user_agent() {`
- `fn` `codex-rs/core/src/default_client.rs:225` `fn is_first_party_originator_matches_known_values() {`
- `fn` `codex-rs/core/src/default_client.rs:234` `async fn test_create_client_sets_default_headers() {`
- `use` `codex-rs/core/src/default_client.rs:239` `use wiremock::Mock;`
- `use` `codex-rs/core/src/default_client.rs:240` `use wiremock::MockServer;`
- `use` `codex-rs/core/src/default_client.rs:241` `use wiremock::ResponseTemplate;`
- `use` `codex-rs/core/src/default_client.rs:242` `use wiremock::matchers::method;`
- `use` `codex-rs/core/src/default_client.rs:243` `use wiremock::matchers::path;`
- `fn` `codex-rs/core/src/default_client.rs:291` `fn test_invalid_suffix_is_sanitized() {`
- `fn` `codex-rs/core/src/default_client.rs:302` `fn test_invalid_suffix_is_sanitized2() {`
- `fn` `codex-rs/core/src/default_client.rs:314` `fn test_macos() {`
- `use` `codex-rs/core/src/default_client.rs:315` `use regex_lite::Regex;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config_loader::ResidencyRequirement;`
- `use crate::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use codex_client::CodexHttpClient;`
- `use reqwest::header::HeaderMap;`
- `use reqwest::header::HeaderValue;`
- `use std::sync::LazyLock;`
- `use std::sync::Mutex;`
- `use std::sync::RwLock;`
- `use super::*;`
- `use core_test_support::skip_if_no_network;`
- `use pretty_assertions::assert_eq;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
- `use regex_lite::Regex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
