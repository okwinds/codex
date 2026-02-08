# 双向覆盖索引（Bidirectional Coverage Index）

- generated_utc: `2026-02-08T10:45:45Z`
- repo_file_count: `2567` (from `docs/workdocjcl/inventory/file_manifest_repo.txt`)

本索引用于回答两个问题：
1) **任意代码文件** → 它的 file capsule 在哪里？属于哪个 crate/package？
2) **任意 crate/package** → 它覆盖了哪些文件？（通过 `file_to_spec_map.json` 可反查）

## 1. 生成物
- 文件到规格映射（机器可读）：`docs/workdocjcl/spec/09_Verification/file_to_spec_map.json`
- 文件胶囊索引：`docs/workdocjcl/spec/10_File_Specs/INDEX.md`
- Rust crate 索引：`docs/workdocjcl/spec/11_Rust_Crate_Specs/INDEX.md`
- Node package 索引：`docs/workdocjcl/spec/12_Node_Package_Specs/INDEX.md`

## 2. 覆盖统计（owners）

### 2.1 Rust crates
- `codex-ansi-escape`: 4 files
- `codex-api`: 26 files
- `codex-app-server`: 73 files
- `codex-app-server-protocol`: 597 files
- `codex-app-server-test-client`: 6 files
- `codex-apply-patch`: 91 files
- `codex-arg0`: 3 files
- `codex-async-utils`: 3 files
- `codex-backend-client`: 7 files
- `codex-backend-openapi-models`: 15 files
- `codex-cli`: 18 files
- `codex-client`: 11 files
- `codex-cloud-requirements`: 3 files
- `codex-cloud-tasks`: 11 files
- `codex-cloud-tasks-client`: 6 files
- `codex-common`: 14 files
- `codex-core`: 318 files
- `codex-debug-client`: 8 files
- `codex-exec`: 24 files
- `codex-exec-server`: 23 files
- `codex-execpolicy`: 14 files
- `codex-execpolicy-legacy`: 30 files
- `codex-experimental-api-macros`: 3 files
- `codex-feedback`: 3 files
- `codex-file-search`: 6 files
- `codex-git`: 10 files
- `codex-keyring-store`: 3 files
- `codex-linux-sandbox`: 13 files
- `codex-lmstudio`: 4 files
- `codex-login`: 11 files
- `codex-mcp-server`: 20 files
- `codex-network-proxy`: 16 files
- `codex-ollama`: 7 files
- `codex-otel`: 27 files
- `codex-process-hardening`: 4 files
- `codex-protocol`: 30 files
- `codex-responses-api-proxy`: 9 files
- `codex-rmcp-client`: 15 files
- `codex-secrets`: 3 files
- `codex-state`: 22 files
- `codex-stdio-to-uds`: 6 files
- `codex-tui`: 730 files
- `codex-utils-absolute-path`: 3 files
- `codex-utils-cache`: 3 files
- `codex-utils-cargo-bin`: 5 files
- `codex-utils-home-dir`: 3 files
- `codex-utils-image`: 4 files
- `codex-utils-json-to-toml`: 3 files
- `codex-utils-pty`: 13 files
- `codex-utils-readiness`: 3 files
- `codex-utils-string`: 3 files

### 2.2 Node packages
- `@openai/codex`: 13 files
- `@openai/codex-sdk`: 28 files
- `@openai/codex-shell-tool-mcp`: 15 files

### 2.3 Repo-level (non-crate/package)
- 224 files

## 3. 使用方式（How to use）
- 查某个文件 `path/to/file`：在 `file_to_spec_map.json` 里找 key，得到 capsule + owner spec 路径。
- 查某个 crate/package 覆盖范围：在 JSON 里筛选 `owner_name`。

