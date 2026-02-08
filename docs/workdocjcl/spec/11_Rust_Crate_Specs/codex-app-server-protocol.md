# `codex-app-server-protocol`

- path: `codex-rs/app-server-protocol`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `clap`
- `codex-experimental-api-macros`
- `codex-protocol`
- `codex-utils-absolute-path`
- `inventory`
- `schemars`
- `serde`
- `serde_json`
- `strum_macros`
- `thiserror`
- `ts-rs`
- `uuid`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use experimental_api::*;`
- `pub use export::GenerateTsOptions;`
- `pub use export::generate_json;`
- `pub use export::generate_json_with_experimental;`
- `pub use export::generate_ts;`
- `pub use export::generate_ts_with_options;`
- `pub use export::generate_types;`
- `pub use jsonrpc_lite::*;`
- `pub use protocol::common::*;`
- `pub use protocol::thread_history::*;`
- `pub use protocol::v1::*;`
- `pub use protocol::v2::*;`
- `pub use schema_fixtures::SchemaFixtureOptions;`
- `pub use schema_fixtures::read_schema_fixture_tree;`
- `pub use schema_fixtures::write_schema_fixtures;`
- `pub use schema_fixtures::write_schema_fixtures_with_options;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
