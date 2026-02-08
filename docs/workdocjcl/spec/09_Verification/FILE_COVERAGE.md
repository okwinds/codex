# 文件级覆盖报告（File Coverage）

Generated (UTC): 2026-02-04

本报告用于证明“无遗漏”的最低层级：**repo 中每个文件都有对应的文件胶囊（file capsule）规格**。

## 1. 覆盖基准（Source of truth）
- repo 文件清单（不包含 `workdocjcl/` 生成物）：`workdocjcl/inventory/file_manifest_repo.txt`
  - 文件数：2431

## 2. 覆盖产物（Output）
- capsule 格式说明：`workdocjcl/spec/10_File_Specs/FORMAT.md`
- capsule 索引：`workdocjcl/spec/10_File_Specs/INDEX.md`
- capsule 目录：`workdocjcl/spec/10_File_Specs/by_path/`

## 3. 覆盖结论
- 覆盖率：100%（`file_manifest_repo.txt` 中的每个路径都存在对应 `by_path/<path>.md` capsule）
- 生成时间与计数：见 `workdocjcl/spec/10_File_Specs/COVERAGE.json`

## 4. 重要说明（“无遗漏”≠“像素级 UI / 运行时矩阵已验证”）
文件级 capsule 保证：
- **没有文件被遗漏**（存在性覆盖）
- 每个文件至少有元数据 + 初步接口/依赖抽取（对 source/config/test/doc）

但要达到“完全复刻无需读源码”的极限目标，仍可能需要**可选深化**（不影响当前仓库实现的行为复刻闭环，但影响复刻便利性/一致性验证）：
- `codex-rs/tui` 的逐 widget 像素级布局/样式规范（当前已覆盖关键交互闭环与状态机）
- 不同 provider 的运行时对照矩阵（headers/events/错误文案差异需要真实环境或 mock server 扩展验证）
- Cloud tasks（实验性/内部特性；可裁剪）

这些深化项的进度与缺口列表见：
- `workdocjcl/spec/09_Verification/KNOWN_GAPS.md`
