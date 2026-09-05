#!/usr/bin/env python3
"""Render context/code/hypridplanner-analysis.md to a self-contained HTML page.

SVG figures are inlined, captions are styled, tables are wrapped in a scroll
container, and a verdict cell that is exactly one bold phrase becomes a pill.
"""
import io
import os
import re
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "context", "code", "hypridplanner-analysis.md")
OUT = os.path.join(ROOT, "context", "code", "hypridplanner-analysis.html")
FIGDIR = os.path.join(ROOT, "context", "code")

HEAD = """<title>hypridplanner on main</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{--bg:#f6f7f9;--surface:#ffffff;--ink:#1a1d24;--ink-2:#4b5160;--ink-3:#7a8090;--rule:#d9dce3;--accent:#4338ca;--accent-soft:#e8e7fb;--hold:#15803d;--hold-bg:#e7f5ec;--diff:#b45309;--diff-bg:#fbeedd;--miss:#b91c1c;--miss-bg:#fbe5e5;--open:#4b5160;--open-bg:#e9ebef;--code-bg:#eceef3;--table-head:#eef0f4}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#15171c;--surface:#1d2026;--ink:#e6e8ee;--ink-2:#b7bcc9;--ink-3:#868c9b;--rule:#343946;--accent:#a5a0ff;--accent-soft:#2a2a4a;--hold:#7cd39a;--hold-bg:#1c3326;--diff:#f2b56b;--diff-bg:#3a2a16;--miss:#f39a9a;--miss-bg:#3d1c1c;--open:#b7bcc9;--open-bg:#2a2e38;--code-bg:#262a33;--table-head:#252932}}
:root[data-theme="dark"]{--bg:#15171c;--surface:#1d2026;--ink:#e6e8ee;--ink-2:#b7bcc9;--ink-3:#868c9b;--rule:#343946;--accent:#a5a0ff;--accent-soft:#2a2a4a;--hold:#7cd39a;--hold-bg:#1c3326;--diff:#f2b56b;--diff-bg:#3a2a16;--miss:#f39a9a;--miss-bg:#3d1c1c;--open:#b7bcc9;--open-bg:#2a2e38;--code-bg:#262a33;--table-head:#252932}
body{background:var(--bg);color:var(--ink);font-family:"Source Sans 3","Segoe UI",system-ui,sans-serif;font-size:16.5px;line-height:1.55;margin:0}
.wrap{display:grid;grid-template-columns:230px minmax(0,1fr);gap:40px;max-width:1240px;margin:0 auto;padding:36px 28px 80px}
@media (max-width:900px){.wrap{grid-template-columns:minmax(0,1fr)}.rail{position:static;max-height:none}}
.rail{position:sticky;top:20px;align-self:start;max-height:calc(100vh - 40px);overflow:auto;font-size:13.5px;line-height:1.45}
.rail .toc>ul{list-style:none;padding:0;margin:0}.rail ul ul{display:none}.rail li{margin:0 0 6px}.rail a{color:var(--ink-2);text-decoration:none}.rail a:hover,.rail a:focus{color:var(--accent);text-decoration:underline}
.rail .eyebrow{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);margin:0 0 10px}
header.masthead{border-bottom:1px solid var(--rule);padding-bottom:22px;margin-bottom:28px}
h1{font-family:Newsreader,Georgia,serif;font-weight:500;font-size:2.2rem;line-height:1.15;margin:0 0 10px;text-wrap:balance;letter-spacing:-.01em}
.sub{color:var(--ink-2);font-size:15.5px;max-width:70ch;margin:0}
.meta{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:14px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12.5px;color:var(--ink-3)}
.meta b{color:var(--ink-2);font-weight:500}
main{min-width:0}main>*{max-width:76ch}main>.table-scroll,main>.fig-scroll,main>hr{max-width:none}
h2{font-family:Newsreader,Georgia,serif;font-weight:500;font-size:1.65rem;margin:52px 0 12px;line-height:1.2;text-wrap:balance}
h3{font-size:1.05rem;font-weight:600;margin:32px 0 8px;letter-spacing:.005em}
p{margin:0 0 14px}li{margin:0 0 6px}ol,ul{padding-left:1.3em}
hr{border:0;border-top:1px solid var(--rule);margin:44px 0}
code{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.86em;background:var(--code-bg);padding:.08em .32em;border-radius:3px}
strong{font-weight:600}
.table-scroll{overflow-x:auto;margin:16px 0 22px;border:1px solid var(--rule);border-radius:4px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:14.5px;line-height:1.45}
th{background:var(--table-head);text-align:left;font-weight:600;padding:9px 12px;border-bottom:1px solid var(--rule);white-space:nowrap}
td{padding:9px 12px;border-top:1px solid var(--rule);vertical-align:top}
td:first-child{min-width:14ch}
.verdict{display:inline-block;font-size:12.5px;font-weight:600;line-height:1.35;padding:2px 8px;border-radius:999px;white-space:normal}
.verdict.hold{color:var(--hold);background:var(--hold-bg)}.verdict.diff{color:var(--diff);background:var(--diff-bg)}.verdict.miss{color:var(--miss);background:var(--miss-bg)}.verdict.open,.verdict.mix{color:var(--open);background:var(--open-bg)}
.fig-scroll{overflow-x:auto;margin:22px 0 8px;padding:14px;background:var(--surface);border:1px solid var(--rule);border-radius:4px}
.fig-scroll svg{display:block;max-width:none;height:auto}
.fig-scroll svg text{font-family:"Source Sans 3",Helvetica,Arial,sans-serif}
p.caption{font-size:14px;color:var(--ink-2);margin:0 0 26px;max-width:76ch}p.caption .fignum{font-weight:600;color:var(--ink);margin-right:6px}
a{color:var(--accent)}
.legend{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto}}
</style>
"""

MASTHEAD = """<header class="masthead"><h1>The study planner as it stands on <code>main</code> of hypridplanner</h1>
<p class="sub">A description of the code, written from the code, to check the thesis's claims against and to compare with Chapter 7. Verdict pills in section 4: <span class="verdict hold">holds</span> <span class="verdict diff">differs</span> <span class="verdict miss">not on main</span> <span class="verdict open">cannot be settled here</span>.</p>
<div class="meta"><span><b>repo</b> morischumacher/hypridplanner</span><span><b>branch</b> main</span><span><b>commit</b> c00ef4f &middot; 2026-09-01</span><span><b>read</b> 2026-09-05</span></div></header>
"""


def verdict_class(text):
    t = re.sub(r"<[^>]+>", "", text).strip().lower()
    if t.startswith("holds"):
        return "hold"
    if t.startswith("differs"):
        return "diff"
    if t.startswith("not on main") or t.startswith("absent"):
        return "miss"
    if t.startswith("cannot") or t.startswith("open"):
        return "open"
    return "mix"


def main():
    text = io.open(SRC, encoding="utf-8").read()

    # Drop the title line and the standfirst; the masthead carries both.
    lines = text.split("\n")
    assert lines[0].startswith("# ")
    body = "\n".join(lines[1:]).lstrip("\n")
    body = body.split("\n", 1)[1].lstrip("\n") if body.startswith("A description of the code") else body

    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    html = md.convert(body)

    # Inline the SVG figures.
    def inline_fig(m):
        alt, path = m.group(1), m.group(2)
        svg = io.open(os.path.join(FIGDIR, path), encoding="utf-8").read()
        svg = re.sub(r"^<\?xml[^>]*\?>\s*", "", svg)
        svg = re.sub(r"^<!DOCTYPE[^>]*>\s*", "", svg)
        return ('<div class="fig-scroll" role="img" aria-label="%s">\n%s\n</div>' % (alt, svg))

    html = re.sub(r'<img alt="([^"]*)" src="([^"]+\.svg)"\s*/?>', inline_fig, html)
    html = re.sub(r"<p>(<div class=\"fig-scroll\".*?</div>)</p>", r"\1", html, flags=re.S)

    # Captions: an italic paragraph beginning "Figure N."
    def caption(m):
        inner = m.group(1)
        n = re.match(r"(Figure\s+\d+\.)\s*(.*)$", inner, flags=re.S)
        if not n:
            return m.group(0)
        return '<p class="caption"><span class="fignum">%s</span> %s</p>' % (n.group(1), n.group(2))

    html = re.sub(r"<p><em>(Figure\s+\d+\..*?)</em></p>", caption, html, flags=re.S)

    # Verdict pills: a cell that is exactly one bold phrase.
    def pill(m):
        inner = m.group(1)
        return '<td><span class="verdict %s">%s</span></td>' % (verdict_class(inner), inner)

    html = re.sub(r"<td><strong>([^<]*(?:<code>[^<]*</code>[^<]*)*)</strong></td>", pill, html)

    html = re.sub(r"(<table>.*?</table>)", r'<div class="table-scroll">\1</div>', html, flags=re.S)

    toc = md.toc
    out = (HEAD + '<div class="wrap"><nav class="rail"><p class="eyebrow">Contents</p>'
           + toc + "</nav><main>\n" + MASTHEAD + html + "\n</main></div>\n")
    io.open(OUT, "w", encoding="utf-8").write(out)
    print("wrote %s (%d bytes, %d table rows, %d figures)"
          % (os.path.relpath(OUT, ROOT), len(out), out.count("<tr>"), out.count('class="fig-scroll"')))


if __name__ == "__main__":
    sys.exit(main())
