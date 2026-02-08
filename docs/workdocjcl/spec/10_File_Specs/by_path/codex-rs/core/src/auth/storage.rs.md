# `codex-rs/core/src/auth/storage.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `25232`
- sha256: `db5ec57608c8c871423c1b74bf616a47491a4d2e28d9c6e45a633e1e32d2ed9e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/auth/storage.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum AuthCredentialsStoreMode {`
- `pub struct AuthDotJson {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/auth/storage.rs:1` `use chrono::DateTime;`
- `use` `codex-rs/core/src/auth/storage.rs:2` `use chrono::Utc;`
- `use` `codex-rs/core/src/auth/storage.rs:3` `use schemars::JsonSchema;`
- `use` `codex-rs/core/src/auth/storage.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/core/src/auth/storage.rs:5` `use serde::Serialize;`
- `use` `codex-rs/core/src/auth/storage.rs:6` `use sha2::Digest;`
- `use` `codex-rs/core/src/auth/storage.rs:7` `use sha2::Sha256;`
- `use` `codex-rs/core/src/auth/storage.rs:8` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/auth/storage.rs:9` `use std::fmt::Debug;`
- `use` `codex-rs/core/src/auth/storage.rs:10` `use std::fs::File;`
- `use` `codex-rs/core/src/auth/storage.rs:11` `use std::fs::OpenOptions;`
- `use` `codex-rs/core/src/auth/storage.rs:12` `use std::io::Read;`
- `use` `codex-rs/core/src/auth/storage.rs:13` `use std::io::Write;`
- `use` `codex-rs/core/src/auth/storage.rs:15` `use std::os::unix::fs::OpenOptionsExt;`
- `use` `codex-rs/core/src/auth/storage.rs:16` `use std::path::Path;`
- `use` `codex-rs/core/src/auth/storage.rs:17` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/auth/storage.rs:18` `use std::sync::Arc;`
- `use` `codex-rs/core/src/auth/storage.rs:19` `use std::sync::Mutex;`
- `use` `codex-rs/core/src/auth/storage.rs:20` `use tracing::warn;`
- `use` `codex-rs/core/src/auth/storage.rs:22` `use crate::token_data::TokenData;`
- `use` `codex-rs/core/src/auth/storage.rs:23` `use codex_app_server_protocol::AuthMode;`
- `use` `codex-rs/core/src/auth/storage.rs:24` `use codex_keyring_store::DefaultKeyringStore;`
- `use` `codex-rs/core/src/auth/storage.rs:25` `use codex_keyring_store::KeyringStore;`
- `use` `codex-rs/core/src/auth/storage.rs:26` `use once_cell::sync::Lazy;`
- `enum` `codex-rs/core/src/auth/storage.rs:31` `pub enum AuthCredentialsStoreMode {`
- `struct` `codex-rs/core/src/auth/storage.rs:45` `pub struct AuthDotJson {`
- `fn` `codex-rs/core/src/auth/storage.rs:73` `fn load(&self) -> std::io::Result<Option<AuthDotJson>>;`
- `fn` `codex-rs/core/src/auth/storage.rs:74` `fn save(&self, auth: &AuthDotJson) -> std::io::Result<()>;`
- `fn` `codex-rs/core/src/auth/storage.rs:75` `fn delete(&self) -> std::io::Result<bool>;`
- `impl` `codex-rs/core/src/auth/storage.rs:83` `impl FileAuthStorage {`
- `impl` `codex-rs/core/src/auth/storage.rs:100` `impl AuthStorageBackend for FileAuthStorage {`
- `fn` `codex-rs/core/src/auth/storage.rs:101` `fn load(&self) -> std::io::Result<Option<AuthDotJson>> {`
- `fn` `codex-rs/core/src/auth/storage.rs:111` `fn save(&self, auth_dot_json: &AuthDotJson) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:130` `fn delete(&self) -> std::io::Result<bool> {`
- `const` `codex-rs/core/src/auth/storage.rs:135` `const KEYRING_SERVICE: &str = "Codex Auth";`
- `fn` `codex-rs/core/src/auth/storage.rs:138` `fn compute_store_key(codex_home: &Path) -> std::io::Result<String> {`
- `struct` `codex-rs/core/src/auth/storage.rs:152` `struct KeyringAuthStorage {`
- `impl` `codex-rs/core/src/auth/storage.rs:157` `impl KeyringAuthStorage {`
- `fn` `codex-rs/core/src/auth/storage.rs:158` `fn new(codex_home: PathBuf, keyring_store: Arc<dyn KeyringStore>) -> Self {`
- `fn` `codex-rs/core/src/auth/storage.rs:165` `fn load_from_keyring(&self, key: &str) -> std::io::Result<Option<AuthDotJson>> {`
- `fn` `codex-rs/core/src/auth/storage.rs:180` `fn save_to_keyring(&self, key: &str, value: &str) -> std::io::Result<()> {`
- `impl` `codex-rs/core/src/auth/storage.rs:195` `impl AuthStorageBackend for KeyringAuthStorage {`
- `fn` `codex-rs/core/src/auth/storage.rs:196` `fn load(&self) -> std::io::Result<Option<AuthDotJson>> {`
- `fn` `codex-rs/core/src/auth/storage.rs:201` `fn save(&self, auth: &AuthDotJson) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:212` `fn delete(&self) -> std::io::Result<bool> {`
- `struct` `codex-rs/core/src/auth/storage.rs:226` `struct AutoAuthStorage {`
- `impl` `codex-rs/core/src/auth/storage.rs:231` `impl AutoAuthStorage {`
- `fn` `codex-rs/core/src/auth/storage.rs:232` `fn new(codex_home: PathBuf, keyring_store: Arc<dyn KeyringStore>) -> Self {`
- `impl` `codex-rs/core/src/auth/storage.rs:240` `impl AuthStorageBackend for AutoAuthStorage {`
- `fn` `codex-rs/core/src/auth/storage.rs:241` `fn load(&self) -> std::io::Result<Option<AuthDotJson>> {`
- `fn` `codex-rs/core/src/auth/storage.rs:252` `fn save(&self, auth: &AuthDotJson) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:262` `fn delete(&self) -> std::io::Result<bool> {`
- `static` `codex-rs/core/src/auth/storage.rs:269` `static EPHEMERAL_AUTH_STORE: Lazy<Mutex<HashMap<String, AuthDotJson>>> =`
- `struct` `codex-rs/core/src/auth/storage.rs:273` `struct EphemeralAuthStorage {`
- `impl` `codex-rs/core/src/auth/storage.rs:277` `impl EphemeralAuthStorage {`
- `fn` `codex-rs/core/src/auth/storage.rs:278` `fn new(codex_home: PathBuf) -> Self {`
- `impl` `codex-rs/core/src/auth/storage.rs:294` `impl AuthStorageBackend for EphemeralAuthStorage {`
- `fn` `codex-rs/core/src/auth/storage.rs:295` `fn load(&self) -> std::io::Result<Option<AuthDotJson>> {`
- `fn` `codex-rs/core/src/auth/storage.rs:299` `fn save(&self, auth: &AuthDotJson) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:306` `fn delete(&self) -> std::io::Result<bool> {`
- `fn` `codex-rs/core/src/auth/storage.rs:319` `fn create_auth_storage_with_keyring_store(`
- `use` `codex-rs/core/src/auth/storage.rs:336` `use super::*;`
- `use` `codex-rs/core/src/auth/storage.rs:337` `use crate::token_data::IdTokenInfo;`
- `use` `codex-rs/core/src/auth/storage.rs:338` `use anyhow::Context;`
- `use` `codex-rs/core/src/auth/storage.rs:339` `use base64::Engine;`
- `use` `codex-rs/core/src/auth/storage.rs:340` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/auth/storage.rs:341` `use serde_json::json;`
- `use` `codex-rs/core/src/auth/storage.rs:342` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/auth/storage.rs:344` `use codex_keyring_store::tests::MockKeyringStore;`
- `use` `codex-rs/core/src/auth/storage.rs:345` `use keyring::Error as KeyringError;`
- `fn` `codex-rs/core/src/auth/storage.rs:348` `async fn file_storage_load_returns_auth_dot_json() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:368` `async fn file_storage_save_persists_auth_dot_json() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:391` `fn file_storage_delete_removes_auth_file() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:410` `fn ephemeral_storage_save_load_delete_is_in_memory_only() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:464` `fn assert_keyring_saved_auth_and_removed_fallback(`
- `fn` `codex-rs/core/src/auth/storage.rs:482` `fn id_token_with_prefix(prefix: &str) -> IdTokenInfo {`
- `struct` `codex-rs/core/src/auth/storage.rs:484` `struct Header {`
- `fn` `codex-rs/core/src/auth/storage.rs:508` `fn auth_with_prefix(prefix: &str) -> AuthDotJson {`
- `fn` `codex-rs/core/src/auth/storage.rs:523` `fn keyring_auth_storage_load_returns_deserialized_auth() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:548` `fn keyring_auth_storage_compute_store_key_for_home_directory() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:558` `fn keyring_auth_storage_save_persists_and_removes_fallback_file() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:592` `fn keyring_auth_storage_delete_removes_keyring_and_file() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:620` `fn auto_auth_storage_load_prefers_keyring_value() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:643` `fn auto_auth_storage_load_uses_file_when_keyring_empty() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:657` `fn auto_auth_storage_load_falls_back_when_keyring_errors() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:676` `fn auto_auth_storage_save_prefers_keyring() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:701` `fn auto_auth_storage_save_falls_back_when_keyring_errors() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/auth/storage.rs:732` `fn auto_auth_storage_delete_removes_keyring_and_file() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use sha2::Digest;`
- `use sha2::Sha256;`
- `use std::collections::HashMap;`
- `use std::fmt::Debug;`
- `use std::fs::File;`
- `use std::fs::OpenOptions;`
- `use std::io::Read;`
- `use std::io::Write;`
- `use std::os::unix::fs::OpenOptionsExt;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use tracing::warn;`
- `use crate::token_data::TokenData;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
