# PhantomSDK

![Status](https://img.shields.io/badge/status-contract%20first-blue)
![SDK](https://img.shields.io/badge/sdk-typescript%20%2B%20python-6f42c1)
![Release](https://img.shields.io/badge/release-v0.3.8-2f9e44)
![Validator](https://img.shields.io/badge/validator-stdlib%20python-success)
![Artifacts](https://img.shields.io/badge/binary%20artifacts-pending-orange)

SDK packaging surface for NOVA external builders, local AIs, connector runtimes, and product surfaces.

PhantomSDK turns NOVA intelligence contracts into installable package surfaces. It is currently **contract-first**: manifests, starter SDK exports, release metadata, and verification gates exist before package publication claims.

## Search Keywords

NOVA SDK, AI agent SDK, MCP SDK, TypeScript AI SDK, Python AI SDK, local AI runtime package, connector client SDK, release manifest, artifact checksum verification, NOVA Build SDK.

## Role

PhantomSDK consumes:

- `nova-intelligence` engine contracts
- `nexus` MDFUC registry records
- `x-mcp-skills` connector skills
- `organism-bots-mcp-server` bot and MCP contracts

It packages:

- TypeScript SDK
- Python SDK
- MCP skill pack
- Connector client
- Runtime contracts
- Release manifests
- Artifact verification helpers

## Quick Start

Validate the SDK and release manifests:

```bash
python tools/validate_phantom_sdk.py
```

Inspect TypeScript starter exports:

```bash
cat packages/typescript/src/index.ts
```

Inspect Python starter exports:

```bash
cat packages/python/phantom_sdk/__init__.py
```

## Current Files

- `phantom-sdk.manifest.json` — SDK role, package surfaces, exports, upstream sources, and proof gates.
- `docs/PACKAGE_SURFACES.md` — first SDK surface map.
- `docs/RELEASE_VERIFICATION.md` — v0.3.8 checksum and upload verification guide.
- `packages/typescript/src/index.ts` — contract-first TypeScript manifest validators.
- `packages/python/phantom_sdk/__init__.py` — contract-first Python manifest validators.
- `tools/validate_phantom_sdk.py` — dependency-free SDK/release manifest validator.
- `releases/v0.3.8/RELEASE_MANIFEST.json` — release artifact checksum map.

## Release Truth Line

The v0.3.8 zip artifacts are registered with checksums, but binary upload is still pending. Do not claim the zip files are committed until they exist in the repository or as GitHub Release assets and their SHA-256 values match `releases/v0.3.8/RELEASE_MANIFEST.json`.

## GitHub Discoverability

Recommended repository topics:

`nova`, `sdk`, `typescript-sdk`, `python-sdk`, `ai-agents`, `mcp`, `model-context-protocol`, `developer-tools`, `local-ai`, `runtime-contracts`, `artifact-verification`.

## Next Gate

Add package build scripts, SDK validation tests, binary-safe release upload, and install docs for external builders.
