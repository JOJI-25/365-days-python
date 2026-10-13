import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
support = pd.DataFrame({
    "centre_A": [
        4.2, 4.5, 4.8, 5.0, 5.1,
        5.3, 5.5, 5.8, 6.0, 6.2,
        6.5, 7.0, 8.5, 12.0, 18.5
    ],
    "centre_B": [
        3.8, 4.0, 4.1, 4.3, 4.5,
        4.6, 4.8, 5.0, 5.2, 5.4,
        5.6, 5.8, 6.2, 9.5, 15.0
    ]
})

# 1. Calculate Descriptive Statistics
def calculate_metrics(df):
    results = {}
    for col in df.columns:
        series = df[col]
        results[col] = {
            "mean": series.mean(),
            "median": series.median(),
            "iqr": stats.iqr(series),
            "std": series.std()
        }
    return pd.DataFrame(results)

summary_stats = calculate_metrics(support)
print("--- 1. Descriptive Statistics ---")
print(summary_stats.round(2), "\n")

# 2. Visualization Code (Box plots and Empirical CDF)
def plot_distributions(df):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Box plot
    sns.boxplot(data=df, ax=axes[0])
    axes[0].set_title("Handling Times Box Plot")
    axes[0].set_ylabel("Minutes")
    
    # ECDF plot
    for col in df.columns:
        x = np.sort(df[col])
        y = np.arange(1, len(x) + 1) / len(x)
        axes[1].plot(x, y, marker='.', linestyle='-', label=col)
    axes[1].set_title("Empirical Cumulative Distribution Function (ECDF)")
    axes[1].set_xlabel("Minutes")
    axes[1].set_ylabel("Cumulative Probability")
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()

# To run visualizations uncomment below:
plot_distributions(support)

# 3. Bootstrap Resampling for 95% Confidence Interval of Difference in Medians
np.random.seed(42)
n_boot = 10000
diff_medians = []
a = support["centre_A"].values
b = support["centre_B"].values

for _ in range(n_boot):
    sample_a = np.random.choice(a, size=len(a), replace=True)
    sample_b = np.random.choice(b, size=len(b), replace=True)
    diff_medians.append(np.median(sample_a) - np.median(sample_b))

ci_lower = np.percentile(diff_medians, 2.5)
ci_upper = np.percentile(diff_medians, 97.5)

print("--- 3. Bootstrap Median Difference (Centre A - Centre B) ---")
print(f"95% Confidence Interval: [{ci_lower:.2f}, {ci_upper:.2f}] minutes\n")

# 4. Non-Parametric Test (Mann-Whitney U Test)
mwu_res = stats.mannwhitneyu(a, b, alternative='two-sided')
print("--- 4. Mann-Whitney U Test ---")
print(f"Statistic: {mwu_res.statistic}, p-value: {mwu_res.pvalue:.4f}")
if mwu_res.pvalue < 0.05:
    print("Result: Reject the null hypothesis (distributions differ significantly at 5% level).")
else:
    print("Result: Fail to reject the null hypothesis (no statistically significant difference at 5% level).\n")

# 5. Recommendation Summary
print("--- 5. Operational Recommendation ---")
print("Management should avoid rushing to prioritise one centre based solely on these metrics, as the distributions do not show statistically significant differences at the 5% level.")