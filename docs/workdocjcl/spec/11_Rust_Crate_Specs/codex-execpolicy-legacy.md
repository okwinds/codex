# `codex-execpolicy-legacy`

- path: `codex-rs/execpolicy-legacy`
- generated_utc: `2026-02-08T10:45:13Z`
- description: Legacy exec policy engine for validating proposed exec calls.
- role: execpolicy rules and enforcement

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-execpolicy-legacy` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `allocative`
- `anyhow`
- `clap`
- `derive_more`
- `env_logger`
- `log`
- `multimap`
- `path-absolutize`
- `regex-lite`
- `serde`
- `serde_json`
- `serde_with`
- `starlark`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use arg_matcher::ArgMatcher;`
- `pub use arg_resolver::PositionalArg;`
- `pub use arg_type::ArgType;`
- `pub use error::Error;`
- `pub use error::Result;`
- `pub use exec_call::ExecCall;`
- `pub use execv_checker::ExecvChecker;`
- `pub use opt::Opt;`
- `pub use policy::Policy;`
- `pub use policy_parser::PolicyParser;`
- `pub use program::Forbidden;`
- `pub use program::MatchedExec;`
- `pub use program::NegativeExamplePassedCheck;`
- `pub use program::PositiveExampleFailedCheck;`
- `pub use program::ProgramSpec;`
- `pub use sed_command::parse_sed_command;`
- `pub use valid_exec::MatchedArg;`
- `pub use valid_exec::MatchedFlag;`
- `pub use valid_exec::MatchedOpt;`
- `pub use valid_exec::ValidExec;`
- `pub fn get_default_policy() -> starlark::Result<Policy> {`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
