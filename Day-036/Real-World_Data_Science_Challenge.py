import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "customer_id": [
        "C101", "C102", "C103", "C104", "C105",
        "C106", "C107", "C108", "C109", "C110",
        "C111", "C112"
    ],
    "orders": [2, 12, 5, 8, 1, 15, 4, 10, 3, 7, 14, 2],
    "total_spend": [
        1800, 15600, 4200, 9200, 700,
        21000, 3500, 11800, 2500, 7600, 18500, 1200
    ],
    "avg_order_value": [
        900, 1300, 840, 1150, 700, 1400,
        875, 1180, 833, 1086, 1321, 600
    ],
    "website_visits": [
        8, 42, 18, 30, 5, 55,
        16, 38, 11, 27, 48, 7
    ],
    "discount_usage_pct": [
        65, 20, 50, 25, 80, 15,
        60, 30, 70, 35, 18, 75
    ]
})

print("--- Summary Statistics ---")
print(customers.describe())
print("\n--- Correlation Matrix ---")
print(customers.corr(numeric_only=True))
print("\n--- Top 3 by Orders ---")
print(customers.nlargest(3, "orders"))
print("\n--- Least 3 by Orders ---")
print(customers.nsmallest(3, "orders"))
print("\n--- Correlation: Orders vs Visits ---")
print(customers[["orders", "website_visits"]].corr())

# Identify high-value customers
customer_segments = customers.copy()
customer_segments["segment"] = customer_segments["total_spend"].apply(
    lambda x: "High" if x >= 10000 else "Medium" if x >= 5000 else "Low"
)
print("\n--- Customer Segments ---")
print(customer_segments[["customer_id", "total_spend", "segment"]])