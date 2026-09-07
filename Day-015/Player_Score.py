class Player:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def add_score(self,points):
        self.score += points
        print("Points Added!")
     
    def remove_score(self,points):
        if points > 0:
            self.score -= points
            print("Points Removed!")
        else:
            print("Invalid Score")

    def display_score(self):
        print(f"{self.name}: {self.score}")

name = input("Enter the Name: ")
score = int(input("Enter the Score: "))

player1 = Player(name,score)
player1.display_score()
player1.add_score(10)
player1.add_score(20)
player1.display_score()
player1.remove_score(5)
player1.display_score()


