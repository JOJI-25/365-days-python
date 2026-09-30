import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Dataset Setup
data = {
    "campaign": [
        "C1",
        "C2",
        "C3",
        "C4",
        "C5",
        "C6",
        "C7",
        "C8",
        "C9",
        "C10",
        "C11",
        "C12",
        "C13",
        "C14",
        "C15",
    ],
    "ad_spend": [
        1200,
        1800,
        2200,
        2500,
        3100,
        3400,
        3900,
        4200,
        4700,
        5100,
        5600,
        6100,
        6800,
        7500,
        11000,
    ],
    "clicks": [
        410,
        570,
        680,
        710,
        850,
        920,
        1010,
        1090,
        1180,
        1250,
        1320,
        1410,
        1520,
        1610,
        1700,
    ],
    "conversions": [
        38,
        52,
        61,
        64,
        79,
        82,
        91,
        94,
        101,
        108,
        111,
        117,
        123,
        129,
        132,
    ],
}
df = pd.DataFrame(data)

# 2. Calculate Conversion Rate (%)
df["conversion_rate"] = (df["conversions"] / df["clicks"]) * 100

# 3. Calculate Pearson Correlations
corr_spend_conv = df["ad_spend"].corr(df["conversions"])
corr_spend_rate = df["ad_spend"].corr(df["conversion_rate"])

print("--- Campaign Data with Conversion Rates ---")
print(df[["campaign", "ad_spend", "clicks", "conversions", "conversion_rate"]])
print(f"\nPearson Correlation (Ad Spend vs Conversions): {corr_spend_conv:.4f}")
print(
    f"Pearson Correlation (Ad Spend vs Conversion Rate): {corr_spend_rate:.4f}"
)

# 4. Create Visualizations with Trend Lines
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Ad Spend vs. Total Conversions
sns.regplot(
    data=df,
    x="ad_spend",
    y="conversions",
    ax=axes[0],
    color="blue",
    scatter_kws={"s": 50},
    line_kws={"color": "red"},
)
axes[0].set_title("Ad Spend vs. Total Conversions")
axes[0].set_xlabel("Ad Spend ($)")
axes[0].set_ylabel("Total Conversions")
axes[0].grid(True, linestyle="--", alpha=0.6)

# Plot 2: Ad Spend vs. Conversion Rate (%)
sns.regplot(
    data=df,
    x="ad_spend",
    y="conversion_rate",
    ax=axes[1],
    color="green",
    scatter_kws={"s": 50},
    line_kws={"color": "orange"},
)
axes[1].set_title("Ad Spend vs. Conversion Rate (%)")
axes[1].set_xlabel("Ad Spend ($)")
axes[1].set_ylabel("Conversion Rate (%)")
axes[1].grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()