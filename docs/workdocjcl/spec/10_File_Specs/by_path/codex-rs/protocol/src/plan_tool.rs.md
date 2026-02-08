# `codex-rs/protocol/src/plan_tool.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `801`
- sha256: `0a5482699b191fbeeb8f58790b62f6b331b64e29a38b3286a669aff4c699fdd9`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/plan_tool.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum StepStatus {`
- `pub struct PlanItemArg {`
- `pub struct UpdatePlanArgs {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/plan_tool.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/plan_tool.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/plan_tool.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/plan_tool.rs:4` `use ts_rs::TS;`
- `enum` `codex-rs/protocol/src/plan_tool.rs:9` `pub enum StepStatus {`
- `struct` `codex-rs/protocol/src/plan_tool.rs:17` `pub struct PlanItemArg {`
- `struct` `codex-rs/protocol/src/plan_tool.rs:24` `pub struct UpdatePlanArgs {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
