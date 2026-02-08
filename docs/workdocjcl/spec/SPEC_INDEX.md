# Specification Index

## Overview
- [00_Overview/PROJECT.md](00_Overview/PROJECT.md) - Project identity and tech stack
- [00_Overview/ARCHITECTURE.md](00_Overview/ARCHITECTURE.md) - System architecture
- [00_Overview/GLOSSARY.md](00_Overview/GLOSSARY.md) - Domain terminology
- [00_Overview/REPO_LAYOUT.md](00_Overview/REPO_LAYOUT.md) - Repo directory responsibilities
- [00_Overview/MODULE_MAP.md](00_Overview/MODULE_MAP.md) - Module-to-responsibility map
- [00_Overview/SPEC_CONVENTIONS.md](00_Overview/SPEC_CONVENTIONS.md) - Spec writing + mapping conventions

## Configuration
- [01_Configuration/ENVIRONMENT.md](01_Configuration/ENVIRONMENT.md) - Environment variables
- [01_Configuration/FEATURE_FLAGS.md](01_Configuration/FEATURE_FLAGS.md) - Feature toggles
- [01_Configuration/CONFIG_TOML.md](01_Configuration/CONFIG_TOML.md) - config.toml location + schema anchor
- [01_Configuration/CONFIG_SCHEMA_REFERENCE.md](01_Configuration/CONFIG_SCHEMA_REFERENCE.md) - Flattened config key reference

## Data Model
- [02_Data/ENTITIES.md](02_Data/ENTITIES.md) - Data entities
- [02_Data/RELATIONSHIPS.md](02_Data/RELATIONSHIPS.md) - Entity relationships
- [02_Data/MIGRATIONS.md](02_Data/MIGRATIONS.md) - Schema history
- [02_Data/ROLLOUT_FORMAT.md](02_Data/ROLLOUT_FORMAT.md) - Rollout JSONL format (session replay)
- [02_Data/ROLLOUT_SEMANTICS.md](02_Data/ROLLOUT_SEMANTICS.md) - Rollout resume/fork semantics + state extraction rules

## API
- [03_API/ENDPOINTS.md](03_API/ENDPOINTS.md) - API endpoints
- [03_API/AUTHENTICATION.md](03_API/AUTHENTICATION.md) - Auth mechanisms
- [03_API/ERRORS.md](03_API/ERRORS.md) - Error handling
- [03_API/CLI.md](03_API/CLI.md) - CLI contract (commands/options)
- [03_API/APP_SERVER.md](03_API/APP_SERVER.md) - JSONL/stdio app-server protocol (initialize, thread/turn/items, approvals)

## Business Logic
- [04_Business_Logic/RULES.md](04_Business_Logic/RULES.md) - Business rules
- [04_Business_Logic/STATE_MACHINES.md](04_Business_Logic/STATE_MACHINES.md) - State transitions
- [04_Business_Logic/WORKFLOWS.md](04_Business_Logic/WORKFLOWS.md) - Multi-step processes
- [04_Business_Logic/PROMPT_ASSEMBLY.md](04_Business_Logic/PROMPT_ASSEMBLY.md) - Base instructions + initial context injection (developer/user/skills/personality)
- [04_Business_Logic/SYSTEM_PRESET_PROMPTS.md](04_Business_Logic/SYSTEM_PRESET_PROMPTS.md) - Model slug → preset prompt selection matrix (verbatim assets)
- [04_Business_Logic/PROMPTS/INDEX.md](04_Business_Logic/PROMPTS/INDEX.md) - Prompt artifacts index + checksums (replication-critical)

## Integrations
- [05_Integrations/MODEL_PROVIDERS.md](05_Integrations/MODEL_PROVIDERS.md) - Model provider registry + auth injection
- [05_Integrations/MODEL_API_COMPATIBILITY.md](05_Integrations/MODEL_API_COMPATIBILITY.md) - Provider/WireApi compatibility matrix (headers/events, Azure store rules, Chat vs Responses)
- [05_Integrations/CHAT_WIRE_MAPPING.md](05_Integrations/CHAT_WIRE_MAPPING.md) - wire_api=chat request mapping (ResponseItem→messages) + Chat SSE parsing (deltas/DONE/tool_calls)
- [05_Integrations/MCP.md](05_Integrations/MCP.md) - MCP client/server integration
- [05_Integrations/TOOLS.md](05_Integrations/TOOLS.md) - Built-in tool catalog (names/enablement)
- [05_Integrations/SKILLS.md](05_Integrations/SKILLS.md) - Skills discovery, enable/disable, mentions, injection, and dependencies
- [05_Integrations/SKILLS_SYSTEM_ARTIFACTS.md](05_Integrations/SKILLS_SYSTEM_ARTIFACTS.md) - Embedded system skills artifacts + checksums
- [05_Integrations/RESPONSES_STREAMING.md](05_Integrations/RESPONSES_STREAMING.md) - Responses API streaming events, retries, and WebSocket→HTTPS fallback
- [05_Integrations/TOOLS_SCHEMA_REFERENCE.md](05_Integrations/TOOLS_SCHEMA_REFERENCE.md) - Tools JSON schema summary (best-effort from Rust)
- [05_Integrations/TOOLS_DETAILED/INDEX.md](05_Integrations/TOOLS_DETAILED/INDEX.md) - Per-tool behavioral specs (replication-critical)

## UI
- [06_UI/TUI.md](06_UI/TUI.md) - Terminal UI architecture and semantics
- [06_UI/TUI_APPROVALS.md](06_UI/TUI_APPROVALS.md) - Approval modals, shortcuts, and full-screen pager overlays
- [06_UI/TUI_KEYBINDINGS.md](06_UI/TUI_KEYBINDINGS.md) - Global key routing, overlay navigation, backtrack bindings (phase 1)
- [06_UI/TUI_RESUME_PICKER.md](06_UI/TUI_RESUME_PICKER.md) - Alt-screen session resume/fork picker (pagination, search, cwd filter)
- [06_UI/TUI_SLASH_COMMANDS.md](06_UI/TUI_SLASH_COMMANDS.md) - Slash command parsing, gating, and dispatch semantics
- [06_UI/TUI_COMPOSER.md](06_UI/TUI_COMPOSER.md) - Bottom-pane composer state machine (input, popups, paste bursts, attachments)
- [06_UI/TUI_PROMPTS.md](06_UI/TUI_PROMPTS.md) - Custom prompts (/prompts:...) args parsing and expansion with text-elements preservation
- [06_UI/TUI_PASTE_BURST.md](06_UI/TUI_PASTE_BURST.md) - PasteBurst state machine for terminals without bracketed paste (Windows-friendly)

## Infrastructure
- [07_Infrastructure/BUILD_SYSTEMS.md](07_Infrastructure/BUILD_SYSTEMS.md) - Cargo/pnpm/Bazel/Nix build details
- [07_Infrastructure/PACKAGING.md](07_Infrastructure/PACKAGING.md) - npm wrapper + vendor binaries
- [07_Infrastructure/SECURITY_SANDBOX.md](07_Infrastructure/SECURITY_SANDBOX.md) - Approvals, sandboxing, execpolicy
- [07_Infrastructure/EXEC_POLICY.md](07_Infrastructure/EXEC_POLICY.md) - Execpolicy language, loading/merge, evaluation, amendments
- [07_Infrastructure/COMMAND_SAFETY.md](07_Infrastructure/COMMAND_SAFETY.md) - Known-safe / dangerous command heuristics used by execpolicy fallback
- [07_Infrastructure/APPROVALS.md](07_Infrastructure/APPROVALS.md) - Approval events, caching semantics, sandbox-deny retry, execpolicy amendment application

## Testing
- [08_Testing/UNIT_SPECS.md](08_Testing/UNIT_SPECS.md) - Unit test specs
- [08_Testing/INTEGRATION_SPECS.md](08_Testing/INTEGRATION_SPECS.md) - Integration test specs
- [08_Testing/E2E_SPECS.md](08_Testing/E2E_SPECS.md) - E2E test specs

## Verification
- [09_Verification/COVERAGE_REPORT.md](09_Verification/COVERAGE_REPORT.md) - Spec coverage
- [09_Verification/CORE_INFRASTRUCTURE_REVIEW.md](09_Verification/CORE_INFRASTRUCTURE_REVIEW.md) - Deep audit of core infra (model API, prompts, tools, skills)
- [09_Verification/REPLICATION_GUIDE.md](09_Verification/REPLICATION_GUIDE.md) - How to replicate
- [09_Verification/KNOWN_GAPS.md](09_Verification/KNOWN_GAPS.md) - Documentation gaps
- [09_Verification/CODE_TO_SPEC_MAP.md](09_Verification/CODE_TO_SPEC_MAP.md) - Bidirectional mapping anchor
- [09_Verification/FILE_COVERAGE.md](09_Verification/FILE_COVERAGE.md) - File-by-file no-omission coverage proof
- [09_Verification/BIDIRECTIONAL_INDEX.md](09_Verification/BIDIRECTIONAL_INDEX.md) - File→capsule→crate/package mapping
- [09_Verification/NO_OMISSION_STATUS.md](09_Verification/NO_OMISSION_STATUS.md) - No-omission status proof

## File Specs
- [10_File_Specs/FORMAT.md](10_File_Specs/FORMAT.md) - Capsule format definition
- [10_File_Specs/INDEX.md](10_File_Specs/INDEX.md) - Capsule index (one entry per repo file)

## Rust Crates
- [11_Rust_Crate_Specs/INDEX.md](11_Rust_Crate_Specs/INDEX.md) - One spec per Cargo workspace crate

## Node Packages
- [12_Node_Package_Specs/INDEX.md](12_Node_Package_Specs/INDEX.md) - One spec per pnpm workspace package

## Indexes
- [13_Indexes/RUST_SYMBOL_INDEX.md](13_Indexes/RUST_SYMBOL_INDEX.md) - All detected Rust public items + mains
- [13_Indexes/TYPESCRIPT_SYMBOL_INDEX.md](13_Indexes/TYPESCRIPT_SYMBOL_INDEX.md) - All detected TypeScript exports
- [13_Indexes/PYTHON_SYMBOL_INDEX.md](13_Indexes/PYTHON_SYMBOL_INDEX.md) - All detected Python top-level defs/classes
