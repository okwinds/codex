# 复刻指南（Replication Guide）

本指南说明如何使用 `docs/workdocjcl/spec/` 下的规格文档复刻该仓库的核心功能。

## 0. 复刻目标（What counts as “done”）
最低复刻闭包（Minimum Viable Replica）：
- `codex` 命令可运行，并具备核心子命令语义（至少：默认交互模式、`exec`、`login/logout/status`、`sandbox`、`resume/fork` 的核心语义）。
- `CODEX_HOME`、`config.toml`、`-c key=value` 的行为一致。
- state.sqlite schema 与关键读写一致（threads/logs/dynamic_tools）。
- 具备基础的安全模型：审批 + 沙箱（不允许默认任意写入/任意联网）。

## 1. 前置知识与工具（Prerequisites）
- 熟悉：CLI 参数解析、事件驱动 UI、HTTP 流式响应、进程沙箱/权限隔离的基本概念
- 工具：
  - Rust 或等价实现语言（若复刻原实现）
  - SQLite（或等价持久化）
  - Node.js（若复刻 npm wrapper / MCP server）

## 2. 推荐复刻顺序（Recommended Order）

### Step 1：建立“仓库结构”与模块边界
- 阅读：`00_Overview/REPO_LAYOUT.md`、`00_Overview/MODULE_MAP.md`
- 落地：在你的新仓库中创建等价模块（core/protocol/cli/state/tui…）

### Step 2：实现配置与环境变量契约
- 阅读：`01_Configuration/ENVIRONMENT.md`、`03_API/CLI.md`
- 必须实现：
  - `CODEX_HOME` 解析
  - `config.toml` 结构（可用 schema 驱动）
  - `-c key=value` 覆盖规则
  - features defaults + 覆盖

### Step 3：实现 state.sqlite（先跑通持久化闭包）
- 阅读：`02_Data/ENTITIES.md`、`02_Data/MIGRATIONS.md`
- 直接以 migrations 作为 schema 来源，保证一字不差。

### Step 4：实现 CLI 与核心 turn loop（最小闭包）
- 阅读：`00_Overview/ARCHITECTURE.md`、`04_Business_Logic/WORKFLOWS.md`
- 先实现 headless `exec`（更易测试），再实现 TUI。

### Step 5：实现 provider registry（能真正跑起来）
- 阅读：`05_Integrations/MODEL_PROVIDERS.md`、`03_API/AUTHENTICATION.md`
- 优先实现 OpenAI provider + Responses API（当前基准提交中 Chat wire 已移除，见 `05_Integrations/CHAT_WIRE_MAPPING.md`）。

### Step 6：实现审批与沙箱（安全闭包）
- 阅读：`07_Infrastructure/SECURITY_SANDBOX.md`
- 先复刻“策略模型”，再按 OS 实现具体隔离机制。

### Step 7：补齐 UI（若需要同等交互体验）
- 阅读：`06_UI/TUI.md`

## 3. 验证清单（Verification Checklist）
- [ ] `CODEX_HOME` 行为一致（缺失/文件/目录）
- [ ] `-c key=value` 行为一致（TOML 解析与回退）
- [ ] state.sqlite schema 与 migrations 一致（0001..0004）
- [ ] Node wrapper 平台选择 + 信号转发一致（若提供 npm 分发）
- [ ] provider registry：OpenAI base_url/env headers 注入一致
- [ ] 登录：stdin API key 与 chatgpt/device-code 的语义一致
- [ ] 至少一个 E2E journey 可跑通（见 `08_Testing/E2E_SPECS.md`）

## 4. 映射锚点（Mapping Anchor）
- 复刻过程中遇到“这段代码对应哪份规格”时，直接查：`09_Verification/CODE_TO_SPEC_MAP.md`

## 来源（Source）
- `docs/workdocjcl/spec/SPEC_INDEX.md`
- `docs/workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
- `docs/workdocjcl/inventory/file_manifest_repo.txt`
