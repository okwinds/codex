# `codex-tui`

- path: `codex-rs/tui`
- generated_utc: `2026-02-08T10:45:13Z`
- role: terminal UI (ratatui-based) and interactive runtime

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-tui` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `base64`
- `chrono`
- `clap`
- `codex-ansi-escape`
- `codex-app-server-protocol`
- `codex-arg0`
- `codex-backend-client`
- `codex-chatgpt`
- `codex-cloud-requirements`
- `codex-common`
- `codex-core`
- `codex-feedback`
- `codex-file-search`
- `codex-login`
- `codex-otel`
- `codex-protocol`
- `codex-state`
- `codex-utils-absolute-path`
- `codex-windows-sandbox`
- `color-eyre`
- `crossterm`
- `derive_more`
- `diffy`
- `dirs`
- `dunce`
- `image`
- `itertools`
- `lazy_static`
- `pathdiff`
- `pulldown-cmark`
- `rand`
- `ratatui`
- `ratatui-macros`
- `regex-lite`
- `reqwest`
- `rmcp`
- `serde`
- `serde_json`
- `shlex`
- `strum`
- `strum_macros`
- `supports-color`
- `tempfile`
- `textwrap`
- `thiserror`
- `tokio`
- `tokio-stream`
- `tokio-util`
- `toml`
- `tracing`
- `tracing-appender`
- `tracing-subscriber`
- `tree-sitter-bash`
- `tree-sitter-highlight`
- `unicode-segmentation`
- `unicode-width`
- `url`
- `uuid`

## Features
- `debug-logs`
- `vt100-tests`

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use app::AppExitInfo;`
- `pub use app::ExitReason;`
- `pub mod custom_terminal;`
- `pub mod insert_history;`
- `pub mod live_wrap;`
- `pub mod onboarding;`
- `pub mod public_widgets;`
- `pub mod update_action;`
- `pub mod test_backend;`
- `pub use cli::Cli;`
- `pub use markdown_render::render_markdown_text;`
- `pub use public_widgets::composer_input::ComposerAction;`
- `pub use public_widgets::composer_input::ComposerInput;`
- `pub enum LoginStatus {`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
