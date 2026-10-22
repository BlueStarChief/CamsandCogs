# Decisions — CamsandCogs

## Stack and shape of the tool — 2026-10-13
- **Chosen:** single-file browser pages (plain JS, Canvas/SVG, no framework, no build), each published as a claude.ai artifact plus a standalone local copy — **Why:** user picked browser JS/TS; offline single files match the best prior art (CamFollowerJS, mechanical-characters, gearforge) and can be opened from disk.
- **Rejected:** Python / OpenSCAD / CAD plug-in — less shareable; React/SolidJS — no weight to carry here.
- **Status:** locked

## Exemplar for architecture — 2026-10-13
- **Chosen:** MHSGhali/Linkage-Design (MIT) as the architecture reference; CamForge (MIT) for cam laws; gearforge (MIT) for kerf-true SVG export — **Why:** only repo covering cams, gears, linkages and Geneva drives, both design directions, sim + STL.
- **Rejected:** CamFollowerJS as a code source (no license → ideas only); chrisspen/gears (unclear license).
- **Status:** locked

## Repo visibility — 2026-10-13
- **Chosen:** PUBLIC repo BlueStarChief/CamsandCogs — **Why:** user's explicit choice ("can be public"); personal hobby project, no client data or PII.
- **Rejected:** private (the default rule for BUILD EVERYTHING) — user overrode for this project.
- **Status:** locked. Pushes must still be checked for secrets/paths; borrowed code stays MIT with attribution.

## Real linkages instead of a faked figure — 2026-10-13
- **Chosen:** every motion goes cam → push rod → connecting link → lever on a pin (bell crank at the shoulder, lever on the neck pin) or a direct rod (hat); the figure only moves by what the solved linkage gives — **Why:** user asked to "see real linkages" and "real numbers"; v1 multiplied lift by a made-up factor.
- **Rejected:** fudge-factor mapping from cam lift to part angle.
- **Status:** locked

## Targets in real units, proved two ways — 2026-10-13
- **Chosen:** user sets degrees / mm; cam lift solved backwards in closed form; mechanism solved forwards by circle–circle intersection; the two compared over 720 samples, plus link-length, transmission-angle, undercut, pressure-angle, cam-spacing, rod-guide and gear-mesh checks — **Why:** "how can I be sure that's what's happening" — independent methods agreeing is the proof.
- **Rejected:** trusting the animation alone.
- **Status:** locked

## Coordinate description for 3D — 2026-10-13
- **Chosen (direction):** describe joints by pivot point + axis (equivalent to DH, easier to author); drive out-of-plane joints with ball-jointed (RSSR) links — the same backwards/forwards proof extends (A·cosθ + B·sinθ = C) — **Why:** DH only describes serial chains; automata drives are closed loops that need a loop-closure equation.
- **Rejected:** strict DH parameter convention — fiddly frame rules, no gain here.
- **Status:** open (not built — see deferred)

## Xylophone layout — 2026-10-13
- **Chosen:** 8 bars, C major one octave (default C6–C7, aluminium 6 mm × 25 mm), lengths from free-free beam theory f = 1.028·c·t/L², cord holes at 22.4%, bars parallel with centres on an arc around the player's turning axis (reach 135 mm) — **Why:** a pure turn then lands on every bar centre; outputs the turn angle and ±landing window per note.
- **Rejected:** straight row — end bars get struck ~49 mm off centre, at the node; radial fan — long bars overlap near the axis.
- **Status:** locked

## Xylophone player drive — 2026-10-13
- **Chosen:** turn cam → horizontal follower with a rack → pinion (16T, m0.5, r = 4 mm) on the vertical waist shaft (angle = travel ÷ radius, exact); strike = snail cam on a rod up the hollow turning shaft to a 10 mm mallet lever; cord-and-drum offered as a switchable alternative (no backlash) — **Why:** linear-to-rotary that is exactly proportional, so each bar is one rack position; snail drop gives the sharp strike.
- **Rejected:** crank + link for the turn — non-linear, and >~110° approaches lock-up.
- **Status:** locked. Open risk: ±0.19 mm rack tolerance (±2.8° at the bars); the turn cam is ~134 mm for "Twinkle" because of the C→G leap.

## Deferred (later, not forgotten) — 2026-10-21
- **Wing flapping** — user's idea; agreed to do the xylophone player first. Status: open
- **Out-of-plane motions (ball-jointed RSSR links / DH-style joint chain)** — discussed, not built; the xylophone turn was solved with rack and pinion instead. Status: open
- **3D view, layer assignment + collision check, STL export** — offered; not yet requested to build. Status: open
- **Xylophone player on the main page with crank, gear train and figure** — offered as next step. Status: open
- **Movable pivot points and a protractor/ruler overlay** — offered. Status: open
- **Real downloads inside the claude.ai viewer (`downloads` capability)** — Copy SVG works there; Download works in the local copies. Status: open
- **Mallet bounce / springy handle** — not modelled; mallet rests on the bar briefly. Status: open
- **Pivoting-lever cam followers** — exemplar and demo use translating followers only. Status: open
- **Two-arm xylophone player** — would cut the 102° sweep to ~45° per arm; user didn't choose yet. Status: open
