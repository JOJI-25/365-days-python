import pandas as pd
import numpy as np

# 1. Initialize Dataset (including realistic spend values)
spend_values = [15000, 12000, 14000, 11000, 13000, 11500, 12500, 10500, 16000, 11000, 15500, 11200]

campaigns = pd.DataFrame({    
    "campaign": [        
        "Google_Search", "Instagram", "YouTube",        
        "LinkedIn", "Google_Search", "Instagram",        
        "YouTube", "LinkedIn", "Google_Search", "Instagram",        
        "YouTube", "LinkedIn"    
    ],    
    "audience": [        
        "Students", "Students", "Professionals",        
        "Professionals", "Professionals", "Students",        
        "Students", "Students", "Students", "Professionals",        
        "Professionals", "Professionals"    
    ],    
    "impressions": [        
        120000, 180000, 150000, 70000,        
        95000, 160000, 135000, 85000,        
        110000, 145000, 170000, 90000    
    ],    
    "clicks": [        
        7200, 5400, 6750, 4200,        
        6650, 4800, 5800, 5100,        
        7700, 4350, 7650, 4950    
    ],    
    "leads": [        
        1200, 850, 1100, 900,        
        1050, 760, 950, 980,        
        1300, 700, 1250, 920    
    ],    
    "enrollments": [        
        180, 95, 165, 150,        
        170, 88, 145, 160,        
        205, 82, 190, 155    
    ],    
    "spend": spend_values
})

print("=" * 70)
print("MARKETING CAMPAIGN PERFORMANCE INTELLIGENCE REPORT")
print("=" * 70)

# 2. Campaign-Level Metrics (Using aggregate sums to prevent ratio bias)
campaign_agg = campaigns.groupby("campaign").agg({
    "impressions": "sum",
    "clicks": "sum",
    "leads": "sum",
    "enrollments": "sum",
    "spend": "sum"
}).reset_index()

campaign_agg["CTR_%"] = (campaign_agg["clicks"] / campaign_agg["impressions"]) * 100
campaign_agg["Lead_Conv_%"] = (campaign_agg["leads"] / campaign_agg["clicks"]) * 100
campaign_agg["Enroll_Conv_%"] = (campaign_agg["enrollments"] / campaign_agg["leads"]) * 100
campaign_agg["CPC"] = campaign_agg["spend"] / campaign_agg["clicks"]
campaign_agg["CPL"] = campaign_agg["spend"] / campaign_agg["leads"]
campaign_agg["CPE"] = campaign_agg["spend"] / campaign_agg["enrollments"]

# Feature Engineering (Part F)
campaign_agg["Click_to_Enroll_Ratio_%"] = (campaign_agg["enrollments"] / campaign_agg["clicks"]) * 100
campaign_agg["Spend_Efficiency_Index"] = (campaign_agg["enrollments"] * 500) / campaign_agg["spend"]

print("\n--- CAMPAIGN PERFORMANCE SUMMARY ---")
print(campaign_agg[["campaign", "CTR_%", "CPC", "CPL", "CPE", "enrollments"]].to_string(index=False))

# 3. Audience-Level Analysis (Students vs Professionals)
audience_agg = campaigns.groupby("audience").agg({
    "impressions": "sum",
    "clicks": "sum",
    "leads": "sum",
    "enrollments": "sum",
    "spend": "sum"
}).reset_index()

audience_agg["CTR_%"] = (audience_agg["clicks"] / audience_agg["impressions"]) * 100
audience_agg["Lead_Conv_%"] = (audience_agg["leads"] / audience_agg["clicks"]) * 100
audience_agg["Enroll_Conv_%"] = (audience_agg["enrollments"] / audience_agg["leads"]) * 100
audience_agg["CPE"] = audience_agg["spend"] / audience_agg["enrollments"]

print("\n--- AUDIENCE ANALYSIS (Students vs Professionals) ---")
print(audience_agg[["audience", "CTR_%", "Lead_Conv_%", "Enroll_Conv_%", "CPE", "enrollments"]].to_string(index=False))

# 4. Funnel Analysis
total_impressions = campaigns["impressions"].sum()
total_clicks = campaigns["clicks"].sum()
total_leads = campaigns["leads"].sum()
total_enrollments = campaigns["enrollments"].sum()

drop_imp_click = (1 - total_clicks / total_impressions) * 100
drop_click_lead = (1 - total_leads / total_clicks) * 100
drop_lead_enroll = (1 - total_enrollments / total_leads) * 100

print("\n--- MARKETING FUNNEL ANALYSIS ---")
print(f"1. Impressions       : {total_impressions:,}")
print(f"2. Clicks            : {total_clicks:,} (Drop-off: {drop_imp_click:.2f}%)")
print(f"3. Leads             : {total_leads:,} (Drop-off: {drop_click_lead:.2f}%)")
print(f"4. Enrollments       : {total_enrollments:,} (Drop-off: {drop_lead_enroll:.2f}%)")
print("=" * 70)