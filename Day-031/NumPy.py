import numpy as np

revenue = np.array([
    [120, 125, 132, 140, 145, 155],
    [200, 198, 205, 215, 218, 225],
    [90,  95,  94,  100, 108, 115],
    [160, 172, 180, 178, 190, 205]
])

# 1. Total six-month revenue for each region (sum across columns)
total_revenue_per_region = np.sum(revenue, axis=1)

# 2. Average monthly revenue for each region (mean across columns)
avg_revenue_per_region = np.mean(revenue, axis=1)

# 3. Percentage growth from January (index 0) to June (index 5) for each region
jan_revenue = revenue[:, 0]
jun_revenue = revenue[:, 5]
percentage_growth = ((jun_revenue - jan_revenue) / jan_revenue) * 100

# 4. Region with the highest percentage growth (0-indexed row number)
highest_growth_region = np.argmax(percentage_growth)

# 5. Total revenue for each month across all regions (sum across rows)
total_revenue_per_month = np.sum(revenue, axis=0)

# 6. Month with the highest combined revenue (0-indexed month: 0=Jan, 5=Jun)
highest_revenue_month = np.argmax(total_revenue_per_month)

# 7. Month-to-month revenue changes for each region (difference between adjacent columns)
monthly_changes = np.diff(revenue, axis=1)

# 8. Identify regions that experienced a revenue decline in at least one month
# (Checks if any diff value is less than 0 along each row)
decline_mask = np.any(monthly_changes < 0, axis=1)
regions_with_decline = np.where(decline_mask)[0]

# 9. Determine the region with the most consistent monthly revenue using standard deviation
# Lower standard deviation indicates higher consistency
std_devs = np.std(revenue, axis=1)
most_consistent_region = np.argmin(std_devs)

# --- Output Results ---
print("Total Revenue per Region:", total_revenue_per_region)
print("Average Monthly Revenue per Region:", avg_revenue_per_region)
print("Percentage Growth (Jan-Jun):", percentage_growth)
print("Region with Highest Percentage Growth Index:", highest_growth_region)
print("Total Revenue per Month:", total_revenue_per_month)
print("Highest Revenue Month Index:", highest_revenue_month)
print("Month-to-Month Changes:\n", monthly_changes)
print("Regions with a Revenue Decline Indices:", regions_with_decline)
print("Most Consistent Region Index:", most_consistent_region)