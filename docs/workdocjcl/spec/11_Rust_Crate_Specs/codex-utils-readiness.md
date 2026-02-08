# `codex-utils-readiness`

- path: `codex-rs/utils/readiness`
- generated_utc: `2026-02-03T09:48:37Z`
- role: shared utility crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `async-trait`
- `thiserror`
- `time`
- `tokio`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub struct Token(i32);`
- `pub trait Readiness: Send + Sync + 'static {`
- `pub struct ReadinessFlag {`
- `pub fn new() -> Self {`
- `pub enum ReadinessError {`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
