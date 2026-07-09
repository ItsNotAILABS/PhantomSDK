# Release Verification

PhantomSDK owns the SDK package surface and release manifest for NOVA local/runtime artifacts.

## v0.3.8 Artifacts

Expected artifacts:

| Artifact | SHA-256 | Status |
| --- | --- | --- |
| `NOVA_CODEX_FULL_RELEASE_v0.3.8.zip` | `b80b1eca31901002a9aa1f03180887ffd3813fbb01f5728800243b64758e8cd8` | Pending binary upload |
| `NOVA_CODEX_DESKTOP_SOURCE_v0.3.8.zip` | `70458f66add767e6726231cdd701d7222375aa919ecba51564c5fcb096d5700b` | Pending binary upload |

## Validate Manifests

```bash
python tools/validate_phantom_sdk.py
```

## Verify Downloaded Artifacts

After binary upload through a Git-capable lane or GitHub Release asset path:

```bash
sha256sum releases/v0.3.8/NOVA_CODEX_FULL_RELEASE_v0.3.8.zip
sha256sum releases/v0.3.8/NOVA_CODEX_DESKTOP_SOURCE_v0.3.8.zip
```

The printed hashes must match `releases/v0.3.8/RELEASE_MANIFEST.json`.

## Truth Line

Do not claim the binary artifacts are committed until they exist in the repository or as GitHub Release assets and their SHA-256 values match the manifest.

## Next Gates

1. Upload the two v0.3.8 zips through a binary-safe lane.
2. Recompute SHA-256 values after upload.
3. Update upload status in Nexus and PhantomSDK release docs.
4. Add CI validation for manifests.
