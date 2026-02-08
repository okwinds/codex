# `codex-backend-client`

- path: `codex-rs/backend-client`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `codex-backend-openapi-models`
- `codex-core`
- `codex-protocol`
- `reqwest`
- `serde`
- `serde_json`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod types;`
- `pub use client::Client;`
- `pub use types::CodeTaskDetailsResponse;`
- `pub use types::CodeTaskDetailsResponseExt;`
- `pub use types::ConfigFileResponse;`
- `pub use types::PaginatedListTaskListItem;`
- `pub use types::TaskListItem;`
- `pub use types::TurnAttemptsSiblingTurnsResponse;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
