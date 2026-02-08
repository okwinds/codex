# `codex-rs/core/src/tools/handlers/plan.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4310`
- sha256: `cdb676ac23ec2211fa30f6a5c7f9bde970f8b5e2acf56dcb22e18eddca2574ed`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/plan.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PlanHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/plan.rs:1` `use crate::client_common::tools::ResponsesApiTool;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:2` `use crate::client_common::tools::ToolSpec;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:3` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:4` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:5` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:6` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:7` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:8` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:9` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:10` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:11` `use crate::tools::spec::JsonSchema;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:12` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:13` `use codex_protocol::config_types::ModeKind;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:14` `use codex_protocol::plan_tool::UpdatePlanArgs;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:15` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:16` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/tools/handlers/plan.rs:17` `use std::sync::LazyLock;`
- `struct` `codex-rs/core/src/tools/handlers/plan.rs:19` `pub struct PlanHandler;`
- `static` `codex-rs/core/src/tools/handlers/plan.rs:21` `pub static PLAN_TOOL: LazyLock<ToolSpec> = LazyLock::new(|| {`
- `impl` `codex-rs/core/src/tools/handlers/plan.rs:64` `impl ToolHandler for PlanHandler {`
- `fn` `codex-rs/core/src/tools/handlers/plan.rs:65` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/plan.rs:69` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/plan.rs:119` `fn parse_update_plan_arguments(arguments: &str) -> Result<UpdatePlanArgs, FunctionCallError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::client_common::tools::ResponsesApiTool;`
- `use crate::client_common::tools::ToolSpec;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use crate::tools::spec::JsonSchema;`
- `use async_trait::async_trait;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::plan_tool::UpdatePlanArgs;`
- `use codex_protocol::protocol::EventMsg;`
- `use std::collections::BTreeMap;`
- `use std::sync::LazyLock;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
