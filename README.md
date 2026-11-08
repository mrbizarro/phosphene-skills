# Phosphene agent skill

An agent skill for [Phosphene](https://phosphene.video/?utm_source=github&utm_medium=skills): free, open-source AI video, pictures, speech and music on your Mac.

```bash
npx skills add mrbizarro/phosphene-skills
```

The skill teaches an agent (Claude Code, Codex and others) to drive a running Phosphene studio through its local CLI and MCP server. Phosphene itself: https://github.com/mrbizarro/Phosphene

## Claude Code plugin

The same skill, plus the MCP server wired up for you, installs as a plugin (needs Phosphene installed on the Mac):

```
/plugin marketplace add mrbizarro/phosphene-skills
/plugin install phosphene@phosphene-skills
```

Source in `plugins/phosphene/`. Privacy: everything runs on your Mac and nothing is sent anywhere (see the plugin README).
