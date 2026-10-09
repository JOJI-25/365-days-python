import pandas as pd
import numpy as np

data = {
    "invoice_id": range(7001, 7013),
    "customer_type": [
        "Residential", "Business", "Residential", "Business",
        "Residential", "Business", "Residential", "Business",
        "Residential", "Business", "Residential", "Business"
    ],
    "units_used": [
        120, 850, 95, 1200, 150, 920,
        110, 1050, 135, 780, 100, 1150
    ],
    "rate_per_unit": [
        6.5, 8.0, 6.5, 8.0, 6.5, 8.0,
        6.5, 8.0, 6.5, 8.0, 6.5, 8.0
    ],
    "adjustment": [
        0, -450, 50, 0, np.nan, -200,
        0, -150, -80, 0, 40, -300
    ],
    "payment_status": [
        "Paid", "Pending", "Paid", "Paid",
        "Pending", "Paid", "Paid", "Pending",
        "Paid", "Paid", "Pending", "Paid"
    ]
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# Task 1: Inspect and Clean Dataset
# ---------------------------------------------------------
print("=== TASK 1: Inspection & Cleaning ===")
print("Missing values per column:\n", df.isnull().sum())
print("Duplicate invoice IDs:", df.duplicated(subset=["invoice_id"]).sum())

# Cleaning Strategy: Replace missing adjustments with 0 (since NaN indicates no adjustment applied)
df["adjustment"] = df["adjustment"].fillna(0)


# ---------------------------------------------------------
# Task 2: Calculate Gross Bill and Final Bill
# ---------------------------------------------------------
df["gross_bill"] = df["units_used"] * df["rate_per_unit"]
df["final_bill"] = df["gross_bill"] + df["adjustment"]


# ---------------------------------------------------------
# Task 3: Compare Residential and Business Customers
# ---------------------------------------------------------
customer_comparison = df.groupby("customer_type").agg(
    total_gross_billing=("gross_bill", "sum"),
    total_final_billing=("final_bill", "sum"),
    average_final_bill=("final_bill", "mean")
)

print("\n=== TASK 3: Customer Comparison ===")
print(customer_comparison)


# ---------------------------------------------------------
# Task 4: Pending Invoices Analysis
# ---------------------------------------------------------
total_final_billing = df["final_bill"].sum()
pending_df = df[df["payment_status"] == "Pending"]
total_pending_billing = pending_df["final_bill"].sum()

pending_percentage = (total_pending_billing / total_final_billing) * 100

pending_by_customer = pending_df.groupby("customer_type")["final_bill"].sum()
largest_pending_customer = pending_by_customer.idxmax()
largest_pending_amount = pending_by_customer.max()

print("\n=== TASK 4: Pending Invoices ===")
print(f"Percentage of total final billing represented by pending invoices: {pending_percentage:.2f}%")
print(f"Customer type with largest pending amount: {largest_pending_customer} ({largest_pending_amount:.2f})")


# ---------------------------------------------------------
# Task 5: Business Interpretation
# ---------------------------------------------------------
print("\n=== TASK 5: Business Interpretation ===")
print("""
1. Missing Adjustments Impact: Unhandled or missing adjustments can distort reported gross and net revenue figures. 
   Treating NaN values correctly as zero (no change) ensures that billing calculations reflect true transactional realities 
   without artificially inflating or deflating revenue.
2. Unpaid (Pending) Invoices vs. Cash Collection: Pending invoices contribute to accounts receivable and accrued revenue, 
   but they do not represent immediate cash inflows. If revenue reporting mixes billed amounts with collected cash, 
   the company risks overestimating its liquid cash position, which can lead to cash flow miscalculations.
""")

# Optional: Display the final cleaned dataframe
print("\nFinal Processed DataFrame:")
print(df[["invoice_id", "customer_type", "gross_bill", "adjustment", "final_bill", "payment_status"]])