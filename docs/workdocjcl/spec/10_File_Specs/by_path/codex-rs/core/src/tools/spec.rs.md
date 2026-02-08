# `codex-rs/core/src/tools/spec.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `95265`
- sha256: `279d12d63fb9cb4fc6fe48390b8bf589ff0f3876b4a6b77d48ece756c1c196d5`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/tools/spec.rs:12` `use crate::tools::registry::ToolRegistryBuilder;`
- `use` `codex-rs/core/src/tools/spec.rs:13` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/core/src/tools/spec.rs:14` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/core/src/tools/spec.rs:15` `use codex_protocol::models::VIEW_IMAGE_TOOL_NAME;`
- `use` `codex-rs/core/src/tools/spec.rs:16` `use codex_protocol::openai_models::ApplyPatchToolType;`
- `use` `codex-rs/core/src/tools/spec.rs:17` `use codex_protocol::openai_models::ConfigShellToolType;`
- `use` `codex-rs/core/src/tools/spec.rs:18` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/tools/spec.rs:19` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/spec.rs:20` `use serde::Serialize;`
- `use` `codex-rs/core/src/tools/spec.rs:21` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/core/src/tools/spec.rs:22` `use serde_json::json;`
- `use` `codex-rs/core/src/tools/spec.rs:23` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/tools/spec.rs:24` `use std::collections::HashMap;`
- `impl` `codex-rs/core/src/tools/spec.rs:43` `impl ToolsConfig {`
- `fn` `codex-rs/core/src/tools/spec.rs:44` `pub fn new(params: &ToolsConfigParams) -> Self {`
- `enum` `codex-rs/core/src/tools/spec.rs:95` `pub enum JsonSchema {`
- `enum` `codex-rs/core/src/tools/spec.rs:131` `pub enum AdditionalProperties {`
- `impl` `codex-rs/core/src/tools/spec.rs:136` `impl From<bool> for AdditionalProperties {`
- `fn` `codex-rs/core/src/tools/spec.rs:137` `fn from(b: bool) -> Self {`
- `impl` `codex-rs/core/src/tools/spec.rs:142` `impl From<JsonSchema> for AdditionalProperties {`
- `fn` `codex-rs/core/src/tools/spec.rs:143` `fn from(s: JsonSchema) -> Self {`
- `fn` `codex-rs/core/src/tools/spec.rs:148` `fn create_approval_parameters(include_prefix_rule: bool) -> BTreeMap<String, JsonSchema> {`
- `fn` `codex-rs/core/src/tools/spec.rs:190` `fn create_exec_command_tool(include_prefix_rule: bool) -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:264` `fn create_write_stdin_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:311` `fn create_shell_tool(include_prefix_rule: bool) -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:364` `fn create_shell_command_tool(include_prefix_rule: bool) -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:426` `fn create_view_image_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:448` `fn create_spawn_agent_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:483` `fn create_send_input_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:521` `fn create_wait_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:555` `fn create_request_user_input_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:638` `fn create_close_agent_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:660` `fn create_test_sync_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:727` `fn create_grep_files_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:778` `fn create_read_file_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:881` `fn create_list_dir_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:927` `fn create_list_mcp_resources_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:961` `fn create_list_mcp_resource_templates_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:995` `fn create_read_mcp_resource_tool() -> ToolSpec {`
- `fn` `codex-rs/core/src/tools/spec.rs:1039` `pub fn create_tools_json_for_responses_api(`
- `fn` `codex-rs/core/src/tools/spec.rs:1128` `fn dynamic_tool_to_openai_tool(`
- `fn` `codex-rs/core/src/tools/spec.rs:1142` `pub fn parse_tool_input_schema(input_schema: &JsonValue) -> Result<JsonSchema, serde_json::Error> {`
- `fn` `codex-rs/core/src/tools/spec.rs:1155` `fn sanitize_json_schema(value: &mut JsonValue) {`
- `use` `codex-rs/core/src/tools/spec.rs:1265` `use crate::tools::handlers::ApplyPatchHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1266` `use crate::tools::handlers::CollabHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1267` `use crate::tools::handlers::DynamicToolHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1268` `use crate::tools::handlers::GrepFilesHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1269` `use crate::tools::handlers::ListDirHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1270` `use crate::tools::handlers::McpHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1271` `use crate::tools::handlers::McpResourceHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1272` `use crate::tools::handlers::PlanHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1273` `use crate::tools::handlers::ReadFileHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1274` `use crate::tools::handlers::RequestUserInputHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1275` `use crate::tools::handlers::ShellCommandHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1276` `use crate::tools::handlers::ShellHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1277` `use crate::tools::handlers::TestSyncHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1278` `use crate::tools::handlers::UnifiedExecHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1279` `use crate::tools::handlers::ViewImageHandler;`
- `use` `codex-rs/core/src/tools/spec.rs:1280` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/spec.rs:1456` `use crate::client_common::tools::FreeformTool;`
- `use` `codex-rs/core/src/tools/spec.rs:1457` `use crate::config::test_config;`
- `use` `codex-rs/core/src/tools/spec.rs:1458` `use crate::models_manager::manager::ModelsManager;`
- `use` `codex-rs/core/src/tools/spec.rs:1459` `use crate::tools::registry::ConfiguredToolSpec;`
- `use` `codex-rs/core/src/tools/spec.rs:1460` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/spec.rs:1462` `use super::*;`
- `fn` `codex-rs/core/src/tools/spec.rs:1464` `fn mcp_tool(`
- `fn` `codex-rs/core/src/tools/spec.rs:1482` `fn mcp_tool_to_openai_tool_inserts_empty_properties() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1504` `fn tool_name(tool: &ToolSpec) -> &str {`
- `fn` `codex-rs/core/src/tools/spec.rs:1514` `fn assert_contains_tool_names(tools: &[ConfiguredToolSpec], expected_subset: &[&str]) {`
- `use` `codex-rs/core/src/tools/spec.rs:1515` `use std::collections::HashSet;`
- `fn` `codex-rs/core/src/tools/spec.rs:1535` `fn shell_tool_name(config: &ToolsConfig) -> Option<&'static str> {`
- `fn` `codex-rs/core/src/tools/spec.rs:1555` `fn strip_descriptions_schema(schema: &mut JsonSchema) {`
- `fn` `codex-rs/core/src/tools/spec.rs:1581` `fn strip_descriptions_tool(spec: &mut ToolSpec) {`
- `fn` `codex-rs/core/src/tools/spec.rs:1591` `fn test_full_toolset_specs_for_gpt5_codex_unified_exec_web_search() {`
- `use` `codex-rs/core/src/tools/spec.rs:1605` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/tools/spec.rs:1606` `use std::collections::HashSet;`
- `fn` `codex-rs/core/src/tools/spec.rs:1655` `fn test_build_specs_collab_tools_enabled() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1674` `fn request_user_input_requires_collaboration_modes_feature() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1700` `fn assert_model_tools(`
- `fn` `codex-rs/core/src/tools/spec.rs:1719` `fn web_search_mode_cached_sets_external_web_access_false() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1741` `fn web_search_mode_live_sets_external_web_access_true() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1763` `fn test_build_specs_gpt5_codex_default() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1785` `fn test_build_specs_gpt51_codex_default() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1807` `fn test_build_specs_gpt5_codex_unified_exec_web_search() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1831` `fn test_build_specs_gpt51_codex_unified_exec_web_search() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1855` `fn test_codex_mini_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1876` `fn test_codex_5_1_mini_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1898` `fn test_gpt_5_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1919` `fn test_gpt_5_1_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1941` `fn test_exp_5_1_defaults() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1964` `fn test_codex_mini_unified_exec_web_search() {`
- `fn` `codex-rs/core/src/tools/spec.rs:1987` `fn test_build_specs_default_shell_present() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2009` `fn test_parallel_support_flags() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2029` `fn test_test_model_info_includes_sync_tool() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2059` `fn test_build_specs_mcp_tools_converted() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2144` `fn test_build_specs_mcp_tools_sorted_by_name() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2188` `fn test_mcp_tool_property_missing_type_defaults_to_string() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2240` `fn test_mcp_tool_integer_normalized_to_number() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2288` `fn test_mcp_tool_array_without_items_gets_default_string_items() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2340` `fn test_mcp_tool_anyof_defaults_to_string() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2390` `fn test_shell_tool() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2420` `fn test_shell_command_tool() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2449` `fn test_get_openai_tools_mcp_tools_with_additional_properties_schema() {`
- `fn` `codex-rs/core/src/tools/spec.rs:2551` `fn chat_tools_include_top_level_name() {`

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
- `use crate::tools::registry::ToolRegistryBuilder;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use codex_protocol::models::VIEW_IMAGE_TOOL_NAME;`
- `use codex_protocol::openai_models::ApplyPatchToolType;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
