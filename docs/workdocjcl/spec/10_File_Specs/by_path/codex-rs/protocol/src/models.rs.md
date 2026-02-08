# `codex-rs/protocol/src/models.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `52649`
- sha256: `2b0811df3db522070345029b596341637b88898d3814fec7986553faee70d5f8`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/models.rs` (read)

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub enum SandboxPermissions {`
- `pub fn requires_escalated_permissions(self) -> bool {`
- `pub enum ResponseInputItem {`
- `pub enum ContentItem {`
- `pub enum MessagePhase {`
- `pub enum ResponseItem {`
- `pub struct BaseInstructions {`
- `pub struct DeveloperInstructions {`
- `pub fn from(`
- `pub fn into_text(self) -> String {`
- `pub fn concat(self, other: impl Into<DeveloperInstructions>) -> Self {`
- `pub fn personality_spec_message(spec: String) -> Self {`
- `pub fn from_policy(`
- `pub fn from_collaboration_mode(collaboration_mode: &CollaborationMode) -> Option<Self> {`
- `pub fn format_allow_prefixes(prefixes: Vec<Vec<String>>) -> Option<String> {`
- `pub fn image_open_tag_text() -> String {`
- `pub fn image_close_tag_text() -> String {`
- `pub fn local_image_label_text(label_number: usize) -> String {`
- `pub fn local_image_open_tag_text(label_number: usize) -> String {`
- `pub fn is_local_image_open_tag_text(text: &str) -> bool {`
- `pub fn is_local_image_close_tag_text(text: &str) -> bool {`
- `pub fn is_image_open_tag_text(text: &str) -> bool {`
- `pub fn is_image_close_tag_text(text: &str) -> bool {`
- `pub fn local_image_content_items_with_label_number(`
- `pub enum LocalShellStatus {`
- `pub enum LocalShellAction {`
- `pub struct LocalShellExecAction {`
- `pub enum WebSearchAction {`
- `pub enum ReasoningItemReasoningSummary {`
- `pub enum ReasoningItemContent {`
- `pub struct ShellToolCallParams {`
- `pub struct ShellCommandToolCallParams {`
- `pub enum FunctionCallOutputContentItem {`
- `pub struct FunctionCallOutputPayload {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/models.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/protocol/src/models.rs:2` `use std::path::Path;`
- `use` `codex-rs/protocol/src/models.rs:4` `use codex_utils_image::load_and_resize_to_fit;`
- `use` `codex-rs/protocol/src/models.rs:5` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/models.rs:6` `use serde::Deserializer;`
- `use` `codex-rs/protocol/src/models.rs:7` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/models.rs:8` `use serde::ser::Serializer;`
- `use` `codex-rs/protocol/src/models.rs:9` `use ts_rs::TS;`
- `use` `codex-rs/protocol/src/models.rs:11` `use crate::config_types::CollaborationMode;`
- `use` `codex-rs/protocol/src/models.rs:12` `use crate::config_types::SandboxMode;`
- `use` `codex-rs/protocol/src/models.rs:13` `use crate::protocol::AskForApproval;`
- `use` `codex-rs/protocol/src/models.rs:14` `use crate::protocol::COLLABORATION_MODE_CLOSE_TAG;`
- `use` `codex-rs/protocol/src/models.rs:15` `use crate::protocol::COLLABORATION_MODE_OPEN_TAG;`
- `use` `codex-rs/protocol/src/models.rs:16` `use crate::protocol::NetworkAccess;`
- `use` `codex-rs/protocol/src/models.rs:17` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/protocol/src/models.rs:18` `use crate::protocol::WritableRoot;`
- `use` `codex-rs/protocol/src/models.rs:19` `use crate::user_input::UserInput;`
- `use` `codex-rs/protocol/src/models.rs:20` `use codex_execpolicy::Policy;`
- `use` `codex-rs/protocol/src/models.rs:21` `use codex_git::GhostCommit;`
- `use` `codex-rs/protocol/src/models.rs:22` `use codex_utils_image::error::ImageProcessingError;`
- `use` `codex-rs/protocol/src/models.rs:23` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/models.rs:25` `use crate::mcp::CallToolResult;`
- `enum` `codex-rs/protocol/src/models.rs:32` `pub enum SandboxPermissions {`
- `impl` `codex-rs/protocol/src/models.rs:40` `impl SandboxPermissions {`
- `fn` `codex-rs/protocol/src/models.rs:41` `pub fn requires_escalated_permissions(self) -> bool {`
- `enum` `codex-rs/protocol/src/models.rs:48` `pub enum ResponseInputItem {`
- `enum` `codex-rs/protocol/src/models.rs:69` `pub enum ContentItem {`
- `enum` `codex-rs/protocol/src/models.rs:77` `pub enum MessagePhase {`
- `enum` `codex-rs/protocol/src/models.rs:84` `pub enum ResponseItem {`
- `const` `codex-rs/protocol/src/models.rs:189` `pub const BASE_INSTRUCTIONS_DEFAULT: &str = include_str!("prompts/base_instructions/default.md");`
- `struct` `codex-rs/protocol/src/models.rs:194` `pub struct BaseInstructions {`
- `impl` `codex-rs/protocol/src/models.rs:198` `impl Default for BaseInstructions {`
- `fn` `codex-rs/protocol/src/models.rs:199` `fn default() -> Self {`
- `struct` `codex-rs/protocol/src/models.rs:210` `pub struct DeveloperInstructions {`
- `const` `codex-rs/protocol/src/models.rs:214` `const APPROVAL_POLICY_NEVER: &str = include_str!("prompts/permissions/approval_policy/never.md");`
- `const` `codex-rs/protocol/src/models.rs:215` `const APPROVAL_POLICY_UNLESS_TRUSTED: &str =`
- `const` `codex-rs/protocol/src/models.rs:217` `const APPROVAL_POLICY_ON_FAILURE: &str =`
- `const` `codex-rs/protocol/src/models.rs:219` `const APPROVAL_POLICY_ON_REQUEST: &str =`
- `const` `codex-rs/protocol/src/models.rs:221` `const APPROVAL_POLICY_ON_REQUEST_RULE: &str =`
- `const` `codex-rs/protocol/src/models.rs:224` `const SANDBOX_MODE_DANGER_FULL_ACCESS: &str =`
- `const` `codex-rs/protocol/src/models.rs:226` `const SANDBOX_MODE_WORKSPACE_WRITE: &str =`
- `const` `codex-rs/protocol/src/models.rs:228` `const SANDBOX_MODE_READ_ONLY: &str = include_str!("prompts/permissions/sandbox_mode/read_only.md");`
- `impl` `codex-rs/protocol/src/models.rs:230` `impl DeveloperInstructions {`
- `fn` `codex-rs/protocol/src/models.rs:235` `pub fn from(`
- `fn` `codex-rs/protocol/src/models.rs:265` `pub fn into_text(self) -> String {`
- `fn` `codex-rs/protocol/src/models.rs:269` `pub fn concat(self, other: impl Into<DeveloperInstructions>) -> Self {`
- `fn` `codex-rs/protocol/src/models.rs:278` `pub fn personality_spec_message(spec: String) -> Self {`
- `fn` `codex-rs/protocol/src/models.rs:285` `pub fn from_policy(`
- `fn` `codex-rs/protocol/src/models.rs:319` `pub fn from_collaboration_mode(collaboration_mode: &CollaborationMode) -> Option<Self> {`
- `fn` `codex-rs/protocol/src/models.rs:332` `fn from_permissions_with_network(`
- `fn` `codex-rs/protocol/src/models.rs:356` `fn from_writable_roots(writable_roots: Option<Vec<WritableRoot>>) -> Self {`
- `fn` `codex-rs/protocol/src/models.rs:377` `fn sandbox_text(mode: SandboxMode, network_access: NetworkAccess) -> DeveloperInstructions {`
- `const` `codex-rs/protocol/src/models.rs:389` `const MAX_RENDERED_PREFIXES: usize = 100;`
- `const` `codex-rs/protocol/src/models.rs:390` `const MAX_ALLOW_PREFIX_TEXT_BYTES: usize = 5000;`
- `const` `codex-rs/protocol/src/models.rs:391` `const TRUNCATED_MARKER: &str = "...\n[Some commands were truncated]";`
- `fn` `codex-rs/protocol/src/models.rs:393` `pub fn format_allow_prefixes(prefixes: Vec<Vec<String>>) -> Option<String> {`
- `fn` `codex-rs/protocol/src/models.rs:432` `fn prefix_combined_str_len(prefix: &[String]) -> usize {`
- `fn` `codex-rs/protocol/src/models.rs:436` `fn render_command_prefix(prefix: &[String]) -> String {`
- `impl` `codex-rs/protocol/src/models.rs:445` `impl From<DeveloperInstructions> for ResponseItem {`
- `fn` `codex-rs/protocol/src/models.rs:446` `fn from(di: DeveloperInstructions) -> Self {`
- `impl` `codex-rs/protocol/src/models.rs:459` `impl From<SandboxMode> for DeveloperInstructions {`
- `fn` `codex-rs/protocol/src/models.rs:460` `fn from(mode: SandboxMode) -> Self {`
- `fn` `codex-rs/protocol/src/models.rs:470` `fn should_serialize_reasoning_content(content: &Option<Vec<ReasoningItemContent>>) -> bool {`
- `fn` `codex-rs/protocol/src/models.rs:479` `fn local_image_error_placeholder(`
- `const` `codex-rs/protocol/src/models.rs:492` `pub const VIEW_IMAGE_TOOL_NAME: &str = "view_image";`
- `const` `codex-rs/protocol/src/models.rs:494` `const IMAGE_OPEN_TAG: &str = "<image>";`
- `const` `codex-rs/protocol/src/models.rs:495` `const IMAGE_CLOSE_TAG: &str = "</image>";`
- `const` `codex-rs/protocol/src/models.rs:496` `const LOCAL_IMAGE_OPEN_TAG_PREFIX: &str = "<image name=";`
- `const` `codex-rs/protocol/src/models.rs:497` `const LOCAL_IMAGE_OPEN_TAG_SUFFIX: &str = ">";`
- `const` `codex-rs/protocol/src/models.rs:498` `const LOCAL_IMAGE_CLOSE_TAG: &str = IMAGE_CLOSE_TAG;`
- `fn` `codex-rs/protocol/src/models.rs:500` `pub fn image_open_tag_text() -> String {`
- `fn` `codex-rs/protocol/src/models.rs:504` `pub fn image_close_tag_text() -> String {`
- `fn` `codex-rs/protocol/src/models.rs:508` `pub fn local_image_label_text(label_number: usize) -> String {`
- `fn` `codex-rs/protocol/src/models.rs:512` `pub fn local_image_open_tag_text(label_number: usize) -> String {`
- `fn` `codex-rs/protocol/src/models.rs:517` `pub fn is_local_image_open_tag_text(text: &str) -> bool {`
- `fn` `codex-rs/protocol/src/models.rs:522` `pub fn is_local_image_close_tag_text(text: &str) -> bool {`
- `fn` `codex-rs/protocol/src/models.rs:526` `pub fn is_image_open_tag_text(text: &str) -> bool {`
- `fn` `codex-rs/protocol/src/models.rs:530` `pub fn is_image_close_tag_text(text: &str) -> bool {`
- `fn` `codex-rs/protocol/src/models.rs:534` `fn invalid_image_error_placeholder(`
- `fn` `codex-rs/protocol/src/models.rs:547` `fn unsupported_image_error_placeholder(path: &std::path::Path, mime: &str) -> ContentItem {`
- `fn` `codex-rs/protocol/src/models.rs:557` `pub fn local_image_content_items_with_label_number(`
- `impl` `codex-rs/protocol/src/models.rs:604` `impl From<ResponseInputItem> for ResponseItem {`
- `fn` `codex-rs/protocol/src/models.rs:605` `fn from(item: ResponseInputItem) -> Self {`
- `enum` `codex-rs/protocol/src/models.rs:637` `pub enum LocalShellStatus {`
- `enum` `codex-rs/protocol/src/models.rs:645` `pub enum LocalShellAction {`
- `struct` `codex-rs/protocol/src/models.rs:650` `pub struct LocalShellExecAction {`
- `enum` `codex-rs/protocol/src/models.rs:660` `pub enum WebSearchAction {`
- `enum` `codex-rs/protocol/src/models.rs:689` `pub enum ReasoningItemReasoningSummary {`
- `enum` `codex-rs/protocol/src/models.rs:695` `pub enum ReasoningItemContent {`
- `impl` `codex-rs/protocol/src/models.rs:700` `impl From<Vec<UserInput>> for ResponseInputItem {`
- `fn` `codex-rs/protocol/src/models.rs:701` `fn from(items: Vec<UserInput>) -> Self {`
- `struct` `codex-rs/protocol/src/models.rs:732` `pub struct ShellToolCallParams {`
- `struct` `codex-rs/protocol/src/models.rs:753` `pub struct ShellCommandToolCallParams {`
- `enum` `codex-rs/protocol/src/models.rs:777` `pub enum FunctionCallOutputContentItem {`
- `struct` `codex-rs/protocol/src/models.rs:792` `pub struct FunctionCallOutputPayload {`
- `enum` `codex-rs/protocol/src/models.rs:801` `enum FunctionCallOutputPayloadSerde {`
- `impl` `codex-rs/protocol/src/models.rs:809` `impl Serialize for FunctionCallOutputPayload {`
- `impl` `codex-rs/protocol/src/models.rs:822` `impl<'de> Deserialize<'de> for FunctionCallOutputPayload {`
- `impl` `codex-rs/protocol/src/models.rs:844` `impl From<&CallToolResult> for FunctionCallOutputPayload {`
- `fn` `codex-rs/protocol/src/models.rs:845` `fn from(call_tool_result: &CallToolResult) -> Self {`
- `fn` `codex-rs/protocol/src/models.rs:897` `fn convert_mcp_content_to_items(`
- `enum` `codex-rs/protocol/src/models.rs:902` `enum McpContent {`
- `impl` `codex-rs/protocol/src/models.rs:945` `impl std::fmt::Display for FunctionCallOutputPayload {`
- `fn` `codex-rs/protocol/src/models.rs:946` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `impl` `codex-rs/protocol/src/models.rs:951` `impl std::ops::Deref for FunctionCallOutputPayload {`
- `type` `codex-rs/protocol/src/models.rs:952` `type Target = str;`
- `fn` `codex-rs/protocol/src/models.rs:953` `fn deref(&self) -> &Self::Target {`
- `use` `codex-rs/protocol/src/models.rs:962` `use super::*;`
- `use` `codex-rs/protocol/src/models.rs:963` `use crate::config_types::SandboxMode;`
- `use` `codex-rs/protocol/src/models.rs:964` `use crate::protocol::AskForApproval;`
- `use` `codex-rs/protocol/src/models.rs:965` `use anyhow::Result;`
- `use` `codex-rs/protocol/src/models.rs:966` `use codex_execpolicy::Policy;`
- `use` `codex-rs/protocol/src/models.rs:967` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/protocol/src/models.rs:968` `use std::path::PathBuf;`
- `use` `codex-rs/protocol/src/models.rs:969` `use tempfile::tempdir;`
- `fn` `codex-rs/protocol/src/models.rs:972` `fn convert_mcp_content_to_items_preserves_data_urls() {`
- `fn` `codex-rs/protocol/src/models.rs:989` `fn convert_mcp_content_to_items_builds_data_urls_when_missing_prefix() {`
- `fn` `codex-rs/protocol/src/models.rs:1006` `fn convert_mcp_content_to_items_returns_none_without_images() {`
- `fn` `codex-rs/protocol/src/models.rs:1016` `fn converts_sandbox_mode_into_developer_instructions() {`
- `fn` `codex-rs/protocol/src/models.rs:1035` `fn builds_permissions_with_network_access_override() {`
- `fn` `codex-rs/protocol/src/models.rs:1057` `fn builds_permissions_from_policy() {`
- `fn` `codex-rs/protocol/src/models.rs:1078` `fn includes_request_rule_instructions_when_enabled() {`
- `fn` `codex-rs/protocol/src/models.rs:1102` `fn render_command_prefix_list_sorts_by_len_then_total_len_then_alphabetical() {`
- `fn` `codex-rs/protocol/src/models.rs:1126` `fn render_command_prefix_list_limits_output_to_max_prefixes() {`
- `fn` `codex-rs/protocol/src/models.rs:1138` `fn format_allow_prefixes_limits_output() {`
- `fn` `codex-rs/protocol/src/models.rs:1158` `fn serializes_success_as_plain_string() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1176` `fn serializes_failure_as_string() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1194` `fn serializes_image_outputs_as_array() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1235` `fn preserves_existing_image_data_urls() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1262` `fn deserializes_array_payload_into_items() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1288` `fn deserializes_compaction_alias() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1303` `fn roundtrips_web_search_call_actions() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1392` `fn deserialize_shell_tool_call_params() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1415` `fn wraps_image_user_input_with_tags() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1442` `fn local_image_read_error_adds_placeholder() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1475` `fn local_image_non_image_adds_placeholder() -> Result<()> {`
- `fn` `codex-rs/protocol/src/models.rs:1508` `fn local_image_unsupported_image_format_adds_placeholder() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use codex_utils_image::load_and_resize_to_fit;`
- `use serde::Deserialize;`
- `use serde::Deserializer;`
- `use serde::Serialize;`
- `use serde::ser::Serializer;`
- `use ts_rs::TS;`
- `use crate::config_types::CollaborationMode;`
- `use crate::config_types::SandboxMode;`
- `use crate::protocol::AskForApproval;`
- `use crate::protocol::COLLABORATION_MODE_CLOSE_TAG;`
- `use crate::protocol::COLLABORATION_MODE_OPEN_TAG;`
- `use crate::protocol::NetworkAccess;`
- `use crate::protocol::SandboxPolicy;`
- `use crate::protocol::WritableRoot;`
- `use crate::user_input::UserInput;`
- `use codex_execpolicy::Policy;`
- `use codex_git::GhostCommit;`
- `use codex_utils_image::error::ImageProcessingError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
