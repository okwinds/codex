# `codex-rs/core/src/config/types.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `31102`
- sha256: `24d947b395ad10a18e67a53ca0e8e6c34742c7f070f4e9003035d12400453640`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `impl` `codex-rs/core/src/config/types.rs:124` `impl<'de> Deserialize<'de> for McpServerConfig {`
- `const` `codex-rs/core/src/config/types.rs:203` `const fn default_enabled() -> bool {`
- `enum` `codex-rs/core/src/config/types.rs:209` `pub enum McpServerTransportConfig {`
- `use` `codex-rs/core/src/config/types.rs:240` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config/types.rs:241` `use serde::Deserializer;`
- `use` `codex-rs/core/src/config/types.rs:242` `use serde::Serializer;`
- `use` `codex-rs/core/src/config/types.rs:243` `use std::time::Duration;`
- `enum` `codex-rs/core/src/config/types.rs:266` `pub enum UriBasedFileOpener {`
- `impl` `codex-rs/core/src/config/types.rs:284` `impl UriBasedFileOpener {`
- `fn` `codex-rs/core/src/config/types.rs:285` `pub fn get_scheme(&self) -> Option<&str> {`
- `struct` `codex-rs/core/src/config/types.rs:299` `pub struct History {`
- `enum` `codex-rs/core/src/config/types.rs:310` `pub enum HistoryPersistence {`
- `struct` `codex-rs/core/src/config/types.rs:323` `pub struct AnalyticsConfigToml {`
- `struct` `codex-rs/core/src/config/types.rs:330` `pub struct FeedbackConfigToml {`
- `enum` `codex-rs/core/src/config/types.rs:339` `pub enum OtelHttpProtocol {`
- `struct` `codex-rs/core/src/config/types.rs:349` `pub struct OtelTlsConfig {`
- `enum` `codex-rs/core/src/config/types.rs:359` `pub enum OtelExporterKind {`
- `struct` `codex-rs/core/src/config/types.rs:382` `pub struct OtelConfigToml {`
- `struct` `codex-rs/core/src/config/types.rs:398` `pub struct OtelConfig {`
- `impl` `codex-rs/core/src/config/types.rs:406` `impl Default for OtelConfig {`
- `fn` `codex-rs/core/src/config/types.rs:407` `fn default() -> Self {`
- `enum` `codex-rs/core/src/config/types.rs:420` `pub enum Notifications {`
- `impl` `codex-rs/core/src/config/types.rs:425` `impl Default for Notifications {`
- `fn` `codex-rs/core/src/config/types.rs:426` `fn default() -> Self {`
- `enum` `codex-rs/core/src/config/types.rs:433` `pub enum NotificationMethod {`
- `impl` `codex-rs/core/src/config/types.rs:440` `impl fmt::Display for NotificationMethod {`
- `fn` `codex-rs/core/src/config/types.rs:441` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/core/src/config/types.rs:453` `pub struct Tui {`
- `const` `codex-rs/core/src/config/types.rs:491` `const fn default_true() -> bool {`
- `struct` `codex-rs/core/src/config/types.rs:499` `pub struct Notice {`
- `impl` `codex-rs/core/src/config/types.rs:516` `impl Notice {`
- `struct` `codex-rs/core/src/config/types.rs:523` `pub struct SkillConfig {`
- `struct` `codex-rs/core/src/config/types.rs:530` `pub struct SkillsConfig {`
- `struct` `codex-rs/core/src/config/types.rs:537` `pub struct SandboxWorkspaceWrite {`
- `impl` `codex-rs/core/src/config/types.rs:548` `impl From<SandboxWorkspaceWrite> for codex_app_server_protocol::SandboxSettings {`
- `fn` `codex-rs/core/src/config/types.rs:549` `fn from(sandbox_workspace_write: SandboxWorkspaceWrite) -> Self {`
- `enum` `codex-rs/core/src/config/types.rs:561` `pub enum ShellEnvironmentPolicyInherit {`
- `struct` `codex-rs/core/src/config/types.rs:578` `pub struct ShellEnvironmentPolicyToml {`
- `type` `codex-rs/core/src/config/types.rs:594` `pub type EnvironmentVariablePattern = WildMatchPattern<'*', '?'>;`
- `struct` `codex-rs/core/src/config/types.rs:604` `pub struct ShellEnvironmentPolicy {`
- `impl` `codex-rs/core/src/config/types.rs:625` `impl From<ShellEnvironmentPolicyToml> for ShellEnvironmentPolicy {`
- `fn` `codex-rs/core/src/config/types.rs:626` `fn from(toml: ShellEnvironmentPolicyToml) -> Self {`
- `impl` `codex-rs/core/src/config/types.rs:656` `impl Default for ShellEnvironmentPolicy {`
- `fn` `codex-rs/core/src/config/types.rs:657` `fn default() -> Self {`
- `use` `codex-rs/core/src/config/types.rs:671` `use super::*;`
- `use` `codex-rs/core/src/config/types.rs:672` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/config/types.rs:675` `fn deserialize_stdio_command_server_config() {`
- `fn` `codex-rs/core/src/config/types.rs:699` `fn deserialize_stdio_command_server_config_with_args() {`
- `fn` `codex-rs/core/src/config/types.rs:722` `fn deserialize_stdio_command_server_config_with_arg_with_args_and_env() {`
- `fn` `codex-rs/core/src/config/types.rs:746` `fn deserialize_stdio_command_server_config_with_env_vars() {`
- `fn` `codex-rs/core/src/config/types.rs:768` `fn deserialize_stdio_command_server_config_with_cwd() {`
- `fn` `codex-rs/core/src/config/types.rs:790` `fn deserialize_disabled_server_config() {`
- `fn` `codex-rs/core/src/config/types.rs:803` `fn deserialize_streamable_http_server_config() {`
- `fn` `codex-rs/core/src/config/types.rs:824` `fn deserialize_streamable_http_server_config_with_env_var() {`
- `fn` `codex-rs/core/src/config/types.rs:846` `fn deserialize_streamable_http_server_config_with_headers() {`
- `fn` `codex-rs/core/src/config/types.rs:871` `fn deserialize_server_config_with_tool_filters() {`
- `fn` `codex-rs/core/src/config/types.rs:886` `fn deserialize_rejects_command_and_url() {`
- `fn` `codex-rs/core/src/config/types.rs:897` `fn deserialize_rejects_env_for_http_transport() {`
- `fn` `codex-rs/core/src/config/types.rs:908` `fn deserialize_rejects_headers_for_stdio() {`
- `fn` `codex-rs/core/src/config/types.rs:927` `fn deserialize_rejects_inline_bearer_token_field() {`

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
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
