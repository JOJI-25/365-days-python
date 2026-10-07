import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data setup
cpu_usage = pd.Series([
    42, 45, 48, 51, 47,
    53, 55, 57, 54, 59,
    61, 63, 60, 65, 67,
    69, 72, 74, 81, 92,
    96, 98
])

# 1. Calculate descriptive statistics
mean_val = cpu_usage.mean()
median_val = cpu_usage.median()
var_val = cpu_usage.var()
std_val = cpu_usage.std()
q1 = cpu_usage.quantile(0.25)
q3 = cpu_usage.quantile(0.75)
iqr = q3 - q1

print("--- 1. Descriptive Statistics ---")
print(f"Mean: {mean_val:.2f}%")
print(f"Median: {median_val:.2f}%")
print(f"Variance: {var_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}%")
print(f"Q1 (25th Percentile): {q1}%")
print(f"Q3 (75th Percentile): {q3}%")
print(f"IQR: {iqr}%\n")

# 2. Use the IQR method to identify potential high-utilisation outliers
upper_bound = q3 + 1.5 * iqr
outliers = cpu_usage[cpu_usage > upper_bound]

print("--- 2. Outlier Detection (IQR Method) ---")
print(f"Upper Bound Threshold: {upper_bound}%")
print(f"High-utilisation outliers: {outliers.tolist() if not outliers.empty else 'None'}\n")

# 3. Create a histogram and box plot to describe the distribution
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram with KDE
sns.histplot(cpu_usage, bins=6, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title("CPU Utilisation Distribution (Histogram)")
axes[0].set_xlabel("CPU Utilisation (%)")
axes[0].set_ylabel("Frequency")
axes[0].grid(True, linestyle="--", alpha=0.5)

# Box Plot
sns.boxplot(y=cpu_usage, ax=axes[1], color='lightgreen')
axes[1].set_title("CPU Utilisation Box Plot")
axes[1].set_ylabel("CPU Utilisation (%)")
axes[1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# 4. Calculate percentage of days where CPU utilisation exceeded 80%
exceed_80_pct = (cpu_usage > 80).mean() * 100

print("--- 4. Capacity Analysis (>80% Utilisation) ---")
print(f"Percentage of days exceeding 80% utilisation: {exceed_80_pct:.2f}%\n")

# 5. Recommendation based on statistical evidence
print("--- 5. Engineering Recommendation ---")
print("""
Recommendation:
The company should investigate the high-utilisation days first before immediately increasing server capacity.

Statistical Reasoning:
- Central Tendency: The median utilisation (around 62%) and mean are well below the critical 80% threshold, 
  indicating that for most days, the current infrastructure handles the workload comfortably.
- Frequency of Spikes: Days exceeding 80% utilisation account for only a minor fraction of the period 
  (approximately 18.2%). 
- Distribution & Outliers: The statistical spread shows that high usage is concentrated in a few upper-end points 
  rather than a chronic shift across the entire dataset. This points towards specific transient events (such as 
  unoptimized batch processes or traffic surges) rather than permanent infrastructure saturation. 
  Optimizing these workloads is a more cost-effective first step than scaling hardware prematurely.
""")