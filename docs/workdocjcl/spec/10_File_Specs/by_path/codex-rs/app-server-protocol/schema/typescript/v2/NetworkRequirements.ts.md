# `codex-rs/app-server-protocol/schema/typescript/v2/NetworkRequirements.ts`

## Identity
- kind: `source`
- ext: `.ts`
- size_bytes: `554`
- sha256: `6710c1bfbff9d58d9b852e889d5e01c01311a1da390fa458f99d8d6b4af3db18`
- generated_utc: `2026-02-08T10:45:14Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/schema/typescript/v2/NetworkRequirements.ts` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `export type NetworkRequirements = { enabled: boolean | null, httpPort: number | null, socksPort: number | null, allowUpstreamProxy: boolean | null, dangerouslyAllowNonLoopbackProxy: boolean | null, dangerouslyAllowNonLoopbackAdmin: boolean | null, allowedDomains: Array<string> | null, deniedDomains: Array<string> | null, allowUnixSockets: Array<string> | null, allowLocalBinding: boolean | null, };`

## Definitions (auto, per-file)
- `export` `codex-rs/app-server-protocol/schema/typescript/v2/NetworkRequirements.ts:5` `export type NetworkRequirements = { enabled: boolean | null, httpPort: number | null, socksPort: number | null, allowUpstreamProxy: boolean | null, dangerouslyAllowNonLoopbackProxy: boolean | null, dangerouslyAllowNonLoopbackAdmin: boolean | null, allowedDomains: Array<string> | null, deniedDomains: Array<string> | null, allowUnixSockets: Array<string> | null, allowLocalBinding: boolean | null, };`

## Dependencies (auto sample)
### Imports / Includes
- `export type NetworkRequirements = { enabled: boolean | null, httpPort: number | null, socksPort: number | null, allowUpstreamProxy: boolean | null, dangerouslyAllowNonLoopbackProxy: boolean | null, dangerouslyAllowNonLoopbackAdmin: boolean | null, allowedDomains: Array<string> | null, deniedDomains: Array<string> | null, allowUnixSockets: Array<string> | null, allowLocalBinding: boolean | null, };`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
