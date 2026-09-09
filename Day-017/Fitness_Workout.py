class workout:
    def __init__(self, excersice_name, duration_minutes, calories_per_minutes):
        self.excersice = excersice_name

        if duration_minutes < 0:
            raise ValueError("Cannot add negative duration")
        if calories_per_minutes < 0:
            raise ValueError("Cannot add negative calories")
        self.duration_minutes = duration_minutes
        self.calories_per_minutes = calories_per_minutes

    def additional_workout_time(self, added_minutes):
        if added_minutes < 0:
            raise ValueError("Cannot add negative duration")
        self.duration_minutes += added_minutes
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Calories Burned: {self.calculate_calories()}")

    def calculate_calories(self):
        return self.duration_minutes * self.calories_per_minutes

    def display_workout(self):
        print(f"Exercise: {self.excersice}")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Calories per minutes: {self.calories_per_minutes}")
        print(f"Total Calories Burned: {self.calculate_calories()}\n")


cycling = workout("Cycling", 30, 8)
cycling.display_workout()
print("Adding 15 minutes to Cycling...\n")
cycling.additional_workout_time(15)
print()
cycling.display_workout()
print("-" * 20 + "\n")

running = workout("Running", 45, 12)
swimming = workout("Swimming", 30, 10)

running.display_workout()
swimming.display_workout()

all_workouts = [cycling, running, swimming]
total_calories_burned = sum(item.calculate_calories() for item in all_workouts)

print("-" * 20)
print(f"Total Calories Burned Across All Workouts: {total_calories_burned}")