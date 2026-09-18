class DigitalClock:
    def __init__(self,hour,minutes):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            print("Invalid hour!")
            self.hour = 0
            
        if 0 <= minutes <= 59:
            self.minutes = minutes
        else:
            print("Invalid minutes!")

    def display(self):
        print(f"{self.hour}:{self.minutes}")

    def time(self,hour,minute):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            print("Invalid hour!")
            self.hour = 0
            
        if 0 <= minute <= 59:
            self.minutes = minute
        else:
            print("Invalid minutes!")
            self.minutes = 0    

time1 = DigitalClock(23,59)

time1.display()

time1.time(10,23)

time1.display()

time1.time(24,0)

time1.display()
        
        
