---
name: daily_time_update
description: >-
  Updates Time_Management daily time tracking by appending today’s row to
  `data2.csv` (asks for your actual Work/Development/Self-Care values while
  copying `Others` from the last row), running `run.py` to regenerate plots, then committing and
  pushing changes and opening a PR. Use when the user asks to add “today’s
  entry” or “update data2.csv daily” for Time_Management.
---

# Daily Time Update (Time_Management)

## Summary of the workflow

1. Detect today’s date and weekday.
2. Check the last recorded date in `Time_Management/data/data2.csv`.
3. If today is missing, append a new CSV row:
   - Ask the user for the actual `Work/Development/Self-Care` hours for today
   - `Others` copied from the last existing row
4. Run `Time_Management/run.py` to pad any missing dates up to today and regenerate plots under `Time_Management/img/`.
5. Review the diff to ensure only the intended recent rows and plot PNGs changed.
6. Commit the CSV + updated PNGs, push a branch, and open a PR.

## Step-by-step instructions

### 1) Identify paths and repo
- CSV: `Time_Management/data/data2.csv`
- Script: `Time_Management/run.py`
- Plots output: `Time_Management/img/`

### 2) Get today + weekday
- Use the system date (local to the machine running the agent).

### 3) Check whether today already exists
- Read the last row from `data2.csv` (by `Date` column) and compare to today.
- If today exists, do not append a new row; continue to step 4 only if plots are stale.

### 4) Append today’s entry (user’s rule)
Before appending, request your actual daily record:

- `Work` hours for today
- `Development` hours for today
- `Self-Care` hours for today

Append exactly one new row (unless multiple days are missing and you choose to let `run.py` pad them):

`YYYY-MM-DD,Weekday,<Work>,<Development>,<Self-Care>,<Others_from_last_row>`

### 5) Run the plot pipeline
- From `Time_Management/`, run:
  - `python run.py`

If `run.py` fails due to OpenMP / matplotlib environment errors (for example “OMP: Error #178 … Operation not permitted”), rerun in a normal environment where those libraries can access required shared memory, then continue.

### 6) Verify changes before committing
- Confirm the modified files are:
  - `Time_Management/data/data2.csv`
  - plot PNGs under `Time_Management/img/`
- Run a `git diff` review for `data2.csv` to confirm the edits are limited to the newest dates.
- If older historical rows changed unexpectedly, stop and ask the user what values should be kept.

### 7) Commit + push
- Create a branch name like:
  - `chore/daily-time-update-YYYY-MM-DD`
- Stage only:
  - `Time_Management/data/data2.csv`
  - updated PNGs under `Time_Management/img/`
- Do NOT commit:
  - `__pycache__/`
  - `.DS_Store`

### 8) Open a PR
- If `gh` is available, use it to create a PR.
- Otherwise, use the browser URL pattern:
  - `https://github.com/<owner>/<repo>/pull/new/<branch>`

## Example

User request: “add today’s entry”
Agent behavior:
1. Detect today is `2026-03-25, Wednesday`.
2. Read last row `2026-03-24, Tuesday` and see today is missing.
3. Ask for today’s `Work/Development/Self-Care` hours, then append:
   `2026-03-25,Wednesday,<Work>,<Development>,<Self-Care>,<Others_last>`.
4. Run `python run.py`, review `git diff`, commit CSV + PNGs, push branch, open PR.

