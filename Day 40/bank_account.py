import json
import random
from account import Account
accounts = []
BANK_CODE = "45598"
ACCOUNT_LENGTH = 11
def find_account(number):
    for account in accounts:
        if account.account_number == number:
            return account
    return None
def save_accounts():
    data = [account.to_dict() for account in accounts]
    with open("accounts.json", "w") as f:
        json.dump(data, f, indent=4)
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter the numbers only!")
def generate_account_number():
    while True:
        random_part = random.randint(100000, 999999)
        number = int(BANK_CODE + str(random_part))
        if find_account(number) is None:
            return number
def ask_for_account():
    number = get_number("Enter the account number: ")
    if len(str(number)) != ACCOUNT_LENGTH:
        print(f"Account Number must be of {ACCOUNT_LENGTH} digits.")
        return None
    account = find_account(number)
    if account is None:
        print("Account not found.")
    return account
def load_accounts():
    try:
        with open("accounts.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return
    for item in data:
        account= Account(item["name"], item["account_number"])
        account.balance = item["balance"]
        account.transactions = item['transactions']
        accounts.append(account)
load_accounts()
while True:
    print("1. Create Account.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Show details.")
    print("5. List all accounts.")
    print("6. Find Account By Name.")
    print("7. Exit.")
    choice = input("Enter the option: ").strip()
    if choice == "1":
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty!")
            continue
        account_number = generate_account_number()
        accounts.append(Account(name, account_number))
        save_accounts()
        print(f"Account created successfully. Your account number is '{account_number}'.")
        print(f"Accounts so far :{len(accounts)}")
    elif choice == "2":
        account = ask_for_account()
        if account is not None:
            amount = get_number("Enter the amount: ")
            account.deposit(amount)
            save_accounts()
    elif choice == "3":
        account = ask_for_account()
        if account is not None:
            amount = get_number("Enter the amount: ")
            account.withdraw(amount)
            save_accounts()
    elif choice == "4":
        account = ask_for_account()
        if account is not None:
            account.show_details()
            account.show_history()
    elif choice == "5":
        if not accounts:
            print("No accounts yet.")
        else:
            for account in accounts:
                print(f"{account.name} - {account.account_number} - Balance: {account.balance}") 
    elif choice == "6":
        name = input("Enter your name: ").strip().lower()
        last_digit = input("Enter the last 4 digits: ").strip()
        if len(last_digit) != 4 or not last_digit.isdigit():
            print("Enter the 4 digits only!")
            continue  
        found = False
        for account in accounts:
            if account.name.lower() == name and str(account.account_number).endswith(last_digit):
                print(f"{account.name} - {account.account_number} - Balance: {account.balance}")
                found = True
        if not found:
            print("No matching account!")
    elif choice == "7":
        print("Good bye user!")
        break 
    else:
        print("Invalid input! Enter from 1 to 7.")
        
                      
    