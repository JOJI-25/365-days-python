import numpy as np

# Data setup
temperature = np.array([
    [62.5, 64.1, 63.8, 65.2, 66.0, 64.7],
    [68.2, 69.5, 70.1, 71.3, 72.0, 73.2],
    [59.8, 60.5, 61.2, 60.9, 62.1, 61.7],
    [75.1, 76.8, 78.2, 77.5, 80.1, 82.4]
])
processors = np.array(["P1", "P2", "P3", "P4"])

# 1. Calculate the mean and maximum temperature for each processor and identify the highest thermal load
mean_temps = np.mean(temperature, axis=1)
max_temps = np.max(temperature, axis=1)
highest_thermal_load_idx = np.argmax(max_temps)

print("--- 1. Mean and Maximum Temperatures ---")
for p, m, mx in zip(processors, mean_temps, max_temps):
    print(f"Processor {p}: Mean = {m:.2f}°C, Max = {mx:.2f}°C")
print(f"Processor with the highest thermal load: {processors[highest_thermal_load_idx]}\n")

# 2. Calculate the temperature increase from the first test to the final test
temp_increases = temperature[:, -1] - temperature[:, 0]
largest_increase_idx = np.argmax(temp_increases)

print("--- 2. Temperature Increase (First to Final Test) ---")
for p, inc in zip(processors, temp_increases):
    print(f"Processor {p}: Increase = {inc:.2f}°C")
print(f"Processor with the largest increase: {processors[largest_increase_idx]}\n")

# 3. Identify every processor-test observation above 75°C using NumPy Boolean indexing
mask_above_75 = temperature > 75.0
obs_indices = np.where(mask_above_75)

print("--- 3. Observations Above 75°C ---")
for proc_idx, test_idx in zip(obs_indices[0], obs_indices[1]):
    print(f"Processor: {processors[proc_idx]}, Test {test_idx + 1}, Temperature: {temperature[proc_idx, test_idx]}°C")
print()

# 4. Calculate the standard deviation and determine the most unstable processor
stds = np.std(temperature, axis=1)
most_unstable_idx = np.argmax(stds)

print("--- 4. Temperature Stability (Standard Deviation) ---")
for p, std in zip(processors, stds):
    print(f"Processor {p}: Std Dev = {std:.2f}")
print(f"Most unstable temperature behavior: {processors[most_unstable_idx]}\n")

# 5. Calculate the percentage of tests below 70°C and rank the processors
below_70_counts = np.sum(temperature < 70.0, axis=1)
pct_below_70 = (below_70_counts / temperature.shape[1]) * 100
ranked_indices = np.argsort(-pct_below_70)

print("--- 5. Percentage of Tests Below 70°C & Ranking ---")
for rank, idx in enumerate(ranked_indices, start=1):
    print(f"Rank {rank}: Processor {processors[idx]} ({pct_below_70[idx]:.1f}% of tests below 70°C)")