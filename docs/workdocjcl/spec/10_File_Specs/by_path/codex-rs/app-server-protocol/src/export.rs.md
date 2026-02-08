# `codex-rs/app-server-protocol/src/export.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `61535`
- sha256: `48538fd01d3fcb1992e1ebbddcf431ae5cefb14e38fa9cf30d88bf4d61323314`
- generated_utc: `2026-02-03T16:08:28Z`

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
- `fn` `codex-rs/app-server-protocol/src/export.rs:248` `fn filter_experimental_type_fields_ts(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:276` `fn filter_experimental_fields_in_ts_file(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:304` `fn filter_experimental_schema(bundle: &mut Value) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:313` `fn filter_experimental_fields_in_root(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:330` `fn filter_experimental_fields_in_definitions(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:341` `fn filter_experimental_fields_in_definitions_map(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:362` `fn is_namespace_map(value: &Value) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:380` `fn definition_matches_type(def_name: &str, type_name: &str) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:384` `fn remove_property_from_schema(schema: &mut Value, field_name: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:398` `fn prune_experimental_methods(bundle: &mut Value, experimental_methods: &[&str]) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:407` `fn prune_experimental_methods_inner(value: &mut Value, experimental_methods: &HashSet<&str>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:424` `fn is_experimental_method_variant(value: &Value, experimental_methods: &HashSet<&str>) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:449` `fn filter_experimental_json_files(out_dir: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:460` `fn experimental_method_types() -> HashSet<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:467` `fn collect_experimental_type_names(entries: &[&str], out: &mut HashSet<String>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:480` `fn remove_generated_type_files(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:503` `fn remove_experimental_method_type_definitions(bundle: &mut Value) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:511` `fn remove_experimental_method_type_definitions_map(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:541` `fn prune_unused_type_imports(content: String, type_alias_body: &str) -> String {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:560` `fn parse_imported_type_name(line: &str) -> Option<&str> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:571` `fn json_files_in_recursive(dir: &Path) -> Result<Vec<PathBuf>> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:590` `fn read_json_value(path: &Path) -> Result<Value> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:596` `fn split_type_alias(content: &str) -> Option<(String, String, String)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:608` `fn type_body_brace_span(content: &str) -> Option<(usize, usize)> {`
- `const` `codex-rs/app-server-protocol/src/export.rs:615` `const INTERFACE_MARKER: &str = "export interface";`
- `fn` `codex-rs/app-server-protocol/src/export.rs:625` `fn find_top_level_brace_span(input: &str) -> Option<(usize, usize)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:644` `fn split_top_level(input: &str, delimiter: char) -> Vec<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:648` `fn split_top_level_multi(input: &str, delimiters: &[char]) -> Vec<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:669` `fn extract_method_from_arm(arm: &str) -> Option<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:686` `fn parse_property(input: &str) -> Option<(String, &str)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:692` `fn strip_leading_block_comments(input: &str) -> &str {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:705` `fn parse_property_name(input: &str) -> Option<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:741` `fn parse_string_literal(input: &str) -> Option<(String, usize)> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:766` `fn is_ident_char(ch: char) -> bool {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:771` `struct ScanState {`
- `impl` `codex-rs/app-server-protocol/src/export.rs:777` `impl ScanState {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:778` `fn observe(&mut self, ch: char) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:814` `fn in_string(&self) -> bool {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:820` `struct Depth {`
- `impl` `codex-rs/app-server-protocol/src/export.rs:827` `impl Depth {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:828` `fn is_top_level(&self) -> bool {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:833` `fn build_schema_bundle(schemas: Vec<GeneratedSchema>) -> Result<Value> {`
- `const` `codex-rs/app-server-protocol/src/export.rs:834` `const SPECIAL_DEFINITIONS: &[&str] = &[`
- `fn` `codex-rs/app-server-protocol/src/export.rs:922` `fn insert_into_namespace(`
- `fn` `codex-rs/app-server-protocol/src/export.rs:984` `fn write_pretty_json(path: PathBuf, value: &impl Serialize) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:992` `fn split_namespace(name: &str) -> (Option<&str>, &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:999` `fn rewrite_refs_to_namespace(value: &mut Value, ns: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1023` `fn collect_namespaced_types(schemas: &[GeneratedSchema]) -> HashMap<String, String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1059` `fn variant_definition_name(base: &str, variant: &Value) -> Option<String> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1101` `fn string_literal(value: &Value) -> Option<&str> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1111` `fn annotate_schema(value: &mut Value, base: Option<&str>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1123` `fn annotate_object(map: &mut Map<String, Value>, base: Option<&str>) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1178` `fn annotate_variant_list(variants: &mut [Value], base: Option<&str>) {`
- `const` `codex-rs/app-server-protocol/src/export.rs:1218` `const DISCRIMINATOR_KEYS: &[&str] = &["type", "method", "mode", "status", "role", "reason"];`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1220` `fn set_discriminator_titles(props: &mut Map<String, Value>, owner: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1235` `fn variant_title(value: &Value) -> Option<&str> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1242` `fn to_pascal_case(input: &str) -> String {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1263` `fn ensure_dir(dir: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1268` `fn rewrite_named_ref_to_namespace(value: &mut Value, ns: &str, name: &str) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1295` `fn prepend_header_if_missing(path: &Path) -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1317` `fn ts_files_in(dir: &Path) -> Result<Vec<PathBuf>> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1332` `fn ts_files_in_recursive(dir: &Path) -> Result<Vec<PathBuf>> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1354` `fn generate_index_ts(out_dir: &Path) -> Result<PathBuf> {`
- `use` `codex-rs/app-server-protocol/src/export.rs:1395` `use super::*;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1396` `use crate::protocol::v2;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1397` `use anyhow::Result;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1398` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1399` `use std::collections::BTreeSet;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1400` `use std::fs;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1401` `use std::path::PathBuf;`
- `use` `codex-rs/app-server-protocol/src/export.rs:1402` `use uuid::Uuid;`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1405` `fn generated_ts_has_no_optional_nullable_fields() -> Result<()> {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:1410` `struct TempDirGuard(PathBuf);`
- `impl` `codex-rs/app-server-protocol/src/export.rs:1412` `impl Drop for TempDirGuard {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1413` `fn drop(&mut self) {`
- `const` `codex-rs/app-server-protocol/src/export.rs:1471` `const SKIP_PREFIXES: &[&str] = &[`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1628` `fn generate_ts_with_experimental_api_retains_experimental_entries() -> Result<()> {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:1633` `struct TempDirGuard(PathBuf);`
- `impl` `codex-rs/app-server-protocol/src/export.rs:1635` `impl Drop for TempDirGuard {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1636` `fn drop(&mut self) {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1676` `fn stable_schema_filter_removes_mock_thread_start_field() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1702` `fn experimental_type_fields_ts_filter_handles_interface_shape() -> Result<()> {`
- `struct` `codex-rs/app-server-protocol/src/export.rs:1706` `struct TempDirGuard(PathBuf);`
- `impl` `codex-rs/app-server-protocol/src/export.rs:1708` `impl Drop for TempDirGuard {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1709` `fn drop(&mut self) {`
- `static` `codex-rs/app-server-protocol/src/export.rs:1724` `static CUSTOM_FIELD: crate::experimental_api::ExperimentalField =`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1740` `fn stable_schema_filter_removes_mock_experimental_method() -> Result<()> {`
- `fn` `codex-rs/app-server-protocol/src/export.rs:1755` `fn generate_json_filters_experimental_fields_and_methods() -> Result<()> {`

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
