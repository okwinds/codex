# 规格文档约定（Spec Conventions）

本规格文档的目标是“可复刻”。为了让读者能仅凭文档实现等价系统，本章明确约定写作格式与映射规范。

## 1. 映射规范（Code ↔ Spec）
- 每个章节必须包含 **来源（Source）** 小节，列出对应实现文件路径（必要时列出关键类型/函数名）。
- 对于“清单类内容”（例如 env vars、crate list、文件清单），优先引用 `workdocjcl/inventory/` 中自动生成的材料，避免人工遗漏。
- 文档中提到的可执行命令/路径/配置键名必须保持与代码一致（大小写敏感）。

## 2. 复刻粒度（Replication Granularity）
本仓库体量较大，复刻可以分为两层：

### 2.1 外部行为等价（Minimum Viable Replica）
满足以下条件即可认为“核心复刻完成”：
- 用户可运行 `codex` 并获得与原项目一致的 CLI 子命令行为（至少：默认交互模式、`exec`、`login/logout/status`、`sandbox`、`resume/fork` 的核心语义）。
- 配置文件（`config.toml`）与关键环境变量（尤其 `CODEX_HOME`）的行为一致。
- 工具调用、审批策略、沙箱策略在关键路径一致（安全模型一致）。
- state.sqlite 的 schema 与读写行为一致（至少 thread 索引/日志写入/动态工具存储）。

### 2.2 内部实现等价（Full Fidelity）
在 2.1 基础上进一步达到：
- 事件粒度、错误类型、日志/metrics 打点、细节 UI 行为（TUI 渲染/交互）一致。
- 与 OpenAI/ChatGPT 的网络交互形状一致（请求/响应字段、重试/限流处理、流式解析）。
- 边界场景与故障处理一致（断网、权限不足、shell 失败、模型超时、MCP 失败等）。

## 3. 7 个拆解问题（每个模块都要回答）
1) 这是什么？（分类与上下文）
2) 为什么存在？（缺失会坏在哪里）
3) 如何工作？（完整分支与边界）
4) 输入是什么？（所有来源/校验/默认值）
5) 输出是什么？（所有形式与副作用）
6) 依赖关系？（上下游、外部系统）
7) 会出什么错？（错误处理与恢复）

## 4. 自动生成材料（防遗漏）
以下文件由扫描脚本生成，作为“无遗漏清单”的基础：
- `workdocjcl/inventory/file_manifest_repo.txt`：repo-only 文件清单（无遗漏基线，不含 `workdocjcl/`）
- `workdocjcl/inventory/file_manifest.txt`：全量文件清单（含 `workdocjcl/` 生成物）
- `workdocjcl/inventory/file_manifest_all.txt`：全量文件清单（更宽口径，含更多生成物）
- `workdocjcl/inventory/repo_stats.json`：扩展名统计/规模快照
- `workdocjcl/inventory/rust_workspace.md`：Rust workspace member 清单
- `workdocjcl/inventory/node_workspace.md`：pnpm workspace package 清单
- `workdocjcl/inventory/env_vars_detected.txt`：源码检测到的环境变量清单
- `workdocjcl/inventory/env_var_usages.md`：环境变量 → 位置（采样）

## 5. 来源（Source）
- 本章为规格约定，不对应单一源码文件；自动生成材料来自 `rg`/`python3` 扫描（见 `workdocjcl/` 下的生成物）。
