# `codex-file-search`

- path: `codex-rs/file-search`
- generated_utc: `2026-02-08T10:45:13Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-file-search` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `clap`
- `crossbeam-channel`
- `ignore`
- `nucleo`
- `serde`
- `serde_json`
- `tokio`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use cli::Cli;`
- `pub struct FileMatch {`
- `pub fn full_path(&self) -> PathBuf {`
- `pub fn file_name_from_path(path: &str) -> String {`
- `pub struct FileSearchResults {`
- `pub struct FileSearchSnapshot {`
- `pub struct FileSearchOptions {`
- `pub trait SessionReporter: Send + Sync + 'static {`
- `pub struct FileSearchSession {`
- `pub fn update_query(&self, pattern_text: &str) {`
- `pub fn create_session(`
- `pub trait Reporter {`
- `pub fn run(`
- `pub fn cmp_by_score_desc_then_path_asc<T, FScore, FPath>(`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
