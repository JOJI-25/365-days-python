import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data setup
data = {
    "transaction_id": range(5001, 5013),
    "store": [
        "Kochi", "Kochi", "Trivandrum", "Trivandrum",
        "Kozhikode", "Kozhikode", "Kochi", "Trivandrum",
        "Kozhikode", "Kochi", "Trivandrum", "Kozhikode"
    ],
    "items": [8, 15, 5, 19, 11, 23, 7, 16, 9, 21, 13, 18],
    "gross_amount": [
        820, 1450, 510, 1820, 1040, 2250,
        760, 1580, 890, 2050, 1270, 1740
    ],
    "discount": [
        40, 120, 20, 160, 70, 220,
        30, 130, 50, 190, 90, 150
    ],
    "customer_rating": [
        4.2, 4.5, 4.0, 4.6, 4.1, 4.7,
        4.3, 4.4, 4.0, 4.6, 4.2, 4.5
    ]
}
df = pd.DataFrame(data)

# 1. Create net_amount and discount_rate columns and identify highest discount rate
df["net_amount"] = df["gross_amount"] - df["discount"]
df["discount_rate"] = df["discount"] / df["gross_amount"]

highest_discount_row = df.loc[df["discount_rate"].idxmax()]

print("--- 1. Net Amount & Discount Rate ---")
print(f"Transaction with Highest Discount Rate: ID {highest_discount_row['transaction_id']} "
      f"({highest_discount_row['discount_rate']:.2%} discount rate)\n")

# 2. Compare the three stores using total net sales, average transaction value, items, and rating
store_comparison = df.groupby("store").agg(
    total_net_sales=("net_amount", "sum"),
    avg_transaction_value=("net_amount", "mean"),
    avg_items=("items", "mean"),
    avg_rating=("customer_rating", "mean")
).reset_index()

print("--- 2. Store Comparison ---")
print(store_comparison.to_string(index=False))
print("\n")

# 3. Create basket-size categories and determine average net amount for each category
df["basket_size"] = pd.cut(
    df["items"], 
    bins=[0, 10, 18, 50], 
    labels=["Small (1-10)", "Medium (11-18)", "Large (19+)"]
)

basket_avg = df.groupby("basket_size", observed=False)["net_amount"].mean().reset_index()

print("--- 3. Average Net Amount by Basket Size ---")
print(basket_avg.to_string(index=False))
print("\n")

# 4. Analyze relationship between number of items and net transaction value using correlation
correlation = df["items"].corr(df["net_amount"])
print("--- 4. Correlation Analysis ---")
print(f"Correlation between Number of Items and Net Amount: {correlation:.4f}\n")

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="items", y="net_amount", hue="store", s=120, palette="Set2")
plt.title("Relationship Between Number of Items and Net Transaction Value")
plt.xlabel("Number of Items (Basket Size)")
plt.ylabel("Net Transaction Amount")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Store")
plt.tight_layout()
plt.show()

# 5. Business Conclusion & Decision Support
print("--- 5. Business Insights & Conclusion ---")
print("""
Conclusion:
Yes, larger baskets are strongly and positively correlated with higher net transaction values. 
With a correlation coefficient close to +1, the data shows that increased basket sizes reliably 
yield higher revenue and net returns for the supermarket. 

Is it strong enough to support a business decision?
While the correlation is very strong, the current dataset contains only 12 transactions. 
Therefore, while it provides a clear directional signal supporting promotions for larger baskets (e.g., bundle discounts), 
management should validate this trend with a larger sample size before executing major capital or strategic decisions.
""")