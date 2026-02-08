# `codex-utils-pty`

- path: `codex-rs/utils/pty`
- generated_utc: `2026-02-03T09:48:37Z`
- role: shared utility crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `portable-pty`
- `tokio`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod pipe;`
- `pub mod process_group;`
- `pub mod pty;`
- `pub use pipe::spawn_process as spawn_pipe_process;`
- `pub use pipe::spawn_process_no_stdin as spawn_pipe_process_no_stdin;`
- `pub use process::ProcessHandle;`
- `pub use process::SpawnedProcess;`
- `pub use pty::conpty_supported;`
- `pub use pty::spawn_process as spawn_pty_process;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
