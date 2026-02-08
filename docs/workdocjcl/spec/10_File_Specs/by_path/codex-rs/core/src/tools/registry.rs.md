# `codex-rs/core/src/tools/registry.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7610`
- sha256: `23fb60719686346223c6d307ff58ba9f72b5a0d1d87d506790b1fe0556fbaffd`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/registry.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ToolKind {`
- `pub trait ToolHandler: Send + Sync {`
- `pub struct ToolRegistry {`
- `pub fn new(handlers: HashMap<String, Arc<dyn ToolHandler>>) -> Self {`
- `pub fn handler(&self, name: &str) -> Option<Arc<dyn ToolHandler>> {`
- `pub struct ConfiguredToolSpec {`
- `pub fn new(spec: ToolSpec, supports_parallel_tool_calls: bool) -> Self {`
- `pub struct ToolRegistryBuilder {`
- `pub fn new() -> Self {`
- `pub fn push_spec(&mut self, spec: ToolSpec) {`
- `pub fn push_spec_with_parallel_support(`
- `pub fn register_handler(&mut self, name: impl Into<String>, handler: Arc<dyn ToolHandler>) {`
- `pub fn build(self) -> (Vec<ConfiguredToolSpec>, ToolRegistry) {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/registry.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/registry.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/registry.rs:3` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/registry.rs:5` `use crate::client_common::tools::ToolSpec;`
- `use` `codex-rs/core/src/tools/registry.rs:6` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/registry.rs:7` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/registry.rs:8` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/registry.rs:9` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/registry.rs:10` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/registry.rs:11` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/tools/registry.rs:12` `use codex_utils_readiness::Readiness;`
- `use` `codex-rs/core/src/tools/registry.rs:13` `use tracing::warn;`
- `enum` `codex-rs/core/src/tools/registry.rs:16` `pub enum ToolKind {`
- `trait` `codex-rs/core/src/tools/registry.rs:22` `pub trait ToolHandler: Send + Sync {`
- `fn` `codex-rs/core/src/tools/registry.rs:23` `fn kind(&self) -> ToolKind;`
- `fn` `codex-rs/core/src/tools/registry.rs:25` `fn matches_kind(&self, payload: &ToolPayload) -> bool {`
- `fn` `codex-rs/core/src/tools/registry.rs:37` `async fn is_mutating(&self, _invocation: &ToolInvocation) -> bool {`
- `fn` `codex-rs/core/src/tools/registry.rs:43` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError>;`
- `struct` `codex-rs/core/src/tools/registry.rs:46` `pub struct ToolRegistry {`
- `impl` `codex-rs/core/src/tools/registry.rs:50` `impl ToolRegistry {`
- `fn` `codex-rs/core/src/tools/registry.rs:51` `pub fn new(handlers: HashMap<String, Arc<dyn ToolHandler>>) -> Self {`
- `fn` `codex-rs/core/src/tools/registry.rs:55` `pub fn handler(&self, name: &str) -> Option<Arc<dyn ToolHandler>> {`
- `fn` `codex-rs/core/src/tools/registry.rs:67` `pub async fn dispatch(`
- `struct` `codex-rs/core/src/tools/registry.rs:153` `pub struct ConfiguredToolSpec {`
- `impl` `codex-rs/core/src/tools/registry.rs:158` `impl ConfiguredToolSpec {`
- `fn` `codex-rs/core/src/tools/registry.rs:159` `pub fn new(spec: ToolSpec, supports_parallel_tool_calls: bool) -> Self {`
- `struct` `codex-rs/core/src/tools/registry.rs:167` `pub struct ToolRegistryBuilder {`
- `impl` `codex-rs/core/src/tools/registry.rs:172` `impl ToolRegistryBuilder {`
- `fn` `codex-rs/core/src/tools/registry.rs:173` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/tools/registry.rs:180` `pub fn push_spec(&mut self, spec: ToolSpec) {`
- `fn` `codex-rs/core/src/tools/registry.rs:184` `pub fn push_spec_with_parallel_support(`
- `fn` `codex-rs/core/src/tools/registry.rs:193` `pub fn register_handler(&mut self, name: impl Into<String>, handler: Arc<dyn ToolHandler>) {`
- `fn` `codex-rs/core/src/tools/registry.rs:222` `pub fn build(self) -> (Vec<ConfiguredToolSpec>, ToolRegistry) {`
- `fn` `codex-rs/core/src/tools/registry.rs:228` `fn unsupported_tool_call_message(payload: &ToolPayload, tool_name: &str) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use crate::client_common::tools::ToolSpec;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use async_trait::async_trait;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_utils_readiness::Readiness;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
