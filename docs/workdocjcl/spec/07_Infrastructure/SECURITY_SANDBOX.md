# 基础设施：安全模型、审批与沙箱（Security, Approvals, Sandbox）

本章以“可复刻的安全边界”为目标，描述 Codex CLI 如何限制模型的本地执行能力，并让用户控制授权范围。

> 重要：该仓库同时存在“产品安全模型”和“开发/测试时的沙箱约束”。复刻时必须确保用户安全模型不被弱化。

## 1. 三个核心概念
- **Approval policy / mode**：是否需要用户确认某类操作（命令执行、文件写入、危险操作等）。
- **Sandbox mode**：执行命令的隔离强度（文件访问范围、可写范围、网络是否可用）。
- **Execpolicy**：允许/禁止某些命令的规则系统（更细粒度的命令白名单/策略）。

## 2. 平台沙箱机制（按 OS）

### 2.1 macOS：Seatbelt（sandbox-exec）
- 原理：通过 `sandbox-exec` 限制子进程读写路径、网络访问等。
- Codex 还提供 `codex sandbox macos`（以及 legacy alias `codex debug seatbelt`）用于单独测试沙箱行为。

### 2.2 Linux：Landlock + seccomp
- 原理：文件系统访问控制（Landlock）+ 系统调用过滤（seccomp）。
- Codex 提供 `codex sandbox linux`（以及 legacy alias `codex debug landlock`）。

### 2.3 Windows：Restricted token
- 原理：使用受限令牌执行命令，降低权限、限制可访问资源。
- Codex 提供 `codex sandbox windows`。

## 3. Sandboxing 与网络策略
对用户可见的核心原则（复刻目标）：
- 在更“自动”的模式下（例如 full-auto），仍需要提供“网络默认禁用”的防线（除非用户明确允许）。
- 文件写入范围应严格限定在 workspace 或明确白名单路径内。

实现细节分散在多个 crate（平台相关 + tool runtime），复刻时建议抽象出统一的“SandboxPolicy”：
- 输入：sandbox_mode + 工作目录 + 允许写入的 roots + 是否允许网络 + 是否记录 denial
- 输出：一个“运行命令”的 wrapper（或基于 OS 的隔离容器/沙箱）

## 4. 审批（Approvals）
审批体系的目标：
- 让模型“能提出行动计划”，但把危险行动交给用户确认。
- 把“允许/拒绝/调整规则（例如 execpolicy amendments）”作为可持久化决策的一部分。

复刻建议：
- 把审批结果写入 session/rollout（用于审计与恢复）
- 在 UI 中清晰展示待批准操作（命令、文件变更、风险等级）

复刻级细节（事件形状、缓存、sandbox deny 重试、amendment 应用）见：
- `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`

## 5. Execpolicy（命令策略）
execpolicy 是更细粒度的命令控制层：
- 用文件/规则表达“哪些命令可以运行、哪些必须批准、哪些禁止”
- 既用于产品安全，也用于企业/组织策略

复刻级细节（规则语言/加载/匹配/决策/落盘）见：
- `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md`
- `docs/workdocjcl/spec/07_Infrastructure/COMMAND_SAFETY.md`（execpolicy fallback 依赖的安全/危险启发式）

## 6. 来源（Source）
- CLI sandbox 子命令：`codex-rs/cli/src/main.rs#Subcommand`
- Execpolicy：`docs/execpolicy.md`、`codex-rs/execpolicy*`
- Sandbox wrappers：`codex-rs/cli` + 平台相关 crate（Seatbelt/Landlock/Windows）
- 协议类型：`codex-rs/protocol/src/protocol.rs#SandboxPolicy`
