class parcel:
    def __init__(self,tracking_id,weight):
        self.tracking_id = tracking_id
        self.weight = weight

    def add_weight(self,amount):
        if amount > 0:
            self.weight += amount
        else:
            print("Error: Cant add negative weight")

    def remove_weight(self,amount):
        if amount > 0:
            self.weight -= amount
        else:
            print("Error: Cant remove negative weight")

    def get_weight(self):
        return self.weight

    def is_heavy(self):
        if self.weight > 20:
            return True
        else:
            return False

    def display(self):
        print("Tracking ID:", self.tracking_id)
        print("Weight:", self.weight)
        print("Heavy:", self.is_heavy())

        

my_parcel = parcel(tracking_id="123456789", weight=10)
my_parcel.display()

my_parcel.add_weight(35)
my_parcel.display()

my_parcel.remove_weight(3)
my_parcel.display()

