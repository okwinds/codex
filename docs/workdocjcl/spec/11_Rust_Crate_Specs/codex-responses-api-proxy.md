# `codex-responses-api-proxy`

- path: `codex-rs/responses-api-proxy`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-responses-api-proxy` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `clap`
- `codex-process-hardening`
- `ctor`
- `libc`
- `reqwest`
- `serde`
- `serde_json`
- `tiny_http`
- `zeroize`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub struct Args {`
- `pub fn run_main(args: Args) -> Result<()> {`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
