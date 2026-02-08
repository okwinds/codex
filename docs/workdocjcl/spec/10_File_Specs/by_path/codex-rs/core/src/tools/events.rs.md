# `codex-rs/core/src/tools/events.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14643`
- sha256: `527cdc06a7f73904d8343c16962f1be958b77d79a0a09dac6ef21b0af4621e0d`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/events.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn new(`
- `pub fn shell(`
- `pub fn apply_patch(changes: HashMap<PathBuf, FileChange>, auto_approved: bool) -> Self {`
- `pub fn unified_exec(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/events.rs:1` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/events.rs:2` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/events.rs:3` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/tools/events.rs:4` `use crate::error::SandboxErr;`
- `use` `codex-rs/core/src/tools/events.rs:5` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/tools/events.rs:6` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/events.rs:7` `use crate::parse_command::parse_command;`
- `use` `codex-rs/core/src/tools/events.rs:8` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tools/events.rs:9` `use crate::protocol::ExecCommandBeginEvent;`
- `use` `codex-rs/core/src/tools/events.rs:10` `use crate::protocol::ExecCommandEndEvent;`
- `use` `codex-rs/core/src/tools/events.rs:11` `use crate::protocol::ExecCommandSource;`
- `use` `codex-rs/core/src/tools/events.rs:12` `use crate::protocol::FileChange;`
- `use` `codex-rs/core/src/tools/events.rs:13` `use crate::protocol::PatchApplyBeginEvent;`
- `use` `codex-rs/core/src/tools/events.rs:14` `use crate::protocol::PatchApplyEndEvent;`
- `use` `codex-rs/core/src/tools/events.rs:15` `use crate::protocol::TurnDiffEvent;`
- `use` `codex-rs/core/src/tools/events.rs:16` `use crate::tools::context::SharedTurnDiffTracker;`
- `use` `codex-rs/core/src/tools/events.rs:17` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/events.rs:18` `use codex_protocol::parse_command::ParsedCommand;`
- `use` `codex-rs/core/src/tools/events.rs:19` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/events.rs:20` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/events.rs:21` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/events.rs:22` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/events.rs:24` `use super::format_exec_output_str;`
- `impl` `codex-rs/core/src/tools/events.rs:34` `impl<'a> ToolEventCtx<'a> {`
- `fn` `codex-rs/core/src/tools/events.rs:35` `pub fn new(`
- `impl` `codex-rs/core/src/tools/events.rs:108` `impl ToolEmitter {`
- `fn` `codex-rs/core/src/tools/events.rs:109` `pub fn shell(`
- `fn` `codex-rs/core/src/tools/events.rs:125` `pub fn apply_patch(changes: HashMap<PathBuf, FileChange>, auto_approved: bool) -> Self {`
- `fn` `codex-rs/core/src/tools/events.rs:132` `pub fn unified_exec(`
- `fn` `codex-rs/core/src/tools/events.rs:148` `pub async fn emit(&self, ctx: ToolEventCtx<'_>, stage: ToolEventStage) {`
- `fn` `codex-rs/core/src/tools/events.rs:254` `pub async fn begin(&self, ctx: ToolEventCtx<'_>) {`
- `fn` `codex-rs/core/src/tools/events.rs:258` `fn format_exec_output_for_model(`
- `fn` `codex-rs/core/src/tools/events.rs:271` `pub async fn finish(`
- `struct` `codex-rs/core/src/tools/events.rs:324` `struct ExecCommandInput<'a> {`
- `impl` `codex-rs/core/src/tools/events.rs:333` `impl<'a> ExecCommandInput<'a> {`
- `fn` `codex-rs/core/src/tools/events.rs:334` `fn new(`
- `struct` `codex-rs/core/src/tools/events.rs:353` `struct ExecCommandResult {`
- `fn` `codex-rs/core/src/tools/events.rs:362` `async fn emit_exec_stage(`
- `fn` `codex-rs/core/src/tools/events.rs:407` `async fn emit_exec_end(`
- `fn` `codex-rs/core/src/tools/events.rs:435` `async fn emit_patch_end(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::error::CodexErr;`
- `use crate::error::SandboxErr;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::parse_command::parse_command;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::ExecCommandBeginEvent;`
- `use crate::protocol::ExecCommandEndEvent;`
- `use crate::protocol::ExecCommandSource;`
- `use crate::protocol::FileChange;`
- `use crate::protocol::PatchApplyBeginEvent;`
- `use crate::protocol::PatchApplyEndEvent;`
- `use crate::protocol::TurnDiffEvent;`
- `use crate::tools::context::SharedTurnDiffTracker;`
- `use crate::tools::sandboxing::ToolError;`
- `use codex_protocol::parse_command::ParsedCommand;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
