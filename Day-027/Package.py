class Package:
    def __init__(self,tracking_id,destination,weight,status):
        self.tracking_id = tracking_id
        self.destination = destination
        self.weight = weight
        self.status = status



    def update_status(self,new_status):
        self.status = new_status

    def calculate_delivery_charge(self):
        rate_per_kg = 50
        
        if self.weight < 5:
            charge = 50
        elif self.weight < 10:
            charge = 100
        elif self.weight < 20:
            charge = 200
        else:
            charge = 300
        
        return charge



    def get_status(self):
        print(f"tracking_id {self.tracking_id}")
        print(f"destination {self.destination}")
        print(f"weight {self.weight}")
        print(f"status {self.status}")


my_package = Package("123456789", "123 Main St", 5, "Pending")


my_package.get_status()
print("Delivery Charge: ", my_package.calculate_delivery_charge())
