# `codex-rs/core/tests/suite/client.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `64412`
- sha256: `411295c82a405167a03f8483acd00ca2bc1ef9746fc345f8de4e5b2010796307`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/client.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::AuthManager;`
- `use codex_core::CodexAuth;`
- `use codex_core::ContentItem;`
- `use codex_core::LocalShellAction;`
- `use codex_core::LocalShellExecAction;`
- `use codex_core::LocalShellStatus;`
- `use codex_core::ModelClient;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::NewThread;`
- `use codex_core::Prompt;`
- `use codex_core::ResponseEvent;`
- `use codex_core::ResponseItem;`
- `use codex_core::ThreadManager;`
- `use codex_core::TransportManager;`
- `use codex_core::WireApi;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::built_in_model_providers;`
- `use codex_core::default_client::originator;`
- `use codex_core::error::CodexErr;`
- `use codex_core::models_manager::manager::ModelsManager;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
