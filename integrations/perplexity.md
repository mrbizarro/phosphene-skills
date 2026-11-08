# Use Phosphene from Perplexity

Phosphene is a free, open-source Mac app for making AI videos, pictures, speech and songs offline. Run LTX-2.5 and MiniMax H3 (Hailuo) locally on Apple Silicon: text-to-video and image-to-video with sound, lip-sync, character LoRA training. Mac app or Pinokio. No cloud, no API key, no NVIDIA GPU. Works with Claude Code, Codex and any MCP agent.

Use the Perplexity Mac app on the same Mac as Phosphene. The documented local setup is below; it has not yet been tested in the Perplexity app. This is a custom connector, not an approved marketplace listing.

1. Install and open [Phosphene](https://phosphene.video/). Install Python 3 if it is not already available.
2. Download or clone [this repository](https://github.com/mrbizarro/phosphene-skills) into `~/phosphene-skills`. If you choose another location, replace the path in the command below.
3. In Perplexity, open **Plugins** and install its **PerplexityXPC** helper when prompted.
4. Choose **Add custom → Simple**. Set the server name to **Phosphene** and copy this command:

```sh
/bin/sh -c 'exec python3 "$HOME/phosphene-skills/plugins/phosphene/bin/phosphene-mcp.py"'
```

5. Save. Open **Plugins → Installed**, wait for **Running**, and enable Phosphene under **Sources**.
6. Ask: “Use Phosphene to check the Studio status and list the installed models. Do not start a render.”

For clients that accept JSON, [copy the equivalent configuration](local-mcp.json). This JSON is not a documented one-click Perplexity installer. No official Perplexity installation deep link was found. The Simple command is the documented route.

If the command cannot find Python, replace `python3` with the absolute path to your Python 3 installation. If Simple is missing and only a server URL appears, this local setup cannot be entered there. Do not put localhost or the Studio web URL in a remote MCP field. Comet/web local-stdio support is not established by the Mac documentation.

Phosphene generates media on the Mac. Perplexity still receives your conversation and tool results under its own data policies. Connecting a cloud assistant does not make that assistant offline.

[Official setup instructions](https://www.perplexity.ai/help-center/en/articles/11502712-local-and-remote-mcps-for-perplexity), checked 8 November 2026.
