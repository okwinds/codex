# `codex-rs/codex-api/tests/models_integration.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4241`
- sha256: `d295c3f3b660048107cd4395f641c2e185925383d23dd499304fd65ab8d895c4`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/tests/models_integration.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_api::AuthProvider;`
- `use codex_api::ModelsClient;`
- `use codex_api::provider::Provider;`
- `use codex_api::provider::RetryConfig;`
- `use codex_client::ReqwestTransport;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelVisibility;`
- `use codex_protocol::openai_models::ModelsResponse;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use codex_protocol::openai_models::TruncationPolicyConfig;`
- `use codex_protocol::openai_models::default_input_modalities;`
- `use http::HeaderMap;`
- `use http::Method;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
