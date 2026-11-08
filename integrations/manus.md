# Manus compatibility notes

Checked 8 November 2026. Not a claim of tested Manus compatibility.

The [official connector page](https://www.manus.im/features/connectors) now offers server URLs, command-based Custom MCP, and JSON import. Open **Connectors → Create → Custom MCP** or **Import MCP by JSON**. A configuration example is in [local-mcp.json](local-mcp.json), but use it only if the runtime executes on the Mac with Phosphene installed.

The [custom MCP guide](https://manus.im/docs/integrations/custom-mcp) describes an HTTPS endpoint, authentication, and a connection test that discovers tools. Those instructions concern a remotely reachable server. Phosphene currently has no public remote MCP endpoint. Command support alone does not prove access to the user's Mac.

No public third-party catalog submission form or repository contribution route was found in these official pages. Publishing a connector to a Manus Project is not global catalog publication. The remaining work is an account-side check of command execution location and a local read-only status test. Do not expose the Studio port to the internet to make this configuration work.
