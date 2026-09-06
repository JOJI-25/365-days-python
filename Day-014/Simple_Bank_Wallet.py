class wallet:
    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amount):
        if amount> 0:
            self.balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid Amount")

    def spend(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print(f"Spent {amount}")
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"Owner: {self.owner_name}")
        print(f"Balance: {self.balance}")
        
wallet1 = wallet("Joji",1000)
wallet1.deposit(500)
wallet1.spend(300)
wallet1.display()