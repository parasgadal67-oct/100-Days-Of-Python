# Day 40 – Bank Account Simulator

A command-line bank app built with Python classes and JSON storage.

## Features
- Create account with auto-generated 11-digit account number (bank code 45598)
- Deposit and withdraw with input checks (no negatives, no overdraft)
- Show account details and transaction history
- List all accounts
- Find account by name + last 4 digits
- Accounts saved to accounts.json and loaded on startup (data survives restart)
- Handles wrong input: letters, wrong length, invalid menu options

## How to run
python bank_account.py

## Files
- account.py – the Account class (deposit, withdraw, details, history, to_dict)
- bank_account.py – menu, helper functions, save/load
- accounts.json – created automatically; ignored by Git to keep customer data private

## What I learned
- Classes, objects, methods and attributes
- Helper functions that return an object or None
- Saving objects to JSON by converting them to dictionaries
- Using .gitignore to keep data files out of GitHub

## Future improvements
- Phone number as unique customer ID (prevent duplicate customers)
- Deposit/withdraw using name + last 4 digits
- Close account (balance must be 0, with confirmation)