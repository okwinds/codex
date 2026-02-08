# `codex-rs/core/src/env.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1280`
- sha256: `b5a54f00e939c8a24768b5c7ce89de4bfa4d98f1e5f21b2cc884240f57325cc7`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/env.rs` (read)
- env: `WSL_DISTRO_NAME`

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn is_wsl() -> bool {`
- `pub fn is_headless_environment() -> bool {`

## Definitions (auto, per-file)
- `fn` `codex-rs/core/src/env.rs:3` `fn env_var_set(key: &str) -> bool {`
- `fn` `codex-rs/core/src/env.rs:8` `pub fn is_wsl() -> bool {`
- `fn` `codex-rs/core/src/env.rs:29` `pub fn is_headless_environment() -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- (none detected)
### Referenced env vars
- `WSL_DISTRO_NAME`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
