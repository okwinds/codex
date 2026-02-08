# 基础设施：打包与分发（Packaging & Distribution）

本章描述 Codex CLI 如何通过 npm/brew/GitHub Releases 分发，并解释 `codex-cli/` 目录的“包装器”职责。

## 1. npm 包 `@openai/codex`（Node wrapper + vendor binaries）

### 1.1 包结构
- `codex-cli/package.json`：
  - `bin.codex = "bin/codex.js"`
  - `files = ["bin", "vendor"]`
- `codex-cli/bin/codex.js`：统一入口
- `codex-cli/vendor/<target-triple>/codex/<codex>`：平台二进制
- `codex-cli/vendor/<target-triple>/path/`：可选额外 PATH 注入目录（如 bundled tools）

### 1.2 平台选择逻辑（复刻重点）
输入：`process.platform` + `process.arch`
输出：`targetTriple`（字符串）
- linux/android:
  - x64 → `x86_64-unknown-linux-musl`
  - arm64 → `aarch64-unknown-linux-musl`
- darwin:
  - x64 → `x86_64-apple-darwin`
  - arm64 → `aarch64-apple-darwin`
- win32:
  - x64 → `x86_64-pc-windows-msvc`
  - arm64 → `aarch64-pc-windows-msvc`

若不支持的组合：抛错 `Unsupported platform: ...`。

### 1.3 子进程执行与信号转发
- 使用 `spawn`（非 spawnSync）以便 Node 可响应信号并转发给 child。
- `stdio: "inherit"`：保证 TUI 等场景行为一致。
- forward signals：`SIGINT`、`SIGTERM`、`SIGHUP`
- 父进程退出语义：
  - child 因 signal 退出：父 re-emit 同 signal（保证 shell 得到 128+n 语义）
  - child exit code：父 `process.exit(code)`

### 1.4 PATH 注入
若存在 `vendor/<triple>/path` 目录：追加到 PATH 头部（优先于系统 PATH）。

### 1.5 安装来源提示（CODEX_MANAGED_BY_*）
wrapper 会根据 `npm_config_user_agent`/安装路径推断包管理器：
- bun → `CODEX_MANAGED_BY_BUN=1`
- 默认 → `CODEX_MANAGED_BY_NPM=1`

复刻建议：保持该环境变量语义，用于 UI/错误提示“如何更新 Codex”。

## 2. 其他分发渠道（概念）
- Homebrew cask：安装平台二进制（细节不在本仓库代码中实现）
- GitHub Releases：提供带 target triple 的 tar.gz/zip（见根 `README.md`）
- DotSlash：Release 中的 `codex` dotslash 文件（见 `docs/install.md`）

## 3. 来源（Source）
- wrapper：`codex-cli/bin/codex.js`
- npm metadata：`codex-cli/package.json`
- 用户说明：`README.md`、`docs/install.md`
