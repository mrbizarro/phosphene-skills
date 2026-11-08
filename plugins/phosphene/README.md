# Phosphene for Claude

Make AI video (with its own sound), pictures, speech and music on your own Mac, from Claude. Phosphene is a free, open-source studio for Apple Silicon: https://phosphene.video/

This plugin connects Claude to the Phosphene you already run on your Mac. Ask for a clip, a poster, a voice line or a song; Claude queues it in Phosphene, waits for the render, and hands you the files.

## What you need

- A Mac with Apple Silicon (video and songs from 16 GB of memory).
- Phosphene installed and open: the Mac app, or Pinokio. Free: https://phosphene.video/
- Python 3 (already on every Mac).

The plugin finds Phosphene by itself (`~/Library/Application Support/Phosphene` for the Mac app, `~/pinokio/api/phosphene*` for Pinokio). To point it somewhere else, set `PHOSPHENE_AGENTS_DIR` to the `agents` folder of your Phosphene.

## Install

```
/plugin marketplace add mrbizarro/phosphene-skills
/plugin install phosphene@phosphene-skills
```

## Tools

| Tool | What it does |
|---|---|
| `phosphene_status` | Is Phosphene running, Free or Pro, which engines, what is rendering (read-only) |
| `phosphene_make_video` | Queue a video clip (text or picture to video) |
| `phosphene_make_image` | Queue still images |
| `phosphene_make_speech` | Text to speech |
| `phosphene_make_music` | A song or an instrumental |
| `phosphene_open_cut` | Hand a finished edit to Phosphene's Editor |
| `phosphene_list_jobs` | Running, queued and recent jobs (read-only) |
| `phosphene_wait` | Wait for a render to finish (read-only) |
| `phosphene_fetch` | Copy finished files into a folder |
| `phosphene_stop` | Stop the render in progress |

Example prompts: "Make a five-second clip of a night ferry crossing a dark harbour in rain, with the sound of the horn." / "Make three 16:9 stills of a red tram poster." / "Read this paragraph aloud with the ryan voice."

Renders take minutes. Claude queues the job and waits; the models' own licences are accepted by you inside Phosphene, never by Claude.

## Privacy

Everything runs locally on your Mac. This plugin talks only to the Phosphene studio on `127.0.0.1` (your own machine). It has no server, no account, no analytics, no telemetry, and it sends nothing anywhere. Your prompts, pictures, audio and finished files stay on your Mac; the plugin stores nothing itself and keeps no data.

Phosphene (the app) runs the models on your own hardware. It may check for updates and download model files you choose to install; that is the app's behaviour, described in its policy.

- Privacy policy: https://phosphene.video/privacy/
- Support: https://phosphene.video/contact/
- Not for children: the plugin is a general creative tool with no age-specific features.

## Source and licence

MIT. Plugin source: https://github.com/mrbizarro/phosphene-skills. The skill in this repo also installs on its own with `npx skills add mrbizarro/phosphene-skills`.
