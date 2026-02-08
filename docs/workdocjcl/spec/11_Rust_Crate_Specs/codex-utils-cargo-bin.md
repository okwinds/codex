# `codex-utils-cargo-bin`

- path: `codex-rs/utils/cargo-bin`
- generated_utc: `2026-02-08T10:45:13Z`
- role: shared utility crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `assert_cmd`
- `runfiles`
- `thiserror`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use runfiles;`
- `pub enum CargoBinError {`
- `pub fn cargo_bin(name: &str) -> Result<PathBuf, CargoBinError> {`
- `pub fn runfiles_available() -> bool {`
- `pub fn resolve_bazel_runfile(`
- `pub fn resolve_cargo_runfile(resource: &Path) -> std::io::Result<PathBuf> {`
- `pub fn repo_root() -> io::Result<PathBuf> {`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
