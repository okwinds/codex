# `codex-rs/app-server-protocol/schema/typescript/RateLimitSnapshot.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `479`
- sha256: `36a18abd5a8d3a0cb5cfe8dbaa64a4dc28c410db64351eda64cbfa024896694f`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/RateLimitSnapshot.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type RateLimitSnapshot = { primary: RateLimitWindow | null, secondary: RateLimitWindow | null, credits: CreditsSnapshot | null, plan_type: PlanType | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/RateLimitSnapshot.ts:4` `import type { CreditsSnapshot } from "./CreditsSnapshot";`
- `import` `codex-rs/app-server-protocol/schema/typescript/RateLimitSnapshot.ts:5` `import type { PlanType } from "./PlanType";`
- `import` `codex-rs/app-server-protocol/schema/typescript/RateLimitSnapshot.ts:6` `import type { RateLimitWindow } from "./RateLimitWindow";`
- `export` `codex-rs/app-server-protocol/schema/typescript/RateLimitSnapshot.ts:8` `export type RateLimitSnapshot = { primary: RateLimitWindow | null, secondary: RateLimitWindow | null, credits: CreditsSnapshot | null, plan_type: PlanType | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { CreditsSnapshot } from "./CreditsSnapshot";`
- `import type { PlanType } from "./PlanType";`
- `import type { RateLimitWindow } from "./RateLimitWindow";`
- `export type RateLimitSnapshot = { primary: RateLimitWindow | null, secondary: RateLimitWindow | null, credits: CreditsSnapshot | null, plan_type: PlanType | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
