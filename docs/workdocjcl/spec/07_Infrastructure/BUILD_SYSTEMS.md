# 基础设施：构建系统（Build Systems）

本章描述仓库如何构建、测试、打包。复刻时可以选择不同构建体系，但应保留等价产物与行为。

## 1. Rust（主实现）

### 1.1 Cargo workspace
- workspace root：`codex-rs/`
- workspace 定义：`codex-rs/Cargo.toml`
- 推荐开发命令（来源 `docs/install.md`）：
```bash
cd codex-rs
cargo build
cargo run --bin codex -- "explain this codebase to me"
just fmt
just fix -p <crate>
cargo test -p codex-tui
```

### 1.2 Justfile（开发辅助）
- repo 根目录存在 `justfile`（默认指向 `codex-rs`）
- 典型用途：统一 fmt/clippy/test/schema generation

### 1.3 Bazel（可选）
- 根目录 `BUILD.bazel`, `MODULE.bazel` 以及相关 `.bzl` 文件
- 目标：提供可复现/可缓存的构建方式（CI/Release 用）

### 1.4 Nix flake（可选）
- `flake.nix` 提供开发环境或构建封装

## 2. Node/TypeScript（workspace packages）

### 2.1 pnpm workspace
- workspace 定义：`pnpm-workspace.yaml`
- 仓库级工具：`package.json`（prettier）

### 2.2 主要 packages 与构建工具
- `codex-cli/`（`@openai/codex`）：Node wrapper，主要是脚本/分发；无 TS build
- `sdk/typescript/`：`tsup` 构建，`jest` 测试
- `shell-tool-mcp/`：`tsup` 构建，`jest` 测试

## 3. 产物（Artifacts）
- 原生二进制：`codex`（多平台 target triple）
- npm 包：`@openai/codex`（携带平台 vendor 二进制 + wrapper）
- TypeScript SDK：`@openai/codex-sdk`（dist JS + d.ts）

## 4. 来源（Source）
- Rust build：`codex-rs/Cargo.toml`、`docs/install.md`
- Node build：各 package 的 `package.json`
- Bazel：`BUILD.bazel`、`MODULE.bazel`
- Nix：`flake.nix`
