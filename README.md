# CiteGuild Skills

Install CiteGuild workflows and tools in Claude Code, ChatGPT, and Codex.

CiteGuild is an opted-in editorial source network for ethical citation and backlink discovery. It is not a general web-search engine: the plugin searches active articles submitted by CiteGuild members so an agent can find relevant sources for a draft, brief, or research task. A result is a citation candidate, not an endorsement, guaranteed placement, or reciprocal-link obligation.

## What is included

- `find-editorial-citations`: finds relevant member articles through the CiteGuild CLI, hosted MCP tool, or versioned REST API, then applies editorial-quality guardrails before suggesting a citation.
- CiteGuild MCP connection: exposes `search_member_articles` and account information through CiteGuild's hosted MCP server, using `CITEGUILD_API_KEY` in Codex and OAuth in Claude Code/ChatGPT.
- Direct agent access: documents `citeguild search --json` for shell agents and `POST /api/v1/search` as the API fallback. All transports share the same v1 search contract.
- Native packaging for Claude Code and the ChatGPT/Codex plugin system.

An active CiteGuild subscription is required to search the member index.

## Install for Claude Code

Add this repository as a marketplace, then install the plugin:

```text
/plugin marketplace add LVTD-LLC/citeguild-skills
/plugin install citeguild@citeguild-skills
```

The equivalent non-interactive commands are:

```bash
claude plugin marketplace add LVTD-LLC/citeguild-skills
claude plugin install citeguild@citeguild-skills
```

## Install for ChatGPT and Codex

Add the repository marketplace and install the plugin:

```bash
codex plugin marketplace add LVTD-LLC/citeguild-skills
codex plugin add citeguild@citeguild-skills
```

The same plugin is usable from supported ChatGPT and Codex plugin surfaces. The Codex bundle reads a CiteGuild API key from `CITEGUILD_API_KEY`; the CiteGuild dashboard's protected Copy Prompt flow places the key in `~/.codex/.env`. Restart or open a new conversation after installation so the environment, skill, and MCP connection are loaded.

## Connect and use

In Codex, use the dashboard's Copy Prompt action to install the plugin and save the generated key as `CITEGUILD_API_KEY` without printing or committing it. In Claude Code and ChatGPT, complete the OAuth sign-in flow on the first CiteGuild tool call.

OpenClaw, Hermes, shell agents, and scripts should prefer the released `citeguild` CLI when installed. Other clients can use the bundled MCP connection or call `POST https://citeguild.lvtd.dev/api/v1/search` with the API key as a Bearer or `X-API-Key` header. See the skill for the full request contract and secret-handling rules.

Try prompts such as:

- `Find CiteGuild member articles that could support the claims in this draft.`
- `Find relevant editorial sources about Django deployment reliability. Exclude example.com.`
- `Review these citation candidates and keep only sources that materially support the paragraph.`

## Repository layout

```text
.agents/plugins/marketplace.json       ChatGPT/Codex marketplace
.claude-plugin/marketplace.json        Claude Code marketplace
plugins/citeguild/
  .codex-plugin/plugin.json            ChatGPT/Codex plugin manifest
  .claude-plugin/plugin.json           Claude Code plugin manifest
  .codex-mcp.json                      Codex API-key MCP connection
  .mcp.json                            Claude Code OAuth MCP connection
  skills/find-editorial-citations/     Shared agent skill
```

## Development

Validate the manifests and skill before opening a pull request:

```bash
make validate
```

## Links

- CiteGuild: https://citeguild.lvtd.dev
- Issues: https://github.com/LVTD-LLC/citeguild-skills/issues
