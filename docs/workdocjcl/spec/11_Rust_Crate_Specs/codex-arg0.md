# `codex-arg0`

- path: `codex-rs/arg0`
- generated_utc: `2026-02-08T10:45:12Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `codex-apply-patch`
- `codex-core`
- `codex-linux-sandbox`
- `dotenvy`
- `tempfile`
- `tokio`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub struct Arg0PathEntryGuard {`
- `pub fn arg0_dispatch() -> Option<Arg0PathEntryGuard> {`
- `pub fn arg0_dispatch_or_else<F, Fut>(main_fn: F) -> anyhow::Result<()>`
- `pub fn prepend_path_entry_for_codex_aliases() -> std::io::Result<Arg0PathEntryGuard> {`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
