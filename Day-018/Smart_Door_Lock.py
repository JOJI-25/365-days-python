class Doorlock:
    def __init__(self,doorname,password):
        self.doorname = doorname 
        self.password = password
        self.is_locked = True

    def unlock(self,passkey):
        if passkey == self.password:
            self.is_locked = False
            return f"Door is Unlocked"
        else:
            return f"Invalid Password!!!"

    def lock(self):
        self.is_locked = True

    def change_password(self,old_password,new_password):
        if old_password == self.password:
            self.password = new_password
            return f"Password Changed!!"
        else:
            return f"Invalid Old Password!!!"

    def display_status(self):
        print(f"Door_name: {self.doorname}")
        if self.is_locked:
            print(f"Door is locked")
        else:
            print(f"Door is Unlocked")

my_door = Doorlock(doorname="Main Door",password="1234")
my_door.display_status()
my_door.unlock("1234")
my_door.display_status()
my_door.lock()
my_door.display_status()

my_door.change_password("1234","5678")
my_door.display_status()