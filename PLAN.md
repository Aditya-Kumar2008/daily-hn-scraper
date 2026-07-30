# Project: daily-hacker-news-scraper

## Problem
Developers often want to demonstrate a highly active GitHub profile (the "green Christmas tree"), but maintaining daily commits manually is impossible. Concurrently, keeping track of top tech trends requires checking Hacker News daily. 

## Solution
A Python script orchestrated by a GitHub Actions Cron Job. It runs every day at 8 AM UTC, fetches the top 10 stories from the Hacker News API, formats them into a neat Markdown file (`README.md` or a daily log), and automatically commits and pushes the changes back to the repository.

## Target User
Aditya (to automate his "premium tech boy" GitHub activity) and anyone who wants an automated daily digest of HN.

## Architecture
- **Language**: Python (for simple, robust scripting).
- **API**: Hacker News Firebase API.
- **Automation**: GitHub Actions (`schedule: - cron: '0 8 * * *'`).

## MVP Scope
- Python script `scraper.py` that queries HN.
- Generates a markdown file `DAILY_DIGEST.md` with links and scores.
- `.github/workflows/cron.yml` to trigger the script and commit the changes using the generic auto-merge identity.
