# `codex-rs/secrets/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7233`
- sha256: `94d4679c7a28dd4cee29eb0e6b738c7c1d2ddcb50f9538e26b67fbe1ab7a0636`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/secrets/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct SecretName(String);`
- `pub fn new(raw: &str) -> Result<Self> {`
- `pub fn as_str(&self) -> &str {`
- `pub enum SecretScope {`
- `pub fn environment(environment_id: impl Into<String>) -> Result<Self> {`
- `pub fn canonical_key(&self, name: &SecretName) -> String {`
- `pub struct SecretListEntry {`
- `pub enum SecretsBackendKind {`
- `pub trait SecretsBackend: Send + Sync {`
- `pub struct SecretsManager {`
- `pub fn new(codex_home: PathBuf, backend_kind: SecretsBackendKind) -> Self {`
- `pub fn new_with_keyring_store(`
- `pub fn set(&self, scope: &SecretScope, name: &SecretName, value: &str) -> Result<()> {`
- `pub fn get(&self, scope: &SecretScope, name: &SecretName) -> Result<Option<String>> {`
- `pub fn delete(&self, scope: &SecretScope, name: &SecretName) -> Result<bool> {`
- `pub fn list(&self, scope_filter: Option<&SecretScope>) -> Result<Vec<SecretListEntry>> {`
- `pub fn environment_id_from_cwd(cwd: &Path) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/secrets/src/lib.rs:1` `use std::fmt;`
- `use` `codex-rs/secrets/src/lib.rs:2` `use std::path::Path;`
- `use` `codex-rs/secrets/src/lib.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/secrets/src/lib.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/secrets/src/lib.rs:6` `use anyhow::Result;`
- `use` `codex-rs/secrets/src/lib.rs:7` `use codex_keyring_store::DefaultKeyringStore;`
- `use` `codex-rs/secrets/src/lib.rs:8` `use codex_keyring_store::KeyringStore;`
- `use` `codex-rs/secrets/src/lib.rs:9` `use schemars::JsonSchema;`
- `use` `codex-rs/secrets/src/lib.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/secrets/src/lib.rs:11` `use serde::Serialize;`
- `use` `codex-rs/secrets/src/lib.rs:12` `use sha2::Digest;`
- `use` `codex-rs/secrets/src/lib.rs:13` `use sha2::Sha256;`
- `mod` `codex-rs/secrets/src/lib.rs:15` `mod local;`
- `const` `codex-rs/secrets/src/lib.rs:19` `const KEYRING_SERVICE: &str = "codex";`
- `struct` `codex-rs/secrets/src/lib.rs:22` `pub struct SecretName(String);`
- `impl` `codex-rs/secrets/src/lib.rs:24` `impl SecretName {`
- `fn` `codex-rs/secrets/src/lib.rs:25` `pub fn new(raw: &str) -> Result<Self> {`
- `fn` `codex-rs/secrets/src/lib.rs:37` `pub fn as_str(&self) -> &str {`
- `impl` `codex-rs/secrets/src/lib.rs:42` `impl fmt::Display for SecretName {`
- `fn` `codex-rs/secrets/src/lib.rs:43` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `enum` `codex-rs/secrets/src/lib.rs:49` `pub enum SecretScope {`
- `impl` `codex-rs/secrets/src/lib.rs:54` `impl SecretScope {`
- `fn` `codex-rs/secrets/src/lib.rs:55` `pub fn environment(environment_id: impl Into<String>) -> Result<Self> {`
- `fn` `codex-rs/secrets/src/lib.rs:62` `pub fn canonical_key(&self, name: &SecretName) -> String {`
- `struct` `codex-rs/secrets/src/lib.rs:74` `pub struct SecretListEntry {`
- `enum` `codex-rs/secrets/src/lib.rs:81` `pub enum SecretsBackendKind {`
- `trait` `codex-rs/secrets/src/lib.rs:86` `pub trait SecretsBackend: Send + Sync {`
- `fn` `codex-rs/secrets/src/lib.rs:87` `fn set(&self, scope: &SecretScope, name: &SecretName, value: &str) -> Result<()>;`
- `fn` `codex-rs/secrets/src/lib.rs:88` `fn get(&self, scope: &SecretScope, name: &SecretName) -> Result<Option<String>>;`
- `fn` `codex-rs/secrets/src/lib.rs:89` `fn delete(&self, scope: &SecretScope, name: &SecretName) -> Result<bool>;`
- `fn` `codex-rs/secrets/src/lib.rs:90` `fn list(&self, scope_filter: Option<&SecretScope>) -> Result<Vec<SecretListEntry>>;`
- `struct` `codex-rs/secrets/src/lib.rs:94` `pub struct SecretsManager {`
- `impl` `codex-rs/secrets/src/lib.rs:98` `impl SecretsManager {`
- `fn` `codex-rs/secrets/src/lib.rs:99` `pub fn new(codex_home: PathBuf, backend_kind: SecretsBackendKind) -> Self {`
- `fn` `codex-rs/secrets/src/lib.rs:109` `pub fn new_with_keyring_store(`
- `fn` `codex-rs/secrets/src/lib.rs:122` `pub fn set(&self, scope: &SecretScope, name: &SecretName, value: &str) -> Result<()> {`
- `fn` `codex-rs/secrets/src/lib.rs:126` `pub fn get(&self, scope: &SecretScope, name: &SecretName) -> Result<Option<String>> {`
- `fn` `codex-rs/secrets/src/lib.rs:130` `pub fn delete(&self, scope: &SecretScope, name: &SecretName) -> Result<bool> {`
- `fn` `codex-rs/secrets/src/lib.rs:134` `pub fn list(&self, scope_filter: Option<&SecretScope>) -> Result<Vec<SecretListEntry>> {`
- `fn` `codex-rs/secrets/src/lib.rs:139` `pub fn environment_id_from_cwd(cwd: &Path) -> String {`
- `fn` `codex-rs/secrets/src/lib.rs:162` `fn get_git_repo_root(base_dir: &Path) -> Option<PathBuf> {`
- `use` `codex-rs/secrets/src/lib.rs:198` `use super::*;`
- `use` `codex-rs/secrets/src/lib.rs:199` `use codex_keyring_store::tests::MockKeyringStore;`
- `use` `codex-rs/secrets/src/lib.rs:200` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/secrets/src/lib.rs:203` `fn environment_id_fallback_has_cwd_prefix() {`
- `fn` `codex-rs/secrets/src/lib.rs:221` `fn manager_round_trips_local_backend() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use anyhow::Result;`
- `use codex_keyring_store::DefaultKeyringStore;`
- `use codex_keyring_store::KeyringStore;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use sha2::Digest;`
- `use sha2::Sha256;`
- `use super::*;`
- `use codex_keyring_store::tests::MockKeyringStore;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
