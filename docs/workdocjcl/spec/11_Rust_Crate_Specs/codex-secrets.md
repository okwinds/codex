# `codex-secrets`

- path: `codex-rs/secrets`
- generated_utc: `2026-02-08T10:45:13Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `age`
- `anyhow`
- `base64`
- `codex-keyring-store`
- `rand`
- `schemars`
- `serde`
- `serde_json`
- `sha2`
- `tracing`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use local::LocalSecretsBackend;`
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

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
