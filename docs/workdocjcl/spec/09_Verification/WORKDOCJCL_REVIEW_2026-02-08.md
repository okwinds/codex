# workdocjcl Review（以代码为准 / 复刻级）

本报告面向协作与复现：说明在 **不修改任何代码** 的前提下，如何把 `docs/workdocjcl/` 规格文档与当前 `codex` 代码严格对齐，并给出可重复运行的证据与脚本入口。

## 0. 基准与结论

- 基准提交（code）：`7f567b11ecb56a92a105b9a624dabadc44147ddd`
- 结论摘要：
  - **Code → Spec：** 本提交下的所有 repo tracked 文件（排除 `docs/workdocjcl/**`）都能映射到唯一 file capsule，且无缺失。
  - **Spec → Code：** `SPEC_INDEX.md` 的链接目标全部存在；`CODE_TO_SPEC_MAP.md` 的 code/spec 路径全部可解析（含 glob）。
  - 迁移后路径已统一为 repo-root 前缀 `docs/workdocjcl/...`，避免“旧前缀 workdocjcl/...”导致的导航错误。

## 1. 证据（可重复运行）

### 1.1 无遗漏证明（File capsules）

- manifests（以 git tracked 为准）：`docs/workdocjcl/inventory/file_manifest_repo.txt`
- capsules（每文件一个）：`docs/workdocjcl/spec/10_File_Specs/by_path/`
- 覆盖 marker：`docs/workdocjcl/spec/10_File_Specs/COVERAGE.json`
- 状态证明（无缺失，且 capsule 计数与 repo 文件数相等）：`docs/workdocjcl/spec/09_Verification/NO_OMISSION_STATUS.json`

说明：
- 每个 capsule 记录 `size_bytes` 与 `sha256`，可用于严格校验代码文件是否与 spec 对应。

### 1.2 导航完整性（Spec index + mapping）

- SPEC_INDEX 链接检查：`docs/workdocjcl/spec/09_Verification/SPEC_INTEGRITY_REPORT.md`
- 机器可读报告：`docs/workdocjcl/spec/09_Verification/SPEC_INTEGRITY_REPORT.json`

## 2. 关键修复点（为什么需要这些修改）

### 2.1 迁移路径导致的“前缀漂移”

workdocjcl 从 repo root 迁移到 `docs/workdocjcl/` 后，历史文档中大量出现的：
- `workdocjcl/spec/...`
- `workdocjcl/inventory/...`

会导致从 repo root 无法直接定位文件（路径错误）。本次已统一替换为：
- `docs/workdocjcl/spec/...`
- `docs/workdocjcl/inventory/...`

并提供一键规范化脚本：`docs/workdocjcl/scripts/normalize_spec_paths.py`。

### 2.2 自动生成物的“幽灵残留”

当 repo 文件清单缩小时，如果不清理旧输出目录，`by_path/` 可能残留已删除文件的 capsule（不影响“缺失检查”，但影响可读性与严格对齐）。

本次已在生成脚本中加入清理逻辑：
- `docs/workdocjcl/scripts/generate_file_capsules.py`（清理 `10_File_Specs/by_path/`）
- `docs/workdocjcl/scripts/generate_symbol_indexes.py`（清理 `13_Indexes/`）
- `docs/workdocjcl/scripts/generate_rust_crate_specs.py`（清理 `11_Rust_Crate_Specs/`）
- `docs/workdocjcl/scripts/generate_node_package_specs.py`（清理 `12_Node_Package_Specs/`）

### 2.3 Chat wire（wire_api=chat）与实际代码不一致

当前基准提交中，`wire_api = "chat"` 已被移除（配置解析阶段直接报错）。为保证“以代码为准”，已更新：
- `docs/workdocjcl/spec/05_Integrations/CHAT_WIRE_MAPPING.md`：改为“当前行为（移除）+ legacy 归档”
- `docs/workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md`：标注 chat 已移除，并移除 `ollama-chat` 内置 provider 描述
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`：移除已不存在的 chat/streaming 源文件映射，改为指向现存实现（如 `model_provider_info.rs`、`aggregate.rs`）

## 3. 推荐维护流程（刷新 + 自检）

见 `docs/workdocjcl/README.md` 的“生成与维护”章节，或直接按以下顺序执行：

1) 刷新清单/库存：
- `python3 docs/workdocjcl/scripts/generate_inventory_repo_files.py`
- `python3 docs/workdocjcl/scripts/generate_inventory_rust_workspace.py`
- `python3 docs/workdocjcl/scripts/generate_inventory_node_workspace.py`

2) 刷新生成物：
- `python3 docs/workdocjcl/scripts/generate_file_capsules.py`
- `python3 docs/workdocjcl/scripts/generate_symbol_indexes.py`
- `python3 docs/workdocjcl/scripts/generate_bidirectional_index.py`
- `python3 docs/workdocjcl/scripts/generate_no_omission_status.py`

3) 自检：
- `python3 docs/workdocjcl/scripts/verify_spec_integrity.py`

## 4. 已知限制（仍需人工判断的“语义复刻”部分）

- File capsules 与索引解决的是“**不遗漏**”与“**可导航**”，但不自动保证所有行为描述都与最新实现逐字一致。
- 深层行为对齐建议以以下章节为主入口并结合代码审阅：
  - `docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md`
  - `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`
  - `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md`
  - `docs/workdocjcl/spec/06_UI/TUI.md`
  - `docs/workdocjcl/spec/09_Verification/CORE_INFRASTRUCTURE_REVIEW.md`

