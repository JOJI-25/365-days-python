class package:
    def __init__(self,tracking_id,destination,weight):
        self.tracking_id = tracking_id
        self.destination = destination
        self.weight = weight
        self.status = "preparing"

    def update_status(self,new_status):
        self.status = new_status

    def calculate_charge(self):
        if self.weight <= 1:
            return 50
        elif self.weight <= 5:
            return 100
        else:
            return 200

    def display_info(self):
        print(f"Tracking ID: {self.tracking_id}")
        print(f"Destination: {self.destination}")
        print(f"Weight: {self.weight} kg")
        print(f"Status: {self.status}")
        print(f"Delivery Charge: ₹{self.calculate_charge()}\n")


package1 = package("PK102", "Kochi", 3)
package2 = package("PK103", "Alappuzha", 0.8)
package3 = package("PK104", "Bengaluru", 7.5)

print("Updating status...\n")
package1.update_status("Shipped")
print(f"Status: {package1.status}\n")

print("Checking the other packages:\n")
package2.display_info()
package3.display_info()