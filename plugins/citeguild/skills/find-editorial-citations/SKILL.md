---
name: find-editorial-citations
description: Search CiteGuild's opted-in member article index for relevant editorial citation candidates. Use when a user wants sources for a draft, article, research brief, or topic; wants to discover member content worth citing; or asks for ethical backlink opportunities through CiteGuild. Do not use for broad web search, independent fact verification, guaranteed link placement, or automatic reciprocal linking.
---

# Find Editorial Citations

Find sources that genuinely improve the user's work. Treat CiteGuild as a focused member corpus, not a replacement for a broad search engine.

## Workflow

1. Extract a focused search query from the topic, passage, claim, or draft. Preserve the user's meaning and avoid sending confidential or unnecessary text.
2. Ask for the user's own domain only when it cannot be inferred and excluding it materially matters. Pass known owned domains in `excluded_domains`.
3. Call `search_member_articles` with the focused query. Start with 10 results; increase the limit or try one narrower query only when the first pass is insufficient.
4. Rank candidates by direct topical and claim-level relevance. Prefer a smaller set of strong matches over filling a quota.
5. Present each useful candidate with its title, URL, domain, and a short explanation of what it could support.
6. If the user is drafting content, recommend a citation only when the source materially supports the surrounding claim. Inspect the article before representing its contents when the search result alone is insufficient.

## Guardrails

- State that results come from opted-in CiteGuild member articles, not the whole web.
- Never describe a candidate as verified, authoritative, or endorsed solely because CiteGuild returned it.
- Never promise a backlink, placement, ranking gain, or reciprocal link.
- Do not add irrelevant citations to manufacture an exchange. Editorial relevance wins.
- Do not imply that finding or citing a member article obligates its owner to cite back.
- Do not fabricate titles, URLs, claims, or source contents.
- Use broader web search or independent verification only when the user separately requests it or the task genuinely requires it; distinguish those results from CiteGuild candidates.

## Authentication and errors

In Codex, use the API key supplied through the `CITEGUILD_API_KEY` environment variable; the bundled MCP server reads it as a bearer token. In Claude Code and ChatGPT, use the MCP client's OAuth flow unless that client has been configured separately with an API key. Never hardcode, print, log, or commit a credential.

If search reports that an active subscription is required, explain the requirement and stop. If the index is temporarily unavailable, preserve the query and suggest retrying rather than substituting invented results.

## Output

Lead with the number of strong matches. For each match, return:

- linked article title and domain
- the claim or section it may support
- one-sentence relevance rationale
- any verification caveat

Say clearly when no result is sufficiently relevant.
