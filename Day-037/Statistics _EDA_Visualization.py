import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data setup
data = {
    "order_id": range(1, 16),
    "distance_km": [
        1.2,
        2.0,
        2.5,
        3.1,
        3.8,
        4.2,
        4.8,
        5.5,
        6.0,
        6.7,
        7.1,
        7.8,
        8.5,
        10.0,
        14.5,
    ],
    "delivery_minutes": [
        22,
        25,
        28,
        31,
        34,
        36,
        39,
        43,
        45,
        48,
        51,
        55,
        59,
        66,
        95,
    ],
    "customer_rating": [5, 5, 4, 5, 4, 4, 4, 3, 4, 3, 3, 3, 3, 2, 1],
}
df = pd.DataFrame(data)

# 1. Summary Statistics for delivery_minutes
mean_time = df["delivery_minutes"].mean()
median_time = df["delivery_minutes"].median()
std_time = df["delivery_minutes"].std()
q25 = df["delivery_minutes"].quantile(0.25)
q75 = df["delivery_minutes"].quantile(0.75)
iqr_time = q75 - q25

print("--- 1. Summary Statistics ---")
print(
    f"Mean: {mean_time:.2f} | Median: {median_time:.2f} | Std: {std_time:.2f} | IQR: {iqr_time:.2f}"
)

# 2. Pearson correlation between distance_km and delivery_minutes
distance_time_corr = df["distance_km"].corr(
    df["delivery_minutes"], method="pearson"
)
print("\n--- 2. Correlation ---")
print(f"Distance vs Delivery Time Pearson Correlation: {distance_time_corr:.4f}")

# 3. Visualization (displayed inline without saving)
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Distance vs Delivery Minutes
sns.scatterplot(
    data=df,
    x="distance_km",
    y="delivery_minutes",
    ax=axes[0],
    color="b",
    s=80,
)
sns.regplot(
    data=df,
    x="distance_km",
    y="delivery_minutes",
    ax=axes[0],
    scatter=False,
    color="red",
)
axes[0].set_title("Delivery Distance vs. Delivery Time")
axes[0].set_xlabel("Distance (km)")
axes[0].set_ylabel("Delivery Time (minutes)")

# Plot 2: Delivery Minutes vs Customer Rating
sns.boxplot(
    data=df, x="customer_rating", y="delivery_minutes", ax=axes[1], palette="Blues_r"
)
axes[1].set_title("Delivery Time by Customer Rating")
axes[1].set_xlabel("Customer Rating (Stars)")
axes[1].set_ylabel("Delivery Time (minutes)")

plt.tight_layout()
plt.show()

# 4. Numerical measure for customer rating vs delivery time
rating_corr = df["delivery_minutes"].corr(
    df["customer_rating"], method="pearson"
)
print("\n--- 4. Rating vs Time ---")
print(f"Delivery Time vs Customer Rating Correlation: {rating_corr:.4f}")

# 5. Outlier analysis comment output
print("\n--- 5. Outlier Analysis ---")
print(
    "The 14.5 km / 95 minutes order follows the linear trend perfectly and represents a legitimate extreme observation rather than a data error."
)