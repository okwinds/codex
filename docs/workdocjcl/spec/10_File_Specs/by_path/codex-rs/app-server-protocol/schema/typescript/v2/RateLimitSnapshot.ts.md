# `codex-rs/app-server-protocol/schema/typescript/v2/RateLimitSnapshot.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `479`
- sha256: `78ccd32aa4d55397d24071364b4dcd0e764a0fb782adcd7ab6acc93f0c1675e2`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/RateLimitSnapshot.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type RateLimitSnapshot = { primary: RateLimitWindow | null, secondary: RateLimitWindow | null, credits: CreditsSnapshot | null, planType: PlanType | null, };`

## Definitions (auto, per-file)
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/RateLimitSnapshot.ts:4` `import type { PlanType } from "../PlanType";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/RateLimitSnapshot.ts:5` `import type { CreditsSnapshot } from "./CreditsSnapshot";`
- `import` `codex-rs/app-server-protocol/schema/typescript/v2/RateLimitSnapshot.ts:6` `import type { RateLimitWindow } from "./RateLimitWindow";`
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/RateLimitSnapshot.ts:8` `export type RateLimitSnapshot = { primary: RateLimitWindow | null, secondary: RateLimitWindow | null, credits: CreditsSnapshot | null, planType: PlanType | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `import type { PlanType } from "../PlanType";`
- `import type { CreditsSnapshot } from "./CreditsSnapshot";`
- `import type { RateLimitWindow } from "./RateLimitWindow";`
- `export type RateLimitSnapshot = { primary: RateLimitWindow | null, secondary: RateLimitWindow | null, credits: CreditsSnapshot | null, planType: PlanType | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
