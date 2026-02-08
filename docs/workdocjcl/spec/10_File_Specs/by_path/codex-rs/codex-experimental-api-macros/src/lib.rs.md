# `codex-rs/codex-experimental-api-macros/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9402`
- sha256: `01effab67dd1c809d81a60ce66cfccec83ac1439e2b7eb622787879e32bb972b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-experimental-api-macros/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn derive_experimental_api(input: TokenStream) -> TokenStream {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:1` `use proc_macro::TokenStream;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:2` `use proc_macro2::Span;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:3` `use quote::quote;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:4` `use syn::Attribute;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:5` `use syn::Data;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:6` `use syn::DataEnum;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:7` `use syn::DataStruct;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:8` `use syn::DeriveInput;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:9` `use syn::Field;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:10` `use syn::Fields;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:11` `use syn::Ident;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:12` `use syn::LitStr;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:13` `use syn::Type;`
- `use` `codex-rs/codex-experimental-api-macros/src/lib.rs:14` `use syn::parse_macro_input;`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:17` `pub fn derive_experimental_api(input: TokenStream) -> TokenStream {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:30` `fn derive_for_struct(input: &DeriveInput, data: &DataStruct) -> TokenStream {`
- `impl` `codex-rs/codex-experimental-api-macros/src/lib.rs:128` `impl #name {`
- `impl` `codex-rs/codex-experimental-api-macros/src/lib.rs:133` `impl crate::experimental_api::ExperimentalApi for #name {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:134` `fn experimental_reason(&self) -> Option<&'static str> {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:142` `fn derive_for_enum(input: &DeriveInput, data: &DataEnum) -> TokenStream {`
- `impl` `codex-rs/codex-experimental-api-macros/src/lib.rs:166` `impl crate::experimental_api::ExperimentalApi for #name {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:167` `fn experimental_reason(&self) -> Option<&'static str> {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:177` `fn experimental_reason(attrs: &[Attribute]) -> Option<LitStr> {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:184` `fn field_serialized_name(field: &Field) -> Option<String> {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:190` `fn snake_to_camel(s: &str) -> String {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:208` `fn experimental_presence_expr(`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:219` `fn index_presence_expr(index: usize, ty: &Type) -> proc_macro2::TokenStream {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:224` `fn presence_expr_for_access(`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:243` `fn presence_expr_for_ref(access: proc_macro2::TokenStream, ty: &Type) -> proc_macro2::TokenStream {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:259` `fn option_inner(ty: &Type) -> Option<&Type> {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:276` `fn is_vec_like(ty: &Type) -> bool {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:280` `fn is_map_like(ty: &Type) -> bool {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:284` `fn is_bool(ty: &Type) -> bool {`
- `fn` `codex-rs/codex-experimental-api-macros/src/lib.rs:288` `fn type_last_ident(ty: &Type) -> Option<Ident> {`

## Dependencies (auto sample)
### Imports / Includes
- `use proc_macro::TokenStream;`
- `use proc_macro2::Span;`
- `use quote::quote;`
- `use syn::Attribute;`
- `use syn::Data;`
- `use syn::DataEnum;`
- `use syn::DataStruct;`
- `use syn::DeriveInput;`
- `use syn::Field;`
- `use syn::Fields;`
- `use syn::Ident;`
- `use syn::LitStr;`
- `use syn::Type;`
- `use syn::parse_macro_input;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
