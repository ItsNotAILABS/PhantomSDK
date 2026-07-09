# NOVA Codex Release v0.3.8

This folder holds the first SDK-side release packet imported from the local Codex Phantasmatis runtime.

## Artifacts

- `NOVA_CODEX_FULL_RELEASE_v0.3.8.zip`: full local runtime release packet.
- `NOVA_CODEX_DESKTOP_SOURCE_v0.3.8.zip`: desktop-source release packet.
- `RELEASE_MANIFEST.json`: integrity and verification manifest.

## Verification

Before upload, the local runtime reported:

- 59/59 tests passed
- compile check passed
- JSON validation passed
- CLI/live endpoint checks passed

Verify artifacts before unpacking:

```bash
sha256sum releases/v0.3.8/NOVA_CODEX_FULL_RELEASE_v0.3.8.zip
sha256sum releases/v0.3.8/NOVA_CODEX_DESKTOP_SOURCE_v0.3.8.zip
```

Expected hashes are stored in `RELEASE_MANIFEST.json`.
