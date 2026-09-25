import matplotlib.pyplot as plt
import numpy as np

# ----------------- 1. Data Setup -----------------
organic_users = np.array(
    [42, 55, 61, 48, 73, 66, 52, 80, 59, 64, 71, 45, 68, 57, 62]
)

ad_users = np.array(
    [35, 41, 46, 39, 52, 44, 48, 55, 37, 42, 50, 46, 40, 53, 45]
)


# ----------------- 2. Statistical Computations -----------------
def get_stats(arr):
    mean_val = np.mean(arr)
    median_val = np.median(arr)
    std_val = np.std(arr, ddof=1)  # Sample standard deviation
    q1 = np.percentile(arr, 25)
    q3 = np.percentile(arr, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = arr[(arr < lower_bound) | (arr > upper_bound)]
    return {
        "mean": mean_val,
        "median": median_val,
        "std": std_val,
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "outliers": outliers,
    }


org_stats = get_stats(organic_users)
ad_stats = get_stats(ad_users)

diff_mean = org_stats["mean"] - ad_stats["mean"]
pct_diff = (diff_mean / org_stats["mean"]) * 100

# Correlation with player index (0 to N-1)
indices = np.arange(len(organic_users))
corr_org = np.corrcoef(indices, organic_users)[0, 1]
corr_ad = np.corrcoef(indices, ad_users)[0, 1]

# ----------------- 3. Display Results -----------------
print("--- SUMMARY STATISTICS ---")
print(
    f"Organic -> Mean: {org_stats['mean']:.2f}, Median: {org_stats['median']:.1f}, Std: {org_stats['std']:.2f}"
)
print(
    f"Ad Users -> Mean: {ad_stats['mean']:.2f}, Median: {ad_stats['median']:.1f}, Std: {ad_stats['std']:.2f}"
)
print(f"Difference in Mean: {diff_mean:.2f} mins")
print(f"Percentage Difference (relative to Organic): {pct_diff:.2f}%")
print(
    f"Organic IQR: {org_stats['iqr']:.2f} (Q1: {org_stats['q1']}, Q3: {org_stats['q3']}), Outliers: {org_stats['outliers'].tolist()}"
)
print(
    f"Ad Users IQR: {ad_stats['iqr']:.2f} (Q1: {ad_stats['q1']}, Q3: {ad_stats['q3']}), Outliers: {ad_stats['outliers'].tolist()}"
)
print(f"Index Correlation -> Organic: {corr_org:.4f}, Ad Users: {corr_ad:.4f}")

# ----------------- 4. Visualization -----------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: Box Plot (Side-by-side distribution & quartiles)
box = axes[0].boxplot(
    [organic_users, ad_users],
    tick_labels=["Organic", "Ad Users"],
    patch_artist=True,
    medianprops=dict(color="black", linewidth=1.5),
)
colors = ["#4C72B0", "#DD8452"]
for patch, color in zip(box["boxes"], colors):
    patch.set_facecolor(color)
axes[0].set_title("First-Week Engagement: Box Plot")
axes[0].set_ylabel("Minutes Played")
axes[0].grid(axis="y", linestyle="--", alpha=0.7)

# Subplot 2: Overlapping Histograms / KDE representation
bins = np.linspace(30, 85, 12)
axes[1].hist(
    organic_users,
    bins=bins,
    alpha=0.6,
    label="Organic",
    color="#4C72B0",
    edgecolor="black",
)
axes[1].hist(
    ad_users,
    bins=bins,
    alpha=0.6,
    label="Ad Users",
    color="#DD8452",
    edgecolor="black",
)
axes[1].set_title("Engagement Distribution Comparison")
axes[1].set_xlabel("Minutes Played")
axes[1].set_ylabel("Player Count")
axes[1].legend()
axes[1].grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()