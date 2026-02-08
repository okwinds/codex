# 系统架构（Architecture）

本章节从“用户如何运行 codex”出发，描述各组件如何协作，并给出可复刻的边界与关键数据流。

## 1. 总览（High-Level Overview）

### 1.1 典型启动链路（npm 安装场景）
```mermaid
flowchart LR
  U[User runs `codex ...`] --> N[codex-cli/bin/codex.js<br/>Node wrapper]
  N -->|select target triple| B[Native binary<br/>codex]
  B --> CLI[codex-rs/cli<br/>clap multitool]
  CLI -->|default| TUI[codex-rs/tui<br/>fullscreen UI]
  CLI -->|codex exec| EXEC[codex-rs/exec<br/>headless mode]
  CLI -->|codex mcp-server| MCPS[codex-rs/mcp-server<br/>stdio MCP server]
  TUI --> CORE[codex-rs/core<br/>agent engine]
  EXEC --> CORE
  CORE -->|model requests| API[OpenAI Responses API / ChatGPT auth]
  CORE -->|tool calls| TOOLS[Tool runtime<br/>shell/apply_patch/etc]
  TOOLS --> SBX[Sandbox wrappers<br/>(Seatbelt/Landlock/Windows token)]
  CORE --> STATE[codex-rs/state<br/>SQLite state + rollouts]
```

### 1.2 关键设计目标（可复刻约束）
- 安全性：命令执行与文件写入遵循“审批模式（approval mode）”与“沙箱模式（sandbox mode）”。
- 可观察性：核心流程以事件流（events）对 UI/调用方输出；并写入日志/rollout。
- 可扩展性：通过 tool router + MCP 等机制扩展工具来源与能力。

## 2. 分层视角（Layers）

> 该项目并非传统 Web 服务，更贴近“本地 agent runtime”。因此这里的分层按职责划分，便于复刻。

### 2.1 入口层（Entry / UX）
- CLI 多工具入口：解析参数、选择子命令、将未指定子命令的输入转交给交互式 TUI。
- 交互式 TUI：渲染对话、展示工具执行与 diff、承接审批/输入。
- Headless exec：面向脚本/CI 的非交互运行。

### 2.2 Agent 引擎层（Core Engine）
- Session/Thread：会话（线程）模型、状态恢复（resume/fork）、rollout 记录。
- Turn loop：每一轮用户输入 → 模型推理 → 工具调用/审批 → 模型继续 → 结束。
- Context manager：把文件/工具输出/历史对话纳入上下文（受 token budget 限制）。
- Tool router：统一调度 shell/apply_patch/文件读写/其他工具（含 dynamic tools）。

### 2.3 协议与类型层（Protocol）
- `codex-rs/protocol/` 定义：
  - 事件（`Event`/`Op`/…）用于驱动 UI 与 headless 输出。
  - 配置类型（`Settings`、`SandboxPolicy`、`AskForApproval`、…）。
  - 模型 I/O（`ResponseInputItem`、`ResponseItem`、…）与工具调用形状。

### 2.4 基础设施层（Integrations / Platform）
- 模型提供方（OpenAI/ChatGPT/OSS providers 等）：HTTP / SSE / WebSocket 传输。
- 本地执行与沙箱：macOS Seatbelt / Linux Landlock+seccomp / Windows restricted token。
- 状态存储：`codex-rs/state` 维护的 `state.sqlite` + rollout 文件（JSONL）。
- Git、终端环境、keyring、通知系统等 OS 级依赖。

## 3. 通信模型（Communication Patterns）

### 3.1 内部：事件驱动（Event Stream）
- 核心引擎向 UI/调用方输出“事件流”（而不是直接打印日志）。
- “提交（`Submission`）→ 事件（`Event`）”是主抽象，可复刻到不同前端（TUI/GUI/IDE）。

### 3.2 外部：模型 API 与工具执行
- 模型 API：以 OpenAI Responses API（以及 ChatGPT 登录流）为主；支持流式输出。
- 工具执行：模型输出 tool calls 后进入本地 runtime，受 sandbox 与审批控制。

## 4. 关键模块依赖（Module Dependencies）

| 模块 | 主要职责 | 依赖 | 被依赖 |
|---|---|---|---|
| `codex-cli`（Node wrapper） | 选择并执行平台二进制；设置部分 env | Node.js | 终端用户 |
| `codex-rs/cli` | clap 多工具入口；分发到 TUI/exec/mcp 等 | `codex-core`, `codex-tui`, `codex-exec`, … | `codex` 二进制 |
| `codex-rs/core` | agent 引擎：turn loop、工具路由、上下文、rollout | `codex-protocol`, `codex-state`, … | `codex-tui`, `codex-exec` |
| `codex-rs/tui` | 全屏 UI；与 core 通过事件交互 | `codex-core`, `codex-protocol` | `codex-rs/cli` |
| `codex-rs/state` | SQLite state DB（threads/logs/tools） | `sqlx`, `codex-protocol` | `codex-core` |

## 5. 来源（Source）
- Node wrapper：`codex-cli/bin/codex.js`
- Rust CLI 多工具入口：`codex-rs/cli/src/main.rs`
- Core 引擎主类型：`codex-rs/core/src/codex.rs`
- 配置类型（`ConfigToml`）：`codex-rs/core/src/config/mod.rs`
- Feature flags：`codex-rs/core/src/features.rs`
- State DB：`codex-rs/state/src/runtime.rs` 与 `codex-rs/state/migrations/*.sql`
