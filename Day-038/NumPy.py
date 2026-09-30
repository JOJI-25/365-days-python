import numpy as np

energy = np.array([
    [42, 45, 44, 48, 51],
    [35, 36, 34, 38, 37],
    [61, 64, 63, 68, 72],
    [28, 31, 29, 30, 32],
    [47, 49, 52, 54, 56],
    [39, 41, 40, 43, 45]
])

departments = np.array([
    "HR",
    "Finance",
    "Engineering",
    "Security",
    "Marketing",
    "Operations"
])

total_energy = energy.sum(axis=1)
max_dept = departments[np.argmax(total_energy)]
print(f"The total energy of {max_dept} is {total_energy[np.argmax(total_energy)]}")

day_avgs = energy.mean(axis=0)
highest_day_idx = day_avgs.argmax()
print("Day averages:", day_avgs.tolist())
print("Highest day index (0-indexed):", highest_day_idx)

total_building_consumption = energy.sum()
percent = (total_energy / total_building_consumption) * 100
print("Total building consumption:", total_building_consumption)
for d, p in zip(departments, percent):
    print(f"{d}: {p:.2f}%")


mask = energy > 55
dept_indices, day_indices = np.where(mask)
high_combos = [(str(departments[d]), int(day_idx) + 1, int(energy[d, day_idx])) for d, day_idx in zip(dept_indices, day_indices)]
print("Greater than 55 kWh:", high_combos)


mean_val = energy.mean()
std_val = energy.std()
standardised = (energy - mean_val) / std_val
max_std_idx = np.unravel_index(standardised.argmax(), standardised.shape)
print(f"Mean: {mean_val}, Std: {std_val}")
print(f"Max standardised value: {standardised[max_std_idx]:.4f} at Department: {departments[max_std_idx[0]]}, Day: {max_std_idx[1] + 1}")