import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

orders = pd.DataFrame({
    "order_id": ["O001", "O002", "O003", "O004", "O005", "O006", "O007", "O008", "O009", "O010", "O011", "O012", "O013", "O014", "O015"],
    "distance_km": [2.1, 5.4, 1.8, 8.2, 3.5, 7.1, 2.7, 9.5, 4.2, 6.8, 1.5, 5.9, 3.1, 7.8, 2.4],
    "delivery_time_min": [25, 42, 21, 61, 34, 55, 29, 72, 39, 51, 20, 45, 31, 65, 26],
    "order_value": [450, 700, 320, 850, 520, 680, 410, 920, 590, 760, 280, 640, 480, 810, 350],
    "restaurant_rating": [4.6, 4.1, 4.8, 3.7, 4.4, 3.9, 4.5, 3.5, 4.2, 4.0, 4.9, 4.1, 4.3, 3.8, 4.7],
    "driver_rating": [4.7, 4.2, 4.8, 3.6, 4.5, 4.0, 4.6, 3.4, 4.3, 4.1, 4.9, 4.2, 4.4, 3.7, 4.8],
    "payment_method": ["UPI", "Card", "UPI", "COD", "UPI", "Card", "UPI", "COD", "Card", "UPI", "UPI", "Card", "COD", "Card", "UPI"],
    "cancelled": [False, False, False, True, False, True, False, True, False, True, False, False, False, True, False]
})

# 1. Dataset Structure, Missing Values, and Duplicates
print("Shape:", orders.shape)
print("Missing Values:\n", orders.isnull().sum())
print("Duplicate Rows:", orders.duplicated().sum())

# 2. Overall Cancellation Rate
cancellation_rate = orders["cancelled"].mean() * 100
print(f"Overall Cancellation Rate: {cancellation_rate:.2f}%")


pattern_comparison = orders.groupby("cancelled").mean(numeric_only=True)
print(pattern_comparison[["distance_km", "delivery_time_min", "order_value", "restaurant_rating", "driver_rating"]])
print("\nCancellation Rate by Payment Method:\n", orders.groupby("payment_method")["cancelled"].mean())

# 1. Speed-Distance Ratio (Estimated speed: km per minute)
orders["speed_km_min"] = orders["distance_km"] / orders["delivery_time_min"]

# 2. Low Quality Flag (Average of restaurant and driver ratings)
orders["avg_quality_rating"] = (orders["restaurant_rating"] + orders["driver_rating"]) / 2

# 3. High Risk Payment Flag (1 if COD, 0 otherwise)
orders["is_cod"] = orders["payment_method"].apply(lambda x: 1 if x == "COD" else 0)

def classify_risk(row):
    if row["payment_method"] == "COD" and (row["delivery_time_min"] > 50 or row["avg_quality_rating"] < 3.8):
        return "High Risk"
    elif row["distance_km"] > 6 or row["avg_quality_rating"] < 4.1:
        return "Medium Risk"
    else:
        return "Low Risk"

orders["risk_segment"] = orders.apply(classify_risk, axis=1)
print(orders[["order_id", "risk_segment", "cancelled"]])

plt.figure(figsize=(14, 4))

# 1. Numerical vs Cancellation Status
plt.subplot(1, 3, 1)
sns.boxplot(x="cancelled", y="delivery_time_min", data=orders, palette="Set2")
plt.title("Delivery Time by Cancellation Status")

# 2. Categorical vs Cancellation Behavior
plt.subplot(1, 3, 2)
sns.barplot(x="payment_method", y="cancelled", data=orders, ci=None, palette="Blues")
plt.title("Cancellation Rate by Payment Method")

# 3. Quality Rating vs Cancellation
plt.subplot(1, 3, 3)
sns.scatterplot(x="avg_quality_rating", y="order_value", hue="cancelled", data=orders, s=100)
plt.title("Order Value vs Quality by Cancellation")

plt.tight_layout()
plt.show()