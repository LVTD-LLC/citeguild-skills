#!/usr/bin/env python3
"""Validate CiteGuild plugin packaging without third-party dependencies."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    paths = [
        ROOT / ".agents/plugins/marketplace.json",
        ROOT / ".claude-plugin/marketplace.json",
        ROOT / "plugins/citeguild/.codex-plugin/plugin.json",
        ROOT / "plugins/citeguild/.claude-plugin/plugin.json",
        ROOT / "plugins/citeguild/.mcp.json",
    ]
    documents = {path: load_json(path) for path in paths}

    codex_marketplace = documents[paths[0]]
    claude_marketplace = documents[paths[1]]
    codex_plugin = documents[paths[2]]
    claude_plugin = documents[paths[3]]
    mcp_config = documents[paths[4]]

    assert codex_marketplace["name"] == "citeguild-skills"
    assert claude_marketplace["name"] == "citeguild-skills"
    assert codex_plugin["name"] == claude_plugin["name"] == "citeguild"
    assert codex_plugin["version"] == claude_plugin["version"]
    assert codex_marketplace["plugins"][0]["source"]["path"] == "./plugins/citeguild"
    assert claude_marketplace["plugins"][0]["source"] == "./plugins/citeguild"
    assert mcp_config["mcpServers"]["citeguild"] == {
        "type": "http",
        "url": "https://citeguild.lvtd.dev/mcp/",
    }

    skill = ROOT / "plugins/citeguild/skills/find-editorial-citations/SKILL.md"
    skill_text = skill.read_text(encoding="utf-8")
    assert skill_text.startswith("---\nname: find-editorial-citations\n")
    assert "TODO" not in skill_text
    assert "guaranteed link" in skill_text

    print("Validated CiteGuild plugin manifests, marketplace paths, MCP config, and skill.")


if __name__ == "__main__":
    main()
