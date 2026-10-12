import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Monthly household electricity bills in rupees
monthly_bill = pd.Series([
    450,
    520,
    560,
    610,
    650,
    690,
    720,
    760,
    810,
    850,
    900,
    950,
    1020,
    1100,
    1200,
    1350,
    1500,
    1800,
    2400,
    3200,
])

# 1. Summary Statistics
mean_bill = monthly_bill.mean()
median_bill = monthly_bill.median()
q1 = monthly_bill.quantile(0.25)
q3 = monthly_bill.quantile(0.75)
std_bill = monthly_bill.std()

print("--- 1. Summary Statistics ---")
print(f"Mean: {mean_bill:.2f}")
print(f"Median: {median_bill:.2f}")
print(f"Q1 (25th percentile): {q1:.2f}")
print(f"Q3 (75th percentile): {q3:.2f}")
print(f"Standard Deviation: {std_bill:.2f}")


# 2. Gini Coefficient Calculation (using the standard relative mean absolute difference formula)
def calculate_gini(x):
  x = np.sort(np.array(x))
  n = len(x)
  cumulative_sum = np.sum(np.arange(1, n + 1) * x)
  return (2 * cumulative_sum) / (n * np.sum(x)) - (n + 1) / n


gini_coeff = calculate_gini(monthly_bill)
print(f"\n--- 2. Gini Coefficient ---")
print(f"Gini Coefficient: {gini_coeff:.4f}")

# 3. Lorenz Curve Data
x_sorted = np.sort(monthly_bill)
cum_households = np.linspace(0, 1, len(x_sorted) + 1)
cum_expenditure = np.insert(np.cumsum(x_sorted) / np.sum(x_sorted), 0, 0)

# Plotting Lorenz Curve
plt.figure(figsize=(6, 6))
plt.plot(
    cum_households,
    cum_expenditure,
    marker="o",
    color="b",
    label="Actual Distribution",
)
plt.plot([0, 1], [0, 1], color="gray", linestyle="--", label="Line of Equality")
plt.title("Lorenz Curve of Household Electricity Expenditure")
plt.xlabel("Cumulative Share of Households")
plt.ylabel("Cumulative Share of Electricity Expenditure")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("lorenz_curve.png")
plt.show()

# 4. Top 20% Analysis
n_top_20 = int(np.ceil(0.20 * len(x_sorted)))
top_20_spending = np.sum(x_sorted[-n_top_20:])
total_spending = np.sum(x_sorted)
top_20_share = (top_20_spending / total_spending) * 100

print(f"\n--- 4. Top 20% Concentration ---")
print(f"Share of total expenditure by top 20% households: {top_20_share:.2f}%")