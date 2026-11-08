# Day 42 – GitHub Profile Viewer (requests)

A command-line app that fetches any GitHub user's public profile using the GitHub API.

## Features
- Enter any GitHub username
- Shows login, public repos, followers and location
- Handles unknown users (404 → "User not found")
- Handles empty fields (shows "not shared" instead of crashing)

## How to run
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python github_viewer.py`

## What I learned
- `requests.get(url)` sends a GET request to an API
- `response.status_code` tells if it worked (200 OK, 404 not found)
- `response.json()` turns the reply into a Python dictionary
- Website URLs return HTML for humans; API URLs return JSON for programs
- `.get()` with a backup value avoids crashes on missing fields
- A typo in a string key fails silently – copy key names from the real data