import numpy as np

consumption = np.array([
    [420, 435, 410, 455, 470, 490, 475],
    [310, 325, 318, 330, 342, 350, 345],
    [580, 610, 595, 625, 640, 660, 645],
    [250, 265, 245, 275, 280, 290, 285],
])
buildings = np.array(["B1", "B2", "B3", "B4"])

total_weekly = np.sum(consumption, axis=1)
avg_daily = np.mean(consumption, axis=1)
highest_building = buildings[np.argmax(total_weekly)]

print("=== 1. Total & Average Weekly Consumption ===")
for b, tot, avg in zip(buildings, total_weekly, avg_daily):
  print(f"Building {b} -> Total: {tot} kWh | Avg Daily: {avg:.2f} kWh")
print(f"Highest Consuming Building: Building {highest_building}\n")

daily_total = np.sum(consumption, axis=0)
daily_avg = np.mean(consumption, axis=0)
highest_day = np.argmax(daily_total) + 1

print("=== 2. Daily Consumption ===")
for d, (tot, avg) in enumerate(zip(daily_total, daily_avg), 1):
  print(f"Day {d} -> Total: {tot} kWh | Avg: {avg:.2f} kWh")
print(f"Highest Combined Usage Day: Day {highest_day}\n")


thresholds = 1.2 * avg_daily[:, np.newaxis]
mask = consumption > thresholds

print("=== 3. Observations > 20% Above Weekly Average ===")
anomalies_found = False
for i in range(len(buildings)):
  for j in range(consumption.shape[1]):
    if mask[i, j]:
      anomalies_found = True
      print(
          f"Building {buildings[i]}, Day {j+1}: {consumption[i, j]} kWh"
          f" (Threshold: {thresholds[i,0]:.2f} kWh)"
      )
if not anomalies_found:
  print("No observations found exceeding 20% above the weekly average.\n")

total_energy = np.sum(total_weekly)
percentages = (total_weekly / total_energy) * 100

print("=== 4. Percentage Contribution ===")
for b, pct in zip(buildings, percentages):
  print(f"Building {b}: {pct:.2f}%")
print()

stds = np.std(consumption, axis=1, ddof=0)
cvs = stds / avg_daily
least_stable_building = buildings[np.argmax(cvs)]

print("=== 5. Coefficient of Variation (Stability) ===")
for b, cv in zip(buildings, cvs):
  print(f"Building {b} -> CV: {cv:.4f}")
print(f"Least Stable Building: Building {least_stable_building}")
print(
    f"Is the highest consuming building ({highest_building}) also the least"
    f" stable? {highest_building == least_stable_building}"
)