import pandas as pd
import numpy as np

support = pd.DataFrame({
    "channel": [
        "Chat", "Chat", "Chat", "Chat", "Chat",
        "Email", "Email", "Email", "Email", "Email"
    ],
    "response_minutes": [
        4, 6, 7, 8, 35,
        18, 20, 22, 24, 27
    ]
})

# 1, 2, 3, 4. Calculate Mean, Median, Std Dev, Q1, Q3, and IQR for each channel
stats = support.groupby("channel")["response_minutes"].agg(
    mean="mean",
    median="median",
    std=lambda x: np.std(x, ddof=1),
    q1=lambda x: np.percentile(x, 25),
    q3=lambda x: np.percentile(x, 75)
).reset_index()

stats["iqr"] = stats["q3"] - stats["q1"]
print("--- Channel Statistics ---")
print(stats)
print()

# 5. Outlier investigation using the IQR method
print("--- Outlier Detection ---")
for channel in ["Chat", "Email"]:
    subset = support[support["channel"] == channel]["response_minutes"]
    q1 = np.percentile(subset, 25)
    q3 = np.percentile(subset, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = subset[(subset < lower_bound) | (subset > upper_bound)]
    print(f"{channel} Outliers:", outliers.tolist())

print()

# Additional SLA Check: Percentage of requests <= 15 minutes
print("--- SLA Compliance (<= 15 minutes) ---")
sla_compliance = support.groupby("channel")["response_minutes"].apply(
    lambda x: f"{(x <= 15).mean() * 100}%"
)
print(sla_compliance)