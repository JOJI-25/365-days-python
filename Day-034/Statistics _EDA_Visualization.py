import pandas as pd

fitness = pd.DataFrame({
    "weekly_exercise_hours": [
        1, 2, 2, 3, 3, 4, 4, 5,
        5, 6, 6, 7, 7, 8, 9
    ],
    "calories_burned": [
        320, 580, 610, 850, 910, 1180, 1210, 1450,
        1520, 1770, 1810, 2050, 2120, 2380, 2700
    ],
    "sleep_hours": [
        5.2, 5.8, 6.0, 6.1, 6.4, 6.5, 6.8, 6.7,
        7.0, 7.1, 7.2, 7.3, 7.5, 7.6, 7.8
    ]
})

# 1. Calculate correlations
correlation_matrix = fitness.corr()
print("--- Correlation Matrix ---")
print(correlation_matrix)

# 3. Average calorie expenditure across groups
group_low = fitness[fitness["weekly_exercise_hours"] < 4]["calories_burned"].mean()
group_mid = fitness[(fitness["weekly_exercise_hours"] >= 4) & (fitness["weekly_exercise_hours"] <= 6)]["calories_burned"].mean()
group_high = fitness[fitness["weekly_exercise_hours"] > 6]["calories_burned"].mean()

print("\n--- Average Calorie Expenditure by Exercise Tier ---")
print(f"Fewer than 4 hours: {group_low:.2f} kcal")
print(f"4–6 hours: {group_mid:.2f} kcal")
print(f"More than 6 hours: {group_high:.2f} kcal")