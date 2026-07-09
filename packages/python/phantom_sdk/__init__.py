"""PhantomSDK contract-first Python surface.

This starter package exposes manifest validation helpers without claiming a
published runtime service. It is safe to import in local tooling and CI.
"""
from __future__ import annotations

from typing import Any

PHANTOM_SDK_STATUS = "contract-first"


def validate_release_manifest(manifest: dict[str, Any]) -> list[str]:
    """Validate the shape of a PhantomSDK release manifest."""
    errors: list[str] = []
    for field in ("schema", "release", "generated_at", "authority", "artifacts"):
        if field not in manifest:
            errors.append(f"missing field: {field}")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("artifacts must be a non-empty list")
        return errors
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            errors.append(f"artifacts[{index}] must be an object")
            continue
        for field in ("name", "path", "sha256", "role"):
            if not isinstance(artifact.get(field), str) or not artifact[field].strip():
                errors.append(f"artifacts[{index}].{field} must be a non-empty string")
        sha = artifact.get("sha256", "")
        if isinstance(sha, str) and len(sha) != 64:
            errors.append(f"artifacts[{index}].sha256 must be 64 characters")
    return errors


def validate_sdk_manifest(manifest: dict[str, Any]) -> list[str]:
    """Validate the shape of the PhantomSDK repo manifest."""
    errors: list[str] = []
    for field in ("schema", "name", "authority", "repo_role", "package_surfaces", "upstream_sources", "proof_gates"):
        if field not in manifest:
            errors.append(f"missing field: {field}")
    for list_field in ("package_surfaces", "upstream_sources", "proof_gates"):
        value = manifest.get(list_field)
        if not isinstance(value, list) or not value:
            errors.append(f"{list_field} must be a non-empty list")
    return errors


__all__ = [
    "PHANTOM_SDK_STATUS",
    "validate_release_manifest",
    "validate_sdk_manifest",
]
