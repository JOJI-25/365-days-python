import numpy as np

daily_revenue = np.array([    
    18200, 19500, 20100, 18700, 21000, 22400, 21800,    
    20500, 19800, 23100, 24000, 22600, 21500, 21900,    
    24500, 23800, 25100, 26200, 27500, 61000, 26800
])

mean_with = np.mean(daily_revenue)
median = np.median(daily_revenue)
std_with = np.std(daily_revenue, ddof=1)

q1 = np.percentile(daily_revenue, 25)
q3 = np.percentile(daily_revenue, 75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = daily_revenue[(daily_revenue < lower_bound) | (daily_revenue > upper_bound)]
no_outlier = daily_revenue[(daily_revenue >= lower_bound) & (daily_revenue <= upper_bound)]

mean_without = np.mean(no_outlier)

pct_diff = ((mean_with - median) / median) * 100

# First half and second half averages
n = len(daily_revenue)
mid = n // 2
first_half = daily_revenue[:mid]
second_half = daily_revenue[mid:] # Note: 21 days, mid is 10. First 10, second 11? Or split 10 and 10, or 10 and 11. Let's check.
# Let's split 0-10 (10 items) and 10-21 (11 items) or 0-10 and 11-21. Let's see: days 1-10 vs 11-21.
first_half_avg = np.mean(daily_revenue[:10])
second_half_avg = np.mean(daily_revenue[10:])

print(f"Mean with outlier: {mean_with:.2f}")
print(f"Median: {median}")
print(f"Std: {std_with:.2f}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
print(f"Outliers: {outliers}")
print(f"Mean without outlier: {mean_without:.2f}")
print(f"Percentage difference (mean vs median): {pct_diff:.2f}%")
print(f"First half avg: {first_half_avg:.2f}")
print(f"Second half avg: {second_half_avg:.2f}")