#!/usr/bin/env python3
"""Validate PhantomSDK manifests and release checksum metadata."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SDK_MANIFEST = ROOT / "phantom-sdk.manifest.json"
RELEASE_MANIFEST = ROOT / "releases" / "v0.3.8" / "RELEASE_MANIFEST.json"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def validate_sdk_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("schema", "name", "authority", "repo_role", "package_surfaces", "upstream_sources", "proof_gates"):
        if field not in manifest:
            errors.append(f"SDK manifest missing field: {field}")
    for field in ("package_surfaces", "upstream_sources", "proof_gates"):
        value = manifest.get(field)
        if not isinstance(value, list) or not value:
            errors.append(f"SDK manifest {field} must be a non-empty list")
    exports = manifest.get("exports", {})
    if exports:
        for label, export_path in exports.items():
            if not isinstance(export_path, str) or not export_path.strip():
                errors.append(f"exports.{label} must be a non-empty path")
    return errors


def validate_release_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        return ["Release manifest artifacts must be non-empty"]
    for index, artifact in enumerate(artifacts):
        label = f"artifacts[{index}]"
        if not isinstance(artifact, dict):
            errors.append(f"{label} must be an object")
            continue
        for field in ("name", "path", "sha256", "role"):
            if not isinstance(artifact.get(field), str) or not artifact[field].strip():
                errors.append(f"{label}.{field} must be a non-empty string")
        sha = artifact.get("sha256", "")
        if isinstance(sha, str) and len(sha) != 64:
            errors.append(f"{label}.sha256 must be a 64-character SHA-256 hex string")
    return errors


def main() -> int:
    sdk_manifest = load_json(SDK_MANIFEST)
    release_manifest = load_json(RELEASE_MANIFEST)
    errors = validate_sdk_manifest(sdk_manifest) + validate_release_manifest(release_manifest)
    if errors:
        print("PhantomSDK validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PhantomSDK validation passed: SDK manifest and v0.3.8 release manifest are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
