class RemoteControl:
    def __init__(self,brand,volume,channel):
        self.brand = brand
        self.volume = volume
        self.channel = channel

    def increase_volume(self):  
        if self.volume<100:
            self.volume+=1
        else:
            print("maximum volume reached")

    def descrease_volume(self):
        if self.volume>0:
            self.volume -= 1
        else:
            print("minimum volume reached")

    def change_channel(self,new_channel):
        self.channel = new_channel

    def show_status(self):
        print("Brand Name : ", self.brand)
        print("Volume : ", self.volume)
        print("Channel : ", self.channel)

my_remote = RemoteControl("Sony", 50, 1)
my_remote.show_status()
my_remote.increase_volume()
my_remote.increase_volume()
my_remote.increase_volume()
my_remote.increase_volume()
my_remote.increase_volume()
my_remote.show_status()
my_remote.descrease_volume()
my_remote.descrease_volume()
my_remote.descrease_volume()
my_remote.show_status()
my_remote.change_channel(10)
my_remote.show_status()

