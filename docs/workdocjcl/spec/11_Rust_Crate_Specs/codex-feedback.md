# `codex-feedback`

- path: `codex-rs/feedback`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `codex-protocol`
- `sentry`
- `tracing`
- `tracing-subscriber`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub struct CodexFeedback {`
- `pub fn new() -> Self {`
- `pub fn make_writer(&self) -> FeedbackMakeWriter {`
- `pub fn logger_layer<S>(&self) -> impl Layer<S> + Send + Sync + 'static`
- `pub fn metadata_layer<S>(&self) -> impl Layer<S> + Send + Sync + 'static`
- `pub fn snapshot(&self, session_id: Option<ThreadId>) -> CodexLogSnapshot {`
- `pub struct FeedbackMakeWriter {`
- `pub struct FeedbackWriter {`
- `pub struct CodexLogSnapshot {`
- `pub fn save_to_temp_file(&self) -> io::Result<PathBuf> {`
- `pub fn upload_feedback(`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
