# 已知文档缺口（Known Gaps）

本仓库体量较大；本规格文档以“仅依赖文档即可复刻当前仓库实现”为目标推进，并用 `FILE_COVERAGE.md`/capsules 保证文件存在性无遗漏。

本文件仅记录**仍可能影响“实现复刻便利性”或“UI 像素级一致性”的可选深化点**；不再列出 replication-blocking 的缺口。

## 1. Intentionally Omitted（刻意不展开到逐函数级）
| Area | 原因 | 影响 |
|---|---|---|
| `codex-rs/tui` 逐 widget 像素级布局/风格规范 | 视觉细节大量且与终端/字体/主题强相关 | 规格已覆盖交互闭环与关键状态机，但未承诺像素级复刻（见 `06_UI/*`） |
| Provider 兼容性矩阵（Responses headers/events 差异） | 需要在真实 provider 上运行对照才能覆盖 | 当前按仓库实现落盘 enablement/解析/回退；若需跨 provider 强一致，需扩充测试矩阵 |

## 2. To Be Documented（待补齐）
| Area | Gap | Priority | Notes |
|---|---|---:|---|
| Tools catalog (deep) | （已补齐）逐 tool schema + 行为规格（审批/沙箱/错误路径） | - | 见：`05_Integrations/TOOLS_SCHEMA_REFERENCE.*` + `05_Integrations/TOOLS_DETAILED/*` |
| Prompt assembly (core) | （已补齐）BaseInstructions 决议、initial context 注入顺序、personality baked/injected 矩阵、Prompt→API payload、compaction 重建 | - | 见：`04_Business_Logic/PROMPT_ASSEMBLY.md` |
| Skills system (core) | （已补齐）skills roots/扫描/解析、启用禁用、mentions 消歧、`<skill>` 注入、env_var 依赖提示、ListSkills 协议 | - | 见：`05_Integrations/SKILLS.md` |
| Rollout semantics | （已补齐）persist policy、resume/fork initial context 策略、reconstruct/compaction 重建、回放边界 | - | 见：`02_Data/ROLLOUT_SEMANTICS.md` |
| Execpolicy | （已补齐）规则语言、匹配逻辑、默认策略、amendment 落盘与审批联动 | - | 见：`07_Infrastructure/EXEC_POLICY.md` + `07_Infrastructure/COMMAND_SAFETY.md` + `07_Infrastructure/APPROVALS.md` |
| App server | （已补齐）stdio JSONL/JSON-RPC-like 协议、initialize 门禁、experimentalApi gating、method/notification 清单、approvals/tool/auth 切面 | - | 见：`03_API/APP_SERVER.md` |
| Cloud tasks | API 形状与错误处理 | L | 实验/内部特性，可裁剪 |

## 3. Unclear Areas（需要结合运行时验证）
| Area | 原因 | 建议 |
|---|---|---|
| Responses API 的完整事件集合与解析边界 | （已补齐）已落盘当前实现支持的 event type 集合与错误分类（SSE/WS 细微差异） | 见：`05_Integrations/RESPONSES_STREAMING.md`；仍建议用 mock server 扩充兼容性矩阵 |
| WebSocket vs SSE 的切换条件 | （已补齐）已落盘 enablement 矩阵与“retry budget exhausted → 一次性禁用 WS 并回退 HTTP” | 见：`05_Integrations/RESPONSES_STREAMING.md`；仍建议做 provider/feature 组合测试 |

## 4. Technical Debt / Notes
- 技能提供的 `discover_project.sh` 与 `verify_coverage.sh` 在 macOS Bash 3.2 + `set -euo pipefail` 下存在兼容性问题（本次已用兼容报告替代，见 `workdocjcl/discovery_report.md` 与 `09_Verification/COVERAGE_REPORT.md`）。

## 来源（Source）
- `docs/workdocjcl/spec/09_Verification/COVERAGE_REPORT.md`
- `docs/workdocjcl/spec/09_Verification/FILE_COVERAGE.md`
- `docs/workdocjcl/spec/09_Verification/WORKDOCJCL_REVIEW_2026-02-08.md`
