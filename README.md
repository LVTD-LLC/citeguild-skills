# CiteGuild Skills

Install CiteGuild workflows and tools in Claude Code, ChatGPT, and Codex.

CiteGuild is an opted-in editorial source network for ethical citation and backlink discovery. It is not a general web-search engine: the plugin searches active articles submitted by CiteGuild members so an agent can find relevant sources for a draft, brief, or research task. A result is a citation candidate, not an endorsement, guaranteed placement, or reciprocal-link obligation.

## What is included

- `find-editorial-citations`: finds relevant member articles and applies editorial-quality guardrails before suggesting a citation.
- CiteGuild MCP connection: exposes `search_member_articles` and account information through CiteGuild's hosted, OAuth-enabled MCP server.
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

The same plugin is usable from supported ChatGPT and Codex plugin surfaces. Restart or open a new conversation after installation so the skill and MCP connection are loaded.

## Connect and use

On the first CiteGuild tool call, complete the OAuth sign-in flow. Do not paste or commit a CiteGuild API key.

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
  .mcp.json                            Hosted CiteGuild MCP connection
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
