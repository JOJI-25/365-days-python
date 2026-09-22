import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "customer_id": [
        "C101", "C102", "C103", "C104", "C105",
        "C106", "C107", "C108", "C109", "C110"
    ],
    "plan": [
        "Basic", "Premium", "Basic", "Standard", "Premium",
        "Standard", "Basic", "Premium", "Standard", "Basic"
    ],
    "signup_date": [
        "2025-01-15", "2025-02-10", "2025-02-21", "2025-03-05",
        "2025-03-18", "2025-04-02", "2025-04-20", "2025-05-11",
        "2025-05-25", "2025-06-03"
    ],
    "monthly_fee": [299, 699, 299, 499, 699, 499, 299, 699, 499, 299],
    "watch_hours": [18, 42, 12, 31, 55, 28, 9, 61, 24, 15],
    "support_tickets": [1, 2, 0, 3, 1, 2, 1, 0, 4, 2],
    "renewed": [
        True, True, False, True, True,
        False, False, True, False, True
    ]
})

# 1. Convert signup_date to datetime
customers["signup_date"] = pd.to_datetime(customers["signup_date"])

# 2. Create watch_hours_per_ticket feature (handling zero tickets safely)
customers["watch_hours_per_ticket"] = np.where(
    customers["support_tickets"] > 0,
    customers["watch_hours"] / customers["support_tickets"],
    customers["watch_hours"] # Fallback for zero tickets
)

# 3. Determine renewal rate for each subscription plan
renewal_by_plan = customers.groupby("plan")["renewed"].mean().reset_index()
renewal_by_plan["renewal_rate_pct"] = renewal_by_plan["renewed"] * 100

# 4. Compare average watch hours between renewed and non-renewed customers
watch_hours_by_renewal = customers.groupby("renewed")["watch_hours"].mean()

# 5. Determine plan with highest potential monthly revenue
total_potential_revenue_per_plan = customers.groupby("plan")["monthly_fee"].sum()

# 6. Plan with highest average support-ticket volume
avg_tickets_by_plan = customers.groupby("plan")["support_tickets"].mean()

# 7. Rank customers within each subscription plan according to their watch hours
customers["rank_in_plan"] = customers.groupby("plan")["watch_hours"].rank(ascending=False, method="dense")

# 8. Comprehensive plan summary table
plan_summary = customers.groupby("plan").agg(
    customer_count=("customer_id", "count"),
    avg_monthly_fee=("monthly_fee", "mean"),
    avg_watch_hours=("watch_hours", "mean"),
    avg_support_tickets=("support_tickets", "mean"),
    renewal_rate_pct=("renewed", lambda x: x.mean() * 100)
).reset_index()

print(plan_summary)