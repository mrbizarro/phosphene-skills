---
name: phosphene
description: Make AI video, pictures, speech and music locally on a Mac with Phosphene (free, open source, Apple Silicon). Use when the user wants to generate a video clip (text-to-video or picture-to-video with LTX-2.5 or Hailuo H3), pictures (FLUX 3 Klein, P-H3-Image), spoken lines or songs on their own Mac instead of a cloud service, or wants to check, wait for or fetch Phosphene renders.
---

# Phosphene: local AI video, pictures and music on a Mac

Phosphene is a free, open-source studio that runs AI video, picture, speech and music models on Apple Silicon Macs. Nothing is uploaded. It runs as a Mac app or in Pinokio, and both expose the same local HTTP API, a small CLI and an MCP server for agents.

Home: https://phosphene.video/?utm_source=skills&utm_medium=agent

## Before you start

- Phosphene must be installed and running on the user's Mac: open the Phosphene app, or press Start on Phosphene in Pinokio. If it is not running, tell the user exactly that; do not try to install models yourself.
- Renders take minutes, not seconds. Queue a job, then wait for it.
- Some models have their own licence (for example Hailuo H3). If the studio answers HTTP 451, ask the user to accept the licence once inside Phosphene. Never accept it for them.

## Connect

The running studio tells you the exact command for this install: open `http://127.0.0.1:8198/agents/info` (the studio's own page on this Mac).

In Pinokio the studio listens on 8198; in the Mac app on a free port between 8930 and 8999. Every running studio announces itself in `~/.phosphene/servers/<port>.json`, so the CLI and MCP server find it on their own. Set `PHOSPHENE_URL` to force one.

Use the CLI below; it ships inside Phosphene, so there is nothing else to install. If the user wants Phosphene's MCP server too, the studio's own page `http://127.0.0.1:8198/agents/info` shows the exact one-line command for this install; let the user add it themselves.

MCP tools: `phosphene_status`, `phosphene_make_video`, `phosphene_make_image`, `phosphene_make_speech`, `phosphene_make_music`, `phosphene_list_jobs`, `phosphene_wait`, `phosphene_fetch`, `phosphene_stop`. A `make_*` tool queues a job and returns its id; `phosphene_wait` blocks up to `timeout_sec` (default 1500) and can be called again.

## CLI

`phosphene` below means `python3 <studio>/agents/phosphene_cli.py` (standard library only, Python 3.9+).

```bash
phosphene status
phosphene video "A night ferry crosses a dark harbour in light rain. Sound: rain on the deck, a low horn." --seconds 5 --out ./clips --wait
phosphene video "..." --image still.png --seconds 5 --wait        # picture to video
phosphene video "..." --engine h3 --quality draft --seconds 10 --wait
phosphene image "a travel poster of a red tram, the words NIGHT LINE at the top" --n 2 --aspect 3:4 --out ./stills
phosphene jobs
phosphene wait JOB_ID --out ./clips
phosphene fetch JOB_ID --out ./clips
phosphene stop
```

Add `--json` for machine-readable output. Exit codes: 0 ok, 1 the studio refused or the job failed (the reason is printed), 2 bad arguments, 3 Phosphene is not running.

## Writing good prompts

- Describe the shot and the sound together: what we see, how the camera moves, then "Sound: ...". Video models here generate audio with the picture.
- Keep it to one clear idea per clip. Five to ten seconds per render; chain clips for longer pieces.
- For pictures with text, put the exact words in quotes; P-H3-Image spells quoted text as written.

## What it can run

Depends on the Mac's memory: video and songs from 16 GB, character training from 24 GB, Hailuo H3 from 36 GB. `phosphene status` reports what this Mac supports. Free covers every feature; an optional Pro gets some speed-ups first.
