# `codex-utils-cache`

- path: `codex-rs/utils/cache`
- generated_utc: `2026-02-03T09:48:37Z`
- role: shared utility crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `lru`
- `sha1`
- `tokio`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub struct BlockingLruCache<K, V> {`
- `pub fn new(capacity: NonZeroUsize) -> Self {`
- `pub fn get_or_insert_with(&self, key: K, value: impl FnOnce() -> V) -> V`
- `pub fn get_or_try_insert_with<E>(`
- `pub fn try_with_capacity(capacity: usize) -> Option<Self> {`
- `pub fn get<Q>(&self, key: &Q) -> Option<V>`
- `pub fn insert(&self, key: K, value: V) -> Option<V> {`
- `pub fn remove<Q>(&self, key: &Q) -> Option<V>`
- `pub fn clear(&self) {`
- `pub fn with_mut<R>(&self, callback: impl FnOnce(&mut LruCache<K, V>) -> R) -> R {`
- `pub fn blocking_lock(&self) -> Option<MutexGuard<'_, LruCache<K, V>>> {`
- `pub fn sha1_digest(bytes: &[u8]) -> [u8; 20] {`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
