# `codex-rs/utils/cache/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5635`
- sha256: `0df19d252803692137ccfab88cc111fa95c3d8fc3f38032d3095c02ccfef346e`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/cache/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct BlockingLruCache<K, V> {`
- `pub fn new(capacity: NonZeroUsize) -> Self {`
- `pub fn get_or_insert_with(&self, key: K, value: impl FnOnce() -> V) -> V`
- `pub fn try_with_capacity(capacity: usize) -> Option<Self> {`
- `pub fn insert(&self, key: K, value: V) -> Option<V> {`
- `pub fn clear(&self) {`
- `pub fn blocking_lock(&self) -> Option<MutexGuard<'_, LruCache<K, V>>> {`
- `pub fn sha1_digest(bytes: &[u8]) -> [u8; 20] {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/cache/src/lib.rs:1` `use std::borrow::Borrow;`
- `use` `codex-rs/utils/cache/src/lib.rs:2` `use std::hash::Hash;`
- `use` `codex-rs/utils/cache/src/lib.rs:3` `use std::num::NonZeroUsize;`
- `use` `codex-rs/utils/cache/src/lib.rs:5` `use lru::LruCache;`
- `use` `codex-rs/utils/cache/src/lib.rs:6` `use sha1::Digest;`
- `use` `codex-rs/utils/cache/src/lib.rs:7` `use sha1::Sha1;`
- `use` `codex-rs/utils/cache/src/lib.rs:8` `use tokio::sync::Mutex;`
- `use` `codex-rs/utils/cache/src/lib.rs:9` `use tokio::sync::MutexGuard;`
- `struct` `codex-rs/utils/cache/src/lib.rs:13` `pub struct BlockingLruCache<K, V> {`
- `fn` `codex-rs/utils/cache/src/lib.rs:23` `pub fn new(capacity: NonZeroUsize) -> Self {`
- `fn` `codex-rs/utils/cache/src/lib.rs:30` `pub fn get_or_insert_with(&self, key: K, value: impl FnOnce() -> V) -> V`
- `fn` `codex-rs/utils/cache/src/lib.rs:68` `pub fn try_with_capacity(capacity: usize) -> Option<Self> {`
- `fn` `codex-rs/utils/cache/src/lib.rs:84` `pub fn insert(&self, key: K, value: V) -> Option<V> {`
- `fn` `codex-rs/utils/cache/src/lib.rs:100` `pub fn clear(&self) {`
- `fn` `codex-rs/utils/cache/src/lib.rs:117` `pub fn blocking_lock(&self) -> Option<MutexGuard<'_, LruCache<K, V>>> {`
- `fn` `codex-rs/utils/cache/src/lib.rs:135` `pub fn sha1_digest(bytes: &[u8]) -> [u8; 20] {`
- `use` `codex-rs/utils/cache/src/lib.rs:146` `use super::BlockingLruCache;`
- `use` `codex-rs/utils/cache/src/lib.rs:147` `use std::num::NonZeroUsize;`
- `fn` `codex-rs/utils/cache/src/lib.rs:150` `async fn stores_and_retrieves_values() {`
- `fn` `codex-rs/utils/cache/src/lib.rs:159` `async fn evicts_least_recently_used() {`
- `fn` `codex-rs/utils/cache/src/lib.rs:173` `fn disabled_without_runtime() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::borrow::Borrow;`
- `use std::hash::Hash;`
- `use std::num::NonZeroUsize;`
- `use lru::LruCache;`
- `use sha1::Digest;`
- `use sha1::Sha1;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::MutexGuard;`
- `use super::BlockingLruCache;`
- `use std::num::NonZeroUsize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
