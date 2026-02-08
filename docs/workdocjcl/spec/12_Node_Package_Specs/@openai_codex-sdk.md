# `@openai/codex-sdk`

- path: `sdk/typescript`
- version: `0.0.0-dev`
- generated_utc: `2026-02-03T09:49:16Z`
- description: TypeScript SDK for Codex APIs.

## Entry Points
- bin: (none)
- exports: `{'.': {'import': './dist/index.js', 'types': './dist/index.d.ts'}}`
- module: `./dist/index.js`
- types: `./dist/index.d.ts`

## Scripts
- `build`: `tsup`
- `build:watch`: `tsup --watch`
- `clean`: `rm -rf dist`
- `coverage`: `jest --coverage`
- `format`: `prettier --check .`
- `format:fix`: `prettier --write .`
- `lint`: `pnpm eslint "src/**/*.ts" "tests/**/*.ts"`
- `lint:fix`: `pnpm eslint --fix "src/**/*.ts" "tests/**/*.ts"`
- `prepare`: `pnpm run build`
- `test`: `jest`
- `test:watch`: `jest --watch`

## Dependencies (direct)
- (none)

## Dev Dependencies (direct)
- `@modelcontextprotocol/sdk`: `^1.24.0`
- `@types/jest`: `^29.5.14`
- `@types/node`: `^20.19.18`
- `eslint`: `^9.36.0`
- `eslint-config-prettier`: `^9.1.2`
- `eslint-plugin-jest`: `^29.0.1`
- `eslint-plugin-node-import`: `^1.0.5`
- `jest`: `^29.7.0`
- `prettier`: `^3.6.2`
- `ts-jest`: `^29.3.4`
- `ts-jest-mock-import-meta`: `^1.3.1`
- `ts-node`: `^10.9.2`
- `tsup`: `^8.5.0`
- `typescript`: `^5.9.2`
- `typescript-eslint`: `^8.45.0`
- `zod`: `^3.24.2`
- `zod-to-json-schema`: `^3.24.6`

## Spec Links
- `workdocjcl/spec/00_Overview/PROJECT.md`
