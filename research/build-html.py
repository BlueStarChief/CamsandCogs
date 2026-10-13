#!/usr/bin/env python3
"""Render similar-repos.md (+ flows.fragment.html) into a standalone similar-repos.html.

The Markdown is the source of truth; never hand-edit the HTML.
Needs: pip install markdown
Run:   python3 research/build-html.py
"""
import pathlib
import markdown

HERE = pathlib.Path(__file__).parent
md = (HERE / "similar-repos.md").read_text()
flows = (HERE / "flows.fragment.html").read_text()

body = markdown.markdown(md, extensions=["tables", "fenced_code"])
# Drop the flow diagrams in right before the "Best practices to copy" heading.
marker = '<h3>Best practices to copy</h3>'
body = body.replace(marker, flows + "\n" + marker, 1) if marker in body else body + flows

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Automata Prior Art</title>
<style>
:root {{
  --bg:#0f0f13; --text:#e8eaf0; --accent:#ffc850; --border:rgba(255,200,80,0.2);
  --success:#56c47d; --blue:#4f9cf9; --red:#ff6b6b; --orange:#ff9f43;
  --muted:rgba(255,255,255,0.55); --code-bg:rgba(255,255,255,0.05);
}}
* {{ box-sizing:border-box; }}
body {{ background:var(--bg); color:var(--text); font:15px/1.6 system-ui,-apple-system,sans-serif;
  max-width:1000px; margin:0 auto; padding:24px 16px 80px; }}
h1 {{ color:var(--accent); font-size:1.7rem; line-height:1.25; }}
h2 {{ color:var(--accent); border-bottom:1px solid var(--border); padding-bottom:.3rem; margin-top:2.4rem; }}
h3 {{ color:var(--text); margin-top:1.8rem; }}
a {{ color:var(--blue); }}
code {{ background:var(--code-bg); padding:.1rem .3rem; border-radius:4px; font-size:.88em; }}
pre {{ background:var(--code-bg); border:1px solid var(--border); border-radius:8px; padding:12px; overflow-x:auto; }}
pre code {{ background:none; padding:0; }}
table {{ border-collapse:collapse; width:100%; display:block; overflow-x:auto; font-size:.9rem; }}
th,td {{ border:1px solid var(--border); padding:.4rem .6rem; text-align:left; vertical-align:top; }}
th {{ background:rgba(255,200,80,0.08); }}
.flow-section {{ overflow-x:auto; }}
.flow-section svg {{ display:block; margin:0 auto; max-width:100%; height:auto; }}
.flow-tabs {{ display:flex; gap:4px; margin-bottom:1rem; flex-wrap:wrap; }}
.flow-tab {{ padding:.4rem 1rem; border-radius:8px; border:1px solid var(--border); background:transparent;
  color:var(--muted); cursor:pointer; font-size:.85rem; font-family:inherit; }}
.flow-tab.active {{ background:var(--accent); color:var(--bg); border-color:var(--accent); font-weight:600; }}
.flow-panel {{ display:none; }}
.flow-panel.active {{ display:block; }}
.flag-list {{ list-style:none; display:flex; flex-direction:column; gap:.5rem; margin-top:.75rem; padding:0; }}
.flag-list li {{ padding:.5rem .75rem; border-radius:6px; font-size:.9rem; }}
.flag-list li.issue {{ background:rgba(255,107,107,0.08); border-left:3px solid var(--red); }}
.flag-list li.unclear {{ background:rgba(255,159,67,0.08); border-left:3px solid var(--orange); }}
.flag-list li.ok {{ background:rgba(86,196,125,0.06); border-left:3px solid var(--success); }}
.flag-label {{ font-weight:600; font-size:.75rem; text-transform:uppercase; letter-spacing:.5px; margin-right:.5rem; }}
.flag-label.issue {{ color:var(--red); }} .flag-label.unclear {{ color:var(--orange); }} .flag-label.ok {{ color:var(--success); }}
</style>
</head>
<body>
{body}
<script>
function showFlow(id) {{
  document.querySelectorAll('.flow-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.flow-tab').forEach(t => t.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  event.target.classList.add('active');
}}
</script>
</body>
</html>
"""
(HERE / "similar-repos.html").write_text(html)
print("wrote", HERE / "similar-repos.html")
