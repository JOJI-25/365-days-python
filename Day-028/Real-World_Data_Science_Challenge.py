import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Define the 'orders' dataset before referencing it in code
orders = [
    {
        "order_id": 1001,
        "customer_id": "C101",
        "category": "Electronics",
        "amount": 1200.50,
        "delivery_time": 25,
        "status": "Completed",
    },
    {
        "order_id": 1002,
        "customer_id": "C102",
        "category": "Clothing",
        "amount": 450.00,
        "delivery_time": 30,
        "status": "Completed",
    },
    {
        "order_id": 1003,
        "customer_id": "C101",
        "category": "Electronics",
        "amount": 800.00,
        "delivery_time": 28,
        "status": "Completed",
    },
    {
        "order_id": 1004,
        "customer_id": "C103",
        "category": "Home & Kitchen",
        "amount": 2100.00,
        "delivery_time": 75,
        "status": "Completed",
    },  # Outlier delivery time
    {
        "order_id": 1005,
        "customer_id": "C102",
        "category": "Electronics",
        "amount": 750.00,
        "delivery_time": 32,
        "status": "Cancelled",
    },
    {
        "order_id": 1006,
        "customer_id": "C104",
        "category": "Clothing",
        "amount": 300.00,
        "delivery_time": 22,
        "status": "Completed",
    },
    {
        "order_id": 1007,
        "customer_id": "C103",
        "category": "Home & Kitchen",
        "amount": 950.00,
        "delivery_time": 29,
        "status": "Completed",
    },
    {
        "order_id": 1008,
        "customer_id": "C101",
        "category": "Books",
        "amount": 150.00,
        "delivery_time": 24,
        "status": "Completed",
    },
    {
        "order_id": 1009,
        "customer_id": "C104",
        "category": "Electronics",
        "amount": 650.00,
        "delivery_time": 31,
        "status": "Completed",
    },
    {
        "order_id": 1010,
        "customer_id": "C105",
        "category": "Home & Kitchen",
        "amount": 1800.00,
        "delivery_time": 27,
        "status": "Completed",
    },
]

# Convert 'orders' list of dicts to a pandas DataFrame
df_orders = pd.DataFrame(orders)

# 2. Data Filtering & Analysis
# Filter completed orders only
completed_orders = df_orders[df_orders["status"] == "Completed"].copy()

# Calculate key business metrics
total_revenue = completed_orders["amount"].sum()
avg_order_value = completed_orders["amount"].mean()

# Category-level breakdown
category_summary = (
    completed_orders.groupby("category")
    .agg(
        total_revenue=("amount", "sum"),
        order_count=("order_id", "count"),
        avg_delivery_time=("delivery_time", "mean"),
    )
    .reset_index()
)

# 3. Identify Delivery Time Outliers using IQR (Interquartile Range)
delivery_times = completed_orders["delivery_time"].values
q75, q25 = np.percentile(delivery_times, [75, 25])
iqr = q75 - q25
upper_bound = q75 + (1.5 * iqr)
outliers = completed_orders[completed_orders["delivery_time"] > upper_bound]

# 4. Print Data Analysis Summary
print("=== Real-World Data Science Challenge Results ===")
print(f"Total Revenue (Completed Orders): ${total_revenue:,.2f}")
print(f"Average Order Value (AOV): ${avg_order_value:,.2f}")

print("\n--- Revenue & Delivery Summary by Category ---")
print(category_summary.to_string(index=False))

print("\n--- Delivery Outliers (> Upper Bound) ---")
if not outliers.empty:
    print(outliers[["order_id", "customer_id", "amount", "delivery_time"]])
else:
    print("No delivery time outliers detected.")
