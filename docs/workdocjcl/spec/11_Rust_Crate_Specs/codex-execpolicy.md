# `codex-execpolicy`

- path: `codex-rs/execpolicy`
- generated_utc: `2026-02-03T09:48:37Z`
- description: Codex exec policy: prefix-based Starlark rules for command decisions.
- role: execpolicy rules and enforcement

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-execpolicy` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `clap`
- `multimap`
- `serde`
- `serde_json`
- `shlex`
- `starlark`
- `thiserror`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod amend;`
- `pub mod decision;`
- `pub mod error;`
- `pub mod execpolicycheck;`
- `pub mod parser;`
- `pub mod policy;`
- `pub mod rule;`
- `pub use amend::AmendError;`
- `pub use amend::blocking_append_allow_prefix_rule;`
- `pub use decision::Decision;`
- `pub use error::Error;`
- `pub use error::ErrorLocation;`
- `pub use error::Result;`
- `pub use error::TextPosition;`
- `pub use error::TextRange;`
- `pub use execpolicycheck::ExecPolicyCheckCommand;`
- `pub use parser::PolicyParser;`
- `pub use policy::Evaluation;`
- `pub use policy::Policy;`
- `pub use rule::Rule;`
- `pub use rule::RuleMatch;`
- `pub use rule::RuleRef;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
