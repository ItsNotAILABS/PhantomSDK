export type PhantomReleaseArtifact = {
  name: string;
  path: string;
  sha256: string;
  size_hint?: string;
  role: string;
};

export type PhantomReleaseManifest = {
  schema: string;
  release: string;
  generated_at: string;
  authority: string;
  artifacts: PhantomReleaseArtifact[];
  verification?: Record<string, string>;
  repo_targets?: Record<string, string>;
};

export type PhantomSdkManifest = {
  schema: string;
  name: string;
  authority: string;
  repo_role: string;
  package_surfaces: string[];
  upstream_sources: string[];
  exports?: Record<string, string>;
  proof_gates: string[];
  next_gates?: string[];
};

export function validateReleaseManifest(manifest: PhantomReleaseManifest): string[] {
  const errors: string[] = [];
  if (!manifest.schema) errors.push("schema is required");
  if (!manifest.release) errors.push("release is required");
  if (!Array.isArray(manifest.artifacts) || manifest.artifacts.length === 0) {
    errors.push("artifacts must be a non-empty array");
    return errors;
  }
  for (const [index, artifact] of manifest.artifacts.entries()) {
    if (!artifact.name) errors.push(`artifacts[${index}].name is required`);
    if (!artifact.path) errors.push(`artifacts[${index}].path is required`);
    if (!/^[a-f0-9]{64}$/i.test(artifact.sha256 || "")) {
      errors.push(`artifacts[${index}].sha256 must be a 64-character SHA-256 hex string`);
    }
  }
  return errors;
}

export function validateSdkManifest(manifest: PhantomSdkManifest): string[] {
  const errors: string[] = [];
  if (!manifest.schema) errors.push("schema is required");
  if (!manifest.name) errors.push("name is required");
  if (!Array.isArray(manifest.package_surfaces) || manifest.package_surfaces.length === 0) {
    errors.push("package_surfaces must be a non-empty array");
  }
  if (!Array.isArray(manifest.proof_gates) || manifest.proof_gates.length === 0) {
    errors.push("proof_gates must be a non-empty array");
  }
  return errors;
}

export const PHANTOM_SDK_STATUS = "contract-first";
