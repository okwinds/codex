# `codex-rs/core/tests/suite/deprecation_notice.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6240`
- sha256: `57cfe1653bbcbaeb4424793adea44133f456812a328f7bd5a6366b95b287f646`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/deprecation_notice.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Ok;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_core::config_loader::ConfigLayerEntry;`
- `use codex_core::config_loader::ConfigLayerStack;`
- `use codex_core::config_loader::ConfigRequirements;`
- `use codex_core::config_loader::ConfigRequirementsToml;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::DeprecationNoticeEvent;`
- `use codex_core::protocol::EventMsg;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_absolute_path;`
- `use core_test_support::test_codex::TestCodex;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event_match;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::BTreeMap;`
- `use toml::Value as TomlValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
