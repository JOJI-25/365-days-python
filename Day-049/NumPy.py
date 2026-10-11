import numpy as np

# Given Data
vibration = np.array([
    [
        [0.12, 0.15, 0.11],
        [0.14, 0.16, 0.13],
        [0.13, 0.14, 0.12],
        [0.15, 0.17, 0.14],
        [0.14, 0.16, 0.13]
    ],
    [
        [0.22, 0.25, 0.20],
        [0.24, 0.28, 0.23],
        [0.27, 0.30, 0.25],
        [0.29, 0.34, 0.28],
        [0.35, 0.40, 0.32]
    ],
    [
        [0.10, 0.11, 0.09],
        [0.11, 0.12, 0.10],
        [0.10, 0.13, 0.11],
        [0.12, 0.12, 0.10],
        [0.11, 0.13, 0.10]
    ]
])
machines = np.array(["M1", "M2", "M3"])


# --- Task 1: Average vibration for each machine across all sessions and axes ---
machine_avg = vibration.mean(axis=(1, 2))
highest_machine_idx = np.argmax(machine_avg)

print("--- Task 1: Average Vibration per Machine ---")
for m, avg in zip(machines, machine_avg):
    print(f"Machine {m}: {avg:.4f} mm/s")
print(f"Highest Overall Vibration: Machine {machines[highest_machine_idx]}\n")


# --- Task 2: Average vibration for each machine during each session & greatest increase ---
session_machine_avg = vibration.mean(axis=2) # Shape: (3, 5)
print("--- Task 2: Average Vibration per Machine per Session ---")
for i, m in enumerate(machines):
    print(f"Machine {m}: {np.round(session_machine_avg[i], 4)}")

# Calculate overall session averages across all machines to find the greatest increase
overall_session_avg = vibration.mean(axis=(0, 2))
session_diffs = np.diff(overall_session_avg)
max_increase_idx = np.argmax(session_diffs)
print(f"Session showing greatest overall increase: Transition from Session {max_increase_idx + 1} to Session {max_increase_idx + 2}\n")


# --- Task 3: Maximum vibration along each sensor axis for every machine ---
max_vibration_axis = vibration.max(axis=1) # Shape: (3, 3) -> Machines x Axes
print("--- Task 3: Max Vibration along Each Sensor Axis ---")
for i, m in enumerate(machines):
    print(f"Machine {m} (Axes 1, 2, 3): {max_vibration_axis[i]}")

flat_idx = np.argmax(max_vibration_axis)
m_idx, ax_idx = np.unravel_index(flat_idx, max_vibration_axis.shape)
print(f"Highest reading combination: Machine {machines[m_idx]}, Axis {ax_idx + 1} "
      f"with {max_vibration_axis[m_idx, ax_idx]} mm/s\n")


# --- Task 4: Percentage increase between the first and final sessions ---
first_session_avg = vibration[:, 0, :].mean(axis=1)
final_session_avg = vibration[:, -1, :].mean(axis=1)
pct_increase = ((final_session_avg - first_session_avg) / first_session_avg) * 100

print("--- Task 4: Percentage Increase (First to Final Session) ---")
for m, pct in zip(machines, pct_increase):
    print(f"Machine {m}: {pct:.2f}%")
max_inc_machine = machines[np.argmax(pct_increase)]
print(f"Machine with the largest increase: {max_inc_machine}\n")


# --- Task 5: Boolean mask for readings above 0.30 mm/s and distribution ---
mask = vibration > 0.30
dist_machines = mask.sum(axis=(1, 2))
dist_axes = mask.sum(axis=(0, 1))

print("--- Task 5: Readings Above 0.30 mm/s ---")
print(f"Total count above 0.30 mm/s: {mask.sum()}")
print("Distribution across machines:")
for m, count in zip(machines, dist_machines):
    print(f"  Machine {m}: {count} readings")
print("Distribution across sensor axes:")
for i, count in enumerate(dist_axes):
    print(f"  Axis {i + 1}: {count} readings")
