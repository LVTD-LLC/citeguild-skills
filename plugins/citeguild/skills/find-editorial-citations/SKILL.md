---
name: find-editorial-citations
description: Use when finding CiteGuild member articles for drafts, research, citations, or ethical backlink discovery via CLI, MCP, or REST API.
---

# Find Editorial Citations

Find sources that genuinely improve the user's work. Treat CiteGuild as a focused member corpus, not a replacement for a broad search engine.

## Workflow

1. Extract a focused search query from the topic, passage, claim, or draft. Preserve the user's meaning and avoid sending confidential or unnecessary text.
2. Ask for the user's own domain only when it cannot be inferred and excluding it materially matters. Pass known owned domains as exact values in `excluded_domains` or repeated `--exclude-domain` flags.
3. Choose one available transport:
   - For OpenClaw, Hermes, shell agents, or scripts, prefer the `citeguild` CLI when it is installed.
   - In a client exposing CiteGuild MCP tools, call `search_member_articles`.
   - Otherwise, call the versioned REST endpoint `POST https://citeguild.lvtd.dev/api/v1/search`.
4. Start with 10 results. Increase the limit or try one narrower query only when the first pass is insufficient.
5. Rank candidates by direct topical and claim-level relevance. Prefer a smaller set of strong matches over filling a quota.
6. Present each useful candidate with its title, canonical URL, domain, and a short explanation of what it could support.
7. If the user is drafting content, recommend a citation only when the source materially supports the surrounding claim. Inspect the article before representing its contents when the search result alone is insufficient.

All three transports use the same v1 search contract: `query` is required; `limit` is 1–50; `language` is optional; and up to 20 exact excluded domains are allowed.

## CLI

Keep the key in `CITEGUILD_API_KEY`. Never pass it as a flag or place it in a URL or config file.

Check configuration and authentication without revealing the key:

```bash
citeguild config status
citeguild auth status
```

For agents and scripts, request stable JSON. Put options before the query:

```bash
citeguild search --json --limit 10 \
  --language en \
  --exclude-domain my-site.example \
  "How do Django transaction commit hooks work?"
```

Use `--` before a query that begins with a hyphen. Diagnostics go to stderr. A JSON failure includes `code`, `message`, `retryable`, `exit_code`, and when available `request_id` and `retry_after_seconds`. Do not install or upgrade the CLI unless the user asks; use MCP or REST when the command is unavailable.

## MCP

Call `search_member_articles` with:

- `query`: question, topic, claim, or draft passage
- `limit`: 10 initially
- `language`: optional language tag
- `excluded_domains`: optional exact domains owned by the user

Use `get_user_info` only when authentication or subscription state needs verification.

## REST API

Send the API key from `CITEGUILD_API_KEY` as either `Authorization: Bearer` or `X-API-Key`. Never put it in a query string.

```bash
curl --fail-with-body --silent --show-error \
  https://citeguild.lvtd.dev/api/v1/search \
  -H "Authorization: Bearer $CITEGUILD_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{"query":"How do Django transaction commit hooks work?","limit":10,"language":"en","excluded_domains":["my-site.example"]}'
```

The success response contains `contract_version: "v1"` and `results`. Each result has `article_id`, `title`, `canonical_url`, `domain`, `excerpt`, `relevance`, `language`, and `last_seen_at`.

## Guardrails

- State that results come from opted-in CiteGuild member articles, not the whole web.
- Never describe a candidate as verified, authoritative, or endorsed solely because CiteGuild returned it.
- Never promise a backlink, placement, ranking gain, or reciprocal link.
- Do not add irrelevant citations to manufacture an exchange. Editorial relevance wins.
- Do not imply that finding or citing a member article obligates its owner to cite back.
- Do not fabricate titles, URLs, claims, or source contents.
- Use broader web search or independent verification only when the user separately requests it or the task genuinely requires it; distinguish those results from CiteGuild candidates.

## Authentication and errors

For CLI, REST, and API-key MCP access, use `CITEGUILD_API_KEY`. In Claude Code and ChatGPT, prefer the MCP client's OAuth flow unless the client is configured separately with an API key. Never hardcode, print, log, or commit a credential.

Handle transport errors consistently:

- `401`: the credential is missing, invalid, or revoked.
- `403` with `subscription_required`: explain that an active subscription is required and stop.
- `422`: correct the request contract.
- `429`: honor `Retry-After` or `retry_after_seconds`.
- `503`: preserve the query and suggest retrying rather than substituting invented results.

## Output

Lead with the number of strong matches. For each match, return:

- linked article title and domain
- the claim or section it may support
- one-sentence relevance rationale
- any verification caveat

Say clearly when no result is sufficiently relevant.
