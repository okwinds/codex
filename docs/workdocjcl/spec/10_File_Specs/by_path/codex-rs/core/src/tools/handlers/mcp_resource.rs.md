# `codex-rs/core/src/tools/handlers/mcp_resource.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `24425`
- sha256: `7071114cd915ece5f9c9a836e3529df27e2316543cb231ebaca782dd85fc4e10`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/mcp_resource.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct McpResourceHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:1` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:2` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:4` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:5` `use std::time::Instant;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:7` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:8` `use codex_protocol::mcp::CallToolResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:9` `use rmcp::model::ListResourceTemplatesResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:10` `use rmcp::model::ListResourcesResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:11` `use rmcp::model::PaginatedRequestParam;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:12` `use rmcp::model::ReadResourceRequestParam;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:13` `use rmcp::model::ReadResourceResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:14` `use rmcp::model::Resource;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:15` `use rmcp::model::ResourceTemplate;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:16` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:17` `use serde::Serialize;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:18` `use serde::de::DeserializeOwned;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:19` `use serde_json::Value;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:21` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:22` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:23` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:24` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:25` `use crate::protocol::McpInvocation;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:26` `use crate::protocol::McpToolCallBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:27` `use crate::protocol::McpToolCallEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:28` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:29` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:30` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:31` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:32` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:34` `pub struct McpResourceHandler;`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:37` `struct ListResourcesArgs {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:46` `struct ListResourceTemplatesArgs {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:55` `struct ReadResourceArgs {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:61` `struct ResourceWithServer {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:67` `impl ResourceWithServer {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:68` `fn new(server: String, resource: Resource) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:74` `struct ResourceTemplateWithServer {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:80` `impl ResourceTemplateWithServer {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:81` `fn new(server: String, template: ResourceTemplate) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:88` `struct ListResourcesPayload {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:96` `impl ListResourcesPayload {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:97` `fn from_single_server(server: String, result: ListResourcesResult) -> Self {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:110` `fn from_all_servers(resources_by_server: HashMap<String, Vec<Resource>>) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:131` `struct ListResourceTemplatesPayload {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:139` `impl ListResourceTemplatesPayload {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:140` `fn from_single_server(server: String, result: ListResourceTemplatesResult) -> Self {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:153` `fn from_all_servers(templates_by_server: HashMap<String, Vec<ResourceTemplate>>) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:174` `struct ReadResourcePayload {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:182` `impl ToolHandler for McpResourceHandler {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:183` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:187` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:243` `async fn handle_list_resources(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:348` `async fn handle_list_resource_templates(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:455` `async fn handle_read_resource(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:542` `fn call_tool_result_from_content(content: &str, success: Option<bool>) -> CallToolResult {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:551` `async fn emit_tool_call_begin(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:568` `async fn emit_tool_call_end(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:589` `fn normalize_optional_string(input: Option<String>) -> Option<String> {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:600` `fn normalize_required_string(field: &str, value: String) -> Result<String, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:625` `fn parse_arguments(raw_args: &str) -> Result<Option<Value>, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:666` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:667` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:668` `use rmcp::model::AnnotateAble;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:669` `use serde_json::json;`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:671` `fn resource(uri: &str, name: &str) -> Resource {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:685` `fn template(uri_template: &str, name: &str) -> ResourceTemplate {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:697` `fn resource_with_server_serializes_server_field() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:707` `fn list_resources_payload_from_single_server_copies_next_cursor() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:724` `fn list_resources_payload_from_all_servers_is_sorted() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:752` `fn call_tool_result_from_content_marks_success() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:759` `fn parse_arguments_handles_empty_and_json() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:777` `fn template_with_server_serializes_server_field() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use async_trait::async_trait;`
- `use codex_protocol::mcp::CallToolResult;`
- `use rmcp::model::ListResourceTemplatesResult;`
- `use rmcp::model::ListResourcesResult;`
- `use rmcp::model::PaginatedRequestParam;`
- `use rmcp::model::ReadResourceRequestParam;`
- `use rmcp::model::ReadResourceResult;`
- `use rmcp::model::Resource;`
- `use rmcp::model::ResourceTemplate;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde::de::DeserializeOwned;`
- `use serde_json::Value;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
