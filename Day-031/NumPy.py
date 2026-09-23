import numpy as np

revenue = np.array([
    [120, 125, 132, 140, 145, 155],
    [200, 198, 205, 215, 218, 225],
    [90,  95,  94,  100, 108, 115],
    [160, 172, 180, 178, 190, 205]
])

# Calculate the total six-month revenue for each region.
total_six_month_revenue = revenue.sum(axis=1)

# Calculate the average monthly revenue for each region.
avg_monthly_revenue = revenue.mean(axis=1)

# Calculate the percentage growth from January to June for each region.
jan_revenue = revenue[:, 0]
jun_revenue = revenue[:, 5]
percentage_growth = ((jun_revenue - jan_revenue) / jan_revenue) * 100

print(percentage_growth)

# 