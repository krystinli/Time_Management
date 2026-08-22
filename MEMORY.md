# Repository Memory

This file records durable context and working notes for the Time Management repository.

## Data workflow

- The primary daily dataset is `data/data2.csv`.
- Columns are `Date`, `Day`, `Work`, `Development`, `Self-Care`, and `Others`.
- `Work`, `Development`, and `Self-Care` are daily hour totals.
- Inputs for those three columns are additive unless explicitly described as replacements or corrections.
- After each new input, report today's provisional totals together with the five most recent recorded days.
- At 9:00 PM America/Toronto time, ask for missing values and confirmation of the final daily totals.
- Do not write, commit, or push provisional totals before confirmation.
- After confirmation, append or correct today's row, validate the CSV, stage only `data/data2.csv`, commit with `update time`, and push `main` to `origin`.
- Do not commit local artifacts such as `.idea/` or `plotting/__pycache__/`.

## Flexible `Others` column

- `Others` is a flexible, non-additive field whose meaning can change between tracking periods.
- In the current tracking period, it represents weight in pounds.
- If no new value is supplied, carry forward the most recent recorded value.
- When a new value is supplied, replace the carried-forward value rather than adding to it.
- Label it as `Others (weight lb)` in summaries while retaining `Others` as the CSV header.

## Notes log

### 2026-08-22

- Created this repository memory file.
- Today's provisional Development total is `1.0` hour.
- Today's `Others` value is `150` lb, carried forward from the previous day.
- The other values currently recorded for today in the CSV are Work `0.0` and Self-Care `0.0`.
