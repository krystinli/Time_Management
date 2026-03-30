---
name: daily_time_update
description: >-
  Updates Time_Management time tracking by padding `data2.csv` with placeholder
  rows for every missing calendar day through today (Work/Development/Self-Care =
  0, Others copied from the last existing row) so the user can enter real hours
  in the file or in chat, then runs `run.py`, regenerates plots, commits, pushes,
  and opens a PR when requested. Use for “today’s entry”, “daily time update”, or
  “update data2.csv daily” for Time_Management.
---

# Daily Time Update (Time_Management)

## Summary of the workflow

1. Detect today’s date (local system).
2. Read `max(Date)` from `Time_Management/data/data2.csv`.
3. If `max(Date) < today`, append **one row per missing calendar day** from `max(Date)+1` through `today` using **placeholders** (see below). If the user asks to “add rows first so I can type hours”, do **only** this step and stop until they are done editing or say to continue.
4. After real `Work` / `Development` / `Self-Care` values are set (manual edit or user message), run `Time_Management/run.py` to refresh plots under `Time_Management/img/`.
5. Review `git diff` so only the intended recent rows and plot PNGs changed.
6. Commit `data/data2.csv` + updated PNGs, push a branch, open a PR (or give the compare URL if `gh` is missing).

## Placeholder rows (default)

For each missing date `d` through today:

`YYYY-MM-DD,<Weekday>,0.0,0.0,0.0,<Others_last>`

- `<Others_last>` is the `Others` value from the **last data row before the gap** (use the same value for every new row unless the user specifies otherwise).
- Weekday must match the calendar `d` (`Monday` … `Sunday`).

## After placeholders

- The user fills in actual hours in `data2.csv`, **or** paste them in chat and the agent updates those cells.
- Then run `python run.py`, verify diffs, commit, push, PR.

## Alternative: chat-first

If the user already provides `Work` / `Development` / `Self-Care` for each missing day, append those values directly and skip placeholders.

## Step-by-step instructions

### 1) Paths

- CSV: `Time_Management/data/data2.csv`
- Script: `Time_Management/run.py`
- Plots: `Time_Management/img/`

### 2) Gap check

- If `max(Date) >= today`, nothing to append; only run `run.py` / commit if plots or data still need refresh.

### 3) Append missing days

- Append placeholder rows as above for the full range through today.
- If multiple days are missing, append **all** of them in one edit (continuous dates).

### 4) Plot pipeline

- From `Time_Management/`: `python run.py`

If OpenMP/matplotlib errors appear (e.g. `OMP: Error #178`), rerun outside a restricted sandbox.

### 5) Verify before commit

- Expect changes in `data/data2.csv` and selected PNGs under `img/`.
- If older history rows changed unexpectedly, stop and ask the user.

### 6) Commit + push

- Branch name e.g. `chore/daily-time-update-YYYY-MM-DD`
- Stage only `data/data2.csv` and updated `img/*.png`
- Do **not** commit `__pycache__/`, `.DS_Store`

### 7) PR

- `gh pr create` if available; else `https://github.com/<owner>/<repo>/pull/new/<branch>`

## Example

User: “daily time update — add rows first so I can enter inputs”

1. Last row `2026-03-25`; today `2026-03-29`; `Others` was `149`.
2. Append `2026-03-26` … `2026-03-29` each as `0.0,0.0,0.0,149`.
3. Wait for user to edit hours.
4. User says “done” → run `run.py` → commit CSV + PNGs → push → PR.
