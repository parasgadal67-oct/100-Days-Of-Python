# Day 44 – Currency Converter (live rates)

A command-line currency converter using the free ExchangeRate-API (open.er-api.com, no key needed).

## Features
- Convert any amount between ~160 currencies (e.g. INR → NPR, USD → INR)
- Accepts lowercase and extra spaces ("  usd " works)
- Rejects invalid amounts (letters, empty, zero, negative) and asks again
- Handles: no internet, slow server, bad status, unsupported currency, unknown target currency
- Rates update once a day

## How to run
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python currency_converter.py`

## What I learned
- Order of checks: status code → .json() → "result" key → rate exists → calculate
- An API can return 200 OK and still report an error inside the JSON
- `continue` in a input-validation loop; `return` exits the function and the loop
- `.get()` returns None for a missing key – check with `is None`
- Test valid inputs too: a key typo ("results") made every currency "not supported"

## Planned upgrades
- Check both currencies at once against one USD rate list (report all mistakes together)