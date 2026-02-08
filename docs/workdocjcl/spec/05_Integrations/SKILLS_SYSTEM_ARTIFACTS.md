# 集成：内置（embedded）system skills 资产规格

本章目标：补齐 skills 系统中“随二进制内嵌并在运行时安装到 `CODEX_HOME/skills/.system`”的那部分资产，使复刻者在不查看源码的情况下也能得到完全一致的 system skills 内容。

skills 的发现/扫描/启用禁用/mentions 消歧/注入语义见：
- `workdocjcl/spec/05_Integrations/SKILLS.md`

---

## 1. embedded system skills 的真实来源（当前仓库实现）
Codex 将“system skills”作为编译期资源内嵌：
- 内嵌目录：`codex-rs/core/src/skills/assets/samples`
- include 方式：`include_dir!`（常量 `SYSTEM_SKILLS_DIR`）
- 安装目标：`CODEX_HOME/skills/.system`
- 安装优化：写入 marker `CODEX_HOME/skills/.system/.codex-system-skills.marker`（fingerprint + salt `"v1"`）

来源：`codex-rs/core/src/skills/system.rs`

> 复刻注意：当前仓库的“system skills”并非大量预置技能集合，而是以 samples 形式提供的 `.system` 技能（例如 skill-creator/skill-installer）。复刻必须保持这一事实，否则“ListSkills”与 `$` mentions 的候选集会偏离。

---

## 2. 规范化副本（verbatim copy）
为满足“仅依赖规格文档即可复刻”，本规格将 embedded system skills 的文件内容完整拷贝到：
- `workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS/`

并提供可验证清单：
- `workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS/MANIFEST.json`

复刻要求：
- 复刻实现应当以该目录内容作为“system skills”权威源，并可在构建阶段校验 sha256。

---

## 3. 安装行为复刻要点（最小闭包）
复刻者至少需要实现：
1) 计算 embedded 目录 fingerprint（递归遍历，记录 dir path 与 file contents hash，排序后 hash；加盐 `"v1"`）
2) 若 marker 存在且等于 fingerprint → 跳过安装
3) 否则清空 `CODEX_HOME/skills/.system` 并写入 embedded 目录结构与文件内容
4) 写入 marker 文件（fingerprint + `\\n`）

对应细节见：
- `workdocjcl/spec/05_Integrations/SKILLS.md`（system skills 安装与 marker 语义）

