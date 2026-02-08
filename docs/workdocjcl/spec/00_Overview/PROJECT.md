# 项目概览（复刻规格文档）

## 身份信息（Identity）
- 项目名称：OpenAI Codex CLI（Monorepo）
- 仓库目录：本地工作区根目录（即本仓库根目录）
- 上游仓库：`openai/codex`（GitHub）
- License：Apache-2.0（见 `LICENSE`）
- 本次规格文档基准提交（以代码为准）：`7f567b11ecb56a92a105b9a624dabadc44147ddd`
- 规格文档固定锚点（tag，便于回滚/重放）：`docs-workdocjcl-20260208`
- 目标：**在不阅读原始代码的前提下，仅凭本规格文档可复刻该项目的关键行为与系统结构**（允许使用不同技术栈复刻，但需达到同等外部接口与行为）

## 项目是什么（What）
Codex CLI 是一个运行在本地终端的 coding agent。它主要提供：
- 交互式 TUI（全屏终端 UI），以“对话 + 工具调用（shell、apply_patch、文件读写等）”方式在本地仓库内完成任务。
- 非交互式/自动化模式（`codex exec` / `codex review` 等）用于 CI 或脚本化调用。
- 沙箱与执行策略（sandbox/execpolicy），用于把命令执行限制在目录/权限/网络策略内。
- MCP（Model Context Protocol）客户端与（实验性）MCP Server。
- 本地状态与回放（rollouts / session），支持 resume/fork、历史记录、线程（thread）索引等。

## 单仓结构与组件（Monorepo Composition）
该仓库并非单一语言项目，核心组件如下：

1) Rust 实现（维护中的主实现）
- 目录：`codex-rs/`
- 产物：`codex` 原生可执行文件（多平台）
- 关键 crate：
  - `codex-rs/cli/`：顶层多工具 CLI（`codex` 子命令入口）
  - `codex-rs/tui/`：交互式终端 UI
  - `codex-rs/core/`：核心 agent/turn 循环、工具路由、配置解析、上下文管理、模型客户端、rollout 记录等
  - `codex-rs/protocol/`：跨 crate 的协议类型（事件、配置类型、模型 I/O 类型等）
  - `codex-rs/state/`：SQLite-backed 状态库（threads、logs、dynamic_tools）

2) Node.js “分发/包装”层（npm 包）
- 目录：`codex-cli/`
- 包名：`@openai/codex`（见 `codex-cli/package.json`）
- 职责：根据 `process.platform`/`process.arch` 选择 `codex-cli/vendor/<target-triple>/codex/<codex>` 并执行；用于 `npm i -g @openai/codex` 的零依赖安装体验。
- 入口：`codex-cli/bin/codex.js`

3) TypeScript SDK
- 目录：`sdk/typescript/`
- 包名：`@openai/codex-sdk`
- 职责：提供 Codex 相关 API/协议的 TypeScript 客户端（用于外部集成/测试/示例）。

4) Shell Tool MCP Server（Node/TS）
- 目录：`shell-tool-mcp/`
- 包名：`@openai/codex-shell-tool-mcp`
- 职责：以 MCP server 形式提供 shell tool（含 patched bash/exec wrapper）的能力。

## 技术栈（Tech Stack）
- Rust：Cargo workspace（`codex-rs/Cargo.toml`；workspace edition 2024）
- Node.js/TypeScript：pnpm workspace（`pnpm-workspace.yaml`）
- 本地数据库：SQLite（用于 state DB，见 `codex-rs/state/`）
- 构建体系：
  - Cargo（Rust build/test）
  - pnpm + tsup + jest（TS packages build/test）
  - Bazel（`BUILD.bazel`, `MODULE.bazel`）与 Nix flake（`flake.nix`）作为可选/补充构建方式

## 运行与构建（Build & Run）
### A. 用户安装（推荐）
```bash
# npm
npm install -g @openai/codex
codex

# Homebrew（macOS）
brew install --cask codex
codex
```

### B. 从源码构建（Rust）
```bash
git clone https://github.com/openai/codex.git
cd codex/codex-rs

# 需要 Rust toolchain
rustup component add rustfmt clippy
cargo install just

cargo build
# 运行（交互式 TUI 默认路径）
cargo run --bin codex -- "explain this codebase to me"
```

### C. TS/Node workspace（用于 SDK 与 MCP server）
```bash
# repo 根目录
pnpm -v
pnpm -C sdk/typescript build
pnpm -C sdk/typescript test

pnpm -C shell-tool-mcp build
pnpm -C shell-tool-mcp test
```

## 环境要求（Environment Requirements）
- 操作系统：macOS 12+ / Linux（推荐容器隔离）/ Windows 11（通过 WSL2）
- Node：仓库维护工具要求 `>=22`（见根 `package.json`），部分包可 `>=18`（见各自 `package.json`）
- Rust：支持 edition 2024 的工具链（见 `codex-rs/Cargo.toml`）
- 运行时关键配置：
  - 配置目录：默认 `~/.codex`，可通过 `CODEX_HOME` 指定（详见 `01_Configuration/ENVIRONMENT.md`）
  - 日志：默认写入 `~/.codex/log/…`

## 代码到规格文档映射（Mapping）
- 本规格文档的“模块/接口/行为”说明会在每个章节末尾提供“来源（Source）”并给出实现位置（文件路径）。
- 完整清单类材料：
  - `docs/workdocjcl/inventory/file_manifest_repo.txt`：repo tracked 文件清单（默认排除 `docs/workdocjcl/**`，避免规格递归）
  - `docs/workdocjcl/inventory/rust_workspace.md`：Rust workspace member 列表
  - `docs/workdocjcl/inventory/node_workspace.md`：pnpm workspace package 列表
