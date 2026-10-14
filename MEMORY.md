# Repository Memory

This file records durable context and working notes for the Time Management repository.

## Data workflow

- The primary daily dataset is `data/data2.csv`.
- Columns are `Date`, `Day`, `Work`, `Development`, `Self-Care`, and `Others`.
- `Work`, `Development`, and `Self-Care` are daily hour totals.
- Inputs for those three columns are additive unless explicitly described as replacements or corrections.
- Treat any missing `Work`, `Development`, or `Self-Care` value as `0.0` unless the user later supplies a value or correction.
- After each new input, report today's provisional totals together with the five most recent recorded days.
- At 9:00 PM America/Toronto time, show any assumed zeros and ask for confirmation of the final daily totals.
- Do not write, commit, or push provisional totals before confirmation.
- After confirmation, append or correct today's row and validate the CSV.
- Never create or update future-dated rows. Record today only using the current America/Toronto date, or a past date explicitly named by the user.
- Run `python3 run.py` from the repository root to refresh the tracked charts under `img/`.
- Verify that `run.py` completes successfully, revalidate `data/data2.csv`, and review the generated image changes.
- Stage `data/data2.csv` together with only the tracked image files changed by `run.py`, commit them in one `update time` commit, and push `main` to `origin`.
- Do not commit local artifacts such as `.idea/` or `plotting/__pycache__/`.

## Flexible `Others` column

- `Others` is a flexible, non-additive field whose meaning can change between tracking periods.
- In the current tracking period, it represents weight in pounds.
- If no new value is supplied, carry forward the most recent recorded value.
- When a new value is supplied, replace the carried-forward value rather than adding to it.
- Label it as `Others (weight lb)` in summaries while retaining `Others` as the CSV header.

## Notes log

### 2026-10-13 — Complete time-log updates

- Read this memory before updating the time log. The user explicitly wants every update to include the related charts; updating the CSV alone is incomplete.
- After saving new or corrected hours, regenerate all 10 current time-tracking charts in `img/`: `work_plot.png`, `work_plot_monthly.png`, `dev_plot.png`, `dev_plot_monthly.png`, `care_plot.png`, `care_plot_monthly.png`, `total_plot.png`, `total_plot_daily.png`, `total_plot_monthly.png`, and `work_plot_weekly.png`.
- Validate the saved dates and hours, confirm chart generation succeeds, and inspect the refreshed charts against the newest recorded entries before reporting completion.
- When the user requests a commit and push, include the updated dataset and refreshed charts together. Check the diff before committing and verify the push succeeds; never report a CSV-only push as a complete update.
- Use a Python environment with pandas, numpy, and matplotlib. `/opt/anaconda3/bin/python` successfully generated the charts on this date. Disable bytecode writes to avoid changing tracked cache files.
- Preserve the recorded dates when refreshing charts; do not invent missing-day entries or add future dates. Historical 2022 charts and journal illustrations need refreshing only when their underlying content changes or the user requests it.

### 2026-08-22

- Created this repository memory file.
- Today's provisional Development total is `1.0` hour.
- Today's `Others` value is `150` lb, carried forward from the previous day.
- The other values currently recorded for today in the CSV are Work `0.0` and Self-Care `0.0`.
