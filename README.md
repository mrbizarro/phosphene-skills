# Phosphene agent skill

Phosphene is a free, open-source Mac app for making AI videos, pictures, speech and songs offline. Run LTX-2.5 and MiniMax H3 (Hailuo) locally on Apple Silicon: text-to-video and image-to-video with sound, lip-sync, character LoRA training. Mac app or Pinokio. No cloud, no API key, no NVIDIA GPU. Works with Claude Code, Codex and any MCP agent.

```bash
npx skills add mrbizarro/phosphene-skills
```

The skill teaches an agent (Claude Code, Codex and others) to drive a running Phosphene studio through its local CLI and MCP server. Phosphene itself: https://github.com/mrbizarro/Phosphene

**Will it run on your Mac?** [phosphene.video/mac-requirements](https://phosphene.video/mac-requirements/?utm_source=github&utm_medium=phosphene-skills) shows what each memory size can make and how long a clip takes.

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

## Where to find Phosphene

Checked on 9 November 2026.

Live now:
- [skills.sh](https://www.skills.sh/mrbizarro/phosphene-skills/phosphene): install with `npx skills add mrbizarro/phosphene-skills`.
- [awesome-mlx](https://github.com/antranapp/awesome-mlx#demo): Phosphene is listed; [PR #59](https://github.com/antranapp/awesome-mlx/pull/59) is merged.

Submitted, awaiting review (coming soon only if accepted; no launch date promised):
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers/pull/18931): coming soon, PR #18931 is open.
- [awesome-mlx by raullenchai](https://github.com/raullenchai/awesome-mlx/issues/44): coming soon, request #44 is open.
