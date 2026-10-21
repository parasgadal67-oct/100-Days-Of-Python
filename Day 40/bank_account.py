import random
from account import Account
accounts = []
def find_account(number):
    for account in accounts:
        if account.account_number == number:
            return account
    return None
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter the numbers only!")
def generate_account_number():
    while True:
        number = random.randint(100000000000, 999999999999)
        if find_account(number) is None:
            return number
def ask_for_account():
    number = get_number("Enter the account number: ")
    account = find_account(number)
    if account is None:
            print("Account not found.")
    return account
while True:
    print("1. Create Account.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Show details.")
    print("5. Exit.")
    choice = input("Enter the option: ").strip()
    if choice == "1":
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty!")
            continue
        account_number = generate_account_number()
        accounts.append(Account(name, account_number))
        print(f"Account created successfully. Your account number is '{account_number}'.")
        print(f"Accounts so far :{len(accounts)}")
    elif choice == "2":
        account = ask_for_account()
        if account is not None:
            amount = get_number("Enter the amount: ")
            account.deposit(amount)
    elif choice == "3":
        account = ask_for_account()
        if account is not None:
            amount = get_number("Enter the amount: ")
            account.withdraw(amount)
    elif choice == "4":
        account = ask_for_account()
        if account is not None:
            account.show_details()
            account.show_history()            
    elif choice == "5":
        print("Good bye user!")
        break 
    else:
        print("Invalid input! Enter from 1 to 5.")
        
                      
    