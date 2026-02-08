# `codex-rs/core/src/tools/handlers/apply_patch.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `16203`
- sha256: `b1457e5e561bc6d9394ae44d395e4b99c190d353a7538492a1822328b7cb5409`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/apply_patch.rs` (read)

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct ApplyPatchHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:1` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:2` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:4` `use crate::apply_patch;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:5` `use crate::apply_patch::InternalApplyPatchInvocation;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:6` `use crate::apply_patch::convert_apply_patch_to_protocol;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:7` `use crate::client_common::tools::FreeformTool;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:8` `use crate::client_common::tools::FreeformToolFormat;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:9` `use crate::client_common::tools::ResponsesApiTool;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:10` `use crate::client_common::tools::ToolSpec;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:11` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:12` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:13` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:14` `use crate::tools::context::SharedTurnDiffTracker;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:15` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:16` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:17` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:18` `use crate::tools::events::ToolEmitter;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:19` `use crate::tools::events::ToolEventCtx;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:20` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:21` `use crate::tools::orchestrator::ToolOrchestrator;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:22` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:23` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:24` `use crate::tools::runtimes::apply_patch::ApplyPatchRequest;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:25` `use crate::tools::runtimes::apply_patch::ApplyPatchRuntime;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:26` `use crate::tools::sandboxing::ToolCtx;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:27` `use crate::tools::spec::ApplyPatchToolArgs;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:28` `use crate::tools::spec::JsonSchema;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:29` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:30` `use codex_apply_patch::ApplyPatchAction;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:31` `use codex_apply_patch::ApplyPatchFileChange;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:32` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `struct` `codex-rs/core/src/tools/handlers/apply_patch.rs:34` `pub struct ApplyPatchHandler;`
- `const` `codex-rs/core/src/tools/handlers/apply_patch.rs:36` `const APPLY_PATCH_LARK_GRAMMAR: &str = include_str!("tool_apply_patch.lark");`
- `fn` `codex-rs/core/src/tools/handlers/apply_patch.rs:38` `fn file_paths_for_action(action: &ApplyPatchAction) -> Vec<AbsolutePathBuf> {`
- `fn` `codex-rs/core/src/tools/handlers/apply_patch.rs:58` `fn to_abs_path(cwd: &Path, path: &Path) -> Option<AbsolutePathBuf> {`
- `impl` `codex-rs/core/src/tools/handlers/apply_patch.rs:63` `impl ToolHandler for ApplyPatchHandler {`
- `fn` `codex-rs/core/src/tools/handlers/apply_patch.rs:64` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/apply_patch.rs:68` `fn matches_kind(&self, payload: &ToolPayload) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/apply_patch.rs:75` `async fn is_mutating(&self, _invocation: &ToolInvocation) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/apply_patch.rs:79` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:371` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:372` `use codex_apply_patch::MaybeApplyPatchVerified;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:373` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/apply_patch.rs:374` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/tools/handlers/apply_patch.rs:377` `fn approval_keys_include_move_destination() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::path::Path;`
- `use crate::apply_patch;`
- `use crate::apply_patch::InternalApplyPatchInvocation;`
- `use crate::apply_patch::convert_apply_patch_to_protocol;`
- `use crate::client_common::tools::FreeformTool;`
- `use crate::client_common::tools::FreeformToolFormat;`
- `use crate::client_common::tools::ResponsesApiTool;`
- `use crate::client_common::tools::ToolSpec;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::SharedTurnDiffTracker;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::events::ToolEmitter;`
- `use crate::tools::events::ToolEventCtx;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::orchestrator::ToolOrchestrator;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
