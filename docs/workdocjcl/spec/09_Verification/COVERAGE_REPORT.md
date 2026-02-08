# 规格覆盖报告（Spec Coverage Report）

Generated (UTC): 2026-02-04

> 说明：仓库规模较大，“逐文件逐函数”级别的覆盖统计不现实且会导致文档噪音。本报告采用 **契约覆盖** 思路：以“关键入口/关键契约/关键持久化 schema”作为复刻的最小闭包，并用自动生成清单（file manifest、workspace members、env vars）保证“存在性不遗漏”。

## 1. Summary（规模快照）
- 代码仓库扫描文件数（忽略常见 build 目录）：约 `2455`（见 `docs/workdocjcl/inventory/repo_stats.json`）
- 规格文档 Markdown 文件数（`docs/workdocjcl/spec/**/*.md`，含自动生成胶囊/索引/资产镜像）：`2594`
  - 逐文件胶囊（`docs/workdocjcl/spec/10_File_Specs/by_path/**`）：`2431`
  - Rust crate specs（`docs/workdocjcl/spec/11_Rust_Crate_Specs/**`）：`51`
  - Node package specs（`docs/workdocjcl/spec/12_Node_Package_Specs/**`）：`5`
  - Indexes（`docs/workdocjcl/spec/13_Indexes/**`）：`3`
  - Prompt 资产镜像（`docs/workdocjcl/spec/04_Business_Logic/PROMPTS/**`）：`13`
  - System skills 资产镜像（`docs/workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS/**`）：`4`
  - 手写“契约级”规格（排除以上自动生成目录）：`87`

## 2. Documented and Anchored（已覆盖的关键契约）

### 2.1 入口与分发（必须）
- npm wrapper：平台探测、binary 选择、PATH/ENV 注入、信号转发
  - 覆盖：`docs/workdocjcl/spec/07_Infrastructure/PACKAGING.md`
  - 源：`codex-cli/bin/codex.js`
- Rust CLI 顶层：子命令与默认交互模式的分发
  - 覆盖：`docs/workdocjcl/spec/03_API/CLI.md`
  - 源：`codex-rs/cli/src/main.rs`

### 2.2 配置与环境（必须）
- `CODEX_HOME` 行为
  - 覆盖：`docs/workdocjcl/spec/01_Configuration/ENVIRONMENT.md`
  - 源：`codex-rs/utils/home-dir/src/lib.rs`
- config 覆盖（`-c key=value`）语义
  - 覆盖：`docs/workdocjcl/spec/03_API/CLI.md`、`docs/workdocjcl/spec/08_Testing/UNIT_SPECS.md`
  - 源：`codex-rs/common/src/config_override.rs`
- features registry（key/stage/default）
  - 覆盖：`docs/workdocjcl/spec/01_Configuration/FEATURE_FLAGS.md`
  - 源：`codex-rs/core/src/features.rs`

### 2.3 持久化（必须）
- state.sqlite schema（threads/logs/thread_dynamic_tools）
  - 覆盖：`docs/workdocjcl/spec/02_Data/*.md`
  - 源：`codex-rs/state/migrations/*.sql`

### 2.4 核心运行模型（必须）
- turn loop / tool execution / approvals / sandbox（契约级）
  - 覆盖：`docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`、`docs/workdocjcl/spec/04_Business_Logic/*.md`、`docs/workdocjcl/spec/07_Infrastructure/SECURITY_SANDBOX.md`
  - 源：`codex-rs/core/src/codex.rs`、`codex-rs/protocol/` 等

### 2.5 Prompt / Skills 资产（复刻必需）
- 系统预置 prompts（verbatim + checksums）
  - 覆盖：`docs/workdocjcl/spec/04_Business_Logic/SYSTEM_PRESET_PROMPTS.md`、`docs/workdocjcl/spec/04_Business_Logic/PROMPTS/INDEX.md`
  - 源：`codex-rs/core/*.md`、`codex-rs/core/templates/*`（编译期 `include_str!`）
- embedded system skills（verbatim + checksums）
  - 覆盖：`docs/workdocjcl/spec/05_Integrations/SKILLS_SYSTEM_ARTIFACTS.md`
  - 源：`codex-rs/core/src/skills/assets/samples/*`（编译期 `include_dir!`）

### 2.6 集成（建议）
- model providers registry + auth injection + retry/timeout
  - 覆盖：`docs/workdocjcl/spec/05_Integrations/MODEL_PROVIDERS.md`
  - 源：`codex-rs/core/src/model_provider_info.rs`
- MCP config + transports + OAuth
  - 覆盖：`docs/workdocjcl/spec/05_Integrations/MCP.md`
  - 源：`codex-rs/core/src/config/types.rs`

## 3. Existence Coverage（无遗漏清单覆盖）
以下“清单类材料”用于保证仓库元素不会被遗漏（至少知道它存在）：
- repo-only 文件清单（**无遗漏基线**，不含 `workdocjcl/`）：`docs/workdocjcl/inventory/file_manifest_repo.txt`
- 全量文件清单（含 `workdocjcl/` 生成物）：`docs/workdocjcl/inventory/file_manifest.txt`
- 全量文件清单（更宽口径，含更多生成物）：`docs/workdocjcl/inventory/file_manifest_all.txt`
- Rust workspace members：`docs/workdocjcl/inventory/rust_workspace.md`
- Node workspace packages：`docs/workdocjcl/inventory/node_workspace.md`
- 源码直读 env vars：`docs/workdocjcl/inventory/env_vars_detected.txt`
- Rust 测试清单：`docs/workdocjcl/inventory/rust_test_manifest.txt`

## 4. Found in Code but Not Fully Specified（仍需深化的区域）
本次规格文档以“可复刻当前仓库实现”为目标，已覆盖并锚定以下此前高优区域：
- tools：全量 schema 参考 + 逐 tool 行为规格（含审批/沙箱/错误路径）已补齐
- rollout：补齐 persist policy、resume/fork 的 initial context 策略、reconstruct/compaction 重建与回放边界
- execpolicy：规则语言、匹配逻辑、默认策略、amendment 落盘与 approvals 联动已补齐
- app-server：stdio JSONL 协议、initialize 门禁、experimentalApi gating、method/notification 清单与 approvals/tool/auth 切面已补齐
- responses streaming：SSE/WS enablement、retry/backoff、WS→HTTP 回退与解析差异已补齐

仍可选深化（不影响“行为复刻”，主要是“实现复刻”的便利性或 UI 像素级一致性）：
1) `codex-rs/tui` 的逐 widget 视觉/布局细节（当前已覆盖关键交互闭环与状态机，但未承诺像素级复刻）
2) provider 兼容性矩阵（不同模型/供应商对 Responses 事件/headers 的差异，需要运行时对照补齐）

## 5. Notes（关于自动化 coverage 脚本）
技能提供的 `verify_coverage.sh` 在 macOS 上会因为 `set -euo pipefail` + `grep` 无匹配返回码导致提前退出，无法生成完整报告。本 repo 的覆盖校验改为：
- 映射锚点：`docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
- 清单覆盖：`docs/workdocjcl/inventory/*`

另外：`docs/workdocjcl/spec/09_Verification/COVERAGE_REPORT.generated.md` 是技能模板产物（非仓库权威报告、内容不完整），仅保留用于追溯“为什么不采用该脚本”的原因。
