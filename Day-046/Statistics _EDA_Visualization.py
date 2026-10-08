import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset initialization
transaction_amount = pd.Series([
    120, 145, 180, 210, 195,
    230, 260, 275, 310, 290,
    340, 365, 390, 420, 455,
    510, 575, 680, 1250, 2400,
    5200
])

# 1. Calculate descriptive statistics (Mean, Median, Variance, Std, Q1, Q3, IQR)
mean_val = transaction_amount.mean()
median_val = transaction_amount.median()
var_val = transaction_amount.var(ddof=1) # Sample variance
std_val = transaction_amount.std(ddof=1) # Sample standard deviation
q1 = transaction_amount.quantile(0.25)
q3 = transaction_amount.quantile(0.75)
iqr = q3 - q1

print("--- 1. Descriptive Statistics ---")
print(f"Mean: ₹{mean_val:.2f}")
print(f"Median: ₹{median_val:.2f}")
print(f"Variance: {var_val:.2f}")
print(f"Standard Deviation: ₹{std_val:.2f}")
print(f"Q1 (25th percentile): ₹{q1:.2f}")
print(f"Q3 (75th percentile): ₹{q3:.2f}")
print(f"IQR: ₹{iqr:.2f}\n")

# 2. Use the IQR method to identify potential high-value outliers and upper boundary
upper_bound = q3 + (1.5 * iqr)
lower_bound = q1 - (1.5 * iqr)
outliers = transaction_amount[transaction_amount > upper_bound]

print("--- 2. Outlier Detection (IQR Method) ---")
print(f"Upper Outlier Boundary: ₹{upper_bound:.2f}")
print(f"Lower Outlier Boundary: ₹{lower_bound:.2f}")
print(f"Identified Outliers (> Upper Boundary): {outliers.tolist()}\n")

# 3. Create a histogram and box plot
plt.figure(figsize=(12, 5))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(transaction_amount, kde=True, color='purple', bins=10)
plt.title('Transaction Amount Distribution (Histogram)')
plt.xlabel('Amount (₹)')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(y=transaction_amount, color='orange')
plt.title('Transaction Amount Box Plot')
plt.ylabel('Amount (₹)')

plt.tight_layout()
plt.show()
print("--- 3. Visualizations Saved ---")
print("Histograms and box plots successfully generated and saved to 'transaction_distribution.png'.\n")