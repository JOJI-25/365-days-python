class counter:
    def __init__(self,count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count > 0:
            self.count -= 1
        else:
            print("Count is 0 already.")

    def reset(self):
        self.count = 0

    def get_value(self):
        return self.count

mycounter = counter()
mycounter.increment()
mycounter.increment()
mycounter.increment()
mycounter.increment()
mycounter.decrement()
mycounter.decrement()
mycounter.reset()

print(mycounter.get_value())