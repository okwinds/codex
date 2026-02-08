# 仓库结构（Repo Layout）

本章面向“复刻实现者”，说明仓库中每个一级目录的职责与边界，并提供进一步深入的入口文件。

## 1. 根目录关键文件
- `README.md`：面向用户的快速安装与入口说明（npm/brew/Release）。
- `LICENSE` / `NOTICE`：许可证与第三方声明。
- `docs/`：用户文档（getting-started、config、sandbox、auth、skills、slash commands 等）。
- `justfile`：开发期常用命令封装（主要针对 `codex-rs/`）。
- `BUILD.bazel` / `MODULE.bazel` / `defs.bzl`：Bazel 构建定义。
- `flake.nix` / `flake.lock`：Nix flake（可选开发/构建方式）。
- `pnpm-workspace.yaml` / `pnpm-lock.yaml` / `package.json`：Node workspace 与仓库级维护工具（prettier）。

## 2. 一级目录说明

| 目录 | 角色 | 你在复刻时通常要做什么 |
|---|---|---|
| `codex-rs/` | **维护中的主实现（Rust）** | 复刻核心：turn loop、工具执行、sandbox、状态管理、TUI、协议 |
| `codex-cli/` | npm 包包装层（运行 Rust 二进制） | 复刻分发：平台探测、binary 选择、PATH/ENV 注入、信号转发 |
| `sdk/typescript/` | TypeScript SDK | 复刻对外 SDK/示例（可选，但建议保留以便生态集成） |
| `shell-tool-mcp/` | Shell Tool MCP server（Node） | 复刻 MCP server 的 shell tool 封装与测试 |
| `docs/` | 用户文档 | 可作为对外行为参考；复刻时要保证文档描述的行为能实现 |
| `scripts/` | 仓库维护脚本 | 用于开发/发布/CI（复刻时可按需简化） |
| `third_party/` / `patches/` | 第三方与补丁 | 支持 Bazel / 打包等（复刻时可根据构建体系决定是否需要） |

## 3. 关键“入口点”导航

### 3.1 用户入口（可执行）
- npm 安装：`codex-cli/bin/codex.js`（Node wrapper）
- Rust 多工具入口：`codex-rs/cli/src/main.rs`（clap Parser）

### 3.2 核心引擎入口（复刻重点）
- `codex-rs/core/src/codex.rs`：`Codex`（Submission/Events 抽象与 turn loop 调度）
- `codex-rs/core/src/config/mod.rs`：`ConfigToml` + 配置加载/编辑
- `codex-rs/core/src/features.rs`：Feature flags（稳定/实验/弃用）
- `codex-rs/core/src/tools/`：tool router + sandboxing + 并发执行
- `codex-rs/protocol/`：跨模块协议类型（events/config/model/tool calls）
- `codex-rs/state/`：SQLite state DB + rollout metadata 抽取

## 4. 来源（Source）
- 目录结构以本仓库 root 为准（见 `docs/workdocjcl/inventory/file_manifest_repo.txt`）。
