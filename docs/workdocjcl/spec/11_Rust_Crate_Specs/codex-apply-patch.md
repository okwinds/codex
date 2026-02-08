# `codex-apply-patch`

- path: `codex-rs/apply-patch`
- generated_utc: `2026-02-08T10:45:12Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `apply_patch` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `similar`
- `thiserror`
- `tree-sitter`
- `tree-sitter-bash`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use parser::Hunk;`
- `pub use parser::ParseError;`
- `pub use parser::parse_patch;`
- `pub use invocation::maybe_parse_apply_patch_verified;`
- `pub use standalone_executable::main;`
- `pub enum ApplyPatchError {`
- `pub struct IoError {`
- `pub struct ApplyPatchArgs {`
- `pub enum ApplyPatchFileChange {`
- `pub enum MaybeApplyPatchVerified {`
- `pub struct ApplyPatchAction {`
- `pub fn is_empty(&self) -> bool {`
- `pub fn changes(&self) -> &HashMap<PathBuf, ApplyPatchFileChange> {`
- `pub fn new_add_for_test(path: &Path, content: String) -> Self {`
- `pub fn apply_patch(`
- `pub fn apply_hunks(`
- `pub struct AffectedPaths {`
- `pub struct ApplyPatchFileUpdate {`
- `pub fn unified_diff_from_chunks(`
- `pub fn unified_diff_from_chunks_with_context(`
- `pub fn print_summary(`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
