import numpy as np

speed = np.array([
    [28.4, 29.1, 28.8, 29.5, 30.0, 29.7],
    [27.8, 28.2, 28.0, 28.6, 28.9, 29.1],
    [30.1, 30.5, 30.2, 30.8, 31.0, 31.2],
    [26.9, 27.4, 27.1, 27.8, 28.0, 27.6]
])
athletes = np.array(["A1", "A2", "A3", "A4"])

mean_speeds = np.mean(speed, axis=1)
fastest_idx = np.argmax(mean_speeds)
fastest_athlete = athletes[fastest_idx]

print("--- 1. Mean Sprint Speed & Fastest Athlete ---")
for i, athlete in enumerate(athletes):
    print(f"- {athlete}: {mean_speeds[i]:.2f} km/h")
print(f"Fastest Athlete: {fastest_athlete} ({mean_speeds[fastest_idx]:.2f} km/h)\n")

improvements = speed[:, -1] - speed[:, 0]
max_imp_idx = np.argmax(improvements)
max_imp_athlete = athletes[max_imp_idx]

print("--- 2. Improvement (First to Final Session) ---")
for i, athlete in enumerate(athletes):
    print(f"- {athlete}: {improvements[i]:+.2f} km/h (From {speed[i, 0]} to {speed[i, -1]})")
print(f"Largest Improvement: {max_imp_athlete} ({improvements[max_imp_idx]:+.2f} km/h)\n")

overall_mean = np.mean(speed)
above_mean_mask = speed > overall_mean
row_indices, col_indices = np.where(above_mean_mask)

print("--- 3. Observations Above Overall Mean ---")
print(f"Overall Mean Speed: {overall_mean:.2f} km/h")
print("Observations exceeding the overall mean:")
for r, c in zip(row_indices, col_indices):
    print(f"- Athlete {athletes[r]}, Session {c + 1}: {speed[r, c]} km/h")
print()

std_devs = np.std(speed, axis=1, ddof=1)
consistent_idx = np.argmin(std_devs)
most_consistent_athlete = athletes[consistent_idx]

print("--- 4. Performance Consistency (Standard Deviation) ---")
for i, athlete in enumerate(athletes):
    print(f"- {athlete}: {std_devs[i]:.2f} km/h")
print(f"Most Consistent Athlete: {most_consistent_athlete} (Lowest std dev: {std_devs[consistent_idx]:.2f} km/h)\n")

exceeding_29 = speed > 29.0
percentages = np.mean(exceeding_29, axis=1) * 100
ranked_indices = np.argsort(percentages)[::-1]

print("--- 5. Percentage of Sessions > 29 km/h & Ranking ---")
for rank, idx in enumerate(ranked_indices, start=1):
    print(f"Rank {rank}: {athletes[idx]} - {percentages[idx]:.1f}% of sessions")