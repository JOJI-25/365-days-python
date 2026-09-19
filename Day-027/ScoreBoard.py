class ScoreBoard:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def add_points(self, player, points):
        if points <= 0:
            print(f"Error: Points to add must be positive. ({points} provided)")
            return

        if player == self.player1_name:
            self.player1_score += points
        elif player == self.player2_name:
            self.player2_score += points
        else:
            print(f"Error: '{player}' is not a registered player.")

    def get_leader(self):
        if self.player1_score > self.player2_score:
            return self.player1_name
        elif self.player2_score > self.player1_score:
            return self.player2_name
        else:
            return "Tie"

    def display_score(self):
        print(f"Player 1: {self.player1_name} -> {self.player1_score}")
        print(f"Player 2: {self.player2_name} -> {self.player2_score}")
        print(f"Leader: {self.get_leader()}\n")




game_board = ScoreBoard("Arun", "Rahul")

print("--- Initial Scores ---")
game_board.display_score()

print("--- Adding Points ---")
game_board.add_points("Arun", 40)
game_board.add_points("Rahul", 30)

game_board.display_score()