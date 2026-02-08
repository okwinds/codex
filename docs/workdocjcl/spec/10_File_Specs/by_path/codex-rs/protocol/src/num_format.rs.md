# `codex-rs/protocol/src/num_format.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3753`
- sha256: `b0ad98383f652d79346c385ac3a67d09318c9f1adfe33e5b06cc7da351eeb072`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/num_format.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn format_with_separators(n: i64) -> String {`
- `pub fn format_si_suffix(n: i64) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/num_format.rs:1` `use std::sync::OnceLock;`
- `use` `codex-rs/protocol/src/num_format.rs:3` `use icu_decimal::DecimalFormatter;`
- `use` `codex-rs/protocol/src/num_format.rs:4` `use icu_decimal::input::Decimal;`
- `use` `codex-rs/protocol/src/num_format.rs:5` `use icu_decimal::options::DecimalFormatterOptions;`
- `use` `codex-rs/protocol/src/num_format.rs:6` `use icu_locale_core::Locale;`
- `fn` `codex-rs/protocol/src/num_format.rs:8` `fn make_local_formatter() -> Option<DecimalFormatter> {`
- `fn` `codex-rs/protocol/src/num_format.rs:13` `fn make_en_us_formatter() -> DecimalFormatter {`
- `fn` `codex-rs/protocol/src/num_format.rs:20` `fn formatter() -> &'static DecimalFormatter {`
- `static` `codex-rs/protocol/src/num_format.rs:21` `static FORMATTER: OnceLock<DecimalFormatter> = OnceLock::new();`
- `fn` `codex-rs/protocol/src/num_format.rs:27` `pub fn format_with_separators(n: i64) -> String {`
- `fn` `codex-rs/protocol/src/num_format.rs:31` `fn format_with_separators_with_formatter(n: i64, formatter: &DecimalFormatter) -> String {`
- `fn` `codex-rs/protocol/src/num_format.rs:35` `fn format_si_suffix_with_formatter(n: i64, formatter: &DecimalFormatter) -> String {`
- `const` `codex-rs/protocol/src/num_format.rs:50` `const UNITS: [(i64, &str); 3] = [(1_000, "K"), (1_000_000, "M"), (1_000_000_000, "G")];`
- `fn` `codex-rs/protocol/src/num_format.rs:75` `pub fn format_si_suffix(n: i64) -> String {`
- `use` `codex-rs/protocol/src/num_format.rs:81` `use super::*;`
- `fn` `codex-rs/protocol/src/num_format.rs:84` `fn kmg() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::OnceLock;`
- `use icu_decimal::DecimalFormatter;`
- `use icu_decimal::input::Decimal;`
- `use icu_decimal::options::DecimalFormatterOptions;`
- `use icu_locale_core::Locale;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
