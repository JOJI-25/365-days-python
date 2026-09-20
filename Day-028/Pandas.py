import pandas as pd

data = {
    "campaign": [
        "Search",
        "Search",
        "Social",
        "Social",
        "Email",
        "Email",
        "Display",
        "Display",
    ],
    "device": [
        "Mobile",
        "Desktop",
        "Mobile",
        "Desktop",
        "Mobile",
        "Desktop",
        "Mobile",
        "Desktop",
    ],
    "impressions": [12000, 8000, 15000, 7000, 5000, 4000, 10000, 6000],
    "clicks": [720, 560, 600, 350, 450, 360, 300, 210],
    "spend": [18000, 16000, 12000, 9000, 5000, 4500, 11000, 8500],
    "conversions": [72, 67, 48, 31, 54, 40, 21, 16],
}

df = pd.DataFrame(data)

# 1. Calculate CTR (Click-Through Rate) for every row
df["CTR"] = df["clicks"] / df["impressions"]

# 2. Calculate conversion rate from clicks for every row
df["Conversion_Rate"] = df["conversions"] / df["clicks"]

# 3. Calculate cost per conversion
df["Cost_Per_Conversion"] = df["spend"] / df["conversions"]

# 4. Determine which campaign + device combination has the best conversion rate
best_row = df.loc[df["Conversion_Rate"].idxmax()]
best_combination = f"{best_row['campaign']} on {best_row['device']}"

# 5. Aggregate the data by campaign and compute overall metrics
campaign_summary = (
    df.groupby("campaign")
    .agg({
        "impressions": "sum",
        "clicks": "sum",
        "spend": "sum",
        "conversions": "sum",
    })
    .reset_index()
)

# Calculate overall rates using aggregated totals (not averaging row percentages)
campaign_summary["Overall_CTR"] = (
    campaign_summary["clicks"] / campaign_summary["impressions"]
)
campaign_summary["Overall_Conversion_Rate"] = (
    campaign_summary["conversions"] / campaign_summary["clicks"]
)
campaign_summary["Overall_Cost_Per_Conversion"] = (
    campaign_summary["spend"] / campaign_summary["conversions"]
)

# 6. Identify the campaign with the lowest cost per conversion
best_cost_campaign_row = campaign_summary.loc[
    campaign_summary["Overall_Cost_Per_Conversion"].idxmin()
]
lowest_cost_campaign = best_cost_campaign_row["campaign"]

# --- Display Results ---
print("--- Row-Level Metrics (First 3 rows sample) ---")
print(
    df[[
        "campaign",
        "device",
        "CTR",
        "Conversion_Rate",
        "Cost_Per_Conversion",
    ]].head(3)
)
print("\n--- Best Campaign + Device Combination (Conversion Rate) ---")
print(
    f"{best_combination} with a conversion rate of"
    f" {best_row['Conversion_Rate']:.2%}"
)

print("\n--- Campaign Summary (Aggregated Totals & Rates) ---")
print(
    campaign_summary[[
        "campaign",
        "impressions",
        "clicks",
        "spend",
        "conversions",
        "Overall_CTR",
        "Overall_Conversion_Rate",
        "Overall_Cost_Per_Conversion",
    ]]
)

print(
    "\n--- Campaign with Lowest Cost Per Conversion ---"
    f" {lowest_cost_campaign} (₹{best_cost_campaign_row['Overall_Cost_Per_Conversion']:.2f} per conversion)"
)