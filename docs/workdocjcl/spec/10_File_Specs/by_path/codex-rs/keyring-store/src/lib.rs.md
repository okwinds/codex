# `codex-rs/keyring-store/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7474`
- sha256: `1bf693468859a71f3381a15587a01e0d8849288012be16e90d31bbc2fb9abbdc`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/keyring-store/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum CredentialStoreError {`
- `pub fn new(error: KeyringError) -> Self {`
- `pub fn message(&self) -> String {`
- `pub fn into_error(self) -> KeyringError {`
- `pub trait KeyringStore: Debug + Send + Sync {`
- `pub struct DefaultKeyringStore;`
- `pub struct MockKeyringStore {`
- `pub fn credential(&self, account: &str) -> Arc<MockCredential> {`
- `pub fn saved_value(&self, account: &str) -> Option<String> {`
- `pub fn set_error(&self, account: &str, error: KeyringError) {`
- `pub fn contains(&self, account: &str) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/keyring-store/src/lib.rs:1` `use keyring::Entry;`
- `use` `codex-rs/keyring-store/src/lib.rs:2` `use keyring::Error as KeyringError;`
- `use` `codex-rs/keyring-store/src/lib.rs:3` `use std::error::Error;`
- `use` `codex-rs/keyring-store/src/lib.rs:4` `use std::fmt;`
- `use` `codex-rs/keyring-store/src/lib.rs:5` `use std::fmt::Debug;`
- `use` `codex-rs/keyring-store/src/lib.rs:6` `use tracing::trace;`
- `enum` `codex-rs/keyring-store/src/lib.rs:9` `pub enum CredentialStoreError {`
- `impl` `codex-rs/keyring-store/src/lib.rs:13` `impl CredentialStoreError {`
- `fn` `codex-rs/keyring-store/src/lib.rs:14` `pub fn new(error: KeyringError) -> Self {`
- `fn` `codex-rs/keyring-store/src/lib.rs:18` `pub fn message(&self) -> String {`
- `fn` `codex-rs/keyring-store/src/lib.rs:24` `pub fn into_error(self) -> KeyringError {`
- `impl` `codex-rs/keyring-store/src/lib.rs:31` `impl fmt::Display for CredentialStoreError {`
- `fn` `codex-rs/keyring-store/src/lib.rs:32` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `trait` `codex-rs/keyring-store/src/lib.rs:42` `pub trait KeyringStore: Debug + Send + Sync {`
- `fn` `codex-rs/keyring-store/src/lib.rs:43` `fn load(&self, service: &str, account: &str) -> Result<Option<String>, CredentialStoreError>;`
- `fn` `codex-rs/keyring-store/src/lib.rs:44` `fn save(&self, service: &str, account: &str, value: &str) -> Result<(), CredentialStoreError>;`
- `fn` `codex-rs/keyring-store/src/lib.rs:45` `fn delete(&self, service: &str, account: &str) -> Result<bool, CredentialStoreError>;`
- `struct` `codex-rs/keyring-store/src/lib.rs:49` `pub struct DefaultKeyringStore;`
- `impl` `codex-rs/keyring-store/src/lib.rs:51` `impl KeyringStore for DefaultKeyringStore {`
- `fn` `codex-rs/keyring-store/src/lib.rs:52` `fn load(&self, service: &str, account: &str) -> Result<Option<String>, CredentialStoreError> {`
- `fn` `codex-rs/keyring-store/src/lib.rs:71` `fn save(&self, service: &str, account: &str, value: &str) -> Result<(), CredentialStoreError> {`
- `fn` `codex-rs/keyring-store/src/lib.rs:89` `fn delete(&self, service: &str, account: &str) -> Result<bool, CredentialStoreError> {`
- `use` `codex-rs/keyring-store/src/lib.rs:110` `use super::CredentialStoreError;`
- `use` `codex-rs/keyring-store/src/lib.rs:111` `use super::KeyringStore;`
- `use` `codex-rs/keyring-store/src/lib.rs:112` `use keyring::Error as KeyringError;`
- `use` `codex-rs/keyring-store/src/lib.rs:113` `use keyring::credential::CredentialApi as _;`
- `use` `codex-rs/keyring-store/src/lib.rs:114` `use keyring::mock::MockCredential;`
- `use` `codex-rs/keyring-store/src/lib.rs:115` `use std::collections::HashMap;`
- `use` `codex-rs/keyring-store/src/lib.rs:116` `use std::sync::Arc;`
- `use` `codex-rs/keyring-store/src/lib.rs:117` `use std::sync::Mutex;`
- `use` `codex-rs/keyring-store/src/lib.rs:118` `use std::sync::PoisonError;`
- `struct` `codex-rs/keyring-store/src/lib.rs:121` `pub struct MockKeyringStore {`
- `impl` `codex-rs/keyring-store/src/lib.rs:125` `impl MockKeyringStore {`
- `fn` `codex-rs/keyring-store/src/lib.rs:126` `pub fn credential(&self, account: &str) -> Arc<MockCredential> {`
- `fn` `codex-rs/keyring-store/src/lib.rs:137` `pub fn saved_value(&self, account: &str) -> Option<String> {`
- `fn` `codex-rs/keyring-store/src/lib.rs:148` `pub fn set_error(&self, account: &str, error: KeyringError) {`
- `fn` `codex-rs/keyring-store/src/lib.rs:153` `pub fn contains(&self, account: &str) -> bool {`
- `impl` `codex-rs/keyring-store/src/lib.rs:162` `impl KeyringStore for MockKeyringStore {`
- `fn` `codex-rs/keyring-store/src/lib.rs:163` `fn load(`
- `fn` `codex-rs/keyring-store/src/lib.rs:187` `fn save(`
- `fn` `codex-rs/keyring-store/src/lib.rs:199` `fn delete(&self, _service: &str, account: &str) -> Result<bool, CredentialStoreError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use keyring::Entry;`
- `use keyring::Error as KeyringError;`
- `use std::error::Error;`
- `use std::fmt;`
- `use std::fmt::Debug;`
- `use tracing::trace;`
- `use super::CredentialStoreError;`
- `use super::KeyringStore;`
- `use keyring::Error as KeyringError;`
- `use keyring::credential::CredentialApi as _;`
- `use keyring::mock::MockCredential;`
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::PoisonError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
