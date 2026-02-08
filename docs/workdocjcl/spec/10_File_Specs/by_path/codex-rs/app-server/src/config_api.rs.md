# `codex-rs/app-server/src/config_api.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10315`
- sha256: `56cfe06508fb2e83cf60a2f2115266c9660815a4f7d3ac2931db21cf576f9d82`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/config_api.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/config_api.rs:1` `use crate::error_code::INTERNAL_ERROR_CODE;`
- `use` `codex-rs/app-server/src/config_api.rs:2` `use crate::error_code::INVALID_REQUEST_ERROR_CODE;`
- `use` `codex-rs/app-server/src/config_api.rs:3` `use codex_app_server_protocol::ConfigBatchWriteParams;`
- `use` `codex-rs/app-server/src/config_api.rs:4` `use codex_app_server_protocol::ConfigReadParams;`
- `use` `codex-rs/app-server/src/config_api.rs:5` `use codex_app_server_protocol::ConfigReadResponse;`
- `use` `codex-rs/app-server/src/config_api.rs:6` `use codex_app_server_protocol::ConfigRequirements;`
- `use` `codex-rs/app-server/src/config_api.rs:7` `use codex_app_server_protocol::ConfigRequirementsReadResponse;`
- `use` `codex-rs/app-server/src/config_api.rs:8` `use codex_app_server_protocol::ConfigValueWriteParams;`
- `use` `codex-rs/app-server/src/config_api.rs:9` `use codex_app_server_protocol::ConfigWriteErrorCode;`
- `use` `codex-rs/app-server/src/config_api.rs:10` `use codex_app_server_protocol::ConfigWriteResponse;`
- `use` `codex-rs/app-server/src/config_api.rs:11` `use codex_app_server_protocol::JSONRPCErrorError;`
- `use` `codex-rs/app-server/src/config_api.rs:12` `use codex_app_server_protocol::NetworkRequirements;`
- `use` `codex-rs/app-server/src/config_api.rs:13` `use codex_app_server_protocol::SandboxMode;`
- `use` `codex-rs/app-server/src/config_api.rs:14` `use codex_core::config::ConfigService;`
- `use` `codex-rs/app-server/src/config_api.rs:15` `use codex_core::config::ConfigServiceError;`
- `use` `codex-rs/app-server/src/config_api.rs:16` `use codex_core::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/app-server/src/config_api.rs:17` `use codex_core::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/app-server/src/config_api.rs:18` `use codex_core::config_loader::LoaderOverrides;`
- `use` `codex-rs/app-server/src/config_api.rs:19` `use codex_core::config_loader::ResidencyRequirement as CoreResidencyRequirement;`
- `use` `codex-rs/app-server/src/config_api.rs:20` `use codex_core::config_loader::SandboxModeRequirement as CoreSandboxModeRequirement;`
- `use` `codex-rs/app-server/src/config_api.rs:21` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/app-server/src/config_api.rs:22` `use serde_json::json;`
- `use` `codex-rs/app-server/src/config_api.rs:23` `use std::path::PathBuf;`
- `use` `codex-rs/app-server/src/config_api.rs:24` `use std::sync::Arc;`
- `use` `codex-rs/app-server/src/config_api.rs:25` `use std::sync::RwLock;`
- `use` `codex-rs/app-server/src/config_api.rs:26` `use toml::Value as TomlValue;`
- `impl` `codex-rs/app-server/src/config_api.rs:36` `impl ConfigApi {`
- `fn` `codex-rs/app-server/src/config_api.rs:51` `fn config_service(&self) -> ConfigService {`
- `fn` `codex-rs/app-server/src/config_api.rs:106` `fn map_requirements_toml_to_api(requirements: ConfigRequirementsToml) -> ConfigRequirements {`
- `fn` `codex-rs/app-server/src/config_api.rs:137` `fn map_sandbox_mode_requirement_to_api(mode: CoreSandboxModeRequirement) -> Option<SandboxMode> {`
- `fn` `codex-rs/app-server/src/config_api.rs:146` `fn map_residency_requirement_to_api(`
- `fn` `codex-rs/app-server/src/config_api.rs:154` `fn map_network_requirements_to_api(`
- `fn` `codex-rs/app-server/src/config_api.rs:171` `fn map_error(err: ConfigServiceError) -> JSONRPCErrorError {`
- `fn` `codex-rs/app-server/src/config_api.rs:183` `fn config_write_error(code: ConfigWriteErrorCode, message: impl Into<String>) -> JSONRPCErrorError {`
- `use` `codex-rs/app-server/src/config_api.rs:195` `use super::*;`
- `use` `codex-rs/app-server/src/config_api.rs:196` `use codex_core::config_loader::NetworkRequirementsToml as CoreNetworkRequirementsToml;`
- `use` `codex-rs/app-server/src/config_api.rs:197` `use codex_protocol::protocol::AskForApproval as CoreAskForApproval;`
- `use` `codex-rs/app-server/src/config_api.rs:198` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/app-server/src/config_api.rs:201` `fn map_requirements_toml_to_api_converts_core_enums() {`
- `fn` `codex-rs/app-server/src/config_api.rs:270` `fn map_requirements_toml_to_api_normalizes_allowed_web_search_modes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error_code::INTERNAL_ERROR_CODE;`
- `use crate::error_code::INVALID_REQUEST_ERROR_CODE;`
- `use codex_app_server_protocol::ConfigBatchWriteParams;`
- `use codex_app_server_protocol::ConfigReadParams;`
- `use codex_app_server_protocol::ConfigReadResponse;`
- `use codex_app_server_protocol::ConfigRequirements;`
- `use codex_app_server_protocol::ConfigRequirementsReadResponse;`
- `use codex_app_server_protocol::ConfigValueWriteParams;`
- `use codex_app_server_protocol::ConfigWriteErrorCode;`
- `use codex_app_server_protocol::ConfigWriteResponse;`
- `use codex_app_server_protocol::JSONRPCErrorError;`
- `use codex_app_server_protocol::NetworkRequirements;`
- `use codex_app_server_protocol::SandboxMode;`
- `use codex_core::config::ConfigService;`
- `use codex_core::config::ConfigServiceError;`
- `use codex_core::config_loader::CloudRequirementsLoader;`
- `use codex_core::config_loader::ConfigRequirementsToml;`
- `use codex_core::config_loader::LoaderOverrides;`
- `use codex_core::config_loader::ResidencyRequirement as CoreResidencyRequirement;`
- `use codex_core::config_loader::SandboxModeRequirement as CoreSandboxModeRequirement;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
