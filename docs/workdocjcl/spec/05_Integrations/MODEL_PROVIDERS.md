# 集成：模型提供方（Model Providers）

本章定义 Codex 如何与“模型服务”交互的可复刻契约：provider registry、鉴权注入、wire protocol（Responses vs Chat）、重试与超时。

## 1. Provider 定义来源（两层覆盖）
Provider 可以来自：
1) **内置默认**（编译进二进制）：保证开箱即用
2) **用户配置**：`~/.codex/config.toml` 的 `model_providers` 表，用于扩展/覆盖默认 provider

复刻要求：实现“内置 provider map + config 覆盖”的合并逻辑（config 覆盖同 key 时应替换内置项）。

## 2. 核心数据结构：`ModelProviderInfo`
关键字段（简述）：
- `name`: 展示名称
- `base_url`: OpenAI-compatible API base（例如 `https://api.openai.com/v1`）
- `env_key`: API key 所在环境变量名（可选）
- `experimental_bearer_token`: 直接写在 config 的 token（不推荐，但支持）
- `wire_api`: `responses` 或 `chat`
- `query_params`: 追加到请求的 query params
- `http_headers`: 固定 header
- `env_http_headers`: header 值来自某个 env var（若 env var 未设置则不注入）
- `request_max_retries` / `stream_max_retries` / `stream_idle_timeout_ms`: 重试/超时控制
- `requires_openai_auth`: 是否需要“OpenAI/ChatGPT 凭据系统”（true 时可能走 login UI/存储）
- `supports_websockets`: 是否支持 Responses API WebSocket transport

## 3. Wire protocol（不可自动探测，必须声明）

### 3.1 `wire_api = "responses"`
- 使用 OpenAI Responses API：`POST /v1/responses`
- 输出包含 streaming response items/tool calls（现代接口）

### 3.2 `wire_api = "chat"`（deprecated）
- 使用 Chat Completions：`POST /v1/chat/completions`
- 项目明确标注该协议“即将移除”，复刻时应保留兼容，但可以优先实现 responses。

## 4. 认证注入策略（Auth Injection）

### 4.1 `requires_openai_auth = true`（OpenAI/ChatGPT 凭据系统）
- token/key 来源于 Codex 的凭据存储（file/keyring）
- 适用于 OpenAI provider（内置 OpenAI provider 设为 `requires_openai_auth: true`）

### 4.2 `env_key`（第三方 provider 的 API key）
- 从环境变量 `env_key` 读取
- 若缺失，应该生成可诊断错误（告诉用户设置哪个 env var）

### 4.3 `env_http_headers`
例如内置 OpenAI provider 支持：
- `OpenAI-Organization` ← `OPENAI_ORGANIZATION`
- `OpenAI-Project` ← `OPENAI_PROJECT`

实现规则：
```
for (header_name, env_var_name) in env_http_headers:
  if env_var is set and non-empty:
    add header header_name: env_value
```

## 5. 默认 provider（内置列表）
内置 provider 列表（概念）：
- `openai`：OpenAI（支持 `OPENAI_BASE_URL` 覆盖）
- `ollama` / `ollama-chat` / `lmstudio`：本地 OSS providers（支持 `CODEX_OSS_*` 覆盖；实验性）

## 6. 重试与超时（Retry/Timeout）
Provider 允许用户配置重试次数，但有 hard cap：
- request retries cap：100
- stream retries cap：100
- stream idle timeout 默认：300_000ms（5 分钟）

复刻建议：
- request 与 stream 分开计数
- stream idle timeout 触发时可尝试重连（最多 stream_max_retries）

## 7. 来源（Source）
- provider registry 与类型：`codex-rs/core/src/model_provider_info.rs`
- 配置入口（ConfigToml.model_providers）：`codex-rs/core/src/config/mod.rs`
