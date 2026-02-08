# No-Omission Status Report

- generated_utc: `2026-02-08T11:22:05Z`

## 1. File-level coverage (hard requirement)
- repo_file_count: `2567` (`workdocjcl/inventory/file_manifest_repo.txt`)
- capsule_file_count: `2567` (`workdocjcl/spec/10_File_Specs/by_path/**/*.md`)
- missing_capsules: `0`

## 2. Crate/package coverage (structure)
- rust_crate_index_present: `true` (`docs/workdocjcl/spec/11_Rust_Crate_Specs/INDEX.md`)
- node_package_index_present: `true` (`docs/workdocjcl/spec/12_Node_Package_Specs/INDEX.md`)

## 3. Symbol indexes (public surfaces)
- symbol_indexes: `PYTHON_SYMBOL_INDEX.md, RUST_SYMBOL_INDEX.md, TYPESCRIPT_SYMBOL_INDEX.md`

## 4. Notes
- File capsules include per-file definition listings (heuristic) and are intended to eliminate “silent omissions”.
- Full replication still depends on semantics; see `KNOWN_GAPS.md` for the deepest remaining “behavioral” gaps.

## 5. 来源（Source）
- `docs/workdocjcl/scripts/generate_no_omission_status.py`
- `docs/workdocjcl/inventory/file_manifest_repo.txt`
- `docs/workdocjcl/spec/11_Rust_Crate_Specs/INDEX.md`
- `docs/workdocjcl/spec/12_Node_Package_Specs/INDEX.md`
- `docs/workdocjcl/spec/13_Indexes`
