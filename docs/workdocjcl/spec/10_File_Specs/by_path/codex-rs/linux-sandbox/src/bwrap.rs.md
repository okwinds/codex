# `codex-rs/linux-sandbox/src/bwrap.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8737`
- sha256: `b99d16c7fb91fc9dd8c9dd144a1e639265f938ba8bc004adabf628366661da2f`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/src/bwrap.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:12` `use std::collections::BTreeSet;`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:13` `use std::path::Path;`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:14` `use std::path::PathBuf;`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:16` `use codex_core::error::CodexErr;`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:17` `use codex_core::error::Result;`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:18` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:19` `use codex_core::protocol::WritableRoot;`
- `impl` `codex-rs/linux-sandbox/src/bwrap.rs:31` `impl Default for BwrapOptions {`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:32` `fn default() -> Self {`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:56` `fn create_bwrap_flags(`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:87` `fn create_filesystem_args(sandbox_policy: &SandboxPolicy, cwd: &Path) -> Result<Vec<String>> {`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:146` `fn collect_read_only_subpaths(writable_roots: &[WritableRoot]) -> Vec<PathBuf> {`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:160` `fn ensure_mount_targets_exist(writable_roots: &[WritableRoot]) -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:173` `fn path_to_string(path: &Path) -> String {`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:178` `fn is_within_allowed_write_paths(path: &Path, allowed_write_paths: &[PathBuf]) -> bool {`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:189` `fn find_symlink_in_path(target_path: &Path, allowed_write_paths: &[PathBuf]) -> Option<PathBuf> {`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:193` `use std::path::Component;`
- `fn` `codex-rs/linux-sandbox/src/bwrap.rs:227` `fn find_first_non_existent_component(target_path: &Path) -> Option<PathBuf> {`
- `use` `codex-rs/linux-sandbox/src/bwrap.rs:231` `use std::path::Component;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_core::error::CodexErr;`
- `use codex_core::error::Result;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::WritableRoot;`
- `use std::path::Component;`
- `use std::path::Component;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
