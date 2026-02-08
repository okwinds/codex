# `codex-rs/core/src/text_encoding.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19474`
- sha256: `d9dc80483822ddf3d1b0343af8771ffb3c7729d811ed0c0bd14af4ce9fed9a7e`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/text_encoding.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn bytes_to_string_smart(bytes: &[u8]) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/text_encoding.rs:9` `use chardetng::EncodingDetector;`
- `use` `codex-rs/core/src/text_encoding.rs:10` `use encoding_rs::Encoding;`
- `use` `codex-rs/core/src/text_encoding.rs:11` `use encoding_rs::IBM866;`
- `use` `codex-rs/core/src/text_encoding.rs:12` `use encoding_rs::WINDOWS_1252;`
- `fn` `codex-rs/core/src/text_encoding.rs:15` `pub fn bytes_to_string_smart(bytes: &[u8]) -> String {`
- `const` `codex-rs/core/src/text_encoding.rs:38` `const WINDOWS_1252_PUNCT_BYTES: [u8; 8] = [`
- `fn` `codex-rs/core/src/text_encoding.rs:49` `fn detect_encoding(bytes: &[u8]) -> &'static Encoding {`
- `fn` `codex-rs/core/src/text_encoding.rs:70` `fn decode_bytes(bytes: &[u8], encoding: &'static Encoding) -> String {`
- `fn` `codex-rs/core/src/text_encoding.rs:93` `fn looks_like_windows_1252_punctuation(bytes: &[u8]) -> bool {`
- `fn` `codex-rs/core/src/text_encoding.rs:115` `fn is_windows_1252_punct(byte: u8) -> bool {`
- `use` `codex-rs/core/src/text_encoding.rs:121` `use super::*;`
- `use` `codex-rs/core/src/text_encoding.rs:122` `use encoding_rs::BIG5;`
- `use` `codex-rs/core/src/text_encoding.rs:123` `use encoding_rs::EUC_KR;`
- `use` `codex-rs/core/src/text_encoding.rs:124` `use encoding_rs::GBK;`
- `use` `codex-rs/core/src/text_encoding.rs:125` `use encoding_rs::ISO_8859_2;`
- `use` `codex-rs/core/src/text_encoding.rs:126` `use encoding_rs::ISO_8859_3;`
- `use` `codex-rs/core/src/text_encoding.rs:127` `use encoding_rs::ISO_8859_4;`
- `use` `codex-rs/core/src/text_encoding.rs:128` `use encoding_rs::ISO_8859_5;`
- `use` `codex-rs/core/src/text_encoding.rs:129` `use encoding_rs::ISO_8859_6;`
- `use` `codex-rs/core/src/text_encoding.rs:130` `use encoding_rs::ISO_8859_7;`
- `use` `codex-rs/core/src/text_encoding.rs:131` `use encoding_rs::ISO_8859_8;`
- `use` `codex-rs/core/src/text_encoding.rs:132` `use encoding_rs::ISO_8859_10;`
- `use` `codex-rs/core/src/text_encoding.rs:133` `use encoding_rs::ISO_8859_13;`
- `use` `codex-rs/core/src/text_encoding.rs:134` `use encoding_rs::SHIFT_JIS;`
- `use` `codex-rs/core/src/text_encoding.rs:135` `use encoding_rs::WINDOWS_874;`
- `use` `codex-rs/core/src/text_encoding.rs:136` `use encoding_rs::WINDOWS_1250;`
- `use` `codex-rs/core/src/text_encoding.rs:137` `use encoding_rs::WINDOWS_1251;`
- `use` `codex-rs/core/src/text_encoding.rs:138` `use encoding_rs::WINDOWS_1253;`
- `use` `codex-rs/core/src/text_encoding.rs:139` `use encoding_rs::WINDOWS_1254;`
- `use` `codex-rs/core/src/text_encoding.rs:140` `use encoding_rs::WINDOWS_1255;`
- `use` `codex-rs/core/src/text_encoding.rs:141` `use encoding_rs::WINDOWS_1256;`
- `use` `codex-rs/core/src/text_encoding.rs:142` `use encoding_rs::WINDOWS_1257;`
- `use` `codex-rs/core/src/text_encoding.rs:143` `use encoding_rs::WINDOWS_1258;`
- `use` `codex-rs/core/src/text_encoding.rs:144` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/text_encoding.rs:147` `fn test_utf8_passthrough() {`
- `fn` `codex-rs/core/src/text_encoding.rs:155` `fn test_cp1251_russian_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:162` `fn test_cp1251_privet_word() {`
- `fn` `codex-rs/core/src/text_encoding.rs:169` `fn test_koi8_r_privet_word() {`
- `fn` `codex-rs/core/src/text_encoding.rs:176` `fn test_cp866_russian_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:183` `fn test_cp866_uppercase_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:190` `fn test_cp866_uppercase_followed_by_ascii() {`
- `fn` `codex-rs/core/src/text_encoding.rs:198` `fn test_windows_1252_quotes() {`
- `fn` `codex-rs/core/src/text_encoding.rs:205` `fn test_windows_1252_multiple_quotes() {`
- `fn` `codex-rs/core/src/text_encoding.rs:215` `fn test_windows_1252_privet_gibberish_is_preserved() {`
- `fn` `codex-rs/core/src/text_encoding.rs:222` `fn test_iso8859_1_latin_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:231` `fn test_iso8859_2_central_european_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:242` `fn test_iso8859_3_south_europe_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:255` `fn test_iso8859_4_baltic_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:266` `fn test_iso8859_5_cyrillic_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:274` `fn test_iso8859_6_arabic_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:282` `fn test_iso8859_7_greek_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:290` `fn test_iso8859_8_hebrew_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:298` `fn test_iso8859_9_turkish_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:307` `fn test_iso8859_10_nordic_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:316` `fn test_iso8859_11_thai_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:330` `fn test_iso8859_13_baltic_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:338` `fn test_windows_1250_central_european_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:348` `fn test_windows_1251_encoded_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:358` `fn test_windows_1253_greek_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:365` `fn test_windows_1254_turkish_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:372` `fn test_windows_1255_hebrew_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:379` `fn test_windows_1256_arabic_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:386` `fn test_windows_1257_baltic_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:393` `fn test_windows_1258_vietnamese_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:400` `fn test_windows_874_thai_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:410` `fn test_windows_932_shift_jis_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:417` `fn test_windows_936_gbk_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:427` `fn test_windows_949_korean_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:434` `fn test_windows_950_big5_text() {`
- `fn` `codex-rs/core/src/text_encoding.rs:441` `fn test_latin1_cafe() {`
- `fn` `codex-rs/core/src/text_encoding.rs:448` `fn test_preserves_ansi_sequences() {`
- `fn` `codex-rs/core/src/text_encoding.rs:455` `fn test_fallback_to_lossy() {`

## Dependencies (auto sample)
### Imports / Includes
- `use chardetng::EncodingDetector;`
- `use encoding_rs::Encoding;`
- `use encoding_rs::IBM866;`
- `use encoding_rs::WINDOWS_1252;`
- `use super::*;`
- `use encoding_rs::BIG5;`
- `use encoding_rs::EUC_KR;`
- `use encoding_rs::GBK;`
- `use encoding_rs::ISO_8859_2;`
- `use encoding_rs::ISO_8859_3;`
- `use encoding_rs::ISO_8859_4;`
- `use encoding_rs::ISO_8859_5;`
- `use encoding_rs::ISO_8859_6;`
- `use encoding_rs::ISO_8859_7;`
- `use encoding_rs::ISO_8859_8;`
- `use encoding_rs::ISO_8859_10;`
- `use encoding_rs::ISO_8859_13;`
- `use encoding_rs::SHIFT_JIS;`
- `use encoding_rs::WINDOWS_874;`
- `use encoding_rs::WINDOWS_1250;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
