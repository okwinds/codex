# Element Inventory
root: /Users/okwinds/BefunCodeRepo/codex
generated: 2026-02-03T07:02:17Z

## 1. API Layer

### Route Definitions
Files likely containing route/endpoint definitions:


### Controllers

### Middleware
(no middleware files found by pattern)

## 2. Data Layer

### Models/Entities
Model directories:
- codex-rs/codex-backend-openapi-models/src/models/

### Migrations
Migration directories:
- codex-rs/state/migrations/
  - codex-rs/state/migrations/0001_threads.sql
  - codex-rs/state/migrations/0003_logs_thread_id.sql
  - codex-rs/state/migrations/0002_logs.sql
  - codex-rs/state/migrations/0004_thread_dynamic_tools.sql

SQL files:
- codex-rs/state/migrations/0001_threads.sql
- codex-rs/state/migrations/0002_logs.sql
- codex-rs/state/migrations/0003_logs_thread_id.sql
- codex-rs/state/migrations/0004_thread_dynamic_tools.sql

### Schemas/DTOs

## 3. Business Logic

### Services

### Use Cases / Domain

### Utils/Helpers
Utility directories:
- codex-rs/utils/

## 4. UI Layer (if applicable)

### Components

### Pages/Views

### State Management

## 5. Integrations

### External API Clients

### Queue/Worker

## 6. Configuration

### Environment Variables

### Config Files
Config files:
- sdk/typescript/tsup.config.ts
- shell-tool-mcp/tsup.config.ts
- sdk/typescript/eslint.config.js

## 7. Testing

Test files found: 6
- sdk/typescript/tests/abort.test.ts
- sdk/typescript/tests/exec.test.ts
- sdk/typescript/tests/run.test.ts
- sdk/typescript/tests/runStreamed.test.ts
- shell-tool-mcp/tests/bashSelection.test.ts
- shell-tool-mcp/tests/osRelease.test.ts

## 8. Infrastructure

### Docker
Docker files:
- .devcontainer/Dockerfile
- .github/workflows/Dockerfile.bazel
- codex-cli/Dockerfile

### CI/CD
CI/CD directories:
- .github/
- codex-rs/.github/
CI/CD files:
- .github/ISSUE_TEMPLATE/2-bug-report.yml
- .github/ISSUE_TEMPLATE/3-docs-issue.yml
- .github/ISSUE_TEMPLATE/4-feature-request.yml
- .github/ISSUE_TEMPLATE/5-vs-code-extension.yml
- .github/actions/linux-code-sign/action.yml
- .github/actions/macos-code-sign/action.yml
- .github/actions/windows-code-sign/action.yml
- .github/workflows/bazel.yml
- .github/workflows/cargo-deny.yml
- .github/workflows/ci.yml
- .github/workflows/cla.yml
- .github/workflows/close-stale-contributor-prs.yml
- .github/workflows/codespell.yml
- .github/workflows/issue-deduplicator.yml
- .github/workflows/issue-labeler.yml
- .github/workflows/rust-ci.yml
- .github/workflows/rust-release-prepare.yml
- .github/workflows/rust-release.yml
- .github/workflows/sdk.yml
- .github/workflows/shell-tool-mcp-ci.yml
- .github/workflows/shell-tool-mcp.yml
- codex-rs/.github/workflows/cargo-audit.yml

## Summary

This inventory provides a starting point for specification extraction.
Review each category and identify which elements require detailed documentation.

Priority order recommendation:
1. Data models (foundation for understanding the domain)
2. API endpoints (external interface contract)
3. Business logic services (core behavior)
4. UI components (if applicable)
5. Integrations (external dependencies)
6. Infrastructure (deployment requirements)
