# `codex-rs/utils/image/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8616`
- sha256: `877a98ba0878c617f83d8c9a680c3dc84593d6ab9793f3d7750db79534d4b8ed`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/image/src/lib.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct EncodedImage {`
- `pub fn into_data_url(self) -> String {`
- `pub fn load_and_resize_to_fit(path: &Path) -> Result<EncodedImage, ImageProcessingError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/image/src/lib.rs:1` `use std::num::NonZeroUsize;`
- `use` `codex-rs/utils/image/src/lib.rs:2` `use std::path::Path;`
- `use` `codex-rs/utils/image/src/lib.rs:3` `use std::sync::LazyLock;`
- `use` `codex-rs/utils/image/src/lib.rs:5` `use crate::error::ImageProcessingError;`
- `use` `codex-rs/utils/image/src/lib.rs:6` `use base64::Engine;`
- `use` `codex-rs/utils/image/src/lib.rs:7` `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use` `codex-rs/utils/image/src/lib.rs:8` `use codex_utils_cache::BlockingLruCache;`
- `use` `codex-rs/utils/image/src/lib.rs:9` `use codex_utils_cache::sha1_digest;`
- `use` `codex-rs/utils/image/src/lib.rs:10` `use image::ColorType;`
- `use` `codex-rs/utils/image/src/lib.rs:11` `use image::DynamicImage;`
- `use` `codex-rs/utils/image/src/lib.rs:12` `use image::GenericImageView;`
- `use` `codex-rs/utils/image/src/lib.rs:13` `use image::ImageEncoder;`
- `use` `codex-rs/utils/image/src/lib.rs:14` `use image::ImageFormat;`
- `use` `codex-rs/utils/image/src/lib.rs:15` `use image::codecs::jpeg::JpegEncoder;`
- `use` `codex-rs/utils/image/src/lib.rs:16` `use image::codecs::png::PngEncoder;`
- `use` `codex-rs/utils/image/src/lib.rs:17` `use image::imageops::FilterType;`
- `const` `codex-rs/utils/image/src/lib.rs:19` `pub const MAX_WIDTH: u32 = 2048;`
- `const` `codex-rs/utils/image/src/lib.rs:21` `pub const MAX_HEIGHT: u32 = 768;`
- `mod` `codex-rs/utils/image/src/lib.rs:23` `pub mod error;`
- `struct` `codex-rs/utils/image/src/lib.rs:26` `pub struct EncodedImage {`
- `impl` `codex-rs/utils/image/src/lib.rs:33` `impl EncodedImage {`
- `fn` `codex-rs/utils/image/src/lib.rs:34` `pub fn into_data_url(self) -> String {`
- `static` `codex-rs/utils/image/src/lib.rs:40` `static IMAGE_CACHE: LazyLock<BlockingLruCache<[u8; 20], EncodedImage>> =`
- `fn` `codex-rs/utils/image/src/lib.rs:43` `pub fn load_and_resize_to_fit(path: &Path) -> Result<EncodedImage, ImageProcessingError> {`
- `fn` `codex-rs/utils/image/src/lib.rs:102` `fn read_file_bytes(path: &Path, path_for_error: &Path) -> Result<Vec<u8>, ImageProcessingError> {`
- `fn` `codex-rs/utils/image/src/lib.rs:120` `fn encode_image(`
- `fn` `codex-rs/utils/image/src/lib.rs:162` `fn format_to_mime(format: ImageFormat) -> String {`
- `use` `codex-rs/utils/image/src/lib.rs:171` `use super::*;`
- `use` `codex-rs/utils/image/src/lib.rs:172` `use image::GenericImageView;`
- `use` `codex-rs/utils/image/src/lib.rs:173` `use image::ImageBuffer;`
- `use` `codex-rs/utils/image/src/lib.rs:174` `use image::Rgba;`
- `use` `codex-rs/utils/image/src/lib.rs:175` `use tempfile::NamedTempFile;`
- `fn` `codex-rs/utils/image/src/lib.rs:178` `async fn returns_original_image_when_within_bounds() {`
- `fn` `codex-rs/utils/image/src/lib.rs:196` `async fn downscales_large_image() {`
- `fn` `codex-rs/utils/image/src/lib.rs:214` `async fn fails_cleanly_for_invalid_images() {`
- `fn` `codex-rs/utils/image/src/lib.rs:226` `async fn reprocesses_updated_file_contents() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::num::NonZeroUsize;`
- `use std::path::Path;`
- `use std::sync::LazyLock;`
- `use crate::error::ImageProcessingError;`
- `use base64::Engine;`
- `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use codex_utils_cache::BlockingLruCache;`
- `use codex_utils_cache::sha1_digest;`
- `use image::ColorType;`
- `use image::DynamicImage;`
- `use image::GenericImageView;`
- `use image::ImageEncoder;`
- `use image::ImageFormat;`
- `use image::codecs::jpeg::JpegEncoder;`
- `use image::codecs::png::PngEncoder;`
- `use image::imageops::FilterType;`
- `use super::*;`
- `use image::GenericImageView;`
- `use image::ImageBuffer;`
- `use image::Rgba;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
