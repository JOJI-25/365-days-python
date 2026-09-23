import pandas as pd

# Define the datasets
orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "customer_id": ["C01", "C02", "C01", "C03", "C04", "C02", "C05", "C03"],
    "product_id": ["P01", "P02", "P03", "P01", "P04", "P03", "P02", "P04"],
    "quantity": [2, 1, 3, 1, 2, 2, 4, 1],
    "order_value": [2400, 900, 2100, 1200, 1800, 1400, 3600, 950]
})

customers = pd.DataFrame({
    "customer_id": ["C01", "C02", "C03", "C04", "C05"],
    "city": ["Kochi", "Bengaluru", "Chennai", "Kochi", "Bengaluru"],
    "customer_segment": ["Premium", "Regular", "Premium", "Regular", "New"]
})

products = pd.DataFrame({
    "product_id": ["P01", "P02", "P03", "P04"],
    "category": ["Electronics", "Home", "Electronics", "Furniture"],
    "product_name": ["Headphones", "Mixer", "Keyboard", "Chair"]
})

# Step 1: Build the combined analytical dataset using sequential merges
combined_df = orders.merge(customers, on="customer_id", how="left").merge(products, on="product_id", how="left")

# 1. Total revenue by customer city
revenue_by_city = combined_df.groupby("city")["order_value"].sum()

# 2. Total revenue by product category
revenue_by_category = combined_df.groupby("category")["order_value"].sum()

# 3. Total revenue by customer segment
revenue_by_segment = combined_df.groupby("customer_segment")["order_value"].sum()

# 4. Customer who generated the highest total revenue
top_customer = combined_df.groupby("customer_id")["order_value"].sum().idxmax()

# 5. Product category with the highest quantity sold
top_category_qty = combined_df.groupby("category")["quantity"].sum().idxmax()

# 6. Average order value for each customer segment
avg_order_value_segment = combined_df.groupby("customer_segment")["order_value"].mean()

# 7. City with the highest average order value
city_avg_order = combined_df.groupby("city")["order_value"].mean()
top_city_aov = city_avg_order.idxmax()

# 8. Pivot table: City × Product Category with total revenue
pivot_city_category = combined_df.pivot_table(index="city", columns="category", values="order_value", aggfunc="sum", fill_value=0)

# 9. Customers who have placed more than one order
order_counts = combined_df.groupby("customer_id")["order_id"].count()
frequent_customers = order_counts[order_counts > 1].index.tolist()

# 10. Premium vs Regular revenue per customer comparison
segment_metrics = combined_df.groupby("customer_segment").agg(
    total_revenue=("order_value", "sum"),
    unique_customers=("customer_id", "nunique")
)
segment_metrics["revenue_per_customer"] = segment_metrics["total_revenue"] / segment_metrics["unique_customers"]
premium_vs_regular = segment_metrics.loc["Premium", "revenue_per_customer"] > segment_metrics.loc["Regular", "revenue_per_customer"]

# --- Output Results ---
print("--- Combined Dataset Sample ---")
print(combined_df.head(), "\n")
print("Revenue by City:\n", revenue_by_city, "\n")
print("Revenue by Category:\n", revenue_by_category, "\n")
print("Revenue by Segment:\n", revenue_by_segment, "\n")
print("Top Customer:", top_customer, "\n")
print("Top Category by Quantity:", top_category_qty, "\n")
print("Average Order Value by Segment:\n", avg_order_value_segment, "\n")
print("City with Highest AOV:", top_city_aov, "\n")
print("Pivot Table (City x Category):\n", pivot_city_category, "\n")
print("Customers with >1 Order:", frequent_customers, "\n")
print("Does Premium generate more revenue per customer than Regular?", premium_vs_regular)
