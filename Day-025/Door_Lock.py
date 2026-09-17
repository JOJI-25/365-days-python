class DoorLock:
    def __init__(self,door_name,password,is_locked):
        self.door_name = door_name
        self.password = password
        self.is_locked = is_locked



    def lock(self):
        self.is_locked = True

    def unlock(self,password):
        if password == self.password:
            self.is_locked = False
            return True
        return False

    def change_password(self,old_password,new_password):
        if self.is_locked == False and old_password == self.password:
            self.password = new_password
            return True
        return False

    def display(self):
        print(f"Door Name: {self.door_name}")
        print(f"Is Locked: {self.is_locked}")


door1 = DoorLock("Main Door","1234",True)
door1.display()
print("\n")

door1.unlock("1234")
door1.display()
print("\n")

door1.change_password("1234","5678")
door1.display()


door2 = DoorLock("Kitchen Door","4321",True)
door2.display()
print("\n")

