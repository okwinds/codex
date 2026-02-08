# Tool: `test_sync_tool` (function, test-only)

## 0. 目的
为测试提供同步/延迟注入工具：
- sleep_before_ms / sleep_after_ms：注入延迟
- barrier：跨并发参与者同步（屏障）

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

仅当 `experimental_supported_tools` 包含 `"test_sync_tool"`：
- `builder.push_spec_with_parallel_support(create_test_sync_tool(), true)`
- `builder.register_handler("test_sync_tool", TestSyncHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_test_sync_tool`
解析类型：`codex-rs/core/src/tools/handlers/test_sync.rs::TestSyncArgs`

字段：
- `sleep_before_ms`（可选）：执行前 sleep
- `sleep_after_ms`（可选）：执行后 sleep
- `barrier`（可选 object）：
  - `id`（必填）：barrier id
  - `participants`（必填）：参与者数量（>0）
  - `timeout_ms`（默认 1000，>0）：等待超时

## 3. 运行时语义
handler：`codex-rs/core/src/tools/handlers/test_sync.rs::TestSyncHandler`

步骤：
1) 若 `sleep_before_ms>0`：sleep
2) 若提供 barrier：`wait_on_barrier`
   - 若 participants==0 → 错误
   - 若 timeout_ms==0 → 错误
   - 通过 `OnceLock<Mutex<HashMap<String, BarrierState>>>` 保存/复用 barrier
   - 若同 id 已存在且 participants 不一致 → 错误
   - `tokio::time::timeout(timeout, barrier.wait())` 超时 → 错误 `"test_sync_tool barrier wait timed out"`
   - leader 会清理 map 中的 barrier（防泄漏）
3) 若 `sleep_after_ms>0`：sleep
4) 返回 `"ok"`

## 4. 输出
`ToolOutput::Function { content:"ok", success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_test_sync_tool`
- handler：`codex-rs/core/src/tools/handlers/test_sync.rs`

