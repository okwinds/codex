# 仓库 ↔ 规格文档对齐审计报告（Alignment Audit Report）

Generated (local): 2026-02-04

本报告回答问题：**当前 `codex` 仓库实现与 `workdocjcl/spec/` 规格文档是否对齐？哪些地方我没有做到“事无巨细”、哪些地方仍不够完善？**

报告结论分为两类：
- **对齐性问题（Documentation Drift / Inconsistency）**：文档内部数字、引用或表述不一致，会误导复刻者。
- **复刻细节缺口（Replication Detail Gaps）**：某些子系统仍以“契约级/概述级”描述，若需要复刻到同等细粒度，应继续补齐。

> 审计声明：本审计以静态阅读代码与文档为主；未在真实 provider 上做运行时对照；未执行全仓库测试矩阵（这类验证属于可选增强，见 Findings）。

---

## 0. 审计方法（我实际做了什么）

### 0.1 结构完整性（硬检查）
- 校验 `workdocjcl/spec/SPEC_INDEX.md` 中所有链接目标文件存在（已通过）。
- 校验 `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md` 中引用的 spec 路径都存在（已通过）。
- 校验 verbatim 资产副本的 `MANIFEST.json`（sha256/bytes）一致性：
  - `workdocjcl/spec/04_Business_Logic/PROMPTS/MANIFEST.json`
  - `workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS/MANIFEST.json`

### 0.2 针对“核心基础设施”的对齐抽样（重点）
围绕你点名的核心基础设施，抽样核对“代码实现 → 规格落点”：
- 模型 API 交互：`codex-rs/codex-api/src/*`、`codex-rs/core/src/model_provider_info.rs`
- prompt 管理与系统预置 prompt：`codex-rs/core/src/codex.rs`、`codex-rs/core/src/models_manager/model_info.rs`、`codex-rs/core/*.md`
- 工具调用与工具路由：`codex-rs/core/src/tools/*` + handlers
- skills：`codex-rs/core/src/skills/*`

### 0.3 “可能遗漏/不够细”的定位方式
- 扫描 `workdocjcl/spec` 中的 “TBD/TODO/Unclear/可选深化” 等标记并人工判断其是否属于 replication-blocking。
- 扫描仓库中仍被 CLI 暴露但在规格中标为“可选/内部”的模块（例如 cloud tasks）。

---

## 1. 总体结论（TL;DR）

### 1.1 已达成：核心能力基础设施的“行为复刻闭环”
下列能力已经具备“仅靠规格文档即可复刻主要行为闭环”的条件（且已有代码锚点映射）：
- Responses API streaming（SSE/WS/回退/重试/headers→事件注入）：`workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md`
- Provider/WireApi/Headers/Azure store/Chat DONE sentinel：`workdocjcl/spec/05_Integrations/MODEL_API_COMPATIBILITY.md`
- Prompt 组装（BaseInstructions 决议 + initial context 注入顺序 + personality baked/injected）：`workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`
- 系统预置 prompts（verbatim + sha256，可在复刻实现中做一致性校验）：`workdocjcl/spec/04_Business_Logic/SYSTEM_PRESET_PROMPTS.md` + `workdocjcl/spec/04_Business_Logic/PROMPTS/*`
- Tools：schema reference + 每个 tool 的运行时语义（审批/沙箱/错误路径/输出 envelope）：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/*`
- Skills：发现/扫描/禁用语义/mentions 消歧/注入/依赖提示：`workdocjcl/spec/05_Integrations/SKILLS.md`
- embedded system skills（verbatim + sha256）：`workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS*`

### 1.2 仍需改进：文档内部一致性与少数模块的“细节复刻”
当前最明确、可操作的不足主要有两类：
1) **覆盖报告/映射文档中的数字与表述漂移**（会误导审阅者）。
2) **少数模块仍是“概念/契约级”描述**，若要“事无巨细”复刻，需要继续补齐（尤其是 `cloud tasks` 与 `wire_api=chat` 的完整映射细节）。

---

## 2. Findings A：对齐性问题（文档内部不一致 / 需要修正）

### A1（高）`COVERAGE_REPORT.md` 的“规格文档 Markdown 文件数”已不真实
- 状态：**已修复（2026-02-04）**
- 修复位置：`workdocjcl/spec/09_Verification/COVERAGE_REPORT.md`
- 修复内容：将单一口径拆分为多口径并行呈现（总量 + 分目录 + “手写契约级 spec”）。
- 修复后口径（静态计数）：
  - `workdocjcl/spec/**/*.md` 总数：`2594`
  - 逐文件胶囊（`10_File_Specs/by_path`）：`2431`
  - 手写“契约级”规格（排除自动生成目录）：`87`

### A2（中）`COVERAGE_REPORT.md` 的小节编号顺序不一致（2.6 出现在 2.5 前）
- 状态：**已修复（2026-02-04）**
- 修复位置：`workdocjcl/spec/09_Verification/COVERAGE_REPORT.md`
- 修复内容：重编号为 `2.5 Prompt / Skills`、`2.6 集成`，保证小节顺序单调递增。

### A3（中）“存在性清单”口径在不同文档中混用 `file_manifest.txt` 与 `file_manifest_repo.txt`
- 状态：**已修复（2026-02-04）**
- 修复位置：
  - `workdocjcl/spec/00_Overview/SPEC_CONVENTIONS.md`
  - `workdocjcl/spec/09_Verification/COVERAGE_REPORT.md`
  - `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
- 修复内容：统一明确三种 manifest 口径，并在“无遗漏基线”语境下优先使用 repo-only：
  - repo-only：`workdocjcl/inventory/file_manifest_repo.txt`（不含 `workdocjcl/`）
  - all-files：`workdocjcl/inventory/file_manifest.txt`（含 `workdocjcl/`）
  - wide：`workdocjcl/inventory/file_manifest_all.txt`

### A4（中）`COVERAGE_REPORT.generated.md` 当前不具备“可追溯生成”的可信信息密度
- 状态：**已修复（最小化修复，2026-02-04）**
- 修复位置：
  - `workdocjcl/spec/09_Verification/COVERAGE_REPORT.generated.md`
  - `workdocjcl/spec/09_Verification/COVERAGE_REPORT.md`
- 修复内容：将其明确标注为“非权威/模板产物”，并给出权威覆盖锚点（`CODE_TO_SPEC_MAP.md` + repo-only manifest + `COVERAGE_REPORT.md`）。

### A5（低）跨章节导航缺少显式链接（不会阻断复刻，但降低“审计可达性”）
示例：
- `PROMPT_ASSEMBLY.md` 当前未显式链接到：
  - `SYSTEM_PRESET_PROMPTS.md`
  - `PROMPTS/INDEX.md`
- `SKILLS.md` 未显式链接到：
  - `SKILLS_SYSTEM_ARTIFACTS.md`（system skills 的 verbatim 副本位置）
影响：
- 对齐审计/溯源时要靠搜索而不是目录导航。
建议：
- 在相关章节的 “See also”/“资产位置”处加链接（不改变语义，只提升可读性）。

---

## 3. Findings B：复刻细节缺口（需要继续补齐才算“事无巨细”）

### B1（中）`wire_api = chat` 的“请求映射细节”尚未写到逐分支可复刻
状态：**已修复（2026-02-04）**

修复内容：
- 新增：`workdocjcl/spec/05_Integrations/CHAT_WIRE_MAPPING.md`
  - 请求侧：`ResponseItem[] → Chat messages/tool_calls/tool outputs` 的逐分支映射（含 reasoning attach、assistant 去重、tool_calls 分组、LocalShell/CustomTool 分支）
  - 响应侧：Chat SSE delta/哨兵/finish_reason/tool_calls 状态机的逐分支映射

复刻边界：
- 本修复覆盖“仓库实现的映射规则”；不展开 provider 运行时差异矩阵（仍由 `MODEL_API_COMPATIBILITY.md` 承担）。

### B2（中）Cloud tasks 模块仍是“可裁剪/内部特性”级别描述
证据：
- CLI 暴露了 `cloud`/`cloud-tasks` 子命令（规格中也提到可选复刻），但缺少：
  - 完整 API shape、错误分类、认证策略、分页等“逐接口复刻”文档。
影响：
- 若复刻目标要求功能完备（包含 cloud tasks），仍需补齐。
建议：
- 如果你决定“cloud tasks 也必须复刻”：需要补齐 `codex-rs/cloud-tasks*` 与 client 的协议与错误模型。
- 如果你接受“可裁剪”：在 `REPLICATION_GUIDE.md` 中明确裁剪开关与行为差异（避免误解）。

### B3（低）TUI 仍未承诺像素级复刻（属于明确声明的可选深化）
- 位置：`workdocjcl/spec/09_Verification/KNOWN_GAPS.md:10`
- 影响：仅当你的复刻目标是“UI 像素级一致”才需要继续。

---

## 4. 我认为“已经足够对齐”的地方（避免重复劳动）

以下内容我不建议再投入“provider 实测矩阵”式的大工作量（除非你改变目标），因为当前规格已经把“实现行为契约”落盘：
- Responses SSE/WS 的 enablement、解析、回退、重试：`RESPONSES_STREAMING.md`
- Provider/WireApi/Azure store/headers→事件注入：`MODEL_API_COMPATIBILITY.md`
- Tools 的逐项语义：`TOOLS_DETAILED/*`
- Skills 的扫描/mentions/注入/依赖提示：`SKILLS.md`
- System preset prompts 与其 verbatim 资产：`SYSTEM_PRESET_PROMPTS.md` + `PROMPTS/*`

---

## 5. “继续补充文档”的最小建议清单（等待你确认）

如果你认为需要继续补充，我建议优先级如下：
1) **修正覆盖报告口径**：让 `COVERAGE_REPORT.md` 的 spec 数量与 manifest 口径不再误导（A1/A3）。
2) **补齐 Chat wire 的完整映射（仅当你要求保留 chat 复刻）**（B1）。
3) **补齐 Cloud tasks（仅当你不接受裁剪）**（B2）。
4) TUI 像素级（仅当你要 UI 完全一致）。（B3）
