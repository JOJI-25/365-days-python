import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

monthly_tickets = pd.Series([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 14, 22, 31, 45])

mean_val = monthly_tickets.mean()
median_val = monthly_tickets.median()
var_val = monthly_tickets.var(ddof=1)
std_val = monthly_tickets.std(ddof=1)
q1 = monthly_tickets.quantile(0.25)
q3 = monthly_tickets.quantile(0.75)
iqr = q3 - q1

print("=== 1. Summary Statistics ===")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val}")
print(f"Variance: {var_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")
print(f"Q1: {q1} | Q3: {q3} | IQR: {iqr}\n")

upper_bound = q3 + 1.5 * iqr
lower_bound = q1 - 1.5 * iqr
outliers = monthly_tickets[monthly_tickets > upper_bound]
max_outlier = outliers.max()
diff_from_q3 = max_outlier - q3

print("=== 2. Outlier Analysis ===")
print(f"Upper Bound Threshold: {upper_bound}")
print(f"Identified Outliers: {outliers.tolist()}")
print(f"Max Outlier (45) is {diff_from_q3} units higher than Q3 ({q3}).\n")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(monthly_tickets, bins=8, color="skyblue", edgecolor="black")
plt.title("Histogram of Monthly Support Tickets", fontweight="bold")
plt.xlabel("Tickets per Month")
plt.ylabel("Customer Count")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.subplot(1, 2, 2)
sns.boxplot(y=monthly_tickets, color="lightcoral")
plt.title("Box Plot of Monthly Support Tickets", fontweight="bold")
plt.ylabel("Tickets per Month")

plt.tight_layout()
plt.show()

pct_le_5 = (monthly_tickets <= 5).mean() * 100
pct_gt_10 = (monthly_tickets > 10).mean() * 100

print("=== 4. Segment Comparisons ===")
print(f"Customers with 5 or fewer tickets: {pct_le_5:.2f}%")
print(f"Customers with more than 10 tickets: {pct_gt_10:.2f}%")