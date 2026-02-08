# Schema Migrations（state.sqlite）

state DB migrations 由 `sqlx::migrate!` 管理，并在运行时自动应用。

## 1. Migration History
来源：`codex-rs/state/migrations/*.sql`

| 版本（文件） | 描述 | 可逆性（Reversible） |
|---|---|---|
| `0001_threads.sql` | 创建 `threads` 表 + 索引 | 部分可逆（DROP TABLE 可逆但会丢数据） |
| `0002_logs.sql` | 创建 `logs` 表 + `idx_logs_ts` | 同上 |
| `0003_logs_thread_id.sql` | 给 `logs` 添加 `thread_id` 列并创建 `idx_logs_thread_id` | 低（SQLite 不易 drop column；需要重建表） |
| `0004_thread_dynamic_tools.sql` | 创建 `thread_dynamic_tools` 表（FK 到 threads，CASCADE） | 同 0001 |

## 2. Current Schema Version
截至本规格文档基准提交，最新 migration 为：`0004_thread_dynamic_tools.sql`。

## 3. Migration Strategy（运行时策略）
- Migrator 定义：`codex-rs/state/src/migrations.rs`（`sqlx::migrate!("./migrations")`）
- 应用时机：state runtime 初始化时（`StateRuntime::init` 打开 DB 后执行迁移）
- DB 文件位置：`<CODEX_HOME>/state.sqlite`（见 `codex-rs/state/src/runtime.rs`）

## 4. Rollback Procedures（复刻建议）
由于 SQLite migration 回滚在实践中通常不做自动化，建议复刻时采取：
1) 以 migration 文件为唯一 schema 来源（不可手写偏差）
2) schema 变更通过“新增 migration”前进式演进
3) 若需回滚：使用备份/重建（导出数据 → 重建旧 schema → 回灌）

## 5. 来源（Source）
- `codex-rs/state/src/migrations.rs`
- `codex-rs/state/src/runtime.rs`
