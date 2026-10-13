# Similar repos: cams, gears and linkages for 1800s-style automata

*Generated 2026-10-13 by `/similar-repos`. Source of truth for `similar-repos.html`.*

## Scope

| Field | Answer |
|---|---|
| **Problem** | Design the mechanical "program" of a clockwork automaton: cams and followers, gears and gear trains, linkages and levers, escapements, Geneva drives. |
| **Stack** | Browser JS/TS. |
| **Outputs** | Cut profiles (SVG/DXF), 3D models (STL) and an animated simulator. |
| **Direction** | Both: describe the motion and get the cam, *or* draw a cam and see the motion. |
| **Dealbreakers** | None. License and health are noted, not filtered. Fabrication method is still undecided. |
| **"Similar" means** | Does the mechanism math (cam profile, involute teeth, linkage synthesis) and turns it into something you can cut or print. |

**Search surface.** About 30 `gh` queries. Concept queries: *cam profile generator, cam follower, cam design, cam mechanism, cam synthesis, involute gear generator, gear generator, gear train calculator, clock gears, linkage simulator, mechanism simulator, mechanism editor, automaton cam, mechanical automata, mechanical characters, geneva drive, escapement clock, kinetic sculpture, openscad gear/cam*. Topic queries: `cam`, `gear-generator`, `linkage`, `kinematics`, `mechanism`. Code searches on rise/dwell/cycloidal terms returned nothing. This is a thin niche on GitHub: no repo has more than about 400 stars, and most of the good ones are hobby projects from 2025–26.

## Ranked landscape

| # | Repo | ★ | License | Competitor? | Why it's similar |
|---|---|---|---|---|---|
| 1 | [jumpjack/CamFollowerJS](https://github.com/jumpjack/CamFollowerJS) | 6 | none → **withheld** | **yes** + reference | The only repo built explicitly for **automata** cams. It turns a flat displacement chart into a polar cam and animates the follower in the browser. It also ships automata reference PDFs and videos. |
| 2 | [MHSGhali/Linkage-Design](https://github.com/MHSGhali/Linkage-Design) | 0 | MIT | reference | **The whole stack in one program:** links, sliders, involute gears, cams, Geneva wheels. It designs in both directions (draw a path → machine) and exports printable STL parts with a manifest. **Clone target.** |
| 3 | [n-nagaya/mechanical-characters](https://github.com/n-nagaya/mechanical-characters) | 2 | MIT | **yes** + reference | Browser port of Disney's *Computational Design of Mechanical Characters* (SIGGRAPH 2013). Sketch a motion curve and it finds and optimizes a crank, linkage and gear mechanism, then exports mm-true DXF. |
| 4 | [EkaEva/CamForge](https://github.com/EkaEva/CamForge) | 4 | MIT | reference | Serious cam engineering: 6+ motion laws, offset followers, roller radius, **pressure-angle and curvature-radius plots**. SolidJS front end with a Rust core. |
| 5 | [1400130-collab/gearforge](https://github.com/1400130-collab/gearforge) | 2 | MIT | reference | Standards-correct involute gears, racks and pulleys in zero-dependency browser JS. **Kerf-compensated SVG/DXF** for laser cutters, plus a caliper inspection report. |
| 6 | [moh-d-m4x/MechAnim](https://github.com/moh-d-m4x/MechAnim) | 0 | MIT | **yes** + reference | "Character motion designer". Draw a path or trace one from video, and a genetic algorithm fits 4-bar, 5-bar, piston or Scotch-yoke linkages. SVG/DXF export. |
| 7 | [HugoFara/pylinkage](https://github.com/HugoFara/pylinkage) | 32 | MIT | reference | The best linkage **synthesis** math found: Burmester and Freudenstein plus PSO/DE. "Tell it where the point should go." Exports DXF and STEP. Python. |
| 8 | [SindiSekkas/geneva-drive-generator](https://github.com/SindiSekkas/geneva-drive-generator) | 2 | MIT | reference | Parametric Geneva drive (intermittent motion) to DXF, using Walsh-handbook formulas. Small, clean TS with Vite and Vitest. |
| 9 | [jes/clock-gear-train-calculator](https://github.com/jes/clock-gear-train-calculator) | 0 | none → **withheld** | reference | Searches wheel and pinion tooth counts that hit a target ratio, which is exactly the clockwork "going train" problem. |
| 10 | [hdrpano/watchmaking](https://github.com/hdrpano/watchmaking) | 5 | MIT | reference | Horological gear trains, Belot wheel and pinion profiles, contact and efficiency analysis, DXF. Clockwork-grade tooth forms (not involute). |
| 11 | [chrisspen/gears](https://github.com/chrisspen/gears) | 403 | unclear → **withheld** | reference | The most-starred gear library: OpenSCAD spur, bevel, worm, rack and herringbone parts, ready for 3D printing. |
| 12 | [piellardj/non-circular-gears](https://github.com/piellardj/non-circular-gears) | 18 | MIT | reference | Non-circular gears for *variable-speed* motion, a da Vinci-era trick that is useful for lifelike easing. |

Also seen and not shortlisted:

- [jauhl/mecEdit](https://github.com/jauhl/mecEdit): MIT linkage PWA.
- [dpellegr/PolyGear](https://github.com/dpellegr/PolyGear): OpenSCAD, no license.
- [joy-boy56/Cam-profile-generator](https://github.com/joy-boy56/Cam-profile-generator): Python, MIT, cam to DXF.
- [hermanncain/Kineticist](https://github.com/hermanncain/Kineticist): kinetic sculpture CAD.
- *ncreighton/premium-automaton-mech-001*: a paid **Notion template** for "automaton cam and lever sequences". It isn't code, but it is a **commercial competitor** and a sign that makers want this tool.

## Tier-1 wiring maps

- **CamFollowerJS.** Plain HTML and JS with `paper.js` (vector canvas). A flat cartesian profile in a JSON file is wrapped to a polar cam, then rotated while the follower is solved for contact. Runs offline from `index.html`. STL is on the wishlist; SVG is converted to STL externally.
- **Linkage-Design.** C99 and SDL2, no other dependencies. The pieces connect in a line:
    - `mechanism.c` is the model.
    - `solver.c` does Gauss-Newton on distance constraints.
    - `cam.c`, `gearing.c`, `joints.c` and `synth.c` are domain modules.
    - `render.c` draws the canvas.
    - `export.c` writes a Blender script; `mesh3d.c` and `print3d.c` write STL plus a manifest.
    - The headless test suite covers every non-SDL module.
- **mechanical-characters.** A single `index.html` with no libraries. Sketch → search a precomputed mechanism database → continuous optimization → play with one crank → export JSON, CSV or DXF (R12, layered: LINK, PIVOT, GEAR…).
- **CamForge.** SolidJS and Tailwind UI. The `camforge-core` Rust crate (motion, profile, geometry, simulation) is shared by a Tauri desktop shell and an Axum web server. Exports go through server routes. `docs/ALGORITHMS.md` documents every formula.
- **gearforge.** Zero-dependency browser JS:
    - `involute.js`, `pulley.js` and `spline.js` make geometry.
    - `geometry.js` handles offsets and bounding boxes.
    - `exporters.js` writes SVG and DXF with kerf.
    - `app.js` is the UI; `tests/run-tests.js` runs on Node.
- **MechAnim.** TS, Vite and React. The mechanism types sit in a 2D canvas simulator; a GA/Monte-Carlo optimizer fits a path; Catmull-Rom smooths video annotations; exports are SVG and DXF.
- **pylinkage.** Python with optional numba, SciPy, SymPy and drawsvg. Joints and linkages feed a solver; synthesis covers Burmester, Freudenstein and the optimizers; visualizers and exporters write DXF and STEP.
- **geneva-drive-generator.** Vite, TS and Vitest. A parameter form feeds derived dimensions, which feed a preview and a DXF writer.
- **clock-gear-train-calculator.** A single JS page. Brute-force search over tooth counts per shaft, with the result filtered by target ratio.
- **watchmaking / chrisspen gears / non-circular-gears.** Respectively: a PyQt analysis app, an OpenSCAD module library, and a TS and SVG generator.

## Clone this one: `MHSGhali/Linkage-Design`

It beat the runners-up because it is the **only repo that covers every mechanism you listed and every output you asked for**:

- cams with a roller follower and return spring, involute gears and racks, linkages, and Geneva wheels;
- design in both directions (motion → machine, and machine → motion);
- an animated simulator plus printable parts.

It is MIT-licensed and actively developed (pushed 2026-09). Every design decision is documented in comments, and the math has headless tests. It is written in C/SDL2 rather than the browser, but the module boundaries carry over to JS almost one-to-one.

- **Backup and reuse source for cam math in TS:** EkaEva/CamForge (MIT).
- **Backup and reuse source for laser-ready gear export:** gearforge (MIT).
- **Best automata-specific UX to learn from:** CamFollowerJS. It has no license, so it is for ideas only.

## Exemplar teardown (Tier 2)

**License gate: MIT → permissive → snippets allowed (`reuse_risk: ok`).** The clone was read, then deleted from `/tmp/similar-repos/`.

### How it's wired

1. **Model.** `mechanism.c`/`.h` holds connectors (joints) and links (rigid bodies stored as pairwise rest distances). Cams, gear wheels, sliders and Geneva wheels attach to links. Deletion uses tombstones, so ids stay stable.
2. **Solver.** `solver.c` runs each frame:
    - It *poses* motor-driven links directly, in dependency order, so an arm can ride on another arm.
    - It solves every other joint with damped Gauss-Newton, warm-started from the last frame so the mechanism stays on the same assembly branch.
    - Gravity is one Verlet step, then projection back onto the constraints.
3. **Domain modules (no UI dependency, so they're fully tested):**
    - `cam.c`: the profile is stored as a **pitch curve** (the path of the roller's centre) sampled every 2°. Contact is one-sided with a preloaded return spring, so a fast cam *floats* the follower, as a real one would. It checks for undercut.
    - `gearing.c`: **the single place tooth shape is decided.** The model snaps every wheel to a *module × whole teeth*, the canvas draws the same outline, and STL extrudes it. What meshes on screen meshes on the print bed.
    - `joints.c`: slider, gear and Geneva kinematics.
    - `synth.c`: draw-a-path synthesis. It fits a Grashof four-bar, or failing that a Fourier chain of rotating arms (which can trace any closed curve).
4. **Outputs.**
    - `render.c` draws the canvas.
    - `export.c` writes a Blender script with 120 keyframes.
    - `mesh3d.c` does ear-clip triangulation, extrusion and binary STL, plus watertightness checks.
    - `print3d.c` assigns parts to **layers** by graph-colouring "shares a pin", adds spacer washers, sizes pin holes with running clearance, and writes `MANIFEST.txt`.

The diagram is in `similar-repos.html` → *System Flows*.

### Best practices to copy

- **Store the cam as a pitch curve, not as the cut surface.** Contact becomes exact (follower distance = pitch radius), and the cut surface is simply an inward offset by the roller radius.
- **Default to the cycloidal motion law.** It has zero velocity *and* zero acceleration at every segment join, so there is no jerk and the automaton runs smoothly.
- **Gears are module × teeth, never a free radius.** Quantize them at the model layer; centre distance = m·(z₁+z₂)/2.
- **One geometry function feeds the screen, SVG, DXF and STL.** Never let the preview and the export compute shapes separately.
- **Refuse unbuildable parts loudly.** Check cam undercut, Grashof (can the crank turn fully?), linkage binding, gears under 14 teeth, and watertight STL. Report each problem; don't silently emit bad geometry.
- **Keep the math free of UI dependencies, so it can be tested headless.** Every template in the gallery runs for 6 s in tests and fails if it binds.
- **Rotating the cam profile is "timing".** In automata, sequencing several cams on one shaft *is* the program.

## Overall architecture (synthesis across the shortlist)

The good projects converge on a **pipeline with a single geometry core**:

```
Intent (motion you want / part you drew)
  → Synthesis (motion law → cam pitch curve · path → four-bar / Fourier arms · ratio → tooth counts)
  → Mechanism model (joints, links, cams, gears, Geneva — gears snapped to module × teeth)
  → Solver (pose motors, Gauss-Newton constraints, one-sided cam contact + spring)
  → Checks (undercut, pressure angle ≤ ~30°, Grashof, binding, min teeth)
  → Outputs: canvas simulator · SVG/DXF (mm-true, kerf-compensated, CUT/ENGRAVE layers) · STL (extruded, layered, pin holes, manifest)
```

**Recommended browser stack for this project.** Use plain TS modules for the math, with no framework in the core, in the style of gearforge and Linkage-Design. Use Canvas or SVG for the simulator. Write your own SVG/DXF R12 writers; they are about 150 lines (see gearforge). Use `three.js` or a small hand-rolled extruder plus an STL writer for 3D. The whole tool can be a single offline `index.html`, as CamFollowerJS and mechanical-characters are.

### Best practices across the shortlist

1. **mm-true exports.** SVG `width`/`height` in mm with a matching `viewBox`, and DXF R12 with a metric header (gearforge, mechanical-characters).
2. **Kerf compensation at export.** Offset each cut loop by kerf/2 so outer contours grow and holes shrink (gearforge).
3. **Plot the diagnostics, not just the shape.** Displacement, velocity, acceleration, pressure angle and curvature radius against cam angle (CamForge).
4. **Inspection report for verifying a part after cutting.** Pitch, base, tip and root diameters, span measurement, centre distance (gearforge).
5. **Offline single file.** No build is needed to *use* the tool (CamFollowerJS, mechanical-characters, gearforge).
6. **Presets and a gallery.** Ship working example mechanisms the user can poke at (Linkage-Design, mechanical-characters).
7. **Synthesis should prefer the simplest machine.** Try a four-bar first and fall back to arms or cams only when the fit is poor (Linkage-Design, mechanical-characters).

## Reusable code

All snippets below are **JS ports adapted from MIT-licensed sources**. Keep the attribution comment.

### 1. Cam motion laws + rise/dwell/fall pitch curve
*source_url:* https://github.com/MHSGhali/Linkage-Design/blob/main/src/cam.c and https://github.com/EkaEva/CamForge/blob/main/docs/ALGORITHMS.md · *license:* MIT · *reuse_risk:* ok

```js
// Adapted from MHSGhali/Linkage-Design (MIT) and EkaEva/CamForge (MIT).
// Each law maps t∈[0,1] → displacement fraction s∈[0,1].
export const MOTION_LAWS = {
  uniform:    t => t,                                         // rigid shock at ends; low speed only
  parabolic:  t => t < 0.5 ? 2*t*t : 1 - 2*(1-t)**2,          // const accel; soft shock
  harmonic:   t => (1 - Math.cos(Math.PI*t)) / 2,             // smooth velocity
  cycloidal:  t => t - Math.sin(2*Math.PI*t) / (2*Math.PI),   // zero vel AND accel at ends — default
  poly345:    t => 10*t**3 - 15*t**4 + 6*t**5,
};

/** Pitch radius (roller-centre path) of a rise / high-dwell / fall / low-dwell cam.
 *  Angles in degrees; scaled down if they exceed 360. */
export function risedwellPitch({ base, lift, rise, highDwell, fall, law = 'cycloidal' }) {
  const L = MOTION_LAWS[law], k = Math.min(1, 360 / (rise + highDwell + fall));
  const a = rise*k*Math.PI/180, b = highDwell*k*Math.PI/180, g = fall*k*Math.PI/180;
  return phi => {
    phi = ((phi % (2*Math.PI)) + 2*Math.PI) % (2*Math.PI);
    if (a > 0 && phi < a)           return base + lift * L(phi / a);
    if (phi < a + b)                return base + lift;
    if (g > 0 && phi < a + b + g)   return base + lift * (1 - L((phi - a - b) / g));
    return base;
  };
}
```
*Adapt:* chain several segments to build an automaton "program" (e.g. nod, hold, turn). Stack one cam per figure motion on a common shaft, and use a phase offset for timing.

### 2. Roller-offset cam surface + undercut check
*source_url:* https://github.com/MHSGhali/Linkage-Design/blob/main/src/cam.c · *license:* MIT · *reuse_risk:* ok

```js
// Adapted from MHSGhali/Linkage-Design (MIT).
/** Physical cam surface = pitch curve offset INWARD by the roller radius. */
export function camSurface(pitch, rollerR, n = 720) {
  const h = 1e-5, pts = [];
  for (let i = 0; i < n; i++) {
    const p = 2*Math.PI*i/n, r = pitch(p), dr = (pitch(p+h) - pitch(p-h)) / (2*h);
    const c = Math.cos(p), s = Math.sin(p);
    const tx = dr*c - r*s, ty = dr*s + r*c, tl = Math.hypot(tx, ty);   // tangent
    const nx = ty/tl, ny = -tx/tl;                                     // outward normal
    pts.push([r*c - nx*rollerR, r*s - ny*rollerR]);
  }
  return pts;
}

/** True if the offset folds back on itself: the roller can't reach into a notch → uncuttable. */
export function isUndercut(pts) {
  for (let i = 0; i < pts.length; i++) {
    const [a, b, d] = [pts[i], pts[(i+1)%pts.length], pts[(i+2)%pts.length]];
    if (Math.hypot(...a) < 1e-9) return true;
    const e0 = [b[0]-a[0], b[1]-a[1]], e1 = [d[0]-b[0], d[1]-b[1]];
    const l0 = Math.hypot(...e0), l1 = Math.hypot(...e1);
    if (l0 > 1e-12 && l1 > 1e-12 && (e0[0]*e1[0] + e0[1]*e1[1]) / (l0*l1) < 0) return true;
  }
  return false;
}
```
*Adapt:* when the check fails, shrink the roller (as Linkage-Design does) or warn. Pair it with CamForge's pressure-angle plot: keep the angle under about 30° for a translating follower.

### 3. Involute spur gear outline (module × teeth)
*source_url:* https://github.com/MHSGhali/Linkage-Design/blob/main/src/gearing.c · *license:* MIT · *reuse_risk:* ok

```js
// Adapted from MHSGhali/Linkage-Design (MIT). Units: mm.
const inv = a => Math.tan(a) - a;
export const pitchRadius = (m, z) => m*z/2;
export const centerDistance = (m, za, zb) => m*(za+zb)/2;          // the ONLY distance they mesh at
export const teethForRadius = (m, r) => Math.max(8, Math.round(2*r/m));

export function gearOutline({ m, z, pa = 20*Math.PI/180, backlash = 0, flank = 8 }) {
  const rp = m*z/2, rb = rp*Math.cos(pa), ra = rp + m, rf = Math.max(rp - 1.25*m, 0.3*rp);
  const half = Math.PI/(2*z) - backlash/(2*rp);
  const fa = r => half + inv(pa) - (r > rb ? inv(Math.acos(rb/r)) : 0);   // flank angle from tooth centreline
  const solve = (want, lo, hi) => { for (let i = 0; i < 60; i++) { const mid = (lo+hi)/2; fa(mid) > want ? lo = mid : hi = mid; } return (lo+hi)/2; };
  const pitchAng = 2*Math.PI/z;
  let r0 = Math.max(rb, rf);
  if (fa(r0) > pitchAng/2 - 0.02) r0 = solve(pitchAng/2 - 0.02, r0, rp);   // keep some root arc
  let r1 = ra; const land = 0.2*m*0.5/ra;
  if (fa(ra) < land) r1 = solve(land, rp, ra);                               // keep a top land
  const P = (r, a) => [r*Math.cos(a), r*Math.sin(a)], out = [];
  const drop = r0 > rf + 1e-9, a0 = fa(r0), a1 = fa(r1);
  for (let k = 0; k < z; k++) {
    const c = pitchAng*k;
    if (drop) out.push(P(rf, c - a0));
    for (let i = 0; i < flank; i++) { const r = r0 + (r1-r0)*i/(flank-1); out.push(P(r, c - fa(r))); }
    for (let i = 1; i <= 3; i++) out.push(P(r1, c - a1 + 2*a1*i/4));
    for (let i = flank-1; i >= 0; i--) { const r = r0 + (r1-r0)*i/(flank-1); out.push(P(r, c + fa(r))); }
    if (drop) out.push(P(rf, c + a0));
    for (let i = 1; i <= 4; i++) out.push(P(rf, c + a0 + (pitchAng - 2*a0)*i/5));
  }
  return out;   // closed CCW polygon, one tooth centred on +x
}
```
*Adapt:* the root-radius floor (`0.3*rp`) is a stand-in; Linkage-Design's own clamp wasn't copied. Rotate the second gear by half a pitch to mesh. For **clockwork-style** wheels and pinions (cycloidal or Belot teeth, low pinion counts like 6–8 leaves), see hdrpano/watchmaking; involute is fine for printed and laser-cut automata.

### 4. mm-true, kerf-compensated SVG export pattern
*source_url:* https://github.com/1400130-collab/gearforge/blob/main/src/exporters.js · *license:* MIT · *reuse_risk:* ok

```js
// Pattern adapted from 1400130-collab/gearforge (MIT).
export function toSVG(loops, { margin = 2 } = {}) {         // loops: [[x,y],...] in mm, already kerf-offset
  const xs = loops.flat().map(p => p[0]), ys = loops.flat().map(p => p[1]);
  const minX = Math.min(...xs), maxY = Math.max(...ys);
  const w = Math.max(...xs) - minX + 2*margin, h = maxY - Math.min(...ys) + 2*margin;
  const f = v => (Math.round(v*1e4)/1e4).toString();
  const d = l => 'M ' + l.map(([x, y]) => `${f(x - minX + margin)} ${f(maxY - y + margin)}`).join(' L ') + ' Z';
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${f(w)}mm" height="${f(h)}mm" viewBox="0 0 ${f(w)} ${f(h)}">
  <g id="CUT" fill="none" stroke="#ff0000" stroke-width="0.1">${loops.map(l => `<path d="${d(l)}"/>`).join('')}</g>
</svg>`;
}
```
*Adapt:* offset outer loops by +kerf/2 and holes by −kerf/2 before calling this. Add an `ENGRAVE` group (blue) for pitch circles and labels. DXF R12 is the same loops written as `POLYLINE`/`VERTEX`/`SEQEND`.

### Withheld (no or unclear license, so ideas only)

- **CamFollowerJS.** Idea worth taking: author the cam as a **flat displacement chart** (x = cam angle, y = lift), which is how automata makers sketch, then wrap it to polar. Edit points with the mouse and save the cam as JSON.
- **clock-gear-train-calculator.** Idea: brute-force tooth counts per shaft (wheel on the first shaft, wheel and pinion on the middle shafts, pinion on the last) and keep the combinations whose product of ratios hits the target within tolerance.
- **chrisspen/gears.** Idea: OpenSCAD modules for spur, bevel, worm and rack parts. Bevel gears are what turn an automaton's motion through 90°.

## Sources worth reading

- Disney Research, *Computational Design of Mechanical Characters* (2013): paper and video, linked from n-nagaya's README.
- `docs/` in CamFollowerJS: *Computer-Aided Design of Mechanical Automata* (PDF).
- KHK Gears, *Basic Gear Terminology and Calculation*, mirrored in dpellegr/PolyGear `docs/`.
