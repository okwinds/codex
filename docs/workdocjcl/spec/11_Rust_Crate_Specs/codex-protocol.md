# `codex-protocol`

- path: `codex-rs/protocol`
- generated_utc: `2026-02-08T10:45:13Z`
- role: shared protocol types (events/config/model I/O) used across crates

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `codex-execpolicy`
- `codex-git`
- `codex-utils-absolute-path`
- `codex-utils-image`
- `icu_decimal`
- `icu_locale_core`
- `icu_provider`
- `mime_guess`
- `schemars`
- `serde`
- `serde_json`
- `serde_with`
- `strum`
- `strum_macros`
- `sys-locale`
- `tracing`
- `ts-rs`
- `uuid`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod account;`
- `pub use thread_id::ThreadId;`
- `pub mod approvals;`
- `pub mod config_types;`
- `pub mod custom_prompts;`
- `pub mod dynamic_tools;`
- `pub mod items;`
- `pub mod mcp;`
- `pub mod message_history;`
- `pub mod models;`
- `pub mod num_format;`
- `pub mod openai_models;`
- `pub mod parse_command;`
- `pub mod plan_tool;`
- `pub mod protocol;`
- `pub mod request_user_input;`
- `pub mod user_input;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
