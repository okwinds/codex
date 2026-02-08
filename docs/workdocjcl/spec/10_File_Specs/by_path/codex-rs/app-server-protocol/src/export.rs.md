# `codex-rs/app-server-protocol/src/export.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `63942`
- sha256: `5bf65863a07eee3f7460c96be67b529e4d0c3e04269a583a89e3531e6608e0fb`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/export.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct GeneratedSchema {`
- `pub fn generate_types(out_dir: &Path, prettier: Option<&Path>) -> Result<()> {`
- `pub struct GenerateTsOptions {`
- `pub fn generate_ts(out_dir: &Path, prettier: Option<&Path>) -> Result<()> {`
- `pub fn generate_ts_with_options(`
- `pub fn generate_json(out_dir: &Path) -> Result<()> {`
- `pub fn generate_json_with_experimental(out_dir: &Path, experimental_api: bool) -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/export.rs:1` `use crate::ClientNotification;`
- `use` `codex-rs/app-server-protocol/src/export.rs:2` `use crate::ClientRequest;`
- `use` `codex-rs/app-server-protocol/src/export.rs:3` `use crate::ServerNotification;`
- `use` `codex-rs/app-server-protocol/src/export.rs:4` `use crate::ServerRequest;`
- `use` `codex-rs/app-server-protocol/src/export.rs:5` `use crate::experimental_api::experimental_fields;`
- `use` `codex-rs/app-server-protocol/src/export.rs:6` `use crate::export_client_notification_schemas;`
- `use` `codex-rs/app-server-protocol/src/export.rs:7` `use crate::export_client_param_schemas;`
- `use` `codex-rs/app-server-protocol/src/export.rs:8` `use crate::export_client_response_schemas;`
- `use` `codex-rs/app-server-protocol/src/export.rs:9` `use crate::export_client_responses;`
- `use` `codex-rs/app-server-protocol/src/export.rs:10` `use crate::export_server_notification_schemas;`
- `use` `codex-rs/app-server-protocol/src/export.rs:11` `use crate::export_server_param_schemas;`
- `use` `codex-rs/app-server-protocol/src/export.rs:12` `use crate::export_server_response_schemas;`
- `use` `codex-rs/app-server-protocol/src/export.rs:13` `use crate::export_server_responses;`
- `use` `codex-rs/app-server-protocol/src/export.rs:14` `use crate::protocol::common::EXPERIMENTAL_CLIENT_METHOD_PARAM_TYPES;`
- `use` `codex-rs/app-server-protocol/src/export.rs:15` `use crate::protocol::common::EXPERIMENTAL_CLIENT_METHOD_RESPONSE_TYPES;`
- `use` `codex-rs/app-server-protocol/src/export.rs:16` `use crate::protocol::common::EXPERIMENTAL_CLIENT_METHODS;`
- `use` `codex-rs/app-server-protocol/src/export.rs:17` `use anyhow::Context;`
- `use` `codex-rs/app-server-protocol/src/export.rs:18` `use anyhow::Result;`
- `use` `codex-rs/app-server-protocol/src/export.rs:19` `use anyhow::anyhow;`
- `use` `codex-rs/app-server-protocol/src/export.rs:20` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/app-server-protocol/src/export.rs:21` `use schemars::JsonSchema;`
- `use` `codex-rs/app-server-protocol/src/export.rs:22` `use schemars::schema_for;`
- `use` `codex-rs/app-server-protocol/src/export.rs:23` `use serde::Serialize;`
- `use` `codex-rs/app-server-protocol/src/export.rs:24` `use serde_json::Map;`
- `use` `codex-rs/app-server-protocol/src/export.rs:25` `use serde_json::Value;`
- `use` `codex-rs/app-server-protocol/src/export.rs:26` `use std::collections::HashMap;`
- `use` `codex-rs/app-server-protocol/src/export.rs:27` `use std::collections::HashSet;`
- `use` `codex-rs/app-server-protocol/src/export.rs:28` `use std::ffi::OsStr;`
- `use` `codex-rs/app-server-protocol/src/export.rs:29` `use std::fs;`
- `use` `codex-rs/app-server-protocol/src/export.rs:30` `use std::io::Read;`
- `use` `codex-rs/app-server-protocol/src/export.rs:31` `use std::io::Write;`
- `use` `codex-rs/app-server-protocol/src/export.rs:32` `use std::path::Path;`
- `use` `codex-rs/app-server-protocol/src/export.rs:33` `use std::path::PathBuf;`
- `use` `codex-rs/app-server-protocol/src/export.rs:34` `use std::process::Command;`
- `use` `codex-rs/app-server-protocol/src/export.rs:35` `use ts_rs::TS;`
- `const` `codex-rs/app-server-protocol/src/export.rs:37` `const HEADER: &str = "// GENERATED CODE! DO NOT MODIFY BY HAND!\n\n";`
- `const` `codex-rs/app-server-protocol/src/export.rs:38` `const IGNORED_DEFINITIONS: &[&str] = &["Option<()>"];`
- `struct` `codex-rs/app-server-protocol/src/export.rs:41` `pub struct GeneratedSchema {`
- `impl` `codex-rs/app-server-protocol/src/export.rs:48` `impl GeneratedSchema {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:49` `fn namespace(&self) -> Option<&str> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:53` `fn logical_name(&self) -> &str {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:57` `fn value(&self) -> &Value {`
- `type` `codex-rs/app-server-protocol/src/export.rs:62` `type JsonSchemaEmitter = fn(&Path) -> Result<GeneratedSchema>;`
- `fn` `codex-rs/app-server-protocol/src/export.rs:63` `pub fn generate_types(out_dir: &Path, prettier: Option<&Path>) -> Result<()> {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:70` `pub struct GenerateTsOptions {`
- `impl` `codex-rs/app-server-protocol/src/export.rs:77` `impl Default for GenerateTsOptions {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:78` `fn default() -> Self {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:88` `pub fn generate_ts(out_dir: &Path, prettier: Option<&Path>) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:92` `pub fn generate_ts_with_options(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:152` `pub fn generate_json(out_dir: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:156` `pub fn generate_json_with_experimental(out_dir: &Path, experimental_api: bool) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:201` `fn filter_experimental_ts(out_dir: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:215` `fn filter_client_request_ts(out_dir: &Path, experimental_methods: &[&str]) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:251` `fn filter_experimental_type_fields_ts(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:279` `fn filter_experimental_fields_in_ts_file(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:310` `fn filter_experimental_schema(bundle: &mut Value) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:319` `fn filter_experimental_fields_in_root(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:336` `fn filter_experimental_fields_in_definitions(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:347` `fn filter_experimental_fields_in_definitions_map(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:368` `fn is_namespace_map(value: &Value) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:386` `fn definition_matches_type(def_name: &str, type_name: &str) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:390` `fn remove_property_from_schema(schema: &mut Value, field_name: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:404` `fn prune_experimental_methods(bundle: &mut Value, experimental_methods: &[&str]) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:413` `fn prune_experimental_methods_inner(value: &mut Value, experimental_methods: &HashSet<&str>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:430` `fn is_experimental_method_variant(value: &Value, experimental_methods: &HashSet<&str>) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:455` `fn filter_experimental_json_files(out_dir: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:466` `fn experimental_method_types() -> HashSet<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:473` `fn collect_experimental_type_names(entries: &[&str], out: &mut HashSet<String>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:486` `fn remove_generated_type_files(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:509` `fn remove_experimental_method_type_definitions(bundle: &mut Value) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:517` `fn remove_experimental_method_type_definitions_map(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:547` `fn prune_unused_type_imports(content: String, type_alias_body: &str) -> String {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:566` `fn parse_imported_type_name(line: &str) -> Option<&str> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:577` `fn json_files_in_recursive(dir: &Path) -> Result<Vec<PathBuf>> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:596` `fn read_json_value(path: &Path) -> Result<Value> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:602` `fn split_type_alias(content: &str) -> Option<(String, String, String)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:614` `fn type_body_brace_span(content: &str) -> Option<(usize, usize)> {`
- `const` `codex-rs/app-server-protocol/src/export.rs:621` `const INTERFACE_MARKER: &str = "export interface";`
- `fn` `codex-rs/app-server-protocol/src/export.rs:631` `fn find_top_level_brace_span(input: &str) -> Option<(usize, usize)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:650` `fn split_top_level(input: &str, delimiter: char) -> Vec<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:654` `fn split_top_level_multi(input: &str, delimiters: &[char]) -> Vec<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:675` `fn extract_method_from_arm(arm: &str) -> Option<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:692` `fn parse_property(input: &str) -> Option<(String, &str)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:698` `fn strip_leading_block_comments(input: &str) -> &str {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:711` `fn parse_property_name(input: &str) -> Option<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:747` `fn parse_string_literal(input: &str) -> Option<(String, usize)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:772` `fn is_ident_char(ch: char) -> bool {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:777` `struct ScanState {`
- `impl` `codex-rs/app-server-protocol/src/export.rs:783` `impl ScanState {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:784` `fn observe(&mut self, ch: char) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:820` `fn in_string(&self) -> bool {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:826` `struct Depth {`
- `impl` `codex-rs/app-server-protocol/src/export.rs:833` `impl Depth {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:834` `fn is_top_level(&self) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:839` `fn build_schema_bundle(schemas: Vec<GeneratedSchema>) -> Result<Value> {`
- `const` `codex-rs/app-server-protocol/src/export.rs:840` `const SPECIAL_DEFINITIONS: &[&str] = &[`
- `fn` `codex-rs/app-server-protocol/src/export.rs:928` `fn insert_into_namespace(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:990` `fn write_pretty_json(path: PathBuf, value: &impl Serialize) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:998` `fn split_namespace(name: &str) -> (Option<&str>, &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1005` `fn rewrite_refs_to_namespace(value: &mut Value, ns: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1029` `fn collect_namespaced_types(schemas: &[GeneratedSchema]) -> HashMap<String, String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1065` `fn variant_definition_name(base: &str, variant: &Value) -> Option<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1107` `fn string_literal(value: &Value) -> Option<&str> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1117` `fn annotate_schema(value: &mut Value, base: Option<&str>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1129` `fn annotate_object(map: &mut Map<String, Value>, base: Option<&str>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1184` `fn annotate_variant_list(variants: &mut [Value], base: Option<&str>) {`
- `const` `codex-rs/app-server-protocol/src/export.rs:1224` `const DISCRIMINATOR_KEYS: &[&str] = &["type", "method", "mode", "status", "role", "reason"];`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1226` `fn set_discriminator_titles(props: &mut Map<String, Value>, owner: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1241` `fn variant_title(value: &Value) -> Option<&str> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1248` `fn to_pascal_case(input: &str) -> String {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1269` `fn ensure_dir(dir: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1274` `fn rewrite_named_ref_to_namespace(value: &mut Value, ns: &str, name: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1301` `fn prepend_header_if_missing(path: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1323` `fn ts_files_in(dir: &Path) -> Result<Vec<PathBuf>> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1338` `fn ts_files_in_recursive(dir: &Path) -> Result<Vec<PathBuf>> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1360` `fn generate_index_ts(out_dir: &Path) -> Result<PathBuf> {`
- `use` `codex-rs/app-server-protocol/src/export.rs:1401` `use super::*;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1402` `use crate::protocol::v2;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1403` `use anyhow::Result;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1404` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1405` `use std::collections::BTreeSet;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1406` `use std::fs;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1407` `use std::path::PathBuf;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1408` `use uuid::Uuid;`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1411` `fn generated_ts_optional_nullable_fields_only_in_params() -> Result<()> {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:1416` `struct TempDirGuard(PathBuf);`
- `impl` `codex-rs/app-server-protocol/src/export.rs:1418` `impl Drop for TempDirGuard {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1419` `fn drop(&mut self) {`
- `const` `codex-rs/app-server-protocol/src/export.rs:1484` `const SKIP_PREFIXES: &[&str] = &[`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1643` `fn generate_ts_with_experimental_api_retains_experimental_entries() -> Result<()> {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:1648` `struct TempDirGuard(PathBuf);`
- `impl` `codex-rs/app-server-protocol/src/export.rs:1650` `impl Drop for TempDirGuard {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1651` `fn drop(&mut self) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1691` `fn stable_schema_filter_removes_mock_thread_start_field() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1717` `fn experimental_type_fields_ts_filter_handles_interface_shape() -> Result<()> {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:1721` `struct TempDirGuard(PathBuf);`
- `impl` `codex-rs/app-server-protocol/src/export.rs:1723` `impl Drop for TempDirGuard {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1724` `fn drop(&mut self) {`
- `static` `codex-rs/app-server-protocol/src/export.rs:1739` `static CUSTOM_FIELD: crate::experimental_api::ExperimentalField =`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1755` `fn experimental_type_fields_ts_filter_keeps_imports_used_in_intersection_suffix() -> Result<()>`
- `struct` `codex-rs/app-server-protocol/src/export.rs:1760` `struct TempDirGuard(PathBuf);`
- `impl` `codex-rs/app-server-protocol/src/export.rs:1762` `impl Drop for TempDirGuard {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1763` `fn drop(&mut self) {`
- `static` `codex-rs/app-server-protocol/src/export.rs:1777` `static CUSTOM_FIELD: crate::experimental_api::ExperimentalField =`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1799` `fn stable_schema_filter_removes_mock_experimental_method() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1814` `fn generate_json_filters_experimental_fields_and_methods() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::ClientNotification;`
- `use crate::ClientRequest;`
- `use crate::ServerNotification;`
- `use crate::ServerRequest;`
- `use crate::experimental_api::experimental_fields;`
- `use crate::export_client_notification_schemas;`
- `use crate::export_client_param_schemas;`
- `use crate::export_client_response_schemas;`
- `use crate::export_client_responses;`
- `use crate::export_server_notification_schemas;`
- `use crate::export_server_param_schemas;`
- `use crate::export_server_response_schemas;`
- `use crate::export_server_responses;`
- `use crate::protocol::common::EXPERIMENTAL_CLIENT_METHOD_PARAM_TYPES;`
- `use crate::protocol::common::EXPERIMENTAL_CLIENT_METHOD_RESPONSE_TYPES;`
- `use crate::protocol::common::EXPERIMENTAL_CLIENT_METHODS;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use codex_protocol::protocol::EventMsg;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
