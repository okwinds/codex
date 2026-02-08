# `codex-rs/core/src/tools/handlers/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1134`
- sha256: `729ac1f6511cc1d2ee4a8fd7a72938b6553a92d4416165043720ff46d8c7606d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:1` `pub mod apply_patch;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:3` `mod dynamic;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:4` `mod grep_files;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:5` `mod list_dir;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:6` `mod mcp;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:7` `mod mcp_resource;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:8` `mod plan;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:9` `mod read_file;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:10` `mod request_user_input;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:11` `mod shell;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:12` `mod test_sync;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:13` `mod unified_exec;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:14` `mod view_image;`
- `use` `codex-rs/core/src/tools/handlers/mod.rs:17` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/mod.rs:19` `use crate::function_tool::FunctionCallError;`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Deserialize;`
- `use crate::function_tool::FunctionCallError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
