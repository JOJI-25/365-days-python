class ATM:
    def __init__(self, initial_notes=None):
        self.denominations = initial_notes if initial_notes else {
            500: 5,
            200: 5,
            100: 10,
            50: 10
        }

    def check_available_cash(self):
        total = sum(note * count for note, count in self.denominations.items())
        return total

    def display_summary(self):
        total = self.check_available_cash()
        print("\n--- ATM Cash Inventory ---")
        for note in sorted(self.denominations.keys(), reverse=True):
            print(f"₹{note} notes : {self.denominations[note]}")
        print(f"Total Cash Available: ₹{total}")
        print("----------------------------\n")

    def _find_notes(self, amount, notes_list, index, current_dispensed, inventory_copy):
        if amount == 0:
            return current_dispensed
        if index >= len(notes_list) or amount < 0:
            return None
        
        note = notes_list[index]
        max_possible = min(amount // note, inventory_copy[note])
        
        for count in range(max_possible, -1, -1):
            if count > 0:
                current_dispensed[note] = count
            
            inventory_copy[note] -= count
            result = self._find_notes(amount - (note * count), notes_list, index + 1, current_dispensed, inventory_copy)
            
            if result is not None:
                return result
            
            inventory_copy[note] += count
            if note in current_dispensed:
                del current_dispensed[note]
                
        return None

    def request_withdrawal(self, amount):
        print(f"Requested Withdrawal: ₹{amount}")

        if amount <= 0 or amount % 50 != 0:
            print("Result: Withdrawal failed. Invalid amount requested.\n")
            return None

        total_cash = self.check_available_cash()
        
        if amount > total_cash:
            print("Result: Withdrawal failed. ATM does not have enough total cash.\n")
            return None

        temp_inventory = self.denominations.copy()
        sorted_notes = sorted(temp_inventory.keys(), reverse=True)
        dispensed = {}

        result = self._find_notes(amount, sorted_notes, 0, dispensed, temp_inventory)

        if result is None:
            print("Result: Withdrawal failed. ATM cannot construct the exact amount using available notes.\n")
            return None

        self.denominations = temp_inventory
        print("Withdrawal successful! Dispensed notes:")
        for note, count in sorted(result.items(), reverse=True):
            print(f"  ₹{note} × {count}")
        print()
        return result


atm = ATM({
    500: 2,
    200: 3,
    100: 5,
    50:  4
})

atm.display_summary()

atm.request_withdrawal(750)

atm.display_summary()

atm.request_withdrawal(2000)

atm.display_summary()