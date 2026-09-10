# creating Bank account stimulator  using  O.O.P(OBJECT ORIENTED PROGRAMMING)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Dear {self.owner}, you have deposited the amount:{amount} successfully,and your new balance is: {self.balance}") 
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Dear {self.owner}, you have withdrawn the amount: {amount} successfully, and your new balance is: {self.balance}")
        
