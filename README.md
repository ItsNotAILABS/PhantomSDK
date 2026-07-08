# PhantomSDK

SDK packaging surface for NOVA external builders, local AIs, and connector runtimes.

## Role

PhantomSDK turns NOVA intelligence contracts into installable package surfaces.

It consumes:

- `nova-intelligence` engine contracts
- `nexus` MDFUC registry records
- `x-mcp-skills` connector skills

It packages:

- TypeScript SDK
- Python SDK
- MCP skill pack
- connector client
- runtime contracts

## Current Files

- `phantom-sdk.manifest.json` — SDK role, surfaces, upstream sources, and proof gates.
- `docs/PACKAGE_SURFACES.md` — first SDK surface map.

## Next Gate

Add `packages/typescript/` and `packages/python/` starter contracts after the first schemas land in `nova-intelligence`.
