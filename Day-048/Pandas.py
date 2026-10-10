import pandas as pd
import numpy as np

# Given Data
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "product_id": ["P01", "P02", "P03", "P01", "P04", "P02", "P05", "P03", "P04", "P06"],
    "quantity": [2, 1, 3, 1, 2, 4, 1, 2, 3, 1],
    "selling_price": [15000, 42000, 8500, 14800, 32000, 41500, 12000, 8700, 31500, 25000],
    "order_status": [
        "Completed", "Completed", "Completed", "Returned",
        "Completed", "Completed", "Completed", "Cancelled",
        "Completed", "Completed"
    ]
})

products = pd.DataFrame({
    "product_id": ["P01", "P02", "P03", "P04", "P05"],
    "category": [
        "Accessories", "Computers", "Accessories",
        "Electronics", "Accessories"
    ],
    "unit_cost": [9500, 30000, 5000, 23000, 8000]
})

# -------------------------------------------------------------
# Task 1: Inspect tables for missing values, duplicates, and unmatched IDs
# -------------------------------------------------------------
print("--- Task 1: Data Quality Inspection ---")
print("Missing values in orders:\n", orders.isnull().sum())
print("Missing values in products:\n", products.isnull().sum())
print("Duplicate product IDs in products:", products['product_id'].duplicated().sum())

# Identify unmatched product IDs
unmatched_ids = set(orders['product_id']) - set(products['product_id'])
print(f"Unmatched product IDs in orders: {unmatched_ids}\n")

# -------------------------------------------------------------
# Task 2: Join tables preserving unmatched orders (Left Join)
# -------------------------------------------------------------
merged_df = pd.merge(orders, products, on="product_id", how="left")

print("--- Task 2: Merged Data (Sample) ---")
print(merged_df[['order_id', 'product_id', 'order_status', 'category', 'unit_cost']].head(3))
print()

# -------------------------------------------------------------
# Task 3: Calculate gross sales and profit for completed orders
# -------------------------------------------------------------
# Filter out Returned and Cancelled orders
completed_df = merged_df[merged_df['order_status'] == 'Completed'].copy()

# Handle missing unit costs (e.g., for unmatched product P06) by filling with 0 or handling separately
completed_df['unit_cost'] = completed_df['unit_cost'].fillna(0)

# Calculate metrics
completed_df['gross_sales'] = completed_df['quantity'] * completed_df['selling_price']
completed_df['total_cost'] = completed_df['quantity'] * completed_df['unit_cost']
completed_df['gross_profit'] = completed_df['gross_sales'] - completed_df['total_cost']

print("--- Task 3: Completed Orders Metrics (Sample) ---")
print(completed_df[['order_id', 'product_id', 'quantity', 'gross_sales', 'gross_profit']].to_string())
print()

# -------------------------------------------------------------
# Task 4: Compare product categories by sales, profit, and margin
# -------------------------------------------------------------
# Fill missing categories for unmatched items as 'Unknown'
completed_df['category'] = completed_df['category'].fillna('Unknown')

category_summary = completed_df.groupby('category').agg(
    total_completed_sales=('gross_sales', 'sum'),
    total_gross_profit=('gross_profit', 'sum')
).reset_index()

# Gross Profit Margin = (Total Gross Profit / Total Gross Sales) * 100
category_summary['gross_profit_margin_percent'] = (
    category_summary['total_gross_profit'] / category_summary['total_completed_sales']
) * 100

print("--- Task 4: Product Category Comparison ---")
print(category_summary.to_string(index=False))
print()

# -------------------------------------------------------------
# Task 5: Summary and Recommendation
# -------------------------------------------------------------
print("--- Task 5: Analysis Insights ---")
print("1. Data Quality Issue: Product 'P06' appears in orders (order_id 110) but is missing from the products table, resulting in missing cost and category data.")
print("2. Recommendation: The retailer should first fix the data integrity gap by adding missing product master records (like P06), and then focus attention on categories with high profitability and strong data completeness.")