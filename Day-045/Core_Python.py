campaigns = [
    {"name": "Search_A", "spend": 12000, "revenue": 31000, "leads": 420},
    {"name": "Social_A", "spend": 9000, "revenue": 18000, "leads": 510},
    {"name": "Search_B", "spend": 15000, "revenue": 39000, "leads": 460},
    {"name": "Email_A", "spend": 5000, "revenue": 16000, "leads": 380},
    {"name": "Social_B", "spend": 11000, "revenue": 20500, "leads": 620},
    {"name": "Display_A", "spend": 8000, "revenue": 12500, "leads": 290},
    {"name": "Email_B", "spend": 6500, "revenue": 21000, "leads": 430},
    {"name": "Search_C", "spend": 18000, "revenue": 42000, "leads": 500}
]

for c in campaigns:
    c["profit"] = c["revenue"] - c["spend"]
    c["roi_pct"] = (c["profit"] / c["spend"]) * 100
    c["cpl"] = c["spend"] / c["leads"]

highest_roi_campaign = max(campaigns, key=lambda x: x["roi_pct"])
highest_profit_campaigns = [c for c in campaigns if c["profit"] == max(x["profit"] for x in campaigns)]

print(f"--- 1 & 2. Performance Metrics & Top Campaigns ---")
print(f"Highest ROI Campaign: {highest_roi_campaign['name']} ({highest_roi_campaign['roi_pct']:.2f}%)")
print("Highest Absolute Profit Campaign(s):", ", ".join([f"{c['name']} (${c['profit']})" for c in highest_profit_campaigns]))

lowest_cpl_campaign = min(campaigns, key=lambda x: x["cpl"])
print(f"\nLowest Cost Per Lead Campaign: {lowest_cpl_campaign['name']} (${lowest_cpl_campaign['cpl']:.2f} per lead)")

def classify_campaign(roi):
    if roi < 100:
        return "Weak"
    elif roi <= 180:
        return "Moderate"
    else:
        return "Strong"

print(f"\n--- 4. Campaign Classifications ---")
for c in campaigns:
    c["classification"] = classify_campaign(c["roi_pct"])
    print(f"Campaign: {c['name']} | ROI: {c['roi_pct']:.2f}% | Classification: {c['classification']}")

print(f"\n--- 5. Analysis: ROI vs. Cost Per Lead ---")
print(f"Highest ROI Campaign: {highest_roi_campaign['name']} (ROI: {highest_roi_campaign['roi_pct']:.2f}%, CPL: ${highest_roi_campaign['cpl']:.2f})")
print(f"Lowest CPL Campaign: {lowest_cpl_campaign['name']} (ROI: {lowest_cpl_campaign['roi_pct']:.2f}%, CPL: ${lowest_cpl_campaign['cpl']:.2f})")
print("""
Reasoning:
The campaign with the highest ROI (Email_B at 223.08%) is NOT the one with the lowest cost per lead (Email_A at $13.16). 
However, Email_B still has a very strong and efficient CPL ($15.12) while generating a much higher return per dollar spent. 
Therefore, while Email_A is marginally cheaper per lead, Email_B is a better overall performer because it balances high capital efficiency (ROI) with a very competitive acquisition cost.
""")