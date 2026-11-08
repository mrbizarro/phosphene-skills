# Phosphene agent skill

Phosphene is a free, open-source Mac app for making AI videos, pictures, speech and songs offline. Run LTX-2.5 and MiniMax H3 (Hailuo) locally on Apple Silicon: text-to-video and image-to-video with sound, lip-sync, character LoRA training. Mac app or Pinokio. No cloud, no API key, no NVIDIA GPU. Works with Claude Code, Codex and any MCP agent.

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

## Other local agents

- [Use Phosphene from Perplexity](integrations/perplexity.md)
- [Local MCP configuration and installation](integrations/llms-install.md)
- [Manus compatibility notes](integrations/manus.md)
- [Directory listing copy](integrations/DIRECTORY_COPY.md)
