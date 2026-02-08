# `codex-rs/core/src/tools/handlers/mcp_resource.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `24342`
- sha256: `6e76ff42d3b381aa1fbef524587391fa7521109b191e4d17fd1e1d2880c57d05`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:3` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:4` `use std::time::Instant;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:6` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:7` `use codex_protocol::mcp::CallToolResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:8` `use rmcp::model::ListResourceTemplatesResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:9` `use rmcp::model::ListResourcesResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:10` `use rmcp::model::PaginatedRequestParam;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:11` `use rmcp::model::ReadResourceRequestParam;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:12` `use rmcp::model::ReadResourceResult;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:13` `use rmcp::model::Resource;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:14` `use rmcp::model::ResourceTemplate;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:15` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:16` `use serde::Serialize;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:17` `use serde::de::DeserializeOwned;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:18` `use serde_json::Value;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:20` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:21` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:22` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:23` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:24` `use crate::protocol::McpInvocation;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:25` `use crate::protocol::McpToolCallBeginEvent;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:26` `use crate::protocol::McpToolCallEndEvent;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:27` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:28` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:29` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:30` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:31` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:33` `pub struct McpResourceHandler;`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:36` `struct ListResourcesArgs {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:45` `struct ListResourceTemplatesArgs {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:54` `struct ReadResourceArgs {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:60` `struct ResourceWithServer {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:66` `impl ResourceWithServer {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:67` `fn new(server: String, resource: Resource) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:73` `struct ResourceTemplateWithServer {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:79` `impl ResourceTemplateWithServer {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:80` `fn new(server: String, template: ResourceTemplate) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:87` `struct ListResourcesPayload {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:95` `impl ListResourcesPayload {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:96` `fn from_single_server(server: String, result: ListResourcesResult) -> Self {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:109` `fn from_all_servers(resources_by_server: HashMap<String, Vec<Resource>>) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:130` `struct ListResourceTemplatesPayload {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:138` `impl ListResourceTemplatesPayload {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:139` `fn from_single_server(server: String, result: ListResourceTemplatesResult) -> Self {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:152` `fn from_all_servers(templates_by_server: HashMap<String, Vec<ResourceTemplate>>) -> Self {`
- `struct` `codex-rs/core/src/tools/handlers/mcp_resource.rs:173` `struct ReadResourcePayload {`
- `impl` `codex-rs/core/src/tools/handlers/mcp_resource.rs:181` `impl ToolHandler for McpResourceHandler {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:182` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:186` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:242` `async fn handle_list_resources(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:349` `async fn handle_list_resource_templates(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:458` `async fn handle_read_resource(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:547` `fn call_tool_result_from_content(content: &str, success: Option<bool>) -> CallToolResult {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:556` `async fn emit_tool_call_begin(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:573` `async fn emit_tool_call_end(`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:594` `fn normalize_optional_string(input: Option<String>) -> Option<String> {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:605` `fn normalize_required_string(field: &str, value: String) -> Result<String, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:631` `fn parse_arguments(raw_args: &str) -> Result<Option<Value>, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:672` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:673` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:674` `use rmcp::model::AnnotateAble;`
- `use` `codex-rs/core/src/tools/handlers/mcp_resource.rs:675` `use serde_json::json;`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:677` `fn resource(uri: &str, name: &str) -> Resource {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:691` `fn template(uri_template: &str, name: &str) -> ResourceTemplate {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:703` `fn resource_with_server_serializes_server_field() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:713` `fn list_resources_payload_from_single_server_copies_next_cursor() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:730` `fn list_resources_payload_from_all_servers_is_sorted() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:758` `fn call_tool_result_from_content_marks_success() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:765` `fn parse_arguments_handles_empty_and_json() {`
- `fn` `codex-rs/core/src/tools/handlers/mcp_resource.rs:783` `fn template_with_server_serializes_server_field() {`

## Dependencies (auto sample)
### Imports / Includes
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
- `use crate::function_tool::FunctionCallError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
