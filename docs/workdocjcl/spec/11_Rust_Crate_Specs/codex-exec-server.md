# `codex-exec-server`

- path: `codex-rs/exec-server`
- generated_utc: `2026-02-08T10:45:13Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins:
  - name: `codex-execve-wrapper` path: `src/bin/main_execve_wrapper.rs`
  - name: `codex-exec-mcp-server` path: `src/bin/main_mcp_server.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `async-trait`
- `clap`
- `codex-core`
- `codex-execpolicy`
- `libc`
- `path-absolutize`
- `rmcp`
- `serde`
- `serde_json`
- `shlex`
- `socket2`
- `tokio`
- `tokio-util`
- `tracing`
- `tracing-subscriber`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use posix::main_execve_wrapper;`
- `pub use posix::main_mcp_server;`
- `pub use posix::ExecResult;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
