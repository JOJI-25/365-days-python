import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load dataset
episodes = pd.DataFrame({
    "episode_id": [
        "E101",
        "E102",
        "E103",
        "E104",
        "E105",
        "E106",
        "E107",
        "E108",
        "E109",
        "E110",
        "E111",
        "E112",
    ],
    "category": [
        "Technology",
        "Comedy",
        "Education",
        "Technology",
        "Comedy",
        "Education",
        "Business",
        "Technology",
        "Business",
        "Comedy",
        "Education",
        "Business",
    ],
    "duration_min": [35, 28, 42, 50, 32, 45, 38, 40, 55, 25, 48, 60],
    "starts": [1200, 1800, 950, 1400, 1600, 1100, 850, 1300, 900, 2000, 1000, 780],
    "completion_25_pct": [
        0.85,
        0.90,
        0.88,
        0.80,
        0.92,
        0.86,
        0.82,
        0.84,
        0.79,
        0.93,
        0.87,
        0.75,
    ],
    "completion_50_pct": [
        0.70,
        0.76,
        0.73,
        0.64,
        0.79,
        0.71,
        0.66,
        0.68,
        0.62,
        0.81,
        0.72,
        0.58,
    ],
    "completion_90_pct": [
        0.42,
        0.48,
        0.46,
        0.35,
        0.51,
        0.43,
        0.38,
        0.40,
        0.32,
        0.54,
        0.44,
        0.29,
    ],
})

# 1. Validate completion-rate columns
# Check for missing values
missing_values = episodes[
    ["completion_25_pct", "completion_50_pct", "completion_90_pct"]
].isnull().sum().sum()

# Check for impossible relationships (milestones should be non-increasing: 25% >= 50% >= 90%)
invalid_logic = episodes[
    (episodes["completion_25_pct"] < episodes["completion_50_pct"])
    | (episodes["completion_50_pct"] < episodes["completion_90_pct"])
]

print(f"--- 1. Validation ---")
print(f"Total missing values in completion rates: {missing_values}")
print(f"Episodes with invalid milestone ordering: {len(invalid_logic)}")

# 2. Create retention_drop_25_to_90 column (percentage-point decline)
episodes["retention_drop_25_to_90"] = (
    episodes["completion_25_pct"] - episodes["completion_90_pct"]
) * 100

# 3. Compare categories using total starts, average 90% completion, and average retention drop
category_summary = (
    episodes.groupby("category")
    .agg(
        total_starts=("starts", "sum"),
        avg_completion_90=("completion_90_pct", lambda x: x.mean() * 100),
        avg_retention_drop=("retention_drop_25_to_90", "mean"),
    )
    .reset_index()
)

print("\n--- 3. Category Summary ---")
print(category_summary.to_string(index=False))

# Identify strongest category at retaining listeners (highest avg 90% completion and lowest drop)
best_retaining_category = category_summary.loc[
    category_summary["avg_completion_90"].idxmax(), "category"
]
print(
    f"\nStrongest category at retaining listeners: {best_retaining_category}"
)

# 4. Create visualization for listener retention across milestones per category
cat_means = (
    episodes.groupby("category")[
        ["completion_25_pct", "completion_50_pct", "completion_90_pct"]
    ]
    .mean()
    * 100
)

plt.figure(figsize=(8, 5))
milestones = ["25%", "50%", "90%"]
for category in cat_means.index:
  plt.plot(
      milestones,
      cat_means.loc[category],
      marker="o",
      linewidth=2,
      label=category,
  )

plt.title("Podcast Listener Retention Drop-off by Category")
plt.xlabel("Completion Milestone")
plt.ylabel("Average Retention Rate (%)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Category")
plt.ylim(20, 100)
plt.tight_layout()
plt.savefig("retention_trends.png")
plt.show()