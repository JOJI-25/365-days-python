class ATM:

  def __init__(self, initial_notes):
    self.inventory = initial_notes

  def get_total_cash(self):
    return sum(denom * count for denom, count in self.inventory.items())

  def check_cash(self):
    print("ATM Cash Inventory:")
    for denom in sorted(self.inventory.keys(), reverse=True):
      print(f"Rs.{denom} -> {self.inventory[denom]}")
    print(f"Total Available Cash: Rs.{self.get_total_cash()}\n")

  def withdraw(self, amount):
    if amount <= 0:
      print("Error: Withdrawal amount must be positive.\n")
      return False

    if amount > self.get_total_cash():
      print("Error: ATM does not have enough total cash.\n")
      return False

    remaining_amount = amount
    temp_inventory = self.inventory.copy()
    dispensed = {}

    sorted_denoms = sorted(self.inventory.keys(), reverse=True)

    for denom in sorted_denoms:
      if remaining_amount <= 0:
        break

      needed = remaining_amount // denom
      available = temp_inventory[denom]
      to_use = min(needed, available)

      if to_use > 0:
        dispensed[denom] = to_use
        remaining_amount -= to_use * denom
        temp_inventory[denom] -= to_use

    if remaining_amount > 0:
      print(
          f"Error: Cannot dispense exact amount Rs.{amount} with available"
          " denominations.\n"
      )
      return False

    self.inventory = temp_inventory
    print(f"Successfully withdrew Rs.{amount}!")
    print("Dispensed Notes:")
    for denom, count in dispensed.items():
      print(f"Rs.{denom} x {count}")
    print()
    return True



initial_cash = {500: 10, 200: 10, 100: 20, 50: 20, 20: 50, 10: 50}
atm = ATM(initial_cash)

atm.check_cash()

atm.withdraw(2000)
atm.check_cash()

atm.withdraw(1750)
atm.check_cash()

atm.withdraw(6000)  
atm.check_cash()
