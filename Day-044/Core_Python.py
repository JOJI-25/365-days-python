user_activity = {
    "U101": [42, 38, 45, 51, 47, 53, 49],
    "U102": [12, 18, 9, 15, 11, 20, 14],
    "U103": [65, 61, 70, 68, 72, 75, 71],
    "U104": [30, 55, 28, 60, 35, 58, 32],
    "U105": [48, 46, 51, 50, 54, 52, 56],
}


def analyze_user_activity(data):
  totals = {}
  averages = {}
  ranges = {}

  for user, minutes in data.items():
    total = sum(minutes)
    avg = total / len(minutes)
    activity_range = max(minutes) - min(minutes)

    totals[user] = total
    averages[user] = round(avg, 2)
    ranges[user] = activity_range

  highest_user = max(totals, key=totals.get)
  lowest_user = min(totals, key=totals.get)

  most_consistent_user = min(ranges, key=ranges.get)

  return totals, averages, ranges, highest_user, lowest_user, most_consistent_user


def classify_user(avg_activity):
  if avg_activity < 25:
    return "Low"
  elif avg_activity < 55:
    return "Moderate"
  else:
    return "Highly Engaged"


totals, averages, ranges, highest_user, lowest_user, most_consistent_user = (
    analyze_user_activity(user_activity)
)

print("=== 1. Total & Average Weekly Activity ===")
for user in user_activity:
  print(
      f"User {user} -> Total: {totals[user]} mins | Average:"
      f" {averages[user]} mins/day"
  )

print("\n=== 2. Extreme Activity Users ===")
print(
    f"Highest Total Activity: User {highest_user} ({totals[highest_user]} mins)"
)
print(f"Lowest Total Activity: User {lowest_user} ({totals[lowest_user]} mins)")

print("\n=== 3. Activity Range & Consistency ===")
for user, rng in ranges.items():
  print(f"User {user} Range: {rng} mins")
print(
    f"Most Consistent User: User {most_consistent_user} (Range:"
    f" {ranges[most_consistent_user]} mins)"
)

print("\n=== 4. Engagement Classification ===")
for user, avg in averages.items():
  print(f"User {user}: {classify_user(avg)}")

print("\n=== 5. Consistency vs. Activity Analysis ===")
print(f"Most Active: User {highest_user}")
print(f"Most Consistent: User {most_consistent_user}")
print(f"Same user? {highest_user == most_consistent_user}")