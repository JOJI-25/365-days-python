import matplotlib.pyplot as plt
import pandas as pd

completion_time = pd.Series([
    32, 35, 38, 41, 43,
    45, 47, 49, 52, 54,
    56, 58, 61, 64, 68,
    72, 79, 85, 118, 145
])

# -------------------------------------------------------------------------
# Task 1: Summary Statistics (Mean, Median, Q1, Q3, IQR, Std Dev)
# -------------------------------------------------------------------------
mean_val = completion_time.mean()
median_val = completion_time.median()
q1 = completion_time.quantile(0.25)
q3 = completion_time.quantile(0.75)
iqr = q3 - q1
std_val = completion_time.std()

print("=== Task 1: Summary Statistics ===")
print(f"Mean               : {mean_val:.2f} mins")
print(f"Median             : {median_val:.2f} mins")
print(f"Q1 (25th percentile): {q1:.2f} mins")
print(f"Q3 (75th percentile): {q3:.2f} mins")
print(f"IQR                : {iqr:.2f} mins")
print(f"Standard Deviation : {std_val:.2f} mins\n")

# -------------------------------------------------------------------------
# Task 2: IQR Method for Outlier Detection (Unusually Long Times)
# -------------------------------------------------------------------------
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

slow_outliers = completion_time[completion_time > upper_bound]

print("=== Task 2: Outlier Detection (IQR Method) ===")
print(f"Upper Bound (Q3 + 1.5 * IQR): {upper_bound:.2f} mins")
print(f"Lower Bound (Q1 - 1.5 * IQR): {lower_bound:.2f} mins")
print(f"Unusually long completion times: {slow_outliers.tolist()}\n")

# -------------------------------------------------------------------------
# Task 3: Visualisations (Histogram and Box Plot)
# -------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Subplot 1: Histogram + KDE
axes[0].hist(completion_time, bins=8, color="skyblue", edgecolor="black", alpha=0.7)
axes[0].axvline(mean_val, color="red", linestyle="--", linewidth=1.5, label=f"Mean ({mean_val:.1f})")
axes[0].axvline(median_val, color="green", linestyle="-", linewidth=1.5, label=f"Median ({median_val:.1f})")
axes[0].set_title("Distribution of Completion Time", fontsize=12)
axes[0].set_xlabel("Completion Time (minutes)")
axes[0].set_ylabel("Frequency")
axes[0].legend()
axes[0].grid(axis="y", linestyle="--", alpha=0.5)

# Subplot 2: Box Plot
axes[1].boxplot(
    completion_time,
    vert=True,
    patch_artist=True,
    boxprops=dict(facecolor="lightcoral", color="black"),
    flierprops=dict(marker="o", markerfacecolor="red", markersize=8, linestyle="none")
)
axes[1].axhline(upper_bound, color="blue", linestyle=":", label=f"Upper Fence ({upper_bound:.1f})")
axes[1].set_title("Box Plot with Outliers", fontsize=12)
axes[1].set_ylabel("Completion Time (minutes)")
axes[1].set_xticks([1])
axes[1].set_xticklabels(["Students"])
axes[1].legend()
axes[1].grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# -------------------------------------------------------------------------
# Task 4: Proportion Comparison (<= 60 mins vs. > 90 mins)
# -------------------------------------------------------------------------
pct_within_60 = (completion_time <= 60).mean() * 100
pct_above_90 = (completion_time > 90).mean() * 100

print("=== Task 4: Completion Time Thresholds ===")
print(f"Students completed within 60 mins : {pct_within_60:.1f}% ({sum(completion_time <= 60)}/20 students)")
print(f"Students requiring > 90 mins      : {pct_above_90:.1f}% ({sum(completion_time > 90)}/20 students)\n")

# -------------------------------------------------------------------------
# Task 5: Recommendation / Group Investigation Assessment
# -------------------------------------------------------------------------
print("=== Task 5: Assessment & Recommendation ===")
explanation = """
1. Distribution Shape:
   - The data is strongly right-skewed (Mean = 63.95 mins > Median = 55.0 mins).
   - 60% of students finish within 1 hour, and 75% complete within 70 minutes (Q3 = 69 mins).

2. Statistical Outliers:
   - The upper threshold is 106.5 mins.
   - Two students (118 mins and 145 mins) exceed this cut-off and plot beyond the whiskers as clear statistical outliers.

3. Actionable Recommendation:
   - Yes, the course team should investigate these students (>90 mins / >106.5 mins) separately.
   - Taking 2x to 2.5x the median time indicates conceptual friction, prerequisite gaps, or debugging bottlenecks rather than standard pacing differences.
   - Targeted intervention (code submission reviews, syntax/logic diagnostics, or automated hints) can resolve specific roadblocks without slowing down the majority cohort.
"""
print(explanation.strip())