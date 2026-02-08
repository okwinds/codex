# `codex-rs/core/tests/common/test_codex_exec.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1199`
- sha256: `81f251466bf3a5ac8571d28fa16570d06b00d498924df65ff02cba9a8b941675`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/common/test_codex_exec.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct TestCodexExecBuilder {`
- `pub fn cmd(&self) -> assert_cmd::Command {`
- `pub fn cmd_with_server(&self, server: &MockServer) -> assert_cmd::Command {`
- `pub fn cwd_path(&self) -> &Path {`
- `pub fn home_path(&self) -> &Path {`
- `pub fn test_codex_exec() -> TestCodexExecBuilder {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::auth::CODEX_API_KEY_ENV_VAR;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use wiremock::MockServer;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
