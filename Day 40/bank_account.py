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
while True:
    print("1. Create Account.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Show details.")
    print("5. Exit.")
    choice = input("Enter the option: ").strip()
    if choice == "1":
        name = input("Enter your name: ")
        account_number = get_number("Enter your account number: ")
        accounts.append(Account(name, account_number))
        print(f"Accounts so far :{len(accounts)}")
    if choice == "2":
        number = get_number("Enter the account number: ")
        account = find_account(number)
        if account is None:
            print("Account not found.")
        else:
            amount = get_number("Enter the amount: ")
            account.deposit(amount)
            
    if choice == "3":
        number = get_number("Enter the account number: ")
        account = find_account(number)
        if account is None:
            print("Account not found.")
        else:
            amount = get_number("Enter the amount: ")
            account.withdraw(amount)
    if choice == "4":
        number = get_number("Enter the account number: ")
        account = find_account(number)
        if account is None:
            print("Account not found.")  
        else:
            account.show_details()
            account.show_history()            
    if choice == "5":
        print("Good bye user!")
        
        break               
    