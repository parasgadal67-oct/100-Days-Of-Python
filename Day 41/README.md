# Day 41 – pip, Virtual Environments and requirements.txt

Setting up an isolated Python environment for a project.

## What I did
- Created a virtual environment with `python -m venv venv`
- Activated it on Windows (and fixed the PowerShell execution policy error)
- Installed `requests` with pip (it brought 4 dependencies with it)
- Saved all packages to `requirements.txt` with `pip freeze`
- Deleted the venv and rebuilt it with `pip install -r requirements.txt`
- Proved isolation: `check.py` works inside the venv, fails outside it

## How to run
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python check.py`

## What I learned
- pip downloads packages from PyPI
- A venv keeps each project's packages separate (no conflicts)
- requirements.txt lets anyone rebuild the same environment
- The venv folder is never uploaded – requirements.txt is