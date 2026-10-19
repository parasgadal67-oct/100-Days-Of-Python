# Building bank account stimulator from scratch 
class Account:
    def __init__( self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.transactions = []
        
    def deposit(self, amount):
        if  amount <= 0:
            print("Invalid Transaction.")
            return
        self.balance = self.balance + amount
        self.transactions.append({"type":"deposit" , "amount":amount})
        print(f"Deposit Successful, Balance: {self.balance}.")
            
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Transaction")
            return
        if self.balance < amount:
            print("Balance Too Low.")
            return
        self.balance = self.balance - amount
        self.transactions.append({"type":"withdraw", "amount":amount})
        print(f"Withdrawal Successful, Balance: {self.balance}.")
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        
    def show_history(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        for record in self.transactions:
            print(f"{record['type']} : {record['amount']}")
   
a = Account("Ramesh", 7689)
a.deposit(5000)
a.withdraw(788)    
a.show_details()
a.show_history()
b = Account("Priya", 8976)
b.deposit(100000)
b.withdraw(5600)
b.show_details()
b.show_history()
c = Account("Test 1", 1)
c.show_details()
c.show_history()
print(a.balance, a.transactions)
print(b.balance, b.transactions)
print(c.balance, c.transactions)