# Changelog

## 0.2.0 - 2026-08-17

- Document the released CiteGuild CLI as the preferred search transport for OpenClaw, Hermes, shell agents, and scripts.
- Add the versioned `POST /api/v1/search` fallback, shared v1 request/response contract, and transport-specific error handling to the editorial-citations skill.
- Bump the plugin package version so existing marketplace installations can discover the expanded skill guidance.

## 0.1.1 - 2026-08-06

- Make the Codex plugin's hosted MCP connection read `CITEGUILD_API_KEY` as a bearer token while preserving OAuth for Claude Code and ChatGPT.
- Document the protected dashboard Copy Prompt flow and the required Codex restart after saving the key.

## 0.1.0 - 2026-08-06

- Add the first CiteGuild skill for finding relevant editorial citation candidates.
- Add shared hosted MCP configuration with OAuth discovery.
- Add installable Claude Code and ChatGPT/Codex plugin manifests and marketplaces.
- Use the CiteGuild site mark for the ChatGPT/Codex plugin logo and composer icon.
- Add exact-head ReviewGate checks for pull requests.
