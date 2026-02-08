# `codex-cloud-tasks-client`

- path: `codex-rs/cloud-tasks-client`
- generated_utc: `2026-02-08T10:45:13Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `async-trait`
- `chrono`
- `codex-backend-client`
- `codex-git`
- `diffy`
- `serde`
- `serde_json`
- `thiserror`

## Features
- `default`
- `mock`
- `online`

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use api::ApplyOutcome;`
- `pub use api::ApplyStatus;`
- `pub use api::AttemptStatus;`
- `pub use api::CloudBackend;`
- `pub use api::CloudTaskError;`
- `pub use api::CreatedTask;`
- `pub use api::DiffSummary;`
- `pub use api::Result;`
- `pub use api::TaskId;`
- `pub use api::TaskListPage;`
- `pub use api::TaskStatus;`
- `pub use api::TaskSummary;`
- `pub use api::TaskText;`
- `pub use api::TurnAttempt;`
- `pub use mock::MockClient;`
- `pub use http::HttpClient;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
