class Alarm:
    def __init__(self,hours,minute):
        if 0<=hours<=23 and 0<=minute<=59:
            self.hours = hours
            self.minute = minute
        else:
            raise ValueError("Invalid time")
        self.status = False

    def enable(self):
        self.status = True

    def disable(self):
        self.status = False

    def show_alarm(self):
        status = "ON" if self.status else "OFF"
        print(f"Alarm: {self.hours:02d}:{self.minute:02d} - {status}")
        

my_alarm = Alarm(hours=7, minute=30)
my_alarm.show_alarm()
my_alarm.enable()
my_alarm.show_alarm()

