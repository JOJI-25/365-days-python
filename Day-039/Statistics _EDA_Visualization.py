import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load Data
order_values = pd.Series(
    [
        420,
        510,
        390,
        620,
        580,
        470,
        530,
        610,
        450,
        490,
        560,
        600,
        720,
        680,
        510,
        475,
        590,
        640,
        710,
        2500,
    ]
)

# 2. Calculate Statistics
mean_val = order_values.mean()
median_val = order_values.median()
std_val = order_values.std(ddof=1)
q1 = order_values.quantile(0.25)
q3 = order_values.quantile(0.75)
iqr = q3 - q1

print(f"--- Original Statistics ---")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Std Dev: {std_val:.2f}")
print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")

# 3. Identify Outliers using IQR Method
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = order_values[
    (order_values < lower_bound) | (order_values > upper_bound)
]
print(f"\nOutlier Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Identified Outliers: {outliers.tolist()}")

# 4. Compare Before and After Removing Outliers
clean_orders = order_values[
    (order_values >= lower_bound) & (order_values <= upper_bound)
]
clean_mean = clean_orders.mean()
clean_median = clean_orders.median()

print(f"\n--- Comparison After Removing Outlier ---")
print(f"Clean Mean: {clean_mean:.2f} (Change: {clean_mean - mean_val:.2f})")
print(
    f"Clean Median: {clean_median:.2f} (Change: {clean_median - median_val:.2f})"
)

# 5. Visualizations
plt.figure(figsize=(12, 5))

# Subplot 1: Boxplot to highlight the extreme value
plt.subplot(1, 2, 1)
sns.boxplot(y=order_values, color="skyblue")
plt.title("Order Values Box Plot (Outlier Visible)")
plt.ylabel("Order Value")

# Subplot 2: Histogram showing the distribution
plt.subplot(1, 2, 2)
sns.histplot(order_values, bins=15, kde=True, color="teal")
plt.axvline(
    mean_val, color="red", linestyle="--", label=f"Mean ({mean_val:.1f})"
)
plt.axvline(
    median_val,
    color="orange",
    linestyle="-",
    label=f"Median ({median_val:.1f})",
)
plt.title("Order Values Distribution & Central Tendency")
plt.xlabel("Order Value")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()
