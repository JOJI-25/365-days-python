import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

prep_time = pd.Series([
    11,
    13,
    14,
    15,
    16,
    17,
    18,
    18,
    19,
    20,
    21,
    21,
    22,
    23,
    24,
    25,
    26,
    28,
    34,
    47,
    62,
])

mean_val = prep_time.mean()
median_val = prep_time.median()
var_val = prep_time.var(ddof=1)
std_val = prep_time.std(ddof=1)
q1 = prep_time.quantile(0.25)
q3 = prep_time.quantile(0.75)
iqr = q3 - q1

print("--- 1. Descriptive Statistics ---")
print(f"Mean: {mean_val:.2f} minutes")
print(f"Median: {median_val} minutes")
print(f"Variance: {var_val:.2f}")
print(f"Standard Deviation: {std_val:.2f} minutes")
print(f"Q1 (25th Percentile): {q1} minutes")
print(f"Q3 (75th Percentile): {q3} minutes")
print(f"IQR: {iqr} minutes\n")

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = prep_time[(prep_time < lower_bound) | (prep_time > upper_bound)]

print("--- 2. Outlier Detection (IQR Method) ---")
print(f"Lower Bound Threshold: {lower_bound:.2f}")
print(f"Upper Bound Threshold: {upper_bound:.2f}")
print(f"Unusually long preparation times (Outliers): {list(outliers.values)}")
print()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(prep_time, bins=8, color="skyblue", edgecolor="black")
plt.title("Histogram of Preparation Times")
plt.xlabel("Preparation Time (Minutes)")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.boxplot(y=prep_time, color="lightgreen")
plt.title("Box Plot of Preparation Times")
plt.ylabel("Preparation Time (Minutes)")
plt.show()
plt.tight_layout()

exceeding_30 = prep_time[prep_time > 30]
pct_gt_30 = (len(exceeding_30) / len(prep_time)) * 100

print("--- 4. Orders Exceeding 30 Minutes ---")
print(f"Percentage of orders > 30 mins: {pct_gt_30:.2f}% ({len(exceeding_30)} out of {len(prep_time)} orders)")
print(
    "Operational KPI Importance: This metric tracks Service Level Agreement (SLA) breaches. "
    "High rates of orders taking over 30 minutes directly degrade customer retention and point to kitchen bottlenecks."
)
print()

print("--- 5. Benchmark Decision & Justification ---")
print(f"Recommended Benchmark: **Median** ({median_val} minutes)")
print(
    "Justification:\n"
    f"- The data is right-skewed with extreme outliers (e.g., 34, 47, and 62 minutes).\n"
    f"- The mean ({mean_val:.2f} minutes) is artificially inflated by these extreme long delays, making it less representative of a typical customer experience.\n"
    "- The median provides a robust, middle-of-the-road performance benchmark that is immune to extreme outliers."
)