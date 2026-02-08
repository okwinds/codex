# `codex-common`

- path: `codex-rs/common`
- generated_utc: `2026-02-08T10:45:13Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `clap`
- `codex-core`
- `codex-lmstudio`
- `codex-ollama`
- `codex-protocol`
- `serde`
- `toml`

## Features
- `cli`
- `elapsed`
- `sandbox_summary`

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod elapsed;`
- `pub use approval_mode_cli_arg::ApprovalModeCliArg;`
- `pub use sandbox_mode_cli_arg::SandboxModeCliArg;`
- `pub mod format_env_display;`
- `pub use config_override::CliConfigOverrides;`
- `pub use sandbox_summary::summarize_sandbox_policy;`
- `pub use config_summary::create_config_summary_entries;`
- `pub mod fuzzy_match;`
- `pub mod approval_presets;`
- `pub mod oss;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
