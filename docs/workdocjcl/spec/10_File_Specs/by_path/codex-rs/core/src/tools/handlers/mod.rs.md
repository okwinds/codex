# `codex-rs/core/src/tools/handlers/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1260`
- sha256: `838ff4b47f505e88f40a3289f16d9bf7b9d278c8ba84629bbae47aead56b5d4c`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:4` `mod get_memory;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:5` `mod grep_files;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:6` `mod list_dir;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:7` `mod mcp;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:8` `mod mcp_resource;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:9` `mod plan;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:10` `mod read_file;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:11` `mod request_user_input;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:12` `mod shell;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:13` `mod test_sync;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:14` `mod unified_exec;`
- `mod` `codex-rs/core/src/tools/handlers/mod.rs:15` `mod view_image;`
- `use` `codex-rs/core/src/tools/handlers/mod.rs:18` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/mod.rs:20` `use crate::function_tool::FunctionCallError;`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Deserialize;`
- `use crate::function_tool::FunctionCallError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
