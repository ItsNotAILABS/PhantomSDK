# PhantomSDK Package Surfaces

PhantomSDK packages NOVA contracts for external builders, local AIs, and connector runtimes.

## First Surfaces

| Surface | Purpose |
| --- | --- |
| TypeScript SDK | Browser, PWA, desktop, and tool UI clients. |
| Python SDK | Local AI, notebook, server, and CLI orchestration clients. |
| MCP Skill Pack | Export skills into MCP-compatible agent systems. |
| Connector Client | Caffeine, Grok Build, and generic agent-server handoffs. |
| Runtime Contracts | Engine manifests and proof gates from `nova-intelligence`. |

## SDK Law

The SDK should package verified contracts and handoff clients. It should not claim a hosted service is deployed unless the deployment proof exists.

## Next Gate

Add `packages/typescript/` and `packages/python/` starter contracts after `nova-intelligence` publishes its first engine schemas.
