# 文件级规格格式（File Capsule Format）

本目录的目标是 **“无遗漏”**：对仓库中每一个文件生成一份“文件胶囊（capsule）”，至少回答：
1) 这是什么文件（类型/角色）？
2) 为什么存在（系统中承担的职责）？
3) 对外接口（导出/入口/配置键）是什么？
4) 依赖与被依赖关系（imports/exports/引用）？
5) 风险与边界（副作用/敏感信息/沙箱相关/网络相关）？

## 1. 命名与路径
- 每个 repo 文件 `X` 对应一个 capsule 文件：`10_File_Specs/by_path/<X>.md`
  - 示例：`codex-cli/bin/codex.js` → `10_File_Specs/by_path/codex-cli/bin/codex.js.md`
- 目录结构与 repo 保持一致，便于按路径导航。

## 2. Capsule 内容结构（固定）
每个 capsule 文件使用如下结构：

```markdown
# <repo-relative-path>

## Identity
- kind: <source|config|doc|build|test|asset|unknown>
- language/ext: <.rs|.ts|...>
- size_bytes: <int>
- sha256: <hex>
- generated_utc: <timestamp>

## Purpose (Why)
<1-6 行，描述文件在系统中的职责与缺失后果。>

## Interfaces (Inputs/Outputs)
### Inputs
- <env vars / CLI args / config keys / stdin / filesystem inputs / network inputs>
### Outputs / Side Effects
- <writes files / spawns processes / network calls / logs / DB writes>

## Public Surface (if applicable)
- exports / pub items / main entrypoint signatures（自动抽取 + 必要时人工补充）

## Dependencies
- imports/includes (sample)
- referenced env vars (sample)

## Error Handling / Edge Cases (if applicable)
- <fatal exits / error returns / retries / defaults>

## Spec Links
- high-level spec anchors this file belongs to (links to `docs/workdocjcl/spec/...`)
```

## 3. 自动抽取策略（Auto-extraction policy）
- 该目录主要由脚本生成（见 `docs/workdocjcl/scripts/generate_file_capsules.py`）。
- 对于体积很大的文件（>1MB）或二进制文件：
  - 不读取全文，只记录元数据与路径角色；
  - 若为关键文件，再手工补充“Purpose/Interfaces”段落。

## 4. “无遗漏”的判定
满足以下条件视为“文件级无遗漏”：
- `docs/workdocjcl/inventory/file_manifest_repo.txt` 中每个路径都存在对应 capsule 文件；
- `10_File_Specs/INDEX.md` 中对每个路径都有索引条目；
- `09_Verification/FILE_COVERAGE.md` 中的覆盖统计为 100%。
