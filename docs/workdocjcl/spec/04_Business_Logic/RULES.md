# 业务规则（Business Rules）

这里的“业务规则”不是电商/订单类规则，而是 **agent 产品规则**：安全、配置、执行策略、会话行为等。

## Rule: 配置目录解析（CODEX_HOME）

### Description
Codex 的所有持久化（config、log、state.sqlite、credentials 等）都以 `CODEX_HOME` 为根；其解析规则必须严格一致。

### Trigger
启动时加载配置（任何子命令只要需要 `Config`）。

### Logic
```
IF CODEX_HOME is set AND non-empty:
  - path must exist
  - path must be a directory
  - canonicalize it, use as codex_home
ELSE:
  - codex_home = ~/.codex
```

### Edge Cases
| Case | Input | Expected | Rationale |
|---|---|---|---|
| CODEX_HOME 指向不存在路径 | `CODEX_HOME=/tmp/missing` | fatal error | 避免误写入奇怪位置 |
| CODEX_HOME 指向文件 | `CODEX_HOME=/tmp/file.txt` | fatal error | 目录语义必须一致 |

### Source
- `codex-rs/utils/home-dir/src/lib.rs`

---

## Rule: API key 登录必须从 stdin 读取

### Description
避免用户把 key 通过命令行参数暴露到 shell history 或进程列表。

### Trigger
用户执行 `codex login --with-api-key`

### Logic
```
IF stdin is a TTY:
  print guidance and exit(1)
ELSE:
  read entire stdin
  trim
  if empty: exit(1)
  else: store credentials and exit(0)
```

### Source
- `codex-rs/cli/src/login.rs`（`read_api_key_from_stdin`）

---

## Rule: OpenAI provider base_url 覆盖

### Description
允许用户通过 env 或 config 将 OpenAI endpoint 指向 proxy/mock，而无需完整 provider TOML 覆盖。

### Trigger
初始化内置 OpenAI provider（provider list 构建阶段）。

### Logic
```
base_url = env.OPENAI_BASE_URL if set and non-empty else None
```

### Source
- `codex-rs/core/src/model_provider_info.rs`（`create_openai_provider`）

---

## Rule: OSS provider base_url/port（实验性）

### Description
为本地/自托管模型（Ollama/LM Studio）提供默认 provider，并允许用 env 快速改端口或 base_url。

### Trigger
构建 built-in providers 列表。

### Logic
```
IF CODEX_OSS_BASE_URL set:
  use it
ELSE:
  port = parse_u16(CODEX_OSS_PORT) or default_provider_port
  base_url = http://localhost:{port}/v1
```

### Source
- `codex-rs/core/src/model_provider_info.rs`（`create_oss_provider`）

---

## Rule: Feature defaults + config 覆盖

### Description
features 必须以 registry 的 `default_enabled` 初始化，再应用 config.toml 的 `[features]` 覆盖。

### Trigger
加载 `Config` 时构建 `Features`。

### Logic
```
features = Features::with_defaults()
for each (key, bool) in config.features:
  if key is known:
     enable/disable accordingly
  else:
     ignore or warn (depending on schema enforcement)
```

### Source
- `codex-rs/core/src/features.rs`

---

## Rule: State DB 运行时迁移

### Description
state.sqlite 必须在运行时自动创建/迁移，以确保 `resume/fork` 与日志等功能稳定。

### Trigger
`StateRuntime::init`（通常在 core session 初始化时）

### Logic（简述）
```
ensure CODEX_HOME exists
open SQLite at CODEX_HOME/state.sqlite
run sqlx migrator (./migrations)
```

### Source
- `codex-rs/state/src/runtime.rs`
- `codex-rs/state/src/migrations.rs`

---

## Rule: npm wrapper 必须转发信号并继承 stdio

### Description
`@openai/codex` 的 Node wrapper 必须作为“透明启动器”：
- child `stdio: inherit`
- SIGINT/SIGTERM/SIGHUP 转发给 child
- exit code / signal 语义保持一致

### Trigger
用户执行 `codex`（npm 安装模式）

### Source
- `codex-cli/bin/codex.js`

## 来源（Source）
- `codex-rs/utils/home-dir/src/lib.rs#find_codex_home_from_env`
- `codex-rs/cli/src/login.rs#read_api_key_from_stdin`
- `codex-rs/core/src/model_provider_info.rs#create_openai_provider`
- `codex-rs/core/src/features.rs`
- `codex-rs/state/src/runtime.rs`
- `codex-cli/bin/codex.js`
