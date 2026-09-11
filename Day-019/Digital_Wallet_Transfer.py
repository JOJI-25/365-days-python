from importlib import readers
class digitalWallet:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def add_money(self,amount):
        if amount < 0:
            raise ValueError("amount is less than 0!!")
        self.balance += amount

    def spend_money(self,amount):
        if amount > self.balance:
            raise ValueError

        self.balance -= amount

    def money_transfer(self, destination_wallet, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Amount is greater than balance.")
        self.balance -= amount
        destination_wallet.balance += amount
        print(f"Success: Transferred ₹{amount} to {destination_wallet.owner}")
    
    def display(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ₹{self.balance}")

wallet1 = digitalWallet("Rohit",1000)
wallet2 = digitalWallet("Aman",2000)
wallet1.display()
wallet2.display()
wallet1.money_transfer(wallet2,500)
wallet1.display()
wallet2.display()