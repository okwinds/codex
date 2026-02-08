# `codex-utils-absolute-path`

- path: `codex-rs/utils/absolute-path`
- generated_utc: `2026-02-08T10:45:13Z`
- role: shared utility crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `dirs`
- `path-absolutize`
- `schemars`
- `serde`
- `ts-rs`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub struct AbsolutePathBuf(PathBuf);`
- `pub fn resolve_path_against_base<P: AsRef<Path>, B: AsRef<Path>>(`
- `pub fn from_absolute_path<P: AsRef<Path>>(path: P) -> std::io::Result<Self> {`
- `pub fn current_dir() -> std::io::Result<Self> {`
- `pub fn join<P: AsRef<Path>>(&self, path: P) -> std::io::Result<Self> {`
- `pub fn parent(&self) -> Option<Self> {`
- `pub fn as_path(&self) -> &Path {`
- `pub fn into_path_buf(self) -> PathBuf {`
- `pub fn to_path_buf(&self) -> PathBuf {`
- `pub fn to_string_lossy(&self) -> std::borrow::Cow<'_, str> {`
- `pub fn display(&self) -> Display<'_> {`
- `pub struct AbsolutePathBufGuard;`
- `pub fn new(base_path: &Path) -> Self {`

## Spec Links
- `docs/workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
