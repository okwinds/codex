# `codex-rs/core/src/config_loader/diagnostics.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12150`
- sha256: `4b3ea0730ed0779f400c071adb4492f98dd8743a633f40884d65c317c20df7a8`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/diagnostics.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct TextPosition {`
- `pub struct TextRange {`
- `pub struct ConfigError {`
- `pub fn new(path: PathBuf, range: TextRange, message: impl Into<String>) -> Self {`
- `pub struct ConfigLoadError {`
- `pub fn new(error: ConfigError, source: Option<toml::de::Error>) -> Self {`
- `pub fn config_error(&self) -> &ConfigError {`
- `pub fn format_config_error(error: &ConfigError, contents: &str) -> String {`
- `pub fn format_config_error_with_source(error: &ConfigError) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:4` `use crate::config::CONFIG_TOML_FILE;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:5` `use crate::config::ConfigToml;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:6` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:7` `use codex_utils_absolute_path::AbsolutePathBufGuard;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:8` `use serde_path_to_error::Path as SerdePath;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:9` `use serde_path_to_error::Segment as SerdeSegment;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:10` `use std::fmt;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:11` `use std::fmt::Write;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:12` `use std::io;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:13` `use std::path::Path;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:14` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:15` `use toml_edit::Document;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:16` `use toml_edit::Item;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:17` `use toml_edit::Table;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:18` `use toml_edit::Value;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:20` `use super::ConfigLayerEntry;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:21` `use super::ConfigLayerStack;`
- `use` `codex-rs/core/src/config_loader/diagnostics.rs:22` `use super::ConfigLayerStackOrdering;`
- `struct` `codex-rs/core/src/config_loader/diagnostics.rs:25` `pub struct TextPosition {`
- `struct` `codex-rs/core/src/config_loader/diagnostics.rs:32` `pub struct TextRange {`
- `struct` `codex-rs/core/src/config_loader/diagnostics.rs:38` `pub struct ConfigError {`
- `impl` `codex-rs/core/src/config_loader/diagnostics.rs:44` `impl ConfigError {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:45` `pub fn new(path: PathBuf, range: TextRange, message: impl Into<String>) -> Self {`
- `struct` `codex-rs/core/src/config_loader/diagnostics.rs:55` `pub struct ConfigLoadError {`
- `impl` `codex-rs/core/src/config_loader/diagnostics.rs:60` `impl ConfigLoadError {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:61` `pub fn new(error: ConfigError, source: Option<toml::de::Error>) -> Self {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:65` `pub fn config_error(&self) -> &ConfigError {`
- `impl` `codex-rs/core/src/config_loader/diagnostics.rs:70` `impl fmt::Display for ConfigLoadError {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:71` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `impl` `codex-rs/core/src/config_loader/diagnostics.rs:83` `impl std::error::Error for ConfigLoadError {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:84` `fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:185` `fn config_path_for_layer(layer: &ConfigLayerEntry) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:199` `fn text_range_from_span(contents: &str, span: std::ops::Range<usize>) -> TextRange {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:210` `pub fn format_config_error(error: &ConfigError, contents: &str) -> String {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:246` `pub fn format_config_error_with_source(error: &ConfigError) -> String {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:253` `fn position_for_offset(contents: &str, index: usize) -> TextPosition {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:284` `fn default_range() -> TextRange {`
- `enum` `codex-rs/core/src/config_loader/diagnostics.rs:292` `enum TomlNode<'a> {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:298` `fn span_for_path(contents: &str, path: &SerdePath) -> Option<std::ops::Range<usize>> {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:308` `fn span_for_config_path(contents: &str, path: &SerdePath) -> Option<std::ops::Range<usize>> {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:317` `fn is_features_table_path(path: &SerdePath) -> bool {`
- `fn` `codex-rs/core/src/config_loader/diagnostics.rs:323` `fn span_for_features_value(contents: &str) -> Option<std::ops::Range<usize>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::CONFIG_TOML_FILE;`
- `use crate::config::ConfigToml;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_utils_absolute_path::AbsolutePathBufGuard;`
- `use serde_path_to_error::Path as SerdePath;`
- `use serde_path_to_error::Segment as SerdeSegment;`
- `use std::fmt;`
- `use std::fmt::Write;`
- `use std::io;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use toml_edit::Document;`
- `use toml_edit::Item;`
- `use toml_edit::Table;`
- `use toml_edit::Value;`
- `use super::ConfigLayerEntry;`
- `use super::ConfigLayerStack;`
- `use super::ConfigLayerStackOrdering;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
