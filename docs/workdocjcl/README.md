# workdocjcl

本目录是 Codex 的“可复刻级”规格文档集合（prompt、tools、skills、approvals、wire mapping 等）。

## 入口

- 规格索引：`spec/SPEC_INDEX.md`

## 生成与维护（以代码为准）

workdocjcl 包含大量“自动生成的无遗漏材料”（file capsules、索引、workspace inventories）。当代码发生变更时，推荐按以下顺序刷新（在 repo root 运行）：

```bash
python3 docs/workdocjcl/scripts/generate_inventory_repo_files.py
python3 docs/workdocjcl/scripts/generate_inventory_rust_workspace.py
python3 docs/workdocjcl/scripts/generate_inventory_node_workspace.py

python3 docs/workdocjcl/scripts/generate_config_schema_reference.py
python3 docs/workdocjcl/scripts/generate_tools_schema_reference.py

python3 docs/workdocjcl/scripts/generate_rust_crate_specs.py
python3 docs/workdocjcl/scripts/generate_node_package_specs.py
python3 docs/workdocjcl/scripts/generate_file_capsules.py
python3 docs/workdocjcl/scripts/generate_symbol_indexes.py
python3 docs/workdocjcl/scripts/generate_bidirectional_index.py
python3 docs/workdocjcl/scripts/generate_no_omission_status.py

python3 docs/workdocjcl/scripts/verify_spec_integrity.py
python3 docs/workdocjcl/scripts/verify_source_anchors.py
```

如发现历史章节仍引用旧路径前缀（`workdocjcl/spec/...`），可运行：

```bash
python3 docs/workdocjcl/scripts/normalize_spec_paths.py
```

## 维护约定

- 本目录以本仓库 `docs/workdocjcl/` 为 canonical 位置（对应 GitHub `okwinds/codex` 同路径；`https://github.com/okwinds/codex`）。
- 该目录曾短暂存在于 sibling 仓库 `agent-sdk` 的 `docs/specs/workdocjcl/`，已于 2026-02-08 迁回此处并以此处为唯一来源。
- `scripts/` 下的生成脚本假设本目录位于 `docs/workdocjcl/`，并依赖仓库根目录的 `codex-rs/`（例如读取 `codex-rs/core/config.schema.json`）。

## 与上游同步（避免被覆盖）

该目录是 fork 的增量内容。为了在同步 `openai/codex` 上游时不“意外覆盖”：

- 同步上游时优先使用 `git merge` / `git rebase`（把上游提交叠加到本仓库历史之上），而不要对分支做 `reset --hard` 到上游某个 commit。
- 若上游未来新增同名路径 `docs/workdocjcl/`，Git 会产生冲突而不是静默覆盖；按冲突提示选择保留/合并即可。
