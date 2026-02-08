# `codex-ansi-escape`

- path: `codex-rs/ansi-escape`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `ansi-to-tui`
- `ratatui`
- `tracing`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub fn ansi_escape_line(s: &str) -> Line<'static> {`
- `pub fn ansi_escape(s: &str) -> Text<'static> {`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
