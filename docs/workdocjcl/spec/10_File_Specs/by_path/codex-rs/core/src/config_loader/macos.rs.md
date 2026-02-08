# `codex-rs/core/src/config_loader/macos.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5697`
- sha256: `32c07478ee04ff02743fb5a8d23327cd8903562bf1f2e08909889895dbfc34ca`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/macos.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/macos.rs:1` `use super::config_requirements::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/config_loader/macos.rs:2` `use super::config_requirements::ConfigRequirementsWithSources;`
- `use` `codex-rs/core/src/config_loader/macos.rs:3` `use super::config_requirements::RequirementSource;`
- `use` `codex-rs/core/src/config_loader/macos.rs:4` `use base64::Engine;`
- `use` `codex-rs/core/src/config_loader/macos.rs:5` `use base64::prelude::BASE64_STANDARD;`
- `use` `codex-rs/core/src/config_loader/macos.rs:6` `use core_foundation::base::TCFType;`
- `use` `codex-rs/core/src/config_loader/macos.rs:7` `use core_foundation::string::CFString;`
- `use` `codex-rs/core/src/config_loader/macos.rs:8` `use core_foundation::string::CFStringRef;`
- `use` `codex-rs/core/src/config_loader/macos.rs:9` `use std::ffi::c_void;`
- `use` `codex-rs/core/src/config_loader/macos.rs:10` `use std::io;`
- `use` `codex-rs/core/src/config_loader/macos.rs:11` `use tokio::task;`
- `use` `codex-rs/core/src/config_loader/macos.rs:12` `use toml::Value as TomlValue;`
- `const` `codex-rs/core/src/config_loader/macos.rs:14` `const MANAGED_PREFERENCES_APPLICATION_ID: &str = "com.openai.codex";`
- `const` `codex-rs/core/src/config_loader/macos.rs:15` `const MANAGED_PREFERENCES_CONFIG_KEY: &str = "config_toml_base64";`
- `const` `codex-rs/core/src/config_loader/macos.rs:16` `const MANAGED_PREFERENCES_REQUIREMENTS_KEY: &str = "requirements_toml_base64";`
- `fn` `codex-rs/core/src/config_loader/macos.rs:50` `fn load_managed_admin_config() -> io::Result<Option<TomlValue>> {`
- `fn` `codex-rs/core/src/config_loader/macos.rs:93` `fn load_managed_admin_requirements() -> io::Result<Option<ConfigRequirementsToml>> {`
- `fn` `codex-rs/core/src/config_loader/macos.rs:101` `fn load_managed_preference(key_name: &str) -> io::Result<Option<String>> {`
- `fn` `codex-rs/core/src/config_loader/macos.rs:104` `fn CFPreferencesCopyAppValue(key: CFStringRef, application_id: CFStringRef) -> *mut c_void;`
- `fn` `codex-rs/core/src/config_loader/macos.rs:125` `fn parse_managed_config_base64(encoded: &str) -> io::Result<TomlValue> {`
- `fn` `codex-rs/core/src/config_loader/macos.rs:142` `fn parse_managed_requirements_base64(encoded: &str) -> io::Result<ConfigRequirementsToml> {`
- `fn` `codex-rs/core/src/config_loader/macos.rs:151` `fn decode_managed_preferences_base64(encoded: &str) -> io::Result<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::config_requirements::ConfigRequirementsToml;`
- `use super::config_requirements::ConfigRequirementsWithSources;`
- `use super::config_requirements::RequirementSource;`
- `use base64::Engine;`
- `use base64::prelude::BASE64_STANDARD;`
- `use core_foundation::base::TCFType;`
- `use core_foundation::string::CFString;`
- `use core_foundation::string::CFStringRef;`
- `use std::ffi::c_void;`
- `use std::io;`
- `use tokio::task;`
- `use toml::Value as TomlValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
