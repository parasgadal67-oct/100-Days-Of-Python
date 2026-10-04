# Using JSON(Java Script Object Notation) building an expense tracker.
import json
def load_expenses():
    try:
        with open('expenses.json') as f:
            data = json.load(f)
            return data
        
    except FileNotFoundError:
        return []
    
expenses = load_expenses()
while True:
   
    print("1. Add new expense.")
    print("2. View all expenses.")
    print("3. Show total expenditure.")
    print("4. Exit.")
    
    choice = input("Enter your choice : ").strip()
    if choice == "1":
        item = input("Item name: ").strip()
        amount = int(input("Item amount:"))
        expense = {"item" : item ,  "amount" : amount}
        expenses.append(expense)
        with open('expenses.json', "w") as f:
            json.dump(expenses, f)
        print("New Expense Added.")
        
    elif choice == "2":
        print("Here are all your expenses.")
        for expense in expenses:
            print(f"{expense['item']} - ₹{expense['amount']}")   
            
    elif choice == "3":
        print("Here is your total expenditure.")
        total = 0
        for expense in expenses:
            total = total + expense['amount']
        print(f"Your total expense is : ₹{total}")
            
    elif choice == "4":
        print("Thank you for using tracker.")
        break
    else:
        print("Invalid Input. Choose from 1 - 4")
              
        