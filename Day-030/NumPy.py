import numpy as np

temperature = np.array([
    [72, 75, 74, 78, 80, 79],
    [68, 70, 71, 69, 72, 73],
    [81, 83, 82, 85, 87, 89],
    [74, 73, 75, 76, 74, 77]
])

# 1. Calculate the mean temperature for each machine (across rows/axis=1)
mean_temp = np.mean(temperature, axis=1)

# 2. Find the maximum temperature recorded by each machine
max_temp = np.max(temperature, axis=1)

# 3. Identify every temperature measurement above 80°C
above_80_mask = temperature > 80
above_80_values = temperature[above_80_mask]

# 4. Count how many potentially problematic measurements each machine has
problematic_counts = np.sum(temperature > 80, axis=1)

# 5. Determine which machine has the greatest temperature variability using standard deviation
std_temp = np.std(temperature, axis=1)
max_variability_machine = np.argmax(std_temp)

# 6. Calculate the temperature change from the first measurement to the last measurement
temp_change = temperature[:, -1] - temperature[:, 0]

# 7. Identify machines whose final temperature is higher than their initial temperature by at least 5°C
increase_at_least_5 = temp_change >= 5

# --- Output Results ---
print("Mean temperatures:", mean_temp)
print("Max temperatures:", max_temp)
print("Measurements above 80°C:", above_80_values)
print("Problematic counts per machine:", problematic_counts)
print("Standard deviations:", std_temp)
print("Machine with greatest variability (index):", max_variability_machine)
print("Temperature changes (Last - First):", temp_change)
print("Machines with increase >= 5°C:", increase_at_least_5)