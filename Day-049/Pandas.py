import pandas as pd
import numpy as np

# Given Data
shipments = pd.DataFrame({
    "shipment_id": [
        "S101", "S102", "S103", "S104", "S105",
        "S106", "S107", "S108", "S109", "S110",
        "S111", "S112", "S112"
    ],
    "carrier": [
        "FastMove", "RoadLink", "FastMove", "CargoPro",
        "RoadLink", "CargoPro", "FastMove", "RoadLink",
        "CargoPro", "FastMove", "RoadLink", "CargoPro",
        "CargoPro"
    ],
    "dispatch_time": [
        "2026-09-01 08:00", "2026-09-01 10:00",
        "2026-09-02 09:00", "2026-09-02 11:00",
        "2026-09-03 07:30", "2026-09-03 13:00",
        "2026-09-04 08:30", "2026-09-04 09:00",
        "2026-09-05 12:00", "2026-09-05 14:00",
        "2026-09-06 08:00", "2026-09-06 10:00",
        "2026-09-06 10:00"
    ],
    "delivery_time": [
        "2026-09-02 07:00", "2026-09-03 15:00",
        "2026-09-03 08:00", "2026-09-05 12:00",
        "2026-09-04 06:00", "2026-09-06 10:00",
        "2026-09-05 09:00", None,
        "2026-09-06 08:00", "2026-09-07 12:00",
        "2026-09-07 06:00", "2026-09-08 15:00",
        "2026-09-08 15:00"
    ],
    "status": [
        "Delivered", "delivered", "Delivered", "Delayed",
        "Delivered", "Delayed", "Delivered", "In Transit",
        "Delivered", "Delivered", "Delivered", "Delayed",
        "Delayed"
    ]
})

# --- Task 1: Data Cleaning & Audit Trail ---
# Standardize status labels to title case
shipments["status"] = shipments["status"].str.title()

# Identify and isolate duplicates and missing timestamps for the audit trail
audit_duplicates = shipments[shipments.duplicated(subset=["shipment_id"], keep=False)].copy()
audit_missing_delivery = shipments[shipments["delivery_time"].isna()].copy()

# Combine excluded records to form the complete audit trail
audit_trail = pd.concat([audit_duplicates, audit_missing_delivery]).drop_duplicates()

# Apply cleaning strategy: Remove duplicate shipment IDs (keeping the first occurrence) and drop missing deliveries
cleaned_shipments = shipments.drop_duplicates(subset=["shipment_id"], keep="first").dropna(subset=["delivery_time"]).copy()

print("--- Task 1: Audit Trail Summary ---")
print(f"Total excluded records captured in audit trail: {len(audit_trail)}\n")


# --- Task 2: Calculate Delivery Hours Safely ---
# Convert datetime columns to datetime objects
cleaned_shipments["dispatch_time"] = pd.to_datetime(cleaned_shipments["dispatch_time"])
cleaned_shipments["delivery_time"] = pd.to_datetime(cleaned_shipments["delivery_time"])

# Compute delivery duration in hours, ensuring missing or incomplete data results in NaN (not zero)
cleaned_shipments["delivery_hours"] = (
    cleaned_shipments["delivery_time"] - cleaned_shipments["dispatch_time"]
).dt.total_seconds() / 3600.0


# --- Task 3: Carrier Metrics ---
# Completed-shipment count, average delivery duration, and percentage of shipments classified as delayed
carrier_metrics = cleaned_shipments.groupby("carrier").agg(
    completed_count=("shipment_id", "count"),
    avg_delivery_hours=("delivery_hours", "mean"),
    delayed_count=("status", lambda x: (x == "Delayed").sum())
).reset_index()

carrier_metrics["delayed_percentage"] = (carrier_metrics["delayed_count"] / carrier_metrics["completed_count"]) * 100

print("--- Task 3: Carrier Performance Metrics ---")
print(carrier_metrics.to_string(index=False))
print()


# --- Task 4: Lowest Average Delivery Duration & Bias Explanation ---
best_carrier = carrier_metrics.loc[carrier_metrics["avg_delivery_hours"].idxmin()]
print("--- Task 4: Lowest Average Delivery Duration ---")
print(f"Carrier with the lowest average delivery duration: {best_carrier['carrier']} "
      f"({best_carrier['avg_delivery_hours']:.2f} hours)\n")

"""
Bias Explanation:
Excluding incomplete shipments (such as those 'In Transit' or missing timestamps) can significantly bias 
the comparison. Often, shipments still in transit are delayed or experiencing operational bottlenecks. 
Dropping them removes slow outliers from the active sample, artificially inflating a carrier's speed 
metrics and making performance appear better than it actually is.
"""


# --- Task 5: Recommendation ---
"""
--- Task 5: Carrier-Selection Strategy Recommendation ---
To make robust, defensible contracting decisions, avoid relying on a single metric (like raw speed or cost alone). 
Instead, adopt a multi-criteria weighted scorecard approach:
1. Delivery Speed: Evaluate average and median delivery hours to ensure timely fulfillment.
2. Reliability & Delay Frequency: Track the percentage of delayed shipments to measure consistency.
3. Data Compliance & Transparency: Factor in data hygiene (rate of missing timestamps or duplicate entries) 
   as a proxy for operational visibility.
4. Shipping Cost: Balance service-level metrics against the cost per shipment to maximize value.
"""
print("--- Task 5: Recommendation ---")
print("Recommended Strategy: Implement a multi-criteria weighted scorecard balancing speed, delay frequency, cost, and data reliability.")