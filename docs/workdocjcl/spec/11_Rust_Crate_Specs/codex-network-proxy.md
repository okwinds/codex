# `codex-network-proxy`

- path: `codex-rs/network-proxy`
- generated_utc: `2026-02-08T10:45:13Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `true`
- explicit_bins:
  - name: `codex-network-proxy` path: `src/main.rs`

## Key Dependencies (direct, from Cargo.toml)
- `anyhow`
- `async-trait`
- `clap`
- `codex-app-server-protocol`
- `codex-core`
- `codex-utils-absolute-path`
- `globset`
- `rama-core`
- `rama-http`
- `rama-http-backend`
- `rama-net`
- `rama-socks5`
- `rama-tcp`
- `rama-tls-rustls`
- `serde`
- `serde_json`
- `time`
- `tokio`
- `tracing`
- `tracing-subscriber`
- `url`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use network_policy::NetworkDecision;`
- `pub use network_policy::NetworkPolicyDecider;`
- `pub use network_policy::NetworkPolicyRequest;`
- `pub use network_policy::NetworkPolicyRequestArgs;`
- `pub use network_policy::NetworkProtocol;`
- `pub use proxy::Args;`
- `pub use proxy::NetworkProxy;`
- `pub use proxy::NetworkProxyBuilder;`
- `pub use proxy::NetworkProxyHandle;`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
