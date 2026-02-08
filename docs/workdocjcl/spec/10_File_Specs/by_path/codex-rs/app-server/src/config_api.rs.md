# `codex-rs/app-server/src/config_api.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6021`
- sha256: `5828bcbc22f31ca2e9872ed7f79e60f7ee42850cd987ac9542ebbd275ba0749a`
- generated_utc: `2026-02-03T16:08:28Z`

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
- `use` `codex-rs/app-server/src/config_api.rs:12` `use codex_app_server_protocol::SandboxMode;`
- `use` `codex-rs/app-server/src/config_api.rs:13` `use codex_core::config::ConfigService;`
- `use` `codex-rs/app-server/src/config_api.rs:14` `use codex_core::config::ConfigServiceError;`
- `use` `codex-rs/app-server/src/config_api.rs:15` `use codex_core::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/app-server/src/config_api.rs:16` `use codex_core::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/app-server/src/config_api.rs:17` `use codex_core::config_loader::LoaderOverrides;`
- `use` `codex-rs/app-server/src/config_api.rs:18` `use codex_core::config_loader::ResidencyRequirement as CoreResidencyRequirement;`
- `use` `codex-rs/app-server/src/config_api.rs:19` `use codex_core::config_loader::SandboxModeRequirement as CoreSandboxModeRequirement;`
- `use` `codex-rs/app-server/src/config_api.rs:20` `use serde_json::json;`
- `use` `codex-rs/app-server/src/config_api.rs:21` `use std::path::PathBuf;`
- `use` `codex-rs/app-server/src/config_api.rs:22` `use toml::Value as TomlValue;`
- `impl` `codex-rs/app-server/src/config_api.rs:29` `impl ConfigApi {`
- `fn` `codex-rs/app-server/src/config_api.rs:81` `fn map_requirements_toml_to_api(requirements: ConfigRequirementsToml) -> ConfigRequirements {`
- `fn` `codex-rs/app-server/src/config_api.rs:101` `fn map_sandbox_mode_requirement_to_api(mode: CoreSandboxModeRequirement) -> Option<SandboxMode> {`
- `fn` `codex-rs/app-server/src/config_api.rs:110` `fn map_residency_requirement_to_api(`
- `fn` `codex-rs/app-server/src/config_api.rs:118` `fn map_error(err: ConfigServiceError) -> JSONRPCErrorError {`
- `fn` `codex-rs/app-server/src/config_api.rs:130` `fn config_write_error(code: ConfigWriteErrorCode, message: impl Into<String>) -> JSONRPCErrorError {`
- `use` `codex-rs/app-server/src/config_api.rs:142` `use super::*;`
- `use` `codex-rs/app-server/src/config_api.rs:143` `use codex_protocol::protocol::AskForApproval as CoreAskForApproval;`
- `use` `codex-rs/app-server/src/config_api.rs:144` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/app-server/src/config_api.rs:147` `fn map_requirements_toml_to_api_converts_core_enums() {`

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
- `use codex_app_server_protocol::SandboxMode;`
- `use codex_core::config::ConfigService;`
- `use codex_core::config::ConfigServiceError;`
- `use codex_core::config_loader::CloudRequirementsLoader;`
- `use codex_core::config_loader::ConfigRequirementsToml;`
- `use codex_core::config_loader::LoaderOverrides;`
- `use codex_core::config_loader::ResidencyRequirement as CoreResidencyRequirement;`
- `use codex_core::config_loader::SandboxModeRequirement as CoreSandboxModeRequirement;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
