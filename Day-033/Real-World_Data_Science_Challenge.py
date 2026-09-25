import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ----------------- 1. Dataset Setup -----------------
customers = pd.DataFrame(
    {
        "customer_id": [
            "C001",
            "C002",
            "C003",
            "C004",
            "C005",
            "C006",
            "C007",
            "C008",
            "C009",
            "C010",
            "C011",
            "C012",
            "C013",
            "C014",
            "C015",
        ],
        "orders_last_90_days": [
            14,
            8,
            2,
            11,
            1,
            16,
            5,
            3,
            12,
            2,
            9,
            4,
            6,
            15,
            7,
        ],
        "avg_order_value": [
            850,
            1200,
            650,
            940,
            1500,
            780,
            1100,
            700,
            920,
            1350,
            820,
            1050,
            760,
            890,
            980,
        ],
        "discount_usage_rate": [
            0.20,
            0.35,
            0.70,
            0.15,
            0.80,
            0.10,
            0.55,
            0.65,
            0.25,
            0.75,
            0.30,
            0.60,
            0.45,
            0.18,
            0.40,
        ],
        "avg_delivery_time": [
            28,
            31,
            42,
            27,
            50,
            25,
            36,
            45,
            29,
            48,
            32,
            39,
            35,
            26,
            33,
        ],
        "avg_rating_given": [
            4.6,
            4.3,
            3.5,
            4.7,
            3.1,
            4.8,
            4.0,
            3.4,
            4.5,
            3.2,
            4.2,
            3.8,
            4.1,
            4.7,
            4.4,
        ],
        "support_tickets": [1, 2, 5, 0, 7, 0, 3, 6, 1, 6, 2, 4, 3, 0, 1],
        "days_since_last_order": [
            3,
            7,
            35,
            5,
            60,
            2,
            14,
            40,
            6,
            55,
            10,
            22,
            18,
            4,
            8,
        ],
    }
)

# ----------------- Part A & D: Value & Feature Engineering -----------------
# Feature 1 (Part A): Estimated 90-day Customer Revenue
customers["estimated_revenue_90d"] = (
    customers["orders_last_90_days"] * customers["avg_order_value"]
)

# Feature 2: Support Ticket Rate per Order (Operational friction)
customers["tickets_per_order"] = (
    customers["support_tickets"] / customers["orders_last_90_days"]
).round(2)

# Feature 3: Full-Price Organic Orders (Non-discounted purchase volume)
customers["full_price_orders"] = (
    customers["orders_last_90_days"] * (1 - customers["discount_usage_rate"])
).round(1)

# Feature 4: Recency Engagement Momentum (Ratio of order frequency to recency days)
customers["recency_velocity"] = (
    customers["orders_last_90_days"] / (customers["days_since_last_order"] + 1)
).round(2)


# ----------------- Part C: Customer Segmentation -----------------
def assign_segment(row):
    high_value = row["estimated_revenue_90d"] >= 8000
    is_active = (
        row["days_since_last_order"] <= 14 and row["orders_last_90_days"] >= 6
    )

    if high_value and is_active:
        return "Champions (High Value, Active)"
    elif not high_value and is_active:
        return "Loyal Regulars (Mid/Low Value, Active)"
    elif high_value and not is_active:
        return "High-Value At Risk"
    else:
        return "Low-Value Inactive / Lost"


customers["segment"] = customers.apply(assign_segment, axis=1)


# ----------------- Part F: Retention Priority Score -----------------
# Min-Max normalization helper
def min_max(series):
    return (series - series.min()) / (series.max() - series.min())


# Risk factors (higher value = higher risk)
r_recency = min_max(customers["days_since_last_order"])
r_tickets = min_max(customers["support_tickets"])
r_delivery = min_max(customers["avg_delivery_time"])
r_rating = min_max(5.0 - customers["avg_rating_given"])
r_inactivity = min_max(
    customers["orders_last_90_days"].max() - customers["orders_last_90_days"]
)

# Churn Risk Index (0 - 100)
customers["churn_risk_score"] = (
    (
        0.30 * r_recency
        + 0.25 * r_tickets
        + 0.20 * r_delivery
        + 0.15 * r_rating
        + 0.10 * r_inactivity
    )
    * 100
).round(1)

# Retention Priority Score: Weighted by AOV potential so we rescue high-value customers first
value_weight = min_max(customers["avg_order_value"])
customers["retention_priority_score"] = (
    0.60 * customers["churn_risk_score"] + 0.40 * (value_weight * 100)
).round(1)

# ----------------- Part E: Visualizations -----------------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Order Frequency vs Estimated Revenue (Bubble Size = AOV)
scatter = axes[0].scatter(
    customers["orders_last_90_days"],
    customers["estimated_revenue_90d"],
    s=customers["avg_order_value"] / 3,
    c=customers["discount_usage_rate"],
    cmap="viridis",
    alpha=0.8,
    edgecolors="black",
)
axes[0].set_title(
    "1. Order Frequency vs. Estimated Revenue\n(Size = AOV, Color = Discount Rate)"
)
axes[0].set_xlabel("Orders in Last 90 Days")
axes[0].set_ylabel("Estimated 90-Day Revenue (₹)")
axes[0].grid(True, linestyle="--", alpha=0.5)
fig.colorbar(scatter, ax=axes[0], label="Discount Usage Rate")

# Plot 2: Delivery Time vs Order Frequency (Color = Support Tickets)
scatter2 = axes[1].scatter(
    customers["avg_delivery_time"],
    customers["orders_last_90_days"],
    c=customers["support_tickets"],
    cmap="Reds",
    s=120,
    edgecolors="black",
)
axes[1].set_title(
    "2. Delivery Time vs. Order Frequency\n(Color = Support Tickets)"
)
axes[1].set_xlabel("Average Delivery Time (minutes)")
axes[1].set_ylabel("Orders in Last 90 Days")
axes[1].grid(True, linestyle="--", alpha=0.5)
fig.colorbar(scatter2, ax=axes[1], label="Support Tickets Logged")

# Plot 3: Churn Risk vs. Basket Size (AOV) by Segment
colors = {
    "Champions (High Value, Active)": "#2ca02c",
    "Loyal Regulars (Mid/Low Value, Active)": "#1f77b4",
    "High-Value At Risk": "#ff7f0e",
    "Low-Value Inactive / Lost": "#d62728",
}
for seg_name, group in customers.groupby("segment"):
    axes[2].scatter(
        group["churn_risk_score"],
        group["avg_order_value"],
        label=seg_name,
        color=colors[seg_name],
        s=120,
        edgecolors="black",
    )
axes[2].set_title("3. Retention Prioritization Grid\n(Risk vs. Basket Value)")
axes[2].set_xlabel("Churn Risk Score (0-100)")
axes[2].set_ylabel("Average Order Value (₹)")
axes[2].legend(loc="upper left", fontsize=8)
axes[2].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# ----------------- Print Summaries -----------------
print("=== TOP 5 CUSTOMERS BY ESTIMATED REVENUE ===")
print(
    customers[
        [
            "customer_id",
            "orders_last_90_days",
            "avg_order_value",
            "estimated_revenue_90d",
            "days_since_last_order",
        ]
    ]
    .sort_values(by="estimated_revenue_90d", ascending=False)
    .head(5)
    .to_string(index=False)
)

print("\n=== TOP 5 CUSTOMERS REQUIRING RETENTION ATTENTION ===")
print(
    customers[
        [
            "customer_id",
            "avg_order_value",
            "orders_last_90_days",
            "avg_delivery_time",
            "support_tickets",
            "days_since_last_order",
            "churn_risk_score",
            "retention_priority_score",
        ]
    ]
    .sort_values(by="retention_priority_score", ascending=False)
    .head(5)
    .to_string(index=False)
)