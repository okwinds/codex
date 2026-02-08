# 集成测试规格（Integration Specs）

本章描述跨模块的关键集成点，应通过 integration tests 或 end-to-end harness 验证。

## 1. 集成：CLI → TUI → Core（默认交互模式）

### Purpose
验证“用户可见的交互模式”在多模块协作下工作正常：参数解析、配置加载、事件流、turn loop。

### Test Cases
| ID | 场景 | Setup | Action | Verification |
|---|---|---|---|---|
| I001 | 启动并提交 prompt | 有 git repo，配置可用 | `codex "hello"` 或启动后输入 | 事件流产生 message deltas；turn complete；退出原因正确 |
| I002 | 需要审批的工具调用 | 模型产生 shell/apply_patch | UI 中批准 | 命令/patch 在沙箱内执行；diff 事件一致；tool output 回注模型 |

## 2. 集成：CLI login → core auth store

### Purpose
验证登录流程对后续模型请求可用且不会泄露 secret。

### Test Cases
| ID | 场景 | Setup | Action | Verification |
|---|---|---|---|---|
| I101 | API key 登录 | stdin pipe key | `codex login --with-api-key` | 凭据持久化；`codex login status` 显示 api-key 模式 |
| I102 | device-code fallback | headless 环境 | `codex login`（触发 fallback） | device code 不可用时回退到 browser login server |

## 3. 集成：core ↔ state.sqlite（threads/logs/dynamic_tools）

### Purpose
验证会话元数据与日志/动态工具的持久化一致性。

### Test Cases
| ID | 场景 | Setup | Action | Verification |
|---|---|---|---|---|
| I201 | 初始化 DB | 新 CODEX_HOME | 启动 Codex | `state.sqlite` 创建 + migrations 已应用 |
| I202 | thread 索引 | 完成一轮对话 | `resume` 打开 picker | thread 列表包含新会话；字段正确 |
| I203 | dynamic tools 持久化 | 注入 dynamic tools | 重启并恢复 | tools 能按 position 恢复 |

## 4. 集成：Node wrapper → Rust binary

### Purpose
验证 `@openai/codex` 作为透明启动器的语义一致。

### Test Cases
| ID | 场景 | Setup | Action | Verification |
|---|---|---|---|---|
| I301 | platform 选择 | 模拟不同 OS/arch | 执行 `codex` | 选择正确 targetTriple；执行 vendor binary |
| I302 | 信号转发 | 启动长任务 | Ctrl+C | child 收到信号并退出；父进程退出语义一致 |

## 5. 清单与定位
- Node/TS 的集成测试可见：`sdk/typescript/tests/*`、`shell-tool-mcp/tests/*`
- Rust 的集成测试与快照测试清单：`workdocjcl/inventory/rust_test_manifest.txt`

## 6. 来源（Source）
- wrapper：`codex-cli/bin/codex.js`
- CLI：`codex-rs/cli/src/main.rs`、`codex-rs/cli/src/login.rs`
- core：`codex-rs/core/src/codex.rs`
- state：`codex-rs/state/src/runtime.rs`
