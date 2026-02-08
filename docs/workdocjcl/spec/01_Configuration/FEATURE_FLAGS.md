# 功能开关（Feature Flags）

Codex 使用集中式 feature registry（`codex-rs/core/src/features.rs`）管理实验性/稳定特性。

## 1. 配置入口
feature flags 主要来自 `config.toml` 的：
```toml
[features]
shell_tool = true
collab = false
```

对应类型：
- `codex_core::features::FeaturesToml`（`entries: BTreeMap<String, bool>`）

## 2. 内建特性清单（以源码 registry 为准）

> 复刻要求：实现一个“key → enabled”的 feature 系统，并按 default_enabled 初始化，再叠加 config.toml 覆盖。

| key | Feature ID（枚举） | stage | default_enabled | 说明（简述） |
|---|---|---|---:|---|
| `undo` | `GhostCommit` | Stable | false | 每 turn 创建 ghost commit（用于 undo） |
| `shell_tool` | `ShellTool` | Stable | true | 默认 shell tool |
| `web_search_request` | `WebSearchRequest` | Deprecated | false | 旧版 web search 请求开关 |
| `web_search_cached` | `WebSearchCached` | Deprecated | false | 旧版 cached web search 开关 |
| `unified_exec` | `UnifiedExec` | Experimental | false | 统一 PTY-backed exec tool（背景终端） |
| `shell_snapshot` | `ShellSnapshot` | Experimental | false | shell 环境快照 |
| `runtime_metrics` | `RuntimeMetrics` | UnderDevelopment | false | 运行时 metrics 快照 |
| `sqlite` | `Sqlite` | UnderDevelopment | false | SQLite state 支持（见 state crate） |
| `child_agents_md` | `ChildAgentsMd` | UnderDevelopment | false | 将 AGENTS.md 附加到子 agent 指令 |
| `apply_patch_freeform` | `ApplyPatchFreeform` | UnderDevelopment | false | freeform apply_patch tool |
| `exec_policy` | `ExecPolicy` | UnderDevelopment | true | execpolicy enforcement |
| `request_rule` | `RequestRule` | Stable | true | 允许模型请求 approval 并提议 exec 规则 |
| `experimental_windows_sandbox` | `WindowsSandbox` | UnderDevelopment | false | Windows sandbox（restricted token） |
| `elevated_windows_sandbox` | `WindowsSandboxElevated` | UnderDevelopment | false | Windows elevated sandbox pipeline |
| `remote_compaction` | `RemoteCompaction` | UnderDevelopment | true | ChatGPT auth 下的远程 compaction |
| `remote_models` | `RemoteModels` | UnderDevelopment | true | 刷新远程模型列表并发出 AppReady |
| `powershell_utf8` | `PowershellUtf8` | Windows:Stable / else:UnderDevelopment | OS-dependent | PowerShell UTF-8 输出强制 |
| `enable_request_compression` | `EnableRequestCompression` | Stable | true | 请求 body 压缩（zstd） |
| `collab` | `Collab` | Experimental | false | Sub-agents（协作/并行） |
| `apps` | `Apps` | Experimental | false | Apps/Connectors（通过 `$` 引用） |
| `skill_mcp_dependency_install` | `SkillMcpDependencyInstall` | Stable | true | 提示并安装缺失 MCP 依赖 |
| `skill_env_var_dependency_prompt` | `SkillEnvVarDependencyPrompt` | UnderDevelopment | false | 提示缺失 skill env var 依赖 |
| `steer` | `Steer` | Experimental | false | Steer conversation（Enter 立即提交、Tab 排队） |
| `collaboration_modes` | `CollaborationModes` | Stable | true | collaboration modes（Plan/Code/…） |
| `personality` | `Personality` | Stable | true | personality 选择 |
| `responses_websockets` | `ResponsesWebsockets` | UnderDevelopment | false | 默认使用 Responses WebSocket 传输 |

## 3. UnderDevelopment 特性告警
若启用 stage 为 `UnderDevelopment` 的 feature，且未设置 `suppress_unstable_features_warning=true`，系统会在 session 配置后推送 warning event，提示用户这些开关不稳定。

## 4. Legacy/兼容开关
项目保留 legacy feature keys（用于向后兼容旧配置），实现位置：
- `codex-rs/core/src/features/legacy.rs`

## 5. 来源（Source）
- Feature registry：`codex-rs/core/src/features.rs`
- Legacy keys：`codex-rs/core/src/features/legacy.rs`
