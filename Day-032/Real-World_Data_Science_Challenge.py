import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
sns.set_theme(style="whitegrid")

# Load customer activity dataset
customers = pd.DataFrame({
    "customer_id": [
        "C001", "C002", "C003", "C004", "C005",
        "C006", "C007", "C008", "C009", "C010",
        "C011", "C012", "C013", "C014", "C015"
    ],
    "age": [
        22, 31, 45, 27, 52,
        36, 24, 41, 29, 58,
        33, 26, 47, 39, 23
    ],
    "monthly_transactions": [
        18, 25, 4, 12, 3,
        20, 15, 5, 22, 2,
        17, 8, 6, 24, 19
    ],
    "monthly_spend": [
        12500, 18500, 3200, 8700, 2100,
        15400, 9800, 4100, 17200, 1800,
        11300, 5200, 3900, 20500, 13100
    ],
    "app_logins": [
        24, 29, 8, 18, 6,
        27, 21, 10, 26, 5,
        23, 14, 11, 30, 25
    ],
    "support_tickets": [
        1, 0, 3, 1, 4,
        0, 1, 3, 1, 5,
        0, 2, 3, 0, 1
    ],
    "days_since_last_transaction": [
        2, 1, 25, 8, 42,
        3, 6, 30, 2, 55,
        4, 18, 35, 1, 3
    ],
    "premium_customer": [
        True, True, False, False, True,
        True, False, False, True, True,
        False, False, True, True, False
    ]
})

# --- A. Data Exploration Summary Stats ---
print("--- A. EDA SUMMARY ---")
print(customers.describe())

# --- B. Feature Engineering ---
customers["spend_per_transaction"] = customers["monthly_spend"] / customers["monthly_transactions"]
customers["logins_per_transaction"] = customers["app_logins"] / customers["monthly_transactions"]
customers["support_ticket_ratio"] = customers["support_tickets"] / (customers["monthly_transactions"] + 1)
customers["recency_risk_flag"] = customers["days_since_last_transaction"] > 14

# --- C. Customer Segmentation ---
def segment_customer(row):
    if row["days_since_last_transaction"] > 30 or row["monthly_transactions"] <= 3:
        return "Inactive"
    elif row["days_since_last_transaction"] > 14 or row["monthly_transactions"] <= 8 or row["support_tickets"] >= 3:
        return "At Risk"
    elif row["monthly_transactions"] <= 18:
        return "Active"
    else:
        return "Highly Active"

customers["segment"] = customers.apply(segment_customer, axis=1)

# --- D. Correlation Matrix ---
print("\n--- D. CORRELATIONS ---")
print(customers[["monthly_transactions", "monthly_spend", "app_logins", "days_since_last_transaction", "support_tickets"]].corr())

# --- E. Risk Prioritisation Scoring ---
max_tx = customers["monthly_transactions"].max()
max_logins = customers["app_logins"].max()

customers["recency_score"] = (customers["days_since_last_transaction"] / 60) * 40
customers["tx_score"] = ((max_tx - customers["monthly_transactions"]) / max_tx) * 30
customers["support_score"] = (customers["support_tickets"] / 5) * 15
customers["login_score"] = ((max_logins - customers["app_logins"]) / max_logins) * 15

customers["inactivity_risk_score"] = (
    customers["recency_score"].clip(upper=40) +
    customers["tx_score"].clip(upper=30) +
    customers["support_score"].clip(upper=15) +
    customers["login_score"].clip(upper=15)
)

print("\n--- E. TOP 5 AT-RISK CUSTOMERS ---")
top_risk = customers.sort_values(by="inactivity_risk_score", ascending=False)[
    ["customer_id", "inactivity_risk_score", "segment", "days_since_last_transaction", "monthly_transactions"]
]
print(top_risk.head(5))

# --- F. Visualizations ---
segment_order = ["Highly Active", "Active", "At Risk", "Inactive"]

# 1. Scatter Plot: App Logins vs Monthly Transactions
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=customers, x="app_logins", y="monthly_transactions", 
    hue="segment", palette="Set1", s=100, edgecolor="black"
)
plt.title("App Logins vs. Monthly Transactions by Segment", fontsize=12, fontweight='bold')
plt.xlabel("App Logins", fontsize=10)
plt.ylabel("Monthly Transactions", fontsize=10)
plt.legend(title="Customer Segment", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('vis_logins_vs_tx.png', dpi=300)
plt.show()

# 2. Bar Plot: Average Days Since Last Transaction by Segment
plt.figure(figsize=(8, 5))
avg_recency = customers.groupby("segment")["days_since_last_transaction"].mean().reindex(segment_order)
ax = sns.barplot(x=avg_recency.index, y=avg_recency.values, hue=avg_recency.index, palette="Blues_d", legend=False)
plt.title("Average Days Since Last Transaction by Customer Segment", fontsize=12, fontweight='bold')
plt.xlabel("Customer Segment", fontsize=10)
plt.ylabel("Average Days Since Last Transaction", fontsize=10)
for p in ax.patches:
    ax.annotate(f"{p.get_height():.1f} days", (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=9, color='black', xytext=(0, 3), textcoords='offset points')
plt.tight_layout()
plt.savefig('vis_recency_by_segment.png', dpi=300)
plt.show()

# 3. Box Plot: Support Tickets Across Segments
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=customers, x="segment", y="support_tickets", 
    order=segment_order, hue="segment", palette="Purples", legend=False
)
plt.title("Support Ticket Distribution Across Customer Segments", fontsize=12, fontweight='bold')
plt.xlabel("Customer Segment", fontsize=10)
plt.ylabel("Support Tickets Logged", fontsize=10)
plt.tight_layout()
plt.savefig('vis_support_by_segment.png', dpi=300)
plt.show()