import numpy as np

calories = np.array([
    [420, 450, 390, 510, 480, 530, 500],
    [300, 320, 350, 310, 330, 360, 340],
    [550, 580, 610, 590, 620, 640, 630],
    [280, 310, 290, 350, 340, 370, 360],
    [460, 440, 480, 500, 520, 510, 540]
])

users = np.array(["U1", "U2", "U3", "U4", "U5"])

# Calculate the total and average calories burned by each user and identify the most active user.

total_calo = calories.sum(axis=1)
avg_calo = calories.mean(axis=1)
active_user_index = total_calo.argmax()
most_active_user = users[active_user_index]
print("1. User Totals & Averages:")
for u, t, m in zip(users, total_calo,avg_calo ):
    print(f"   {u}: Total = {t}, Average = {m:.2f}")
print(f"   Most active user: {most_active_user} ({total_calo[active_user_index]} total calories)\n")

# Calculate the average calories burned on each day and identify the day with the highest average activity.

day_means = calories.mean(axis=0)
high_day_index = day_means.argmax()
days = [f"Day {i+1}" for i in range(7)]

print("2. Daily Averages:")
for d, m in zip(days, day_means):
    print(f"   {d}: Average = {m:.2f}")
print(f"   Highest average activity day: {days[high_day_index]} ({day_means[high_day_index]:.2f} avg)\n")

# Identify every user-day combination where calories burned exceeded 550.
exceed_550 = np.where(calories > 550)
print("3. User-day combinations exceeding 550 calories:")
for u_idx, d_idx in zip(exceed_550[0], exceed_550[1]):
    print(f"   User {users[u_idx]} on Day {d_idx+1}: {calories[u_idx, d_idx]} calories")
print()

# Calculate each user's percentage contribution to the total calories burned across all users and days.

grand_total = calories.sum()
user_percentages = (total_calo / grand_total) * 100
print("4. Percentage contribution by user:")
for u, p in zip(users, user_percentages):
    print(f"   {u}: {p:.2f}%")
print(f"   Grand Total: {grand_total}\n")

# Create a Boolean NumPy array indicating whether each value is above the overall average calorie burn, and determine which user has the highest proportion of above-average days.

overall_mean = calories.mean()
above_avg_mask = calories > overall_mean
print("5. Boolean array (above overall mean):")
print(above_avg_mask)

user_above_proportions = above_avg_mask.mean(axis=1)
highest_prop_user_idx = user_above_proportions.argmax()
print(f"   Overall Average: {overall_mean:.2f}")
print("   Proportion of above-average days per user:")
for u, prop in zip(users, user_above_proportions):
    print(f"   {u}: {prop*100:.1f}% ({int(prop*7)} days)")
print(f"   User with highest proportion: {users[highest_prop_user_idx]}")