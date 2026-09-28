import numpy as np

steps = np.array([
    [8200, 9100, 7600, 10500, 9800, 11200, 8700],
    [5400, 6200, 5800, 6100, 5900, 6400, 6000],
    [12000, 11500, 13200, 12800, 14000, 13600, 14500],
    [7600, 8100, 7900, 8300, 8500, 8000, 8200],
    [4300, 5100, 4800, 4600, 5200, 5500, 5000],
    [9700, 10200, 9900, 10800, 11100, 10500, 10900],
    [6800, 7200, 7500, 7100, 7800, 7600, 8000],
    [15000, 14200, 13800, 15500, 16100, 15800, 14900]
])

# 1. Weekly total and average steps for every user
weekly_totals = np.sum(steps, axis=1)
weekly_averages = np.mean(steps, axis=1)

print("Weekly Totals:", weekly_totals)
print("Weekly Averages:", weekly_averages)

# 2. Most active and least active users
most_active_user = np.argmax(weekly_averages) + 1
least_active_user = np.argmin(weekly_averages) + 1
print(f"Most active user: User {most_active_user} ({weekly_averages[most_active_user-1]:.2f})")
print(f"Least active user: User {least_active_user} ({weekly_averages[least_active_user-1]:.2f})")

# 3. Average steps for each day and most active day
daily_averages = np.mean(steps, axis=0)
most_active_day = np.argmax(daily_averages) + 1
print("Daily averages:", daily_averages)
print(f"Most active day: Day {most_active_day}")

# 4. Users above 10,000 steps and percentage
above_10k = np.where(weekly_averages > 10000)[0] + 1
percentage = (len(above_10k) / len(weekly_averages)) * 100
print(f"Users above 10,000: User {above_10k}, Percentage: {percentage}%")

# 5. Each user's deviation from the overall daily average / overall average
overall_daily_avg = np.mean(steps, axis=0) # or overall average of all steps? Let's check both interpretations.
# "deviation from the overall daily average" could mean user's average minus overall average, or user's daily steps minus overall daily average.
# Let's compute user average vs overall grand average, or user daily deviation. Let's look closely at standard wording.
grand_avg = np.mean(steps)
user_deviations = weekly_averages - grand_avg
print("Grand Average:", grand_avg)
print("User deviations from grand average:", user_deviations)
max_diff_user = np.argmax(np.abs(user_deviations)) + 1
print(f"User who differs the most: User {max_diff_user}")