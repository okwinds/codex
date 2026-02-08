# `codex-state`

- path: `codex-rs/state`
- generated_utc: `2026-02-08T10:45:13Z`
- role: SQLite-backed state DB and rollout metadata extraction

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `chrono`
- `clap`
- `codex-otel`
- `codex-protocol`
- `dirs`
- `log`
- `owo-colors`
- `serde`
- `serde_json`
- `sqlx`
- `tokio`
- `tracing`
- `tracing-subscriber`
- `uuid`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod log_db;`
- `pub use model::LogEntry;`
- `pub use model::LogQuery;`
- `pub use model::LogRow;`
- `pub use runtime::StateRuntime;`
- `pub use extract::apply_rollout_item;`
- `pub use model::Anchor;`
- `pub use model::BackfillState;`
- `pub use model::BackfillStats;`
- `pub use model::BackfillStatus;`
- `pub use model::ExtractionOutcome;`
- `pub use model::SortKey;`
- `pub use model::ThreadMemory;`
- `pub use model::ThreadMetadata;`
- `pub use model::ThreadMetadataBuilder;`
- `pub use model::ThreadsPage;`
- `pub use runtime::STATE_DB_FILENAME;`
- `pub use runtime::STATE_DB_VERSION;`
- `pub use runtime::state_db_filename;`
- `pub use runtime::state_db_path;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
