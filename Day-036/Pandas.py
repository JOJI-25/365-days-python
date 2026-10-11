import pandas as pd

orders = pd.DataFrame({
    "order_id": [
        "O101", "O102", "O103", "O104", "O105",
        "O106", "O107", "O108", "O109", "O110"
    ],
    "customer_id": [
        "C01", "C02", "C01", "C03", "C04",
        "C02", "C05", "C03", "C04", "C05"
    ],
    "order_date": [
        "2026-01-05", "2026-01-07", "2026-01-12", "2026-01-15",
        "2026-01-18", "2026-01-20", "2026-01-23", "2026-01-25",
        "2026-01-28", "2026-01-30"
    ],
    "category": [
        "Fiction", "Technology", "Fiction", "Science",
        "Business", "Technology", "Fiction", "Science",
        "Business", "Technology"
    ],
    "amount": [
        850, 1450, 620, 1100, 1750,
        920, 780, 1350, 2100, 1250
    ],
    "status": [
        "Delivered", "Delivered", "Cancelled", "Delivered",
        "Returned", "Delivered", "Delivered", "Cancelled",
        "Delivered", "Returned"
    ]
})

# Task 1
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['day_of_week'] = orders['order_date'].dt.day_name()
print("--- Task 1 ---")
print(orders[['order_id', 'order_date', 'day_of_week']])

# Task 2
total_orders = len(orders)
cancelled_rate = (orders['status'] == 'Cancelled').sum() / total_orders * 100
returned_rate = (orders['status'] == 'Returned').sum() / total_orders * 100
print("\n--- Task 2 ---")
print(f"Cancellation Rate: {cancelled_rate:.2f}%")
print(f"Return Rate: {returned_rate:.2f}%")

# Task 3
orders['is_bad_status'] = orders['status'].isin(['Cancelled', 'Returned'])
customer_summary = orders.groupby('customer_id').agg(
    total_orders=('order_id', 'count'),
    total_spending=('amount', 'sum'),
    cancelled_returned_count=('is_bad_status', 'sum')
).reset_index()
print("\n--- Task 3 ---")
print(customer_summary)

# Task 4
cat_summary = orders.groupby('category').agg(
    avg_amount=('amount', 'mean'),
    total_count=('order_id', 'count'),
    bad_status_count=('is_bad_status', 'sum')
).reset_index()
cat_summary['bad_status_rate'] = cat_summary['bad_status_count'] / cat_summary['total_count'] * 100
print("\n--- Task 4 Category Stats ---")
print(cat_summary)

# Task 5
customer_summary['risk_flag'] = customer_summary.apply(
    lambda row: "At Risk" if row['cancelled_returned_count'] >= (row['total_orders'] / 2) else "Normal",
    axis=1
)
print("\n--- Task 5 ---")
print(customer_summary[['customer_id', 'total_orders', 'cancelled_returned_count', 'risk_flag']])