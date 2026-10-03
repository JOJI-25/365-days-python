import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
data = {
    "restaurant_id": range(401, 413),
    "cuisine": [
        "Indian",
        "Chinese",
        "Italian",
        "Indian",
        "Mexican",
        "Chinese",
        "Italian",
        "Indian",
        "Mexican",
        "Chinese",
        "Italian",
        "Mexican",
    ],
    "orders": [420, 310, 280, 510, 190, 350, 260, 470, 220, 390, 300, 240],
    "avg_order_value": [
        520,
        610,
        780,
        490,
        690,
        580,
        820,
        510,
        720,
        600,
        760,
        680,
    ],
    "rating": [4.4, 4.1, 4.6, 4.3, 3.9, 4.2, 4.7, 4.5, 4.0, 4.3, 4.5, 4.1],
    "complaints": [12, 18, 9, 15, 22, 16, 7, 11, 20, 14, 8, 19],
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# Task 1: Revenue column & restaurant with highest revenue
# ---------------------------------------------------------
df["revenue"] = df["orders"] * df["avg_order_value"]
top_revenue_restaurant = df.loc[df["revenue"].idxmax()]

print("=== Task 1: Highest Revenue Restaurant ===")
print(
    f"Restaurant ID : {top_revenue_restaurant['restaurant_id']}\n"
    f"Cuisine       : {top_revenue_restaurant['cuisine']}\n"
    f"Revenue       : {top_revenue_restaurant['revenue']:,}\n"
)

# ---------------------------------------------------------
# Task 2: Average metrics per cuisine
# ---------------------------------------------------------
cuisine_stats = (
    df.groupby("cuisine")
    .agg(
        avg_orders=("orders", "mean"),
        avg_order_value=("avg_order_value", "mean"),
        avg_rating=("rating", "mean"),
        avg_complaints=("complaints", "mean"),
    )
    .reset_index()
)

print("=== Task 2: Cuisine Averages ===")
print(cuisine_stats.to_string(index=False))
print()

# ---------------------------------------------------------
# Task 3: Complaint rate & restaurant with highest rate
# ---------------------------------------------------------
df["complaint_rate"] = (df["complaints"] / df["orders"]) * 100
top_complaint_restaurant = df.loc[df["complaint_rate"].idxmax()]

print("=== Task 3: Highest Complaint Rate Restaurant ===")
print(
    f"Restaurant ID  : {top_complaint_restaurant['restaurant_id']}\n"
    f"Cuisine        : {top_complaint_restaurant['cuisine']}\n"
    f"Complaint Rate : {top_complaint_restaurant['complaint_rate']:.2f}%\n"
)

# ---------------------------------------------------------
# Task 4: Correlation analysis & scatter plot visualization
# ---------------------------------------------------------
corr_pearson = df["rating"].corr(df["revenue"], method="pearson")
corr_spearman = df["rating"].corr(df["revenue"], method="spearman")

print("=== Task 4: Correlation (Rating vs Revenue) ===")
print(f"Pearson Correlation  (r)     : {corr_pearson:.4f}")
print(f"Spearman Correlation (rho)   : {corr_spearman:.4f}")

# Visualization
plt.figure(figsize=(9, 5))
colors = {
    "Indian": "tab:orange",
    "Chinese": "tab:red",
    "Italian": "tab:green",
    "Mexican": "tab:blue",
}

for cuisine, group in df.groupby("cuisine"):
    plt.scatter(
        group["rating"],
        group["revenue"],
        label=cuisine,
        color=colors.get(cuisine, "black"),
        s=90,
        alpha=0.85,
        edgecolors="k",
    )

plt.title("Customer Rating vs. Total Revenue by Restaurant", fontsize=13)
plt.xlabel("Rating (Out of 5.0)", fontsize=11)
plt.ylabel("Revenue", fontsize=11)
plt.legend(title="Cuisine")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Task 5: Recommendation summary
# ---------------------------------------------------------
cuisine_summary = (
    df.groupby("cuisine")
    .agg(
        total_revenue=("revenue", "sum"),
        avg_orders=("orders", "mean"),
        avg_rating=("rating", "mean"),
        avg_complaint_rate=("complaint_rate", "mean"),
    )
    .sort_values(by="total_revenue", ascending=False)
)

print("\n=== Task 5: Cuisine Comparison for Expansion ===")
print(cuisine_summary.to_string())