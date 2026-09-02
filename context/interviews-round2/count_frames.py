#!/usr/bin/env python3
"""Definitive frame count and process metrics for the evaluation study.

Point it at the stage-log folder:

    python3 count_frames.py /path/to/evaluation-study/analysis/stage-logs

Why this exists. Three different totals for the same labelled record were in
circulation: 2,158 in the thesis text and appendix, 2,157 in Table 8.2 and in
`analysis/process-metrics.md`, and 2,192 from an independent re-parse during the
2026-08-31 review. All three were wrong, in three different ways, and the reasons
are worth recording because each is a parsing decision rather than a labelling
disagreement.

  * The row pattern. `process-figures/compute_process_metrics.py` matches a frame
    row on a 3-to-4-digit timestamp (`\\d{3,4}`). P1-A and P1-B write their first
    ten timestamps without zero padding (`0`, `10`, ... `90`), so twenty genuine
    frames, ten in each run, were never counted.

  * Rows that are not frames. The stage-log files also contain analysis tables
    whose first column is a number (episode indices, lane listings). A pattern
    loose enough to catch the unpadded timestamps also catches seventeen of these.
    They are excluded here by requiring the surface column to name an actual
    surface, which is what the original script's `normalise_surface` already did.

  * One stray row. P5-B contains a per-semester lane listing whose first cell
    reads `0800`, so it matches the frame pattern on any reading. Its surface cell
    is `Semester 7`, so the surface check drops it. Counting it is where the
    thesis's 2,158 comes from: 2,157 plus that row.

Taking the union of the two fixes, the count is what this script prints. Nothing
here changes a single label; it changes which rows are read as labelled frames.
"""

import collections
import glob
import json
import os
import re
import statistics as st
import sys

SURFACES = {"guide", "quest", "auth", "load", "table", "graph", "other"}

# Any leading integer, so the unpadded timestamps in P1-A and P1-B are seen.
ROW = re.compile(r"^\s*\|?\s*(\d+)\s*\|(.*)$")


def normalise_surface(cell):
    """Map a surface cell onto one of SURFACES, or None if it is not one."""
    s = cell.strip().replace("**", "").replace("`", "").lower()
    s = re.sub(r"\(.*?\)", "", s)
    s = s.split("/")[0].strip()
    for known in SURFACES:
        if s.startswith(known):
            return known
    return None


def parse_run(paths):
    """Frames of one scenario run, deduplicated by timestamp across chunk files."""
    rows = []
    for path in sorted(paths):
        for line in open(path, errors="ignore"):
            m = ROW.match(line)
            if not m:
                continue
            cells = [c.strip() for c in m.group(2).split("|")]
            if len(cells) < 3:
                continue
            surface = normalise_surface(cells[0])
            if not surface:          # an analysis-table row, not a frame
                continue
            rows.append(
                {
                    "t": int(m.group(1)),
                    "surface": surface,
                    "sidebar": cells[1].lower(),
                    "panels": cells[2].lower(),
                }
            )
    seen, out = set(), []
    for r in sorted(rows, key=lambda x: x["t"]):
        if r["t"] in seen:
            continue
        seen.add(r["t"])
        out.append(r)
    return out


def load_runs(logs_dir):
    groups = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(logs_dir, "P*.md"))):
        m = re.match(r"P(\d+)-([AB])", os.path.basename(f))
        if m:
            groups["P%02d-%s" % (int(m.group(1)), m.group(2))].append(f)
    return {k: parse_run(v) for k, v in sorted(groups.items())}


def state(row):
    """The compound process state: the dashboard coexists with the table."""
    s = row["surface"]
    if s == "graph":
        return "GRAPH"
    if s != "table":
        return "OFF"
    dash = "dash" in row["panels"]
    cat = re.search(r"\bcat\b", row["sidebar"]) is not None
    if dash and cat:
        return "DASH+CAT"
    if dash:
        return "DASH"
    if cat:
        return "CAT"
    return "TABLE"


ORDER = ["DASH+CAT", "CAT", "GRAPH", "DASH", "TABLE", "OFF"]


def condition_stats(runs, keys):
    occ, entries, trans = collections.Counter(), collections.Counter(), collections.Counter()
    dwells = collections.defaultdict(list)
    recs_frames = 0
    for k in keys:
        rows = runs[k]
        seq = [state(r) for r in rows]
        occ.update(seq)
        recs_frames += sum(1 for r in rows if "recs" in r["panels"] or "recs" in r["sidebar"])
        entries[seq[0]] += 1
        cur, run_len = seq[0], 1
        for a, b in zip(seq, seq[1:]):
            if a != b:
                trans[(a, b)] += 1
                entries[b] += 1
                dwells[cur].append(run_len)
                cur, run_len = b, 1
            else:
                run_len += 1
        dwells[cur].append(run_len)
    n = sum(occ.values())
    total_trans = sum(trans.values())
    return {
        "frames": n,
        "runs": len(keys),
        "occupancy": {s: round(100 * occ[s] / n, 1) for s in ORDER if occ[s]},
        "entries": {s: entries[s] for s in ORDER if occ[s]},
        "dwell_s": {s: round(10 * st.mean(dwells[s])) for s in ORDER if dwells[s]},
        "transition_share_pct": {
            "%s->%s" % t: round(100 * c / total_trans, 1) for t, c in trans.most_common(6)
        },
        "transitions_total": total_trans,
        "recs_occupancy_pct": round(100 * recs_frames / n, 1),
    }


def main():
    logs_dir = sys.argv[1] if len(sys.argv) > 1 else "stage-logs"
    runs = load_runs(logs_dir)
    if not runs:
        raise SystemExit(f"no stage-log files found in {logs_dir!r}")

    a = sorted(k for k in runs if k.endswith("-A"))
    b = sorted(k for k in runs if k.endswith("-B"))
    total = sum(len(v) for v in runs.values())

    print(f"TOTAL LABELLED FRAMES: {total} across {len(runs)} runs")
    print(f"  Scenario A: {sum(len(runs[k]) for k in a)} frames, {len(a)} runs")
    print(f"  Scenario B: {sum(len(runs[k]) for k in b)} frames, {len(b)} runs")
    print()
    for label, keys in (("A", a), ("B", b)):
        s = condition_stats(runs, keys)
        print(f"=== Scenario {label} ({s['runs']} runs, {s['frames']} frames)")
        print(f"{'state':10s} {'occ %':>6s} {'entries':>8s} {'dwell s':>8s}")
        for st_name in ORDER:
            if st_name in s["occupancy"]:
                print(
                    f"{st_name:10s} {s['occupancy'][st_name]:6.1f} "
                    f"{s['entries'][st_name]:8d} {s['dwell_s'][st_name]:8d}"
                )
        print(f"  recommendation panel open: {s['recs_occupancy_pct']} % of frames")
        print(f"  transitions: {s['transitions_total']}")
        for name, share in s["transition_share_pct"].items():
            print(f"    {name:26s} {share:5.1f} %")
        print()

    per_run = {k: len(v) for k, v in runs.items()}
    out = {
        "total_frames": total,
        "runs": len(runs),
        "frames_per_run": per_run,
        "scenario_A": condition_stats(runs, a),
        "scenario_B": condition_stats(runs, b),
    }
    dest = os.path.join(os.path.dirname(os.path.abspath(logs_dir)), "frame-count.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"written: {dest}")


if __name__ == "__main__":
    main()
