# `codex-rs/network-proxy/src/state.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15627`
- sha256: `0ff5ec704797e90920158b526cb860243c6b5609fad003474e43eb8757b89f41`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/state.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/state.rs:1` `use crate::config::NetworkMode;`
- `use` `codex-rs/network-proxy/src/state.rs:2` `use crate::config::NetworkProxyConfig;`
- `use` `codex-rs/network-proxy/src/state.rs:3` `use crate::policy::DomainPattern;`
- `use` `codex-rs/network-proxy/src/state.rs:4` `use crate::policy::compile_globset;`
- `use` `codex-rs/network-proxy/src/state.rs:5` `use crate::runtime::ConfigState;`
- `use` `codex-rs/network-proxy/src/state.rs:6` `use crate::runtime::LayerMtime;`
- `use` `codex-rs/network-proxy/src/state.rs:7` `use anyhow::Context;`
- `use` `codex-rs/network-proxy/src/state.rs:8` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/state.rs:9` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/network-proxy/src/state.rs:10` `use codex_core::config::CONFIG_TOML_FILE;`
- `use` `codex-rs/network-proxy/src/state.rs:11` `use codex_core::config::Constrained;`
- `use` `codex-rs/network-proxy/src/state.rs:12` `use codex_core::config::ConstraintError;`
- `use` `codex-rs/network-proxy/src/state.rs:13` `use codex_core::config::find_codex_home;`
- `use` `codex-rs/network-proxy/src/state.rs:14` `use codex_core::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/network-proxy/src/state.rs:15` `use codex_core::config_loader::ConfigLayerStack;`
- `use` `codex-rs/network-proxy/src/state.rs:16` `use codex_core::config_loader::ConfigLayerStackOrdering;`
- `use` `codex-rs/network-proxy/src/state.rs:17` `use codex_core::config_loader::LoaderOverrides;`
- `use` `codex-rs/network-proxy/src/state.rs:18` `use codex_core::config_loader::RequirementSource;`
- `use` `codex-rs/network-proxy/src/state.rs:19` `use codex_core::config_loader::load_config_layers_state;`
- `use` `codex-rs/network-proxy/src/state.rs:20` `use serde::Deserialize;`
- `use` `codex-rs/network-proxy/src/state.rs:21` `use std::collections::HashSet;`
- `fn` `codex-rs/network-proxy/src/state.rs:72` `fn collect_layer_mtimes(stack: &ConfigLayerStack) -> Vec<LayerMtime> {`
- `struct` `codex-rs/network-proxy/src/state.rs:95` `struct PartialConfig {`
- `struct` `codex-rs/network-proxy/src/state.rs:101` `struct PartialNetworkProxyConfig {`
- `struct` `codex-rs/network-proxy/src/state.rs:112` `struct PartialNetworkPolicy {`
- `fn` `codex-rs/network-proxy/src/state.rs:136` `fn enforce_trusted_constraints(`
- `fn` `codex-rs/network-proxy/src/state.rs:146` `fn network_proxy_constraints_from_trusted_layers(`
- `fn` `codex-rs/network-proxy/src/state.rs:204` `fn is_user_controlled_layer(layer: &ConfigLayerSource) -> bool {`
- `fn` `codex-rs/network-proxy/src/state.rs:217` `fn invalid_value(`
- `fn` `codex-rs/network-proxy/src/state.rs:422` `fn network_mode_rank(mode: NetworkMode) -> u8 {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::NetworkMode;`
- `use crate::config::NetworkProxyConfig;`
- `use crate::policy::DomainPattern;`
- `use crate::policy::compile_globset;`
- `use crate::runtime::ConfigState;`
- `use crate::runtime::LayerMtime;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_core::config::CONFIG_TOML_FILE;`
- `use codex_core::config::Constrained;`
- `use codex_core::config::ConstraintError;`
- `use codex_core::config::find_codex_home;`
- `use codex_core::config_loader::CloudRequirementsLoader;`
- `use codex_core::config_loader::ConfigLayerStack;`
- `use codex_core::config_loader::ConfigLayerStackOrdering;`
- `use codex_core::config_loader::LoaderOverrides;`
- `use codex_core::config_loader::RequirementSource;`
- `use codex_core::config_loader::load_config_layers_state;`
- `use serde::Deserialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
