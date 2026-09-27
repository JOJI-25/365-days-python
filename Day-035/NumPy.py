import numpy as np

sensor_data = np.array([    
    [72.5, 4.2, 2.1],    
    [75.1, 4.5, 2.4],    
    [71.8, 4.1, 1.9],    
    [91.2, 5.8, 6.7],    
    [74.6, 4.3, 2.2],    
    [88.5, 5.4, 5.9],    
    [73.2, 4.0, 2.0],    
    [76.4, 4.6, 2.6]
])

# Define warning thresholds: Temp > 85, Pressure > 5.0, Vibration > 5.0
thresholds = np.array([85.0, 5.0, 5.0])
sensor_names = ["Temperature", "Pressure", "Vibration"]

# 1. Mean of each sensor
sensor_means = np.mean(sensor_data, axis=0)

# 2. Standard deviation of each sensor
sensor_stds = np.std(sensor_data, axis=0)

# 3. Boolean anomaly matrix
anomaly_matrix = sensor_data > thresholds

# 4. Count violations per machine
violation_counts = np.sum(anomaly_matrix, axis=1)

# 5. Machines with at least one warning
warning_mask = violation_counts > 0
warning_machines = np.where(warning_mask)[0]

# 6. Machine with the greatest number of violations
max_violation_machine = np.argmax(violation_counts)

# 7. Normal machines (zero violations)
normal_mask = violation_counts == 0
normal_machines = np.where(normal_mask)[0]

# 8. Percentage of machines with at least one warning
warning_percentage = (np.sum(warning_mask) / len(sensor_data)) * 100

# 9. Average sensor values for normal vs warning machines
normal_avg = np.mean(sensor_data[normal_mask], axis=0)
warning_avg = np.mean(sensor_data[warning_mask], axis=0)

# 10. Sensor contributing most frequently to anomalies
sensor_violation_counts = np.sum(anomaly_matrix, axis=0)
most_frequent_sensor_idx = np.argmax(sensor_violation_counts)
most_frequent_sensor = sensor_names[most_frequent_sensor_idx]

# --- PRINT STATEMENTS ---
print("=" * 40)
print("SENSOR ANOMALY DETECTION REPORT")
print("=" * 40)

print("\n1. Sensor Means:")
for name, mean in zip(sensor_names, sensor_means):
    print(f"   - {name}: {mean:.2f}")

print("\n2. Sensor Standard Deviations:")
for name, std in zip(sensor_names, sensor_stds):
    print(f"   - {name}: {std:.2f}")

print("\n3. Boolean Anomaly Matrix (Rows = Machines, Cols = Temp, Pressure, Vibration):")
print(anomaly_matrix)

print("\n4. Violation counts for every machine:")
for i, count in enumerate(violation_counts):
    print(f"   - Machine {i}: {count} violations")

print(f"\n5. Machines with at least one warning: {list(warning_machines)}")
print(f"6. Machine with the greatest number of violations: Machine {max_violation_machine}")
print(f"7. Normal machines (within limits): {list(normal_machines)}")
print(f"8. Percentage of machines with warnings: {warning_percentage:.1f}%")

print("\n9. Average sensor values comparison:")
print(f"   - Normal machines average: {np.round(normal_avg, 2).tolist()}")
print(f"   - Warning machines average: {np.round(warning_avg, 2).tolist()}")

print(f"\n10. Sensor contributing most frequently to anomalies: {most_frequent_sensor}")
print("=" * 40)