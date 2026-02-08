# `codex-rs/secrets/src/local.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14099`
- sha256: `20a7c7402589b3b67adab651bed0d094264256b5ddee2b86b5cdf0dcd7fb5d62`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/secrets/src/local.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct LocalSecretsBackend {`
- `pub fn new(codex_home: PathBuf, keyring_store: Arc<dyn KeyringStore>) -> Self {`
- `pub fn set(&self, scope: &SecretScope, name: &SecretName, value: &str) -> Result<()> {`
- `pub fn get(&self, scope: &SecretScope, name: &SecretName) -> Result<Option<String>> {`
- `pub fn delete(&self, scope: &SecretScope, name: &SecretName) -> Result<bool> {`
- `pub fn list(&self, scope_filter: Option<&SecretScope>) -> Result<Vec<SecretListEntry>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/secrets/src/local.rs:1` `use std::collections::BTreeMap;`
- `use` `codex-rs/secrets/src/local.rs:2` `use std::fs;`
- `use` `codex-rs/secrets/src/local.rs:3` `use std::io::Write;`
- `use` `codex-rs/secrets/src/local.rs:4` `use std::path::Path;`
- `use` `codex-rs/secrets/src/local.rs:5` `use std::path::PathBuf;`
- `use` `codex-rs/secrets/src/local.rs:6` `use std::sync::Arc;`
- `use` `codex-rs/secrets/src/local.rs:7` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/secrets/src/local.rs:8` `use std::sync::atomic::compiler_fence;`
- `use` `codex-rs/secrets/src/local.rs:9` `use std::time::SystemTime;`
- `use` `codex-rs/secrets/src/local.rs:10` `use std::time::UNIX_EPOCH;`
- `use` `codex-rs/secrets/src/local.rs:12` `use age::decrypt;`
- `use` `codex-rs/secrets/src/local.rs:13` `use age::encrypt;`
- `use` `codex-rs/secrets/src/local.rs:14` `use age::scrypt::Identity as ScryptIdentity;`
- `use` `codex-rs/secrets/src/local.rs:15` `use age::scrypt::Recipient as ScryptRecipient;`
- `use` `codex-rs/secrets/src/local.rs:16` `use age::secrecy::ExposeSecret;`
- `use` `codex-rs/secrets/src/local.rs:17` `use age::secrecy::SecretString;`
- `use` `codex-rs/secrets/src/local.rs:18` `use anyhow::Context;`
- `use` `codex-rs/secrets/src/local.rs:19` `use anyhow::Result;`
- `use` `codex-rs/secrets/src/local.rs:20` `use base64::Engine as _;`
- `use` `codex-rs/secrets/src/local.rs:21` `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use` `codex-rs/secrets/src/local.rs:22` `use codex_keyring_store::KeyringStore;`
- `use` `codex-rs/secrets/src/local.rs:23` `use rand::TryRngCore;`
- `use` `codex-rs/secrets/src/local.rs:24` `use rand::rngs::OsRng;`
- `use` `codex-rs/secrets/src/local.rs:25` `use serde::Deserialize;`
- `use` `codex-rs/secrets/src/local.rs:26` `use serde::Serialize;`
- `use` `codex-rs/secrets/src/local.rs:27` `use tracing::warn;`
- `use` `codex-rs/secrets/src/local.rs:29` `use super::SecretListEntry;`
- `use` `codex-rs/secrets/src/local.rs:30` `use super::SecretName;`
- `use` `codex-rs/secrets/src/local.rs:31` `use super::SecretScope;`
- `use` `codex-rs/secrets/src/local.rs:32` `use super::SecretsBackend;`
- `use` `codex-rs/secrets/src/local.rs:33` `use super::compute_keyring_account;`
- `use` `codex-rs/secrets/src/local.rs:34` `use super::keyring_service;`
- `const` `codex-rs/secrets/src/local.rs:36` `const SECRETS_VERSION: u8 = 1;`
- `const` `codex-rs/secrets/src/local.rs:37` `const LOCAL_SECRETS_FILENAME: &str = "local.age";`
- `struct` `codex-rs/secrets/src/local.rs:40` `struct SecretsFile {`
- `impl` `codex-rs/secrets/src/local.rs:45` `impl SecretsFile {`
- `fn` `codex-rs/secrets/src/local.rs:46` `fn new_empty() -> Self {`
- `struct` `codex-rs/secrets/src/local.rs:55` `pub struct LocalSecretsBackend {`
- `impl` `codex-rs/secrets/src/local.rs:60` `impl LocalSecretsBackend {`
- `fn` `codex-rs/secrets/src/local.rs:61` `pub fn new(codex_home: PathBuf, keyring_store: Arc<dyn KeyringStore>) -> Self {`
- `fn` `codex-rs/secrets/src/local.rs:68` `pub fn set(&self, scope: &SecretScope, name: &SecretName, value: &str) -> Result<()> {`
- `fn` `codex-rs/secrets/src/local.rs:76` `pub fn get(&self, scope: &SecretScope, name: &SecretName) -> Result<Option<String>> {`
- `fn` `codex-rs/secrets/src/local.rs:82` `pub fn delete(&self, scope: &SecretScope, name: &SecretName) -> Result<bool> {`
- `fn` `codex-rs/secrets/src/local.rs:92` `pub fn list(&self, scope_filter: Option<&SecretScope>) -> Result<Vec<SecretListEntry>> {`
- `fn` `codex-rs/secrets/src/local.rs:110` `fn secrets_dir(&self) -> PathBuf {`
- `fn` `codex-rs/secrets/src/local.rs:114` `fn secrets_path(&self) -> PathBuf {`
- `fn` `codex-rs/secrets/src/local.rs:118` `fn load_file(&self) -> Result<SecretsFile> {`
- `fn` `codex-rs/secrets/src/local.rs:146` `fn save_file(&self, file: &SecretsFile) -> Result<()> {`
- `fn` `codex-rs/secrets/src/local.rs:159` `fn load_or_create_passphrase(&self) -> Result<SecretString> {`
- `impl` `codex-rs/secrets/src/local.rs:183` `impl SecretsBackend for LocalSecretsBackend {`
- `fn` `codex-rs/secrets/src/local.rs:184` `fn set(&self, scope: &SecretScope, name: &SecretName, value: &str) -> Result<()> {`
- `fn` `codex-rs/secrets/src/local.rs:188` `fn get(&self, scope: &SecretScope, name: &SecretName) -> Result<Option<String>> {`
- `fn` `codex-rs/secrets/src/local.rs:192` `fn delete(&self, scope: &SecretScope, name: &SecretName) -> Result<bool> {`
- `fn` `codex-rs/secrets/src/local.rs:196` `fn list(&self, scope_filter: Option<&SecretScope>) -> Result<Vec<SecretListEntry>> {`
- `fn` `codex-rs/secrets/src/local.rs:201` `fn write_file_atomically(path: &Path, contents: &[u8]) -> Result<()> {`
- `fn` `codex-rs/secrets/src/local.rs:273` `fn generate_passphrase() -> Result<SecretString> {`
- `fn` `codex-rs/secrets/src/local.rs:284` `fn wipe_bytes(bytes: &mut [u8]) {`
- `fn` `codex-rs/secrets/src/local.rs:293` `fn encrypt_with_passphrase(plaintext: &[u8], passphrase: &SecretString) -> Result<Vec<u8>> {`
- `fn` `codex-rs/secrets/src/local.rs:298` `fn decrypt_with_passphrase(ciphertext: &[u8], passphrase: &SecretString) -> Result<Vec<u8>> {`
- `fn` `codex-rs/secrets/src/local.rs:303` `fn parse_canonical_key(canonical_key: &str) -> Option<SecretListEntry> {`
- `use` `codex-rs/secrets/src/local.rs:334` `use super::*;`
- `use` `codex-rs/secrets/src/local.rs:335` `use codex_keyring_store::tests::MockKeyringStore;`
- `use` `codex-rs/secrets/src/local.rs:336` `use keyring::Error as KeyringError;`
- `use` `codex-rs/secrets/src/local.rs:337` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/secrets/src/local.rs:340` `fn load_file_rejects_newer_schema_versions() -> Result<()> {`
- `fn` `codex-rs/secrets/src/local.rs:362` `fn set_fails_when_keyring_is_unavailable() -> Result<()> {`
- `fn` `codex-rs/secrets/src/local.rs:387` `fn save_file_does_not_leave_temp_files() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::fs;`
- `use std::io::Write;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::atomic::Ordering;`
- `use std::sync::atomic::compiler_fence;`
- `use std::time::SystemTime;`
- `use std::time::UNIX_EPOCH;`
- `use age::decrypt;`
- `use age::encrypt;`
- `use age::scrypt::Identity as ScryptIdentity;`
- `use age::scrypt::Recipient as ScryptRecipient;`
- `use age::secrecy::ExposeSecret;`
- `use age::secrecy::SecretString;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use base64::Engine as _;`
- `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
