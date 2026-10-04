import numpy as np

production = np.array([
    [820, 850, 790, 875, 860, 890],
    [760, 780, 745, 800, 770, 815],
    [910, 925, 940, 935, 950, 965],
    [680, 710, 695, 720, 705, 730],
    [845, 830, 860, 850, 875, 865]
])
lines = np.array(["L1", "L2", "L3", "L4", "L5"])

# 1. Total and mean production for each line, and identify strongest/weakest lines
line_totals = np.sum(production, axis=1)
line_means = np.mean(production, axis=1)

strongest_line = lines[np.argmax(line_totals)]
weakest_line = lines[np.argmin(line_totals)]

print("--- 1. Production Line Totals and Means ---")
for i, line in enumerate(lines):
    print(f"{line}: Total = {line_totals[i]}, Mean = {line_means[i]:.2f}")
print(f"Strongest Line: {strongest_line}")
print(f"Weakest Line: {weakest_line}\n")


# 2. Total production for each day and determine the highest output day
day_totals = np.sum(production, axis=0)
highest_day_idx = np.argmax(day_totals)

print("--- 2. Daily Total Production ---")
for day, total in enumerate(day_totals, 1):
    print(f"Day {day}: {total}")
print(f"Highest Output Day: Day {highest_day_idx + 1} ({day_totals[highest_day_idx]}) units\n")


# 3. Percentage contribution of each line to total production
total_company_production = np.sum(production)
line_percentages = (line_totals / total_company_production) * 100

print("--- 3. Percentage Contribution per Line ---")
for i, line in enumerate(lines):
    print(f"{line}: {line_percentages[i]:.2f}%")
print()


# 4. Identify production values below overall mean using NumPy Boolean masking
overall_mean = np.mean(production)
below_mean_mask = production < overall_mean
below_mean_values = production[below_mean_mask]

print("--- 4. Values Below Overall Mean ---")
print(f"Overall Mean Production: {overall_mean:.2f}")
print(f"Values below mean: {list(below_mean_values)}")
print()


# 5. Coefficient of Variation (CV) for each line to determine instability
line_stds = np.std(production, axis=1)
line_cvs = line_stds / line_means
most_unstable_line = lines[np.argmax(line_cvs)]

print("--- 5. Coefficient of Variation (CV) ---")
for i, line in enumerate(lines):
    print(f"{line}: CV = {line_cvs[i]:.4f} (Std: {line_stds[i]:.2f}, Mean: {line_means[i]:.2f})")
print(f"Most Unstable Line: {most_unstable_line}")