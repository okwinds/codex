# `codex-git`

- path: `codex-rs/utils/git`
- generated_utc: `2026-02-08T10:45:13Z`
- role: shared utility crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `once_cell`
- `regex`
- `schemars`
- `serde`
- `tempfile`
- `thiserror`
- `ts-rs`
- `walkdir`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use apply::ApplyGitRequest;`
- `pub use apply::ApplyGitResult;`
- `pub use apply::apply_git_patch;`
- `pub use apply::extract_paths_from_patch;`
- `pub use apply::parse_git_apply_output;`
- `pub use apply::stage_paths;`
- `pub use branch::merge_base_with_head;`
- `pub use errors::GitToolingError;`
- `pub use ghost_commits::CreateGhostCommitOptions;`
- `pub use ghost_commits::GhostSnapshotConfig;`
- `pub use ghost_commits::GhostSnapshotReport;`
- `pub use ghost_commits::IgnoredUntrackedFile;`
- `pub use ghost_commits::LargeUntrackedDir;`
- `pub use ghost_commits::RestoreGhostCommitOptions;`
- `pub use ghost_commits::capture_ghost_snapshot_report;`
- `pub use ghost_commits::create_ghost_commit;`
- `pub use ghost_commits::create_ghost_commit_with_report;`
- `pub use ghost_commits::restore_ghost_commit;`
- `pub use ghost_commits::restore_ghost_commit_with_options;`
- `pub use ghost_commits::restore_to_commit;`
- `pub use platform::create_symlink;`
- `pub struct GhostCommit {`
- `pub fn new(`
- `pub fn id(&self) -> &str {`
- `pub fn parent(&self) -> Option<&str> {`
- `pub fn preexisting_untracked_files(&self) -> &[PathBuf] {`
- `pub fn preexisting_untracked_dirs(&self) -> &[PathBuf] {`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
