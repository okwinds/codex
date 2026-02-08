# 状态机（State Machines）

本章描述 Codex CLI 的关键状态机，以确保复刻时“外部可观测行为（events/状态）”一致。

## 1. Agent 生命周期状态机（`AgentStatus`）

### States
| 状态 | 含义 | 进入条件 | 退出条件 |
|---|---|---|---|
| `pending_init` | 等待初始化 | session 尚未配置完成或 agent 尚未启动 | 收到 `turn_started` 或 `shutdown_complete` 等终态 |
| `running` | 正在运行 turn | 收到 `turn_started` | 收到 `turn_complete` / `turn_aborted` / `error` / `shutdown_complete` |
| `completed(last_message?)` | 正常完成 | 收到 `turn_complete` | 终态 |
| `errored(message)` | 异常终止 | 收到 `turn_aborted` 或 `error` | 终态 |
| `shutdown` | 关闭完成 | 收到 `shutdown_complete` | 终态 |
| `not_found` | 查询不到 agent | 查询不存在的 thread_id | 终态（对查询者而言） |

### Transitions
```mermaid
stateDiagram-v2
  [*] --> pending_init
  pending_init --> running: turn_started
  running --> completed: turn_complete
  running --> errored: turn_aborted / error
  pending_init --> shutdown: shutdown_complete
  running --> shutdown: shutdown_complete
  state completed {
    [*] --> completed
  }
  state errored {
    [*] --> errored
  }
```

### Transition Details（关键映射）
| From | To | Trigger（EventMsg） | Side Effects（对外） |
|---|---|---|---|
| `pending_init` | `running` | `TurnStarted` | UI 显示“任务进行中”；可能禁止重复提交或进入 steer 模式 |
| `running` | `completed` | `TurnComplete` | 输出最终 assistant message；更新 session 状态与 rollout |
| `running` | `errored` | `TurnAborted` | 输出 abort reason；可能提示用户重试/检查权限/登录等 |
| `running` | `errored` | `Error` | 输出 error message；记录日志 |
| `*` | `shutdown` | `ShutdownComplete` | 资源清理完成 |

### Invalid Transitions
- `completed/errored/shutdown` 不应回到 `running`（除非开启新 turn，体现在新一轮事件，而不是复用旧状态对象）。

### Source
- 状态定义：`codex-rs/protocol/src/protocol.rs`（`AgentStatus`）
- 事件到状态映射：`codex-rs/core/src/agent/status.rs`（`agent_status_from_event`）

## 2. Thread 归档状态（state DB 层）

### States
| 状态 | 存储字段 | 含义 |
|---|---|---|
| active | `threads.archived = 0` | 默认状态，可 resume/fork |
| archived | `threads.archived = 1` | 归档状态，通常默认过滤；仍可恢复/查看（取决于 UI） |

### Source
- schema：`codex-rs/state/migrations/0001_threads.sql`
- 查询过滤：`codex-rs/state/src/runtime.rs`（thread filters）
