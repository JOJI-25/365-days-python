import numpy as np

rainfall = np.array([
    [12.5, 8.2, 15.4, 4.1, 0.0, 18.3, 11.7],
    [5.2, 7.8, 6.4, 9.1, 12.6, 10.4, 8.9],
    [22.1, 18.5, 25.7, 30.2, 16.8, 27.4, 21.9],
    [2.4, 0.0, 4.8, 3.2, 6.1, 5.5, 1.8]
])

regions = np.array(["North", "South", "East", "West"])
days = np.array(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"])

# -------------------------------------------------------------------------
# Task 1: Total and average rainfall per region & region with highest average
# -------------------------------------------------------------------------
total_rainfall_region = np.sum(rainfall, axis=1)
avg_rainfall_region = np.mean(rainfall, axis=1)
highest_avg_idx = np.argmax(avg_rainfall_region)

print("=== Task 1: Regional Rainfall (Total & Average) ===")
for r, tot, avg in zip(regions, total_rainfall_region, avg_rainfall_region):
    print(f"{r:<6}: Total = {tot:5.1f} mm | Average = {avg:4.2f} mm")

print(f"\nRegion with highest average rainfall: {regions[highest_avg_idx]} ({avg_rainfall_region[highest_avg_idx]:.2f} mm)\n")

# -------------------------------------------------------------------------
# Task 2: Daily total rainfall & the wettest day
# -------------------------------------------------------------------------
daily_total = np.sum(rainfall, axis=0)
wettest_day_idx = np.argmax(daily_total)

print("=== Task 2: Daily Totals & Wettest Day ===")
for d, tot in zip(days, daily_total):
    print(f"{d}: {tot:5.1f} mm")

print(f"\nWettest day: {days[wettest_day_idx]} ({daily_total[wettest_day_idx]:.1f} mm)\n")

# -------------------------------------------------------------------------
# Task 3: Region-day observations where rainfall > 20 mm (Boolean Indexing)
# -------------------------------------------------------------------------
mask_gt_20 = rainfall > 20.0
region_indices, day_indices = np.where(mask_gt_20)

print("=== Task 3: Observations Exceeding 20 mm ===")
for r_idx, d_idx in zip(region_indices, day_indices):
    print(f"Region: {regions[r_idx]:<5} | Day: {days[d_idx]} | Rainfall: {rainfall[r_idx, d_idx]:.1f} mm")
print()

# -------------------------------------------------------------------------
# Task 4: Percentage of days with rainfall < 5 mm per region
# -------------------------------------------------------------------------
pct_less_than_5 = np.mean(rainfall < 5.0, axis=1) * 100

print("=== Task 4: Percentage of Days with Rainfall < 5 mm ===")
for r, pct in zip(regions, pct_less_than_5):
    print(f"{r:<6}: {pct:5.2f}%")
print()

# -------------------------------------------------------------------------
# Task 5: Standard deviation per region & most variable region
# -------------------------------------------------------------------------
std_rainfall_region = np.std(rainfall, axis=1)
most_variable_idx = np.argmax(std_rainfall_region)

print("=== Task 5: Standard Deviation & Variability ===")
for r, s in zip(regions, std_rainfall_region):
    print(f"{r:<6}: Std Dev = {s:.2f} mm")

print(f"\nMost variable rainfall pattern: {regions[most_variable_idx]} (Std Dev = {std_rainfall_region[most_variable_idx]:.2f} mm)")