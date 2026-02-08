# `codex-rs/core/tests/common/test_codex.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `13621`
- sha256: `4c8eeb21a6559f9e9ac2d18fe0dddfd32c572b51e891119127db465a78b7c61e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/common/test_codex.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub enum ApplyPatchModelOutput {`
- `pub enum ShellModelOutput {`
- `pub struct TestCodexBuilder {`
- `pub fn with_auth(mut self, auth: CodexAuth) -> Self {`
- `pub fn with_model(self, model: &str) -> Self {`
- `pub fn with_home(mut self, home: Arc<TempDir>) -> Self {`
- `pub struct TestCodex {`
- `pub fn cwd_path(&self) -> &Path {`
- `pub fn codex_home_path(&self) -> &Path {`
- `pub fn workspace_path(&self, rel: impl AsRef<Path>) -> PathBuf {`
- `pub struct TestCodexHarness {`
- `pub fn server(&self) -> &MockServer {`
- `pub fn test(&self) -> &TestCodex {`
- `pub fn cwd(&self) -> &Path {`
- `pub fn path(&self, rel: impl AsRef<Path>) -> PathBuf {`
- `pub fn test_codex() -> TestCodexBuilder {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::mem::swap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use anyhow::Result;`
- `use codex_core::CodexAuth;`
- `use codex_core::CodexThread;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::ThreadManager;`
- `use codex_core::built_in_model_providers;`
- `use codex_core::config::Config;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::SessionConfiguredEvent;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::user_input::UserInput;`
- `use serde_json::Value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
