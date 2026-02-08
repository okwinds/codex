# 端到端测试规格（E2E Specs）

E2E 关注“用户完成任务”的闭环体验，覆盖安装、登录、交互式 turn loop、工具执行与会话恢复。

## Journey: 首次运行与登录（Login Onboarding）

### Description
用户首次运行 `codex`，完成登录（ChatGPT 或 API key），确保后续模型请求可用。

### Preconditions
- `CODEX_HOME` 指向空目录或未设置（默认 `~/.codex`）
- 环境允许打开浏览器（或使用 device-code / API key）

### Steps
| Step | Action | Expected Result |
|---:|---|---|
| 1 | 运行 `codex` | 出现 onboarding/login 指引（若需要） |
| 2 | 选择 ChatGPT 登录并完成授权 | CLI/TUI 显示登录成功；凭据写入存储 |
| 3 | 运行 `codex login status` | 显示已登录（ChatGPT 或 API key） |

### Variations
- 使用 API key：`printenv OPENAI_API_KEY | codex login --with-api-key`
- headless：device-code flow 或 fallback

## Journey: 交互式执行一次工具调用（Tool Call Turn）

### Description
在 TUI 中输入 prompt，模型产生 tool call（例如 shell），用户审批后执行并回注模型。

### Preconditions
- 已登录或使用可用 provider（对于 OSS provider 可不登录）
- 工作目录是一个 git repo（便于 diff 展示）

### Steps
| Step | Action | Expected Result |
|---:|---|---|
| 1 | `codex` 启动 TUI | UI 正常渲染，显示当前 cwd |
| 2 | 输入 prompt 触发工具调用 | 事件流显示模型输出与 tool call |
| 3 | UI 中批准执行 | 命令在沙箱内执行；stdout/stderr 可见；若有文件变更显示 diff |
| 4 | turn 完成 | 显示最终回答；state.sqlite 记录 thread 元数据 |

### Variations
- apply_patch 工具：生成 diff 并批准写入
- 不批准：tool call 返回错误输出，模型继续或中止

## Journey: 恢复与分叉会话（Resume/Fork）

### Preconditions
- 存在至少一个历史 thread（完成过一次 turn）

### Steps
| Step | Action | Expected Result |
|---:|---|---|
| 1 | `codex resume --last` | 直接进入最近会话并继续对话 |
| 2 | `codex fork --last` | 创建新 thread（新 id），包含旧历史作为上下文 |

## Journey: 非交互执行（Headless exec）

### Preconditions
- 可用 provider

### Steps
| Step | Action | Expected Result |
|---:|---|---|
| 1 | `codex exec \"do X\"` | 进程运行直到认为任务完成并退出 |
| 2 | 检查退出码 | 成功为 0；失败为 1 |

### Known Issues
- 真实模型调用依赖网络与有效凭据；CI 中通常使用 mock server 或跳过 live tests。

## 来源（Source）
- TUI 入口与 onboarding：`codex-rs/tui/src/lib.rs`、`codex-rs/tui/src/onboarding/`
- resume/fork CLI：`codex-rs/cli/src/main.rs`
- state DB：`codex-rs/state/`
