# `codex-rs/core/src/config/types.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `33225`
- sha256: `c737aa36e75b02de35606a504d1cd0385428aa10a8eb75f92c929283e3e7052e`
- generated_utc: `2026-02-08T10:45:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config/types.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum McpServerDisabledReason {`
- `pub struct McpServerConfig {`
- `pub enum McpServerTransportConfig {`
- `pub enum UriBasedFileOpener {`
- `pub fn get_scheme(&self) -> Option<&str> {`
- `pub struct History {`
- `pub enum HistoryPersistence {`
- `pub struct AnalyticsConfigToml {`
- `pub struct FeedbackConfigToml {`
- `pub enum AppDisabledReason {`
- `pub struct AppConfig {`
- `pub struct AppsConfigToml {`
- `pub enum OtelHttpProtocol {`
- `pub struct OtelTlsConfig {`
- `pub enum OtelExporterKind {`
- `pub struct OtelConfigToml {`
- `pub struct OtelConfig {`
- `pub enum Notifications {`
- `pub enum NotificationMethod {`
- `pub struct Tui {`
- `pub struct Notice {`
- `pub struct SkillConfig {`
- `pub struct SkillsConfig {`
- `pub struct SandboxWorkspaceWrite {`
- `pub enum ShellEnvironmentPolicyInherit {`
- `pub struct ShellEnvironmentPolicyToml {`
- `pub struct ShellEnvironmentPolicy {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config/types.rs:6` `use crate::config_loader::RequirementSource;`
- `use` `codex-rs/core/src/config/types.rs:11` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config/types.rs:12` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/config/types.rs:13` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/config/types.rs:14` `use std::fmt;`
- `use` `codex-rs/core/src/config/types.rs:15` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/config/types.rs:16` `use std::time::Duration;`
- `use` `codex-rs/core/src/config/types.rs:17` `use wildmatch::WildMatchPattern;`
- `use` `codex-rs/core/src/config/types.rs:19` `use schemars::JsonSchema;`
- `use` `codex-rs/core/src/config/types.rs:20` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config/types.rs:21` `use serde::Deserializer;`
- `use` `codex-rs/core/src/config/types.rs:22` `use serde::Serialize;`
- `use` `codex-rs/core/src/config/types.rs:23` `use serde::de::Error as SerdeError;`
- `const` `codex-rs/core/src/config/types.rs:25` `pub const DEFAULT_OTEL_ENVIRONMENT: &str = "dev";`
- `enum` `codex-rs/core/src/config/types.rs:28` `pub enum McpServerDisabledReason {`
- `impl` `codex-rs/core/src/config/types.rs:33` `impl fmt::Display for McpServerDisabledReason {`
- `fn` `codex-rs/core/src/config/types.rs:34` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/core/src/config/types.rs:45` `pub struct McpServerConfig {`
- `impl` `codex-rs/core/src/config/types.rs:130` `impl<'de> Deserialize<'de> for McpServerConfig {`
- `const` `codex-rs/core/src/config/types.rs:211` `const fn default_enabled() -> bool {`
- `enum` `codex-rs/core/src/config/types.rs:217` `pub enum McpServerTransportConfig {`
- `use` `codex-rs/core/src/config/types.rs:248` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config/types.rs:249` `use serde::Deserializer;`
- `use` `codex-rs/core/src/config/types.rs:250` `use serde::Serializer;`
- `use` `codex-rs/core/src/config/types.rs:251` `use std::time::Duration;`
- `enum` `codex-rs/core/src/config/types.rs:274` `pub enum UriBasedFileOpener {`
- `impl` `codex-rs/core/src/config/types.rs:292` `impl UriBasedFileOpener {`
- `fn` `codex-rs/core/src/config/types.rs:293` `pub fn get_scheme(&self) -> Option<&str> {`
- `struct` `codex-rs/core/src/config/types.rs:307` `pub struct History {`
- `enum` `codex-rs/core/src/config/types.rs:318` `pub enum HistoryPersistence {`
- `struct` `codex-rs/core/src/config/types.rs:331` `pub struct AnalyticsConfigToml {`
- `struct` `codex-rs/core/src/config/types.rs:338` `pub struct FeedbackConfigToml {`
- `enum` `codex-rs/core/src/config/types.rs:345` `pub enum AppDisabledReason {`
- `impl` `codex-rs/core/src/config/types.rs:350` `impl fmt::Display for AppDisabledReason {`
- `fn` `codex-rs/core/src/config/types.rs:351` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/core/src/config/types.rs:362` `pub struct AppConfig {`
- `struct` `codex-rs/core/src/config/types.rs:375` `pub struct AppsConfigToml {`
- `enum` `codex-rs/core/src/config/types.rs:385` `pub enum OtelHttpProtocol {`
- `struct` `codex-rs/core/src/config/types.rs:395` `pub struct OtelTlsConfig {`
- `enum` `codex-rs/core/src/config/types.rs:405` `pub enum OtelExporterKind {`
- `struct` `codex-rs/core/src/config/types.rs:428` `pub struct OtelConfigToml {`
- `struct` `codex-rs/core/src/config/types.rs:444` `pub struct OtelConfig {`
- `impl` `codex-rs/core/src/config/types.rs:452` `impl Default for OtelConfig {`
- `fn` `codex-rs/core/src/config/types.rs:453` `fn default() -> Self {`
- `enum` `codex-rs/core/src/config/types.rs:466` `pub enum Notifications {`
- `impl` `codex-rs/core/src/config/types.rs:471` `impl Default for Notifications {`
- `fn` `codex-rs/core/src/config/types.rs:472` `fn default() -> Self {`
- `enum` `codex-rs/core/src/config/types.rs:479` `pub enum NotificationMethod {`
- `impl` `codex-rs/core/src/config/types.rs:486` `impl fmt::Display for NotificationMethod {`
- `fn` `codex-rs/core/src/config/types.rs:487` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/core/src/config/types.rs:499` `pub struct Tui {`
- `const` `codex-rs/core/src/config/types.rs:543` `const fn default_true() -> bool {`
- `struct` `codex-rs/core/src/config/types.rs:551` `pub struct Notice {`
- `impl` `codex-rs/core/src/config/types.rs:568` `impl Notice {`
- `struct` `codex-rs/core/src/config/types.rs:575` `pub struct SkillConfig {`
- `struct` `codex-rs/core/src/config/types.rs:582` `pub struct SkillsConfig {`
- `struct` `codex-rs/core/src/config/types.rs:589` `pub struct SandboxWorkspaceWrite {`
- `impl` `codex-rs/core/src/config/types.rs:600` `impl From<SandboxWorkspaceWrite> for codex_app_server_protocol::SandboxSettings {`
- `fn` `codex-rs/core/src/config/types.rs:601` `fn from(sandbox_workspace_write: SandboxWorkspaceWrite) -> Self {`
- `enum` `codex-rs/core/src/config/types.rs:613` `pub enum ShellEnvironmentPolicyInherit {`
- `struct` `codex-rs/core/src/config/types.rs:630` `pub struct ShellEnvironmentPolicyToml {`
- `type` `codex-rs/core/src/config/types.rs:646` `pub type EnvironmentVariablePattern = WildMatchPattern<'*', '?'>;`
- `struct` `codex-rs/core/src/config/types.rs:656` `pub struct ShellEnvironmentPolicy {`
- `impl` `codex-rs/core/src/config/types.rs:677` `impl From<ShellEnvironmentPolicyToml> for ShellEnvironmentPolicy {`
- `fn` `codex-rs/core/src/config/types.rs:678` `fn from(toml: ShellEnvironmentPolicyToml) -> Self {`
- `impl` `codex-rs/core/src/config/types.rs:708` `impl Default for ShellEnvironmentPolicy {`
- `fn` `codex-rs/core/src/config/types.rs:709` `fn default() -> Self {`
- `use` `codex-rs/core/src/config/types.rs:723` `use super::*;`
- `use` `codex-rs/core/src/config/types.rs:724` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/config/types.rs:727` `fn deserialize_stdio_command_server_config() {`
- `fn` `codex-rs/core/src/config/types.rs:752` `fn deserialize_stdio_command_server_config_with_args() {`
- `fn` `codex-rs/core/src/config/types.rs:775` `fn deserialize_stdio_command_server_config_with_arg_with_args_and_env() {`
- `fn` `codex-rs/core/src/config/types.rs:799` `fn deserialize_stdio_command_server_config_with_env_vars() {`
- `fn` `codex-rs/core/src/config/types.rs:821` `fn deserialize_stdio_command_server_config_with_cwd() {`
- `fn` `codex-rs/core/src/config/types.rs:843` `fn deserialize_disabled_server_config() {`
- `fn` `codex-rs/core/src/config/types.rs:857` `fn deserialize_required_server_config() {`
- `fn` `codex-rs/core/src/config/types.rs:870` `fn deserialize_streamable_http_server_config() {`
- `fn` `codex-rs/core/src/config/types.rs:891` `fn deserialize_streamable_http_server_config_with_env_var() {`
- `fn` `codex-rs/core/src/config/types.rs:913` `fn deserialize_streamable_http_server_config_with_headers() {`
- `fn` `codex-rs/core/src/config/types.rs:938` `fn deserialize_server_config_with_tool_filters() {`
- `fn` `codex-rs/core/src/config/types.rs:953` `fn deserialize_rejects_command_and_url() {`
- `fn` `codex-rs/core/src/config/types.rs:964` `fn deserialize_rejects_env_for_http_transport() {`
- `fn` `codex-rs/core/src/config/types.rs:975` `fn deserialize_rejects_headers_for_stdio() {`
- `fn` `codex-rs/core/src/config/types.rs:994` `fn deserialize_rejects_inline_bearer_token_field() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config_loader::RequirementSource;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use std::collections::BTreeMap;`
- `use std::collections::HashMap;`
- `use std::fmt;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use wildmatch::WildMatchPattern;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Deserializer;`
- `use serde::Serialize;`
- `use serde::de::Error as SerdeError;`
- `use serde::Deserialize;`
- `use serde::Deserializer;`
- `use serde::Serializer;`
- `use std::time::Duration;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
