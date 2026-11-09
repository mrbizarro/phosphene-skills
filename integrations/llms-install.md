# Install Phosphene MCP for a local agent

Free AI video, pictures and songs, made offline on your Mac. Works with Claude Code, Codex and other AI agents.

Requires an Apple Silicon Mac, Python 3, and Phosphene installed and open. This repository supplies a standard-library Python stdio launcher; it discovers the existing Mac app or Pinokio installation. It does not install models or start a render.

Clone this repository into `~/phosphene-skills`, or use its existing checkout. Configure the local MCP client with `python3` as the command and the absolute path to `plugins/phosphene/server/phosphene-mcp.py` as its single argument. Preserve other configured servers. The [portable JSON example](local-mcp.json) assumes the documented clone location and expands HOME through `/bin/sh`.

List tools and call `phosphene_status`. If it reports Phosphene is not installed, install Phosphene from https://phosphene.video/ and open Studio before retrying. Never treat the installation-help fallback as a successful generation test. Ask before downloading models or rendering.

This launcher needs the local Mac installation. A cloud Linux runtime or Docker container cannot use it unchanged. No API key is required by Phosphene. The agent provider's own account requirements still apply.
