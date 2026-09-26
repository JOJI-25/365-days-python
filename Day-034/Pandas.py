import pandas as pd

sales = pd.DataFrame({
    "month": [
        "2026-01", "2026-01", "2026-01", "2026-01",
        "2026-02", "2026-02", "2026-02", "2026-02",
        "2026-03", "2026-03", "2026-03", "2026-03",
        "2026-04", "2026-04", "2026-04", "2026-04"
    ],
    "product": [
        "Laptop", "Phone", "Tablet", "Monitor",
        "Laptop", "Phone", "Tablet", "Monitor",
        "Laptop", "Phone", "Tablet", "Monitor",
        "Laptop", "Phone", "Tablet", "Monitor"
    ],
    "units_sold": [
        120, 180, 90, 75,
        135, 170, 105, 82,
        150, 165, 110, 88,
        172, 190, 98, 95
    ],
    "revenue": [
        720000, 540000, 270000, 225000,
        810000, 510000, 315000, 246000,
        900000, 495000, 330000, 264000,
        1032000, 570000, 294000, 285000
    ]
})

# 1. Convert month into datetime representation
sales['month'] = pd.to_datetime(sales['month'])
sales = sales.sort_values(['product', 'month'])

# 2 & 3. Total revenue and total units sold for each product
total_revenue = sales.groupby('product')['revenue'].sum()
total_units = sales.groupby('product')['units_sold'].sum()

# 4 & 5. Month-over-month revenue change and percentage growth
sales['prev_revenue'] = sales.groupby('product')['revenue'].shift(1)
sales['mom_revenue_change'] = sales['revenue'] - sales['prev_revenue']
sales['mom_growth_pct'] = (sales['mom_revenue_change'] / sales['prev_revenue']) * 100

# 6. Highlights
highest_revenue_product = total_revenue.idxmax()
highest_units_product = total_units.idxmax()
avg_monthly_growth = sales.groupby('product')['mom_growth_pct'].mean()
highest_growth_product = avg_monthly_growth.idxmax()

# 7. 3-month rolling average of revenue
sales['rolling_3m_revenue'] = sales.groupby('product')['revenue'].rolling(window=3, min_periods=1).mean().reset_index(0, drop=True)

# 8. Identify products with a revenue decline from one month to the next
revenue_declines = sales[sales['mom_revenue_change'] < 0]

# 9. Product-level summary
summary = sales.groupby('product').agg(
    total_revenue=('revenue', 'sum'),
    avg_monthly_revenue=('revenue', 'mean'),
    total_units_sold=('units_sold', 'sum'),
    avg_monthly_growth=('mom_growth_pct', 'mean'),
    highest_monthly_revenue=('revenue', 'max')
).reset_index()

# Rank products according to total revenue
summary['revenue_rank'] = summary['total_revenue'].rank(ascending=False, method='min')
summary = summary.sort_values('total_revenue', ascending=False)

print("--- Product Summary Table ---")
print(summary.to_string(index=False))

print(f"\nHighest Total Revenue: {highest_revenue_product}")
print(f"Highest Total Unit Sales: {highest_units_product}")
print(f"Highest Average Monthly Growth: {highest_growth_product}")
print(f"Is highest revenue product also the highest growth product? {highest_revenue_product == highest_growth_product}")