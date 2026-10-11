import numpy as np

defects = np.array([
    [12, 15, 11, 14, 18, 13, 16, 15], # Line_A
    [7,  9,  8,  10, 6,  11, 9,  8],  # Line_B
    [21, 18, 25, 23, 27, 20, 29, 24], # Line_C
    [4,  6,  5,  7,  4,  8,  6,  5]   # Line_D
])
lines = np.array(["Line_A", "Line_B", "Line_C", "Line_D"])

# 1. Total and average number of defects for each production line
total_defects = defects.sum(axis=1)
avg_defects = defects.mean(axis=1)
highest_line = lines[np.argmax(total_defects)]

print("--- 1. Defect Totals & Averages per Line ---")
for i, line in enumerate(lines):
    print(f"{line}: Total = {total_defects[i]}, Average = {avg_defects[i]:.2f}")
print(f"Line with Highest Defect Rate: {highest_line}\n")


# 2. Total defects recorded on each day and identifying the peak day
daily_totals = defects.sum(axis=0)
highest_day = np.argmax(daily_totals) + 1  # 1-indexed day

print("--- 2. Daily Defect Totals ---")
for day, total in enumerate(daily_totals, 1):
    print(f"Day {day}: {total} defects")
print(f"Day with Highest Overall Defect Count: Day {highest_day} ({daily_totals[highest_day - 1]} defects)\n")


# 3. Percentage of each line's observations above the overall mean defect count
overall_mean = defects.mean()
above_mean_pct = [(defects[i] > overall_mean).mean() * 100 for i in range(len(lines))]

print("--- 3. Percentage Above Overall Mean ---")
print(f"Overall Mean Defect Count: {overall_mean:.2f}")
for i, line in enumerate(lines):
    print(f"{line}: {above_mean_pct[i]:.1f}% of observations above mean")
print()


# 4. Standard deviation and Coefficient of Variation (CV) for relative instability
stds = defects.std(axis=1)
cvs = stds / avg_defects  # CV = Standard Deviation / Mean
most_unstable_line = lines[np.argmax(cvs)]

print("--- 4. Stability Analysis ---")
for i, line in enumerate(lines):
    print(f"{line}: Std Dev = {stds[i]:.2f}, CV = {cvs[i]:.4f}")
print(f"Line with Greatest Relative Instability (Highest CV): {most_unstable_line}\n")


# 5. Boolean mask for defect counts > 20 and count per production line
mask = defects > 20
mask_counts = mask.sum(axis=1)

print("--- 5. Defect Counts > 20 (Boolean Mask) ---")
print("Boolean Mask Matrix:\n", mask)
print("\nObservations > 20 per line:")
for i, line in enumerate(lines):
    print(f"{line}: {mask_counts[i]} instances")