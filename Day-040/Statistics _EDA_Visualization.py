import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Input data
resolution_hours = pd.Series([
    1.8,
    2.1,
    2.5,
    2.7,
    3.0,
    3.2,
    3.4,
    3.7,
    4.0,
    4.2,
    4.5,
    4.8,
    5.1,
    5.5,
    6.0,
    6.4,
    7.2,
    8.1,
    11.5,
    18.0,
])

# 1. Calculate mean, median, variance, standard deviation, Q1, Q3, and IQR
mean_val = resolution_hours.mean()
median_val = resolution_hours.median()
var_val = resolution_hours.var(ddof=1)
std_val = resolution_hours.std(ddof=1)
q1 = resolution_hours.quantile(0.25)
q3 = resolution_hours.quantile(0.75)
iqr = q3 - q1

print("--- 1. Summary Statistics ---")
print(f"Mean: {mean_val:.2f} hours")
print(f"Median: {median_val:.2f} hours")
print(f"Variance: {var_val:.2f}")
print(f"Standard Deviation: {std_val:.2f} hours")
print(f"Q1: {q1:.2f} | Q3: {q3:.2f} | IQR: {iqr:.2f}\n")

# 2. Investigate potential outliers using the IQR rule
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = resolution_hours[
    (resolution_hours < lower_bound) | (resolution_hours > upper_bound)
]

print("--- 2. Outlier Investigation (IQR Rule) ---")
print(f"Lower Bound: {lower_bound:.2f} | Upper Bound: {upper_bound:.2f}")
print(f"Outliers: {outliers.tolist()}\n")

# 3. Analyse skewness by comparing mean and median
print("--- 3. Skewness Analysis ---")
if mean_val > median_val:
  print(
      f"Mean ({mean_val:.2f}) > Median ({median_val:.2f}) indicates a"
      " right-skewed distribution."
  )
  print(
      "This confirms that severe, long-running incidents are inflating the"
      " overall average."
  )
print()

# 4. Visualisations (Distribution Plot & Box Plot)
plt.figure(figsize=(12, 5))

# Distribution Plot
plt.subplot(1, 2, 1)
sns.histplot(resolution_hours, kde=True, color="skyblue", bins=8)
plt.title("Distribution Plot")
plt.xlabel("Resolution Hours")
plt.ylabel("Frequency")

# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(y=resolution_hours, color="lightgreen")
plt.title("Box Plot (Highlighting Outliers)")
plt.ylabel("Resolution Hours")

plt.tight_layout()
plt.show()

# 5. Recommendation for Management
print("--- 5. Management Recommendation ---")
print(
    f"Recommendation: Use the Median ({median_val:.2f} hours) as the primary"
    " indicator."
)
print(
    "Justification: The mean is pulled up by extreme outliers, whereas the"
    " median reflects the true typical experience of developers."
)