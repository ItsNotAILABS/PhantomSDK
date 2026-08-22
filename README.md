# PhantomSDK

**Developer SDK and verification layer for NEXUS ecosystem protocols.**

PhantomSDK gives applications and external developers a client-facing surface for capability discovery, schema validation, compatibility checks, receipt verification and release-evidence inspection without embedding the full POCKET/NEXUS control plane.

```text
Application / external client
          │
          ▼
      PhantomSDK
          │
          ├── protocol/schema clients
          ├── capability discovery
          ├── compatibility checks
          ├── receipt verification
          └── release evidence verification
          │
          ▼
NEXUS / POCKET / worker runtimes
```

## NEXUS federation

Declaration: [`ecosystem.surface.json`](ecosystem.surface.json).

Primary responsibilities:

```text
schema.validate
capability.client
receipt.verify
release.verify
compatibility.check
```

PhantomSDK packages protocol interaction; it does not become the identity, policy or execution authority.

## Developer workflow

A client integration should follow this shape:

```text
1. discover capability
2. validate supported protocol versions
3. construct typed request
4. submit through POCKET/NEXUS gateway
5. receive artifact/receipt
6. verify receipt and correlation
7. persist only application-owned state
```

## Core contracts

PhantomSDK clients are expected to understand the shared NEXUS objects most useful to application developers:

```text
nexus.capability.v1
nexus.task.v1
nexus.plan.v1
nexus.job.v1
nexus.health.v1
nexus.artifact.v1
nexus.execution-receipt.v1
nexus.compatibility.v1
nexus.handoff.v1
nexus.release-evidence.v1
```

## Verification behavior

Receipt verification should check:

```text
schema/version
request ID
component/action
status
artifact references
runtime timestamps
digest/hash
expected tenant/session correlation where present
```

Compatibility checks should fail closed on protocol versions the SDK cannot safely interpret.

## Release flow

```text
source SDK
 -> tests
 -> package/build
 -> checksums
 -> release manifest
 -> publish
 -> downstream install verification
```

Use repository-specific package/release commands for the language/runtime being published and keep the published version aligned with the protocol versions declared in `ecosystem.surface.json`.

## NEXUS validation

After changing shared protocol support, validate against the canonical registry:

```bash
# from ItsNotAILABS/nexus
python tools/validate_ecosystem_protocols.py
python tools/validate_ecosystem_registry.py
python tools/production_gate.py
```

## Ecosystem

- [NEXUS](https://github.com/ItsNotAILABS/nexus) — canonical protocol registry
- [POCKET](https://github.com/ItsNotAILABS/pocket) — product gateway and tenancy
- [POCKET Agent](https://github.com/ItsNotAILABS/pocket-agent) — execution client target
- [Pocket Voice](https://github.com/ItsNotAILABS/pocket-voice-to-text) — conversational API target
- [nova-connector-control-plane](https://github.com/ItsNotAILABS/nova-connector-control-plane) — external worker routing

PhantomSDK is the clean developer edge of the ecosystem: **typed clients in, verified receipts out.**
