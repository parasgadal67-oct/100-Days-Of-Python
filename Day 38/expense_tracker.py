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
print(expenses)
            