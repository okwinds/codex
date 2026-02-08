# `codex-rs/core/tests/suite/client.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `65740`
- sha256: `ad68efe8958159b643cf8a0f6414dfefb9637e5c44aee902c6b0de960ec12efa`
- generated_utc: `2026-02-08T10:45:35Z`

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
- `use codex_core::WireApi;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::built_in_model_providers;`
- `use codex_core::default_client::originator;`
- `use codex_core::error::CodexErr;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_core::protocol::EventMsg;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
