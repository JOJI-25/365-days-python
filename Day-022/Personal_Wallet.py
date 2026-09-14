class Wallet:
    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("Balance after deposit : ", self.balance)
        else:
            print("Error: Cannot deposit negative amount")
    
    def spend(self,amount):
        if amount > 0:
            if self.balance - amount < 0:
                print("Error: Not enough balance.")
            else:
                self.balance -= amount
                print("Balance after spending: ", self.balance)
        else:
            print("Error: Cannot spend negative amount")

        
    def display(self):
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")

person1 = Wallet("Anu",1000)
person1.display()

person1.deposit(500)
person1.display()
person1.spend(200)
person1.display()
person1.spend(2000)
person1.display()
