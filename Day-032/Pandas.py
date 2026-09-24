import pandas as pd

inventory = pd.DataFrame({
    "date": [
        "2026-09-01", "2026-09-01", "2026-09-01",
        "2026-09-02", "2026-09-02", "2026-09-02",
        "2026-09-03", "2026-09-03", "2026-09-03",
        "2026-09-04", "2026-09-04", "2026-09-04"
    ],
    "product": [
        "Rice", "Milk", "Coffee",
        "Rice", "Milk", "Coffee",
        "Rice", "Milk", "Coffee",
        "Rice", "Milk", "Coffee"
    ],
    "stock": [
        120, 80, 55,
        95, 62, 48,
        70, 45, 42,
        48, 31, 36
    ],
    "units_sold": [
        25, 18, 12,
        30, 20, 15,
        22, 17, 13,
        28, 21, 14
    ],
    "reorder_level": [
        50, 40, 30,
        50, 40, 30,
        50, 40, 30,
        50, 40, 30
    ]
})

# 1. Convert date to a datetime column
inventory["date"] = pd.to_datetime(inventory["date"])

# 2. Feature indicating whether each product has fallen below its reorder level
inventory["below_reorder"] = inventory["stock"] < inventory["reorder_level"]

# 3. Average daily units sold for each product
avg_units_sold = inventory.groupby("product")["units_sold"].mean()
print("=== 3. Average Daily Units Sold ===")
print(avg_units_sold)

# 4. Product with the fastest inventory depletion
fastest_depletion = avg_units_sold.idxmax()
print(f"\n=== 4. Fastest Inventory Depletion ===\n{fastest_depletion}")

# 5. Percentage reduction in stock from first day to final day
first_last_stock = inventory.sort_values("date").groupby("product").agg(
    initial_stock=("stock", "first"),
    final_stock=("stock", "last")
)
stock_reduction_pct = (
    (first_last_stock["initial_stock"] - first_last_stock["final_stock"]) / first_last_stock["initial_stock"]
) * 100
print("\n=== 5. Percentage Reduction in Stock ===")
print(stock_reduction_pct)

# 6. First date on which each product fell below its reorder level
first_reorder_date = inventory[inventory["below_reorder"]].groupby("product")["date"].min()
print("\n=== 6. First Reorder-Alert Date ===")
print(first_reorder_date)

# 7. Rank products according to their final stock level (lowest stock = Rank 1)
final_stocks = inventory.sort_values("date").groupby("product")["stock"].last()
stock_rank = final_stocks.rank(ascending=True)
print("\n=== 7. Final Stock Ranking (Lowest stock = Rank 1) ===")
print(stock_rank)

# 8. 3-day rolling average of units sold for each product
inventory = inventory.sort_values(["product", "date"])
inventory["rolling_avg_units_sold"] = (
    inventory.groupby("product")["units_sold"]
    .rolling(window=3, min_periods=1)
    .mean()
    .reset_index(level=0, drop=True)
)
print("\n=== 8. 3-Day Rolling Average of Units Sold ===")
print(inventory[["date", "product", "units_sold", "rolling_avg_units_sold"]])

# 9. Create a comprehensive summary
summary = inventory.groupby("product").agg(
    initial_stock=("stock", "first"),
    final_stock=("stock", "last"),
    total_units_sold=("units_sold", "sum"),
    avg_daily_sales=("units_sold", "mean"),
    max_daily_sales=("units_sold", "max")
)
summary["first_reorder_date"] = first_reorder_date
print("\n=== 9. Comprehensive Summary Table ===")
print(summary)

# 10. Identify product with highest replenishment priority
summary["deficit"] = inventory.groupby("product")["reorder_level"].first() - summary["final_stock"]
highest_priority_product = summary["deficit"].idxmax()
print(f"\n=== 10. Highest Replenishment Priority ===\n{highest_priority_product}")