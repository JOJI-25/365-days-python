class Player:
    def __init__(self, name, position, points_scored=0):
        self.name = name
        self.position = position
        self.points_scored = points_scored

    def score_points(self, points):
        """Adds points to this specific player's total."""
        if points > 0:
            self.points_scored += points

    def display_info(self):
        """Returns the player's details as a formatted string."""
        return f"{self.name} - {self.position} - {self.points_scored} points"


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = [] 

    def add_player(self, new_player):
        for player in self.players:
            if player.name == new_player.name:
                print(f"Error: {new_player.name} is already on the team.")
                return
        
        self.players.append(new_player)

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                print(f"Success: {player_name} has been removed.")
                return
        
        print(f"Notice: Could not find {player_name} on the team.")

    def calculate_total_points(self):
        total = 0
        for player in self.players:
            total += player.points_scored
        return total

    def display_team(self):
        print(f"Team: {self.team_name}\n")
        print("Players:")
        
        if not self.players:
            print("No players on the team yet.")
        else:
            for index, player in enumerate(self.players, start=1):
                print(f"{index}. {player.display_info()}")
                
        print(f"\nTotal Team Points: {self.calculate_total_points()}")
        print("-" * 30)



thunder = Team("Thunder")
arjun = Player("Arjun", "Forward", 25)
rahul = Player("Rahul", "Guard", 18)
kiran = Player("Kiran", "Center", 30)
thunder.add_player(arjun)
thunder.add_player(rahul)
thunder.add_player(kiran)

thunder.display_team()

print("-> Testing: Adding a duplicate player (Arjun)...")
thunder.add_player(arjun)

print("\n-> Testing: Removing a player who doesn't exist (Vikram)...")
thunder.remove_player("Vikram")

print("\n-> Testing: Rahul scores 5 more points...")
rahul.score_points(5)

print("\n-> Testing: Removing Kiran...")
thunder.remove_player("Kiran")
print("-" * 30)

thunder.display_team()