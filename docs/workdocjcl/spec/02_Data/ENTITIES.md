# 数据实体（Data Entities）

本仓库主要是“本地 agent”。数据层并非业务数据库，而是用于**会话索引与诊断**的 SQLite state DB（`state.sqlite`）。

## Entity: `threads`

### Purpose
存储每个 thread/session 的**索引元数据**，用于：
- `resume` / `fork` 的会话选择器展示
- 基于时间、source/provider、归档等筛选
- 保存与 repo/git 相关的上下文快照（sha/branch/origin）

### Fields（表结构）
来源：`codex-rs/state/migrations/0001_threads.sql`

| 字段 | SQLite 类型 | Nullable | Default | 约束 | 描述 |
|---|---|---:|---|---|---|
| `id` | TEXT | No | - | PK | thread id（通常为 UUID 字符串） |
| `rollout_path` | TEXT | No | - | - | rollout JSONL 的路径 |
| `created_at` | INTEGER | No | - | - | 创建时间（epoch seconds） |
| `updated_at` | INTEGER | No | - | - | 更新时间（epoch seconds） |
| `source` | TEXT | No | - | - | session source（与协议一致） |
| `model_provider` | TEXT | No | - | - | 使用的模型 provider id（如 `openai`） |
| `cwd` | TEXT | No | - | - | 启动时工作目录 |
| `title` | TEXT | No | - | - | thread 标题 |
| `sandbox_policy` | TEXT | No | - | - | 沙箱策略快照（字符串化） |
| `approval_mode` | TEXT | No | - | - | 审批模式快照（字符串化） |
| `tokens_used` | INTEGER | No | `0` | - | token 使用量累计 |
| `has_user_event` | INTEGER | No | `0` | - | 是否出现过用户事件（0/1） |
| `archived` | INTEGER | No | `0` | - | 是否归档（0/1） |
| `archived_at` | INTEGER | Yes | - | - | 归档时间（epoch seconds） |
| `git_sha` | TEXT | Yes | - | - | 启动时 git sha |
| `git_branch` | TEXT | Yes | - | - | 启动时 git branch |
| `git_origin_url` | TEXT | Yes | - | - | 启动时 remote origin URL |

### Indexes
- `idx_threads_created_at`：`(created_at DESC, id DESC)`
- `idx_threads_updated_at`：`(updated_at DESC, id DESC)`
- `idx_threads_archived`：`(archived)`
- `idx_threads_source`：`(source)`
- `idx_threads_provider`：`(model_provider)`

### Lifecycle
- Created：创建 thread/session 时写入（rollout_path 初始确定）
- Updated：每次 turn 或元数据变更时更新（updated_at/tokens_used/title 等）
- Deleted：通过 foreign key 的 cascade 影响 dynamic tools；threads 本身通常保留（可归档）

## Entity: `logs`

### Purpose
以结构化方式存储日志，用于 UI 查看与诊断。

### Fields
来源：`codex-rs/state/migrations/0002_logs.sql` 与 `0003_logs_thread_id.sql`

| 字段 | SQLite 类型 | Nullable | Default | 约束 | 描述 |
|---|---|---:|---|---|---|
| `id` | INTEGER | No | auto | PK | 自增主键 |
| `ts` | INTEGER | No | - | - | 秒级时间戳 |
| `ts_nanos` | INTEGER | No | - | - | 纳秒补偿 |
| `level` | TEXT | No | - | - | 日志级别 |
| `target` | TEXT | No | - | - | logger target |
| `message` | TEXT | Yes | - | - | 日志消息 |
| `module_path` | TEXT | Yes | - | - | Rust module path |
| `file` | TEXT | Yes | - | - | 源文件 |
| `line` | INTEGER | Yes | - | - | 行号 |
| `thread_id` | TEXT | Yes | - | - | 关联 thread id |

### Indexes
- `idx_logs_ts`：`(ts DESC, ts_nanos DESC, id DESC)`
- `idx_logs_thread_id`：`(thread_id)`

## Entity: `thread_dynamic_tools`

### Purpose
存储 thread 级别的 dynamic tools（工具定义持久化）。

### Fields
来源：`codex-rs/state/migrations/0004_thread_dynamic_tools.sql`

| 字段 | SQLite 类型 | Nullable | Default | 约束 | 描述 |
|---|---|---:|---|---|---|
| `thread_id` | TEXT | No | - | PK(1) / FK | 关联 threads.id |
| `position` | INTEGER | No | - | PK(2) | 工具顺序（稳定排序） |
| `name` | TEXT | No | - | - | tool name |
| `description` | TEXT | No | - | - | tool description |
| `input_schema` | TEXT | No | - | - | JSON Schema（序列化字符串） |

### Indexes
- `idx_thread_dynamic_tools_thread(thread_id)`

## state.sqlite 的位置与初始化
- 文件名：`state.sqlite`（`STATE_DB_FILENAME`，见 `codex-rs/state/src/runtime.rs`）
- 路径：`<CODEX_HOME>/state.sqlite`
- 初始化：`StateRuntime::init` 会确保 `CODEX_HOME` 存在，并打开/迁移数据库。

## 来源（Source）
- SQLite migrations：`codex-rs/state/migrations/*.sql`
- State runtime：`codex-rs/state/src/runtime.rs`
