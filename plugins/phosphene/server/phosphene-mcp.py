#!/usr/bin/env python3
"""Launcher for the Phosphene MCP server (stdio). Standard library only.

Finds the Phosphene you already have on this Mac (the Mac app, or Pinokio) and runs its own
agents/phosphene_mcp.py. Nothing is downloaded and nothing leaves the Mac. If Phosphene is not
installed, a one-tool stand-in tells the agent (and you) how to get it.
"""
import glob
import json
import os
import sys

sys.dont_write_bytecode = True
HOME = os.path.expanduser("~")
HINT = ("Phosphene is not installed on this Mac. Install the free Phosphene app "
        "(Mac app, or Pinokio), open it, then restart this agent.")


def candidates():
    env = os.environ.get("PHOSPHENE_AGENTS_DIR", "").strip()
    if env:
        yield os.path.expanduser(env)
    app = os.path.join(HOME, "Library", "Application Support", "Phosphene", "app")
    yield os.path.join(app, "current", "agents")
    for d in sorted(glob.glob(os.path.join(app, "v*")), reverse=True):
        yield os.path.join(d, "agents")
    for name in ("phosphene.git", "phosphene", "Phosphene"):
        yield os.path.join(HOME, "pinokio", "api", name, "agents")
    for d in sorted(glob.glob(os.path.join(HOME, "pinokio", "api", "*phosphene*", "agents"))):
        yield d


def find():
    for d in candidates():
        if os.path.isfile(os.path.join(d, "phosphene_mcp.py")):
            return d
    return None


def stand_in():
    tool = {"name": "phosphene_status", "title": "Check Phosphene status",
            "description": "Is Phosphene installed and running on this Mac.",
            "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
            "annotations": {"title": "Check Phosphene status", "readOnlyHint": True, "openWorldHint": False}}
    for line in sys.stdin:
        try:
            m = json.loads(line)
        except ValueError:
            continue
        if not isinstance(m, dict) or m.get("id") is None:
            continue
        meth, mid = m.get("method"), m["id"]
        if meth == "initialize":
            res = {"protocolVersion": (m.get("params") or {}).get("protocolVersion") or "2025-06-18",
                   "capabilities": {"tools": {"listChanged": False}},
                   "serverInfo": {"name": "phosphene", "version": "1.0.0"}, "instructions": HINT}
        elif meth == "tools/list":
            res = {"tools": [tool]}
        elif meth == "tools/call":
            res = {"content": [{"type": "text", "text": HINT}], "isError": True}
        elif meth == "ping":
            res = {}
        else:
            print(json.dumps({"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": "Method not found"}}), flush=True)
            continue
        print(json.dumps({"jsonrpc": "2.0", "id": mid, "result": res}), flush=True)


# Hints for Phosphene versions that predate built-in tool titles (the current ones ship their own).
HINTS = {
    "phosphene_status": ("Check Phosphene status", {"readOnlyHint": True}),
    "phosphene_list_jobs": ("List render jobs", {"readOnlyHint": True}),
    "phosphene_wait": ("Wait for a render", {"readOnlyHint": True}),
    "phosphene_stop": ("Stop the current render", {"readOnlyHint": False, "destructiveHint": True}),
}


def main():
    d = find()
    if not d:
        return stand_in()
    sys.path.insert(0, d)
    import phosphene_mcp as m
    for t in m.TOOLS:
        if "annotations" in t:
            continue
        title, hints = HINTS.get(t["name"], (t["name"].replace("phosphene_", "").replace("_", " ").capitalize(),
                                             {"readOnlyHint": False, "destructiveHint": False}))
        t["title"] = title
        t["annotations"] = {"title": title, **hints, "openWorldHint": False}
    m.serve()


main()
