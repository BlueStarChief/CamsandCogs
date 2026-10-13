# Cams and Cogs

Tools for designing 1800s-style mechanical automata: cams and followers, gear trains, linkages and clockwork. The goal is a browser tool that goes from the motion you want to parts you can laser-cut or 3D-print.

## What's here

- `demo/index.html`: **the working demo. Open it straight from disk.** Describe each motion as rise / hold / fall steps; it designs the cams and gear train, animates the machine, and gives a true-scale SVG cutting file. Your edits are remembered in that browser only (Safari blocks this for files opened from disk; Chrome and Firefox keep them).
- `demo/automaton-designer.html`: the source of the demo (the published page). Edit this file, then run `demo/make-local.sh` to regenerate `index.html`.

- `research/similar-repos.md`: a survey of existing open-source cam, gear and linkage tools, with the recommended architecture and MIT-licensed JS snippets (cam motion laws, undercut check, involute gears, SVG export). Open `research/similar-repos.html` for the formatted version with diagrams.
- `research/build-html.py`: rebuilds the HTML from the Markdown (`pip install markdown`, then `python3 research/build-html.py`).

Snippets adapted from [MHSGhali/Linkage-Design](https://github.com/MHSGhali/Linkage-Design), [EkaEva/CamForge](https://github.com/EkaEva/CamForge) and [1400130-collab/gearforge](https://github.com/1400130-collab/gearforge), all MIT. Attribution is kept in each snippet.
