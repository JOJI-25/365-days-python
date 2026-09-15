class Player:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def add_score(self,point):
        print(f"Adding {point} points to {self.name}")
        self.score += point

    def remove_score(self,point):
        if self.score - point < 0:
            print("Error: Cannot remove points")
        else:
            print(f"Removing {point} points from {self.name}")
            self.score -= point

    def display(self):
        print(f"Player: {self.name}")
        print(f"Score: {self.score}")


player1 = Player("Aarav",0)
print(f"Player: {player1.name}")
print(f"Score: {player1.score}")
print("-" * 20)

player1.add_score(10)
print(f"Score: {player1.score}")

player1.remove_score(5)
print(f"Score: {player1.score}")

player1.display()

