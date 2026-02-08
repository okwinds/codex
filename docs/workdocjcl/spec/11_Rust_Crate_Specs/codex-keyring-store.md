# `codex-keyring-store`

- path: `codex-rs/keyring-store`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `keyring`
- `tracing`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub enum CredentialStoreError {`
- `pub fn new(error: KeyringError) -> Self {`
- `pub fn message(&self) -> String {`
- `pub fn into_error(self) -> KeyringError {`
- `pub trait KeyringStore: Debug + Send + Sync {`
- `pub struct DefaultKeyringStore;`
- `pub mod tests {`
- `pub struct MockKeyringStore {`
- `pub fn credential(&self, account: &str) -> Arc<MockCredential> {`
- `pub fn saved_value(&self, account: &str) -> Option<String> {`
- `pub fn set_error(&self, account: &str, error: KeyringError) {`
- `pub fn contains(&self, account: &str) -> bool {`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
