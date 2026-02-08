# `codex-rs/core/src/features.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `20031`
- sha256: `a48731adba853cfbbfbb74e7be36e5aca916e0720e93e38357ac66d6e7945c04`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/features.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum Stage {`
- `pub fn experimental_menu_name(self) -> Option<&'static str> {`
- `pub fn experimental_menu_description(self) -> Option<&'static str> {`
- `pub fn experimental_announcement(self) -> Option<&'static str> {`
- `pub enum Feature {`
- `pub fn key(self) -> &'static str {`
- `pub fn stage(self) -> Stage {`
- `pub fn default_enabled(self) -> bool {`
- `pub struct LegacyFeatureUsage {`
- `pub struct Features {`
- `pub struct FeatureOverrides {`
- `pub fn with_defaults() -> Self {`
- `pub fn enabled(&self, f: Feature) -> bool {`
- `pub fn enable(&mut self, f: Feature) -> &mut Self {`
- `pub fn disable(&mut self, f: Feature) -> &mut Self {`
- `pub fn record_legacy_usage_force(&mut self, alias: &str, feature: Feature) {`
- `pub fn record_legacy_usage(&mut self, alias: &str, feature: Feature) {`
- `pub fn legacy_feature_usages(&self) -> impl Iterator<Item = &LegacyFeatureUsage> + '_ {`
- `pub fn emit_metrics(&self, otel: &OtelManager) {`
- `pub fn apply_map(&mut self, m: &BTreeMap<String, bool>) {`
- `pub fn from_config(`
- `pub fn enabled_features(&self) -> Vec<Feature> {`
- `pub fn is_known_feature_key(key: &str) -> bool {`
- `pub struct FeaturesToml {`
- `pub struct FeatureSpec {`
- `pub fn maybe_push_unstable_features_warning(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/features.rs:8` `use crate::config::CONFIG_TOML_FILE;`
- `use` `codex-rs/core/src/features.rs:9` `use crate::config::Config;`
- `use` `codex-rs/core/src/features.rs:10` `use crate::config::ConfigToml;`
- `use` `codex-rs/core/src/features.rs:11` `use crate::config::profile::ConfigProfile;`
- `use` `codex-rs/core/src/features.rs:12` `use crate::protocol::Event;`
- `use` `codex-rs/core/src/features.rs:13` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/features.rs:14` `use crate::protocol::WarningEvent;`
- `use` `codex-rs/core/src/features.rs:15` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/features.rs:16` `use schemars::JsonSchema;`
- `use` `codex-rs/core/src/features.rs:17` `use serde::Deserialize;`
- `use` `codex-rs/core/src/features.rs:18` `use serde::Serialize;`
- `use` `codex-rs/core/src/features.rs:19` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/features.rs:20` `use std::collections::BTreeSet;`
- `use` `codex-rs/core/src/features.rs:21` `use toml::Value as TomlValue;`
- `mod` `codex-rs/core/src/features.rs:23` `mod legacy;`
- `enum` `codex-rs/core/src/features.rs:29` `pub enum Stage {`
- `impl` `codex-rs/core/src/features.rs:46` `impl Stage {`
- `fn` `codex-rs/core/src/features.rs:47` `pub fn experimental_menu_name(self) -> Option<&'static str> {`
- `fn` `codex-rs/core/src/features.rs:54` `pub fn experimental_menu_description(self) -> Option<&'static str> {`
- `fn` `codex-rs/core/src/features.rs:63` `pub fn experimental_announcement(self) -> Option<&'static str> {`
- `enum` `codex-rs/core/src/features.rs:73` `pub enum Feature {`
- `impl` `codex-rs/core/src/features.rs:134` `impl Feature {`
- `fn` `codex-rs/core/src/features.rs:135` `pub fn key(self) -> &'static str {`
- `fn` `codex-rs/core/src/features.rs:139` `pub fn stage(self) -> Stage {`
- `fn` `codex-rs/core/src/features.rs:143` `pub fn default_enabled(self) -> bool {`
- `fn` `codex-rs/core/src/features.rs:147` `fn info(self) -> &'static FeatureSpec {`
- `struct` `codex-rs/core/src/features.rs:156` `pub struct LegacyFeatureUsage {`
- `struct` `codex-rs/core/src/features.rs:165` `pub struct Features {`
- `struct` `codex-rs/core/src/features.rs:171` `pub struct FeatureOverrides {`
- `impl` `codex-rs/core/src/features.rs:176` `impl FeatureOverrides {`
- `fn` `codex-rs/core/src/features.rs:177` `fn apply(self, features: &mut Features) {`
- `impl` `codex-rs/core/src/features.rs:187` `impl Features {`
- `fn` `codex-rs/core/src/features.rs:189` `pub fn with_defaults() -> Self {`
- `fn` `codex-rs/core/src/features.rs:202` `pub fn enabled(&self, f: Feature) -> bool {`
- `fn` `codex-rs/core/src/features.rs:206` `pub fn enable(&mut self, f: Feature) -> &mut Self {`
- `fn` `codex-rs/core/src/features.rs:211` `pub fn disable(&mut self, f: Feature) -> &mut Self {`
- `fn` `codex-rs/core/src/features.rs:216` `pub fn record_legacy_usage_force(&mut self, alias: &str, feature: Feature) {`
- `fn` `codex-rs/core/src/features.rs:226` `pub fn record_legacy_usage(&mut self, alias: &str, feature: Feature) {`
- `fn` `codex-rs/core/src/features.rs:233` `pub fn legacy_feature_usages(&self) -> impl Iterator<Item = &LegacyFeatureUsage> + '_ {`
- `fn` `codex-rs/core/src/features.rs:237` `pub fn emit_metrics(&self, otel: &OtelManager) {`
- `fn` `codex-rs/core/src/features.rs:253` `pub fn apply_map(&mut self, m: &BTreeMap<String, bool>) {`
- `fn` `codex-rs/core/src/features.rs:288` `pub fn from_config(`
- `fn` `codex-rs/core/src/features.rs:325` `pub fn enabled_features(&self) -> Vec<Feature> {`
- `fn` `codex-rs/core/src/features.rs:330` `fn legacy_usage_notice(alias: &str, feature: Feature) -> (String, Option<String>) {`
- `fn` `codex-rs/core/src/features.rs:362` `fn web_search_details() -> &'static str {`
- `fn` `codex-rs/core/src/features.rs:367` `fn feature_for_key(key: &str) -> Option<Feature> {`
- `fn` `codex-rs/core/src/features.rs:377` `pub fn is_known_feature_key(key: &str) -> bool {`
- `struct` `codex-rs/core/src/features.rs:383` `pub struct FeaturesToml {`
- `struct` `codex-rs/core/src/features.rs:390` `pub struct FeatureSpec {`
- `const` `codex-rs/core/src/features.rs:397` `pub const FEATURES: &[FeatureSpec] = &[`
- `fn` `codex-rs/core/src/features.rs:583` `pub fn maybe_push_unstable_features_warning(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::CONFIG_TOML_FILE;`
- `use crate::config::Config;`
- `use crate::config::ConfigToml;`
- `use crate::config::profile::ConfigProfile;`
- `use crate::protocol::Event;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::WarningEvent;`
- `use codex_otel::OtelManager;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::collections::BTreeMap;`
- `use std::collections::BTreeSet;`
- `use toml::Value as TomlValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
