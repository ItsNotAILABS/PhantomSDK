# Artifact Import Note

The v0.3.8 release zips exist in the Codex Phantasmatis local workspace and were verified before this PR pass.

## Local Artifacts

| Artifact | SHA-256 | Size |
| --- | --- | --- |
| `NOVA_CODEX_FULL_RELEASE_v0.3.8.zip` | `b80b1eca31901002a9aa1f03180887ffd3813fbb01f5728800243b64758e8cd8` | 772K |
| `NOVA_CODEX_DESKTOP_SOURCE_v0.3.8.zip` | `70458f66add767e6726231cdd701d7222375aa919ecba51564c5fcb096d5700b` | 152K |

## GitHub Upload Gate

The current connector path can write UTF-8 files and repository objects, but the chat-shaped payload channel truncated the binary/base64 zip payload before it could be safely committed as a Git blob. The release therefore includes:

- integrity manifest;
- release notes;
- checksum table;
- registry entries in Nexus;
- pending binary-upload gate for a Git-capable lane, GitHub Release upload, or local agent with repository credentials.

Do not treat the binary artifacts as present in this branch until the two zip files are committed or attached to a GitHub Release and their SHA-256 values match `RELEASE_MANIFEST.json`.
