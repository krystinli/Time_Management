# Time Management Project Instructions

## Updating `recent_trend.md`

When the user says “update `recent_trend.md`”:

1. Read the latest entries from `data/data2.csv` and use the newest recorded date as the report cutoff.
2. Compare the current month-to-date with the previous calendar month. Do not compare partial-month totals directly.
3. Normalize the comparison for weekday/weekend mix using:

   `normalized week = 5 × average weekday hours + 2 × average weekend hours`

4. Analyze Work, Development, Self-Care, and Total at a high level. Include:
   - weekday versus weekend averages;
   - category mix and how it changed month over month;
   - performance against the current weekday/weekend targets in `run.py`;
   - momentum across complete recent ISO weeks.
5. Write in a warm, casual, second-person voice for a personal reflection. Prefer language such as “You did lots of Development this month” over business terms such as “capacity,” “allocation,” “executive view,” or “operating pace.”
6. Keep the numbers accurate but explain them simply. Make the main story and one gentle thing to notice easy to scan.
7. Create or refresh a cozy personal-journal-style illustration for the month and embed it near the top of the report. Use a symbolic character unless the user supplies a reference photo; do not claim a generated character is a literal likeness.
8. Preserve the report and image in the repository, validate Markdown links and calculations, and do not commit or push unless the user explicitly asks.
