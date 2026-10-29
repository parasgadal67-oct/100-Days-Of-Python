# Day 40 – Bank Account Simulator

A command-line bank app built with Python classes.

## Features
- Create account with auto-generated 11-digit account number (bank code 45598)
- Deposit and withdraw with input checks (no negatives, no overdraft)
- Show account details and transaction history
- List all accounts
- Find account by name + last 4 digits
- Handles wrong input: letters, wrong length, invalid menu options

## How to run
python bank_account.py

## Files
- account.py – the Account class (deposit, withdraw, details, history)
- bank_account.py – menu and helper functions

## Future improvements
- Save/load accounts with JSON
- Deposit/withdraw using name + last 4 digits
- Phone number as unique customer ID
- Close account (balance must be 0, with confirmation)