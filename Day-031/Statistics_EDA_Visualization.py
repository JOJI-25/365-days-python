import numpy as np
import matplotlib.pyplot as plt

control = np.array([
    2, 3, 1, 4, 2, 3, 2, 5, 1, 3,
    2, 4, 3, 2, 1, 3, 2, 4, 3, 2
])

treatment = np.array([
    3, 4, 2, 5, 3, 4, 3, 6, 2, 4,
    3, 5, 4, 3, 2, 4, 3, 5, 4, 3
])

# 1. Mean purchases for each group
mean_control = np.mean(control)
mean_treatment = np.mean(treatment)

# 2. Median for each group
median_control = np.median(control)
median_treatment = np.median(treatment)

# 3. Standard deviation for each group
std_control = np.std(control, ddof=1)
std_treatment = np.std(treatment, ddof=1)

# 4. Difference in mean purchases (Treatment - Control)
mean_difference = mean_treatment - mean_control

# 5. Percentage improvement from control to treatment
pct_improvement = (mean_difference / mean_control) * 100

# 6. Visualization
plt.figure(figsize=(8, 5))
plt.boxplot([control, treatment], tick_labels=['Control', 'Treatment'], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2))
plt.title('A/B Test Comparison: Control vs Treatment Purchases')
plt.ylabel('Number of Purchases')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- Output Results ---
print(f"Control Mean: {mean_control:.2f} | Median: {median_control} | Std: {std_control:.2f}")
print(f"Treatment Mean: {mean_treatment:.2f} | Median: {median_treatment} | Std: {std_treatment:.2f}")
print(f"Mean Difference: {mean_difference:.2f}")
print(f"Percentage Improvement: {pct_improvement:.2f}%")