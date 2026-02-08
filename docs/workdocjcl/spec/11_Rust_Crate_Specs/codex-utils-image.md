# `codex-utils-image`

- path: `codex-rs/utils/image`
- generated_utc: `2026-02-03T09:48:37Z`
- role: shared utility crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `base64`
- `codex-utils-cache`
- `image`
- `thiserror`
- `tokio`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod error;`
- `pub struct EncodedImage {`
- `pub fn into_data_url(self) -> String {`
- `pub fn load_and_resize_to_fit(path: &Path) -> Result<EncodedImage, ImageProcessingError> {`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
