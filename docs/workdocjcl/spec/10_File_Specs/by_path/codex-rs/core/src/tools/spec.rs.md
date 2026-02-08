# `codex-rs/core/src/tools/spec.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `97172`
- sha256: `07564916d7d2939c38394a8dd3e885ecd76e732a321f9dbf2a6b4b9dda151f3f`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/spec.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn new(params: &ToolsConfigParams) -> Self {`
- `pub enum JsonSchema {`
- `pub enum AdditionalProperties {`
- `pub fn create_tools_json_for_responses_api(`
- `pub fn parse_tool_input_schema(input_schema: &JsonValue) -> Result<JsonSchema, serde_json::Error> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/spec.rs:1` `use crate::agent::AgentRole;`
- `use` `codex-rs/core/src/tools/spec.rs:2` `use crate::client_common::tools::ResponsesApiTool;`
- `use` `codex-rs/core/src/tools/spec.rs:3` `use crate::client_common::tools::ToolSpec;`
- `use` `codex-rs/core/src/tools/spec.rs:4` `use crate::features::Feature;`
- `use` `codex-rs/core/src/tools/spec.rs:5` `use crate::features::Features;`
- `use` `codex-rs/core/src/tools/spec.rs:6` `use crate::tools::handlers::PLAN_TOOL;`
- `use` `codex-rs/core/src/tools/spec.rs:7` `use crate::tools::handlers::apply_patch::create_apply_patch_freeform_tool;`
- `use` `codex-rs/core/src/tools/spec.rs:8` `use crate::tools::handlers::apply_patch::create_apply_patch_json_tool;`
- `use` `codex-rs/core/src/tools/spec.rs:9` `use crate::tools::handlers::collab::DEFAULT_WAIT_TIMEOUT_MS;`
- `use` `codex-rs/core/src/tools/spec.rs:10` `use crate::tools::handlers::collab::MAX_WAIT_TIMEOUT_MS;`
- `use` `codex-rs/core/src/tools/spec.rs:11` `use crate::tools::handlers::collab::MIN_WAIT_TIMEOUT_MS;`
- `use` `codex-rs/core/src/tools/spec.rs:12` `use crate::tools::handlers::request_user_input_tool_description;`
- `use` `codex-rs/core/src/tools/spec.rs:13` `use crate::tools::registry::ToolRegistryBuilder;`
- `use` `codex-rs/core/src/tools/spec.rs:14` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/core/src/tools/spec.rs:15` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/core/src/tools/spec.rs:16` `use codex_protocol::models::VIEW_IMAGE_TOOL_NAME;`
- `use` `codex-rs/core/src/tools/spec.rs:17` `use codex_protocol::openai_models::ApplyPatchToolType;`
- `use` `codex-rs/core/src/tools/spec.rs:18` `use codex_protocol::openai_models::ConfigShellToolType;`
- `use` `codex-rs/core/src/tools/spec.rs:19` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/tools/spec.rs:20` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/spec.rs:21` `use serde::Serialize;`
- `use` `codex-rs/core/src/tools/spec.rs:22` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/core/src/tools/spec.rs:23` `use serde_json::json;`
- `use` `codex-rs/core/src/tools/spec.rs:24` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/tools/spec.rs:25` `use std::collections::HashMap;`
- `impl` `codex-rs/core/src/tools/spec.rs:45` `impl ToolsConfig {`
- `fn` `codex-rs/core/src/tools/spec.rs:46` `pub fn new(params: &ToolsConfigParams) -> Self {`
- `enum` `codex-rs/core/src/tools/spec.rs:99` `pub enum JsonSchema {`
- `enum` `codex-rs/core/src/tools/spec.rs:135` `pub enum AdditionalProperties {`
- `impl` `codex-rs/core/src/tools/spec.rs:140` `impl From<bool> for AdditionalProperties {`
- `fn` `codex-rs/core/src/tools/spec.rs:141` `fn from(b: bool) -> Self {`
- `impl` `codex-rs/core/src/tools/spec.rs:146` `impl From<JsonSchema> for AdditionalProperties {`
- `fn` `codex-rs/core/src/tools/spec.rs:147` `fn from(s: JsonSchema) -> Self {`
- `fn` `codex-rs/core/src/tools/spec.rs:152` `fn create_approval_parameters(include_prefix_rule: bool) -> BTreeMap<String, JsonSchema> {`
- `fn` `codex-rs/core/src/tools/spec.rs:194` `fn create_exec_command_tool(include_prefix_rule: bool) -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:268` `fn create_write_stdin_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:315` `fn create_shell_tool(include_prefix_rule: bool) -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:368` `fn create_shell_command_tool(include_prefix_rule: bool) -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:430` `fn create_view_image_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:452` `fn create_spawn_agent_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:487` `fn create_send_input_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:525` `fn create_resume_agent_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:548` `fn create_wait_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:582` `fn create_request_user_input_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:663` `fn create_get_memory_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:685` `fn create_close_agent_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:707` `fn create_test_sync_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:774` `fn create_grep_files_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:825` `fn create_read_file_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:928` `fn create_list_dir_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:974` `fn create_list_mcp_resources_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:1008` `fn create_list_mcp_resource_templates_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:1042` `fn create_read_mcp_resource_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:1086` `pub fn create_tools_json_for_responses_api(`
- `fn` `codex-rs/core/src/tools/spec.rs:1139` `fn dynamic_tool_to_openai_tool(`
- `fn` `codex-rs/core/src/tools/spec.rs:1153` `pub fn parse_tool_input_schema(input_schema: &JsonValue) -> Result<JsonSchema, serde_json::Error> {`
- `fn` `codex-rs/core/src/tools/spec.rs:1166` `fn sanitize_json_schema(value: &mut JsonValue) {`
- `use` `codex-rs/core/src/tools/spec.rs:1276` `use crate::tools::handlers::ApplyPatchHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1277` `use crate::tools::handlers::CollabHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1278` `use crate::tools::handlers::DynamicToolHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1279` `use crate::tools::handlers::GetMemoryHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1280` `use crate::tools::handlers::GrepFilesHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1281` `use crate::tools::handlers::ListDirHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1282` `use crate::tools::handlers::McpHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1283` `use crate::tools::handlers::McpResourceHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1284` `use crate::tools::handlers::PlanHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1285` `use crate::tools::handlers::ReadFileHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1286` `use crate::tools::handlers::RequestUserInputHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1287` `use crate::tools::handlers::ShellCommandHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1288` `use crate::tools::handlers::ShellHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1289` `use crate::tools::handlers::TestSyncHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1290` `use crate::tools::handlers::UnifiedExecHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1291` `use crate::tools::handlers::ViewImageHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1292` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/spec.rs:1485` `use crate::client_common::tools::FreeformTool;`
- `use` `codex-rs/core/src/tools/spec.rs:1486` `use crate::config::test_config;`
- `use` `codex-rs/core/src/tools/spec.rs:1487` `use crate::models_manager::manager::ModelsManager;`
- `use` `codex-rs/core/src/tools/spec.rs:1488` `use crate::tools::registry::ConfiguredToolSpec;`
- `use` `codex-rs/core/src/tools/spec.rs:1489` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/spec.rs:1491` `use super::*;`
- `fn` `codex-rs/core/src/tools/spec.rs:1493` `fn mcp_tool(`
- `fn` `codex-rs/core/src/tools/spec.rs:1511` `fn mcp_tool_to_openai_tool_inserts_empty_properties() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1533` `fn tool_name(tool: &ToolSpec) -> &str {`
- `fn` `codex-rs/core/src/tools/spec.rs:1543` `fn assert_contains_tool_names(tools: &[ConfiguredToolSpec], expected_subset: &[&str]) {`
- `use` `codex-rs/core/src/tools/spec.rs:1544` `use std::collections::HashSet;`
- `fn` `codex-rs/core/src/tools/spec.rs:1564` `fn shell_tool_name(config: &ToolsConfig) -> Option<&'static str> {`
- `fn` `codex-rs/core/src/tools/spec.rs:1584` `fn strip_descriptions_schema(schema: &mut JsonSchema) {`
- `fn` `codex-rs/core/src/tools/spec.rs:1610` `fn strip_descriptions_tool(spec: &mut ToolSpec) {`
- `fn` `codex-rs/core/src/tools/spec.rs:1620` `fn test_full_toolset_specs_for_gpt5_codex_unified_exec_web_search() {`
- `use` `codex-rs/core/src/tools/spec.rs:1634` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/tools/spec.rs:1635` `use std::collections::HashSet;`
- `fn` `codex-rs/core/src/tools/spec.rs:1684` `fn test_build_specs_collab_tools_enabled() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1709` `fn request_user_input_requires_collaboration_modes_feature() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1736` `fn get_memory_requires_memory_tool_feature() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1762` `fn assert_model_tools(`
- `fn` `codex-rs/core/src/tools/spec.rs:1780` `fn assert_default_model_tools(`
- `fn` `codex-rs/core/src/tools/spec.rs:1797` `fn web_search_mode_cached_sets_external_web_access_false() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1819` `fn web_search_mode_live_sets_external_web_access_true() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1841` `fn test_build_specs_gpt5_codex_default() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1863` `fn test_build_specs_gpt51_codex_default() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1885` `fn test_build_specs_gpt5_codex_unified_exec_web_search() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1909` `fn test_build_specs_gpt51_codex_unified_exec_web_search() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1933` `fn test_codex_mini_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1954` `fn test_codex_5_1_mini_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1976` `fn test_gpt_5_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1997` `fn test_gpt_5_1_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2019` `fn test_exp_5_1_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2042` `fn test_codex_mini_unified_exec_web_search() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2065` `fn test_build_specs_default_shell_present() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2087` `fn test_parallel_support_flags() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2107` `fn test_test_model_info_includes_sync_tool() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2137` `fn test_build_specs_mcp_tools_converted() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2222` `fn test_build_specs_mcp_tools_sorted_by_name() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2266` `fn test_mcp_tool_property_missing_type_defaults_to_string() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2318` `fn test_mcp_tool_integer_normalized_to_number() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2366` `fn test_mcp_tool_array_without_items_gets_default_string_items() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2418` `fn test_mcp_tool_anyof_defaults_to_string() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2468` `fn test_shell_tool() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2498` `fn test_shell_command_tool() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2527` `fn test_get_openai_tools_mcp_tools_with_additional_properties_schema() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2629` `fn chat_tools_include_top_level_name() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::agent::AgentRole;`
- `use crate::client_common::tools::ResponsesApiTool;`
- `use crate::client_common::tools::ToolSpec;`
- `use crate::features::Feature;`
- `use crate::features::Features;`
- `use crate::tools::handlers::PLAN_TOOL;`
- `use crate::tools::handlers::apply_patch::create_apply_patch_freeform_tool;`
- `use crate::tools::handlers::apply_patch::create_apply_patch_json_tool;`
- `use crate::tools::handlers::collab::DEFAULT_WAIT_TIMEOUT_MS;`
- `use crate::tools::handlers::collab::MAX_WAIT_TIMEOUT_MS;`
- `use crate::tools::handlers::collab::MIN_WAIT_TIMEOUT_MS;`
- `use crate::tools::handlers::request_user_input_tool_description;`
- `use crate::tools::registry::ToolRegistryBuilder;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use codex_protocol::models::VIEW_IMAGE_TOOL_NAME;`
- `use codex_protocol::openai_models::ApplyPatchToolType;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use serde::Deserialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
