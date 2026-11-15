# Day 45 – Hacker News Headlines Scraper (BeautifulSoup)

A command-line app that scrapes the top 30 headlines from the Hacker News front page.

## Features
- Fetches the live Hacker News front page with requests
- Parses the HTML with BeautifulSoup and finds every headline (`span.titleline`)
- Prints the headlines numbered 1–30
- Handles no internet, slow server and bad status codes

## How to run
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python hn_headline.py`

## Scraping politely
- Checked https://news.ycombinator.com/robots.txt first – the front page is allowed
- The site asks for a 30-second crawl delay, so the app makes only one request per run

## What I learned
- APIs send JSON for programs; normal pages send HTML for humans – scraping reads the HTML
- Find the right tag and class with View Source (Ctrl + U) or Inspect before coding
- `BeautifulSoup(response.text, "html.parser")`, `find_all("span", class_="titleline")`, `.text`
- `class_` has an underscore because `class` is a Python keyword
- Install name `beautifulsoup4`, import name `bs4`