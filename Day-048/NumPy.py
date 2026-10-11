import numpy as np

# Given Data
returns = np.array([
    [0.012, -0.008, 0.015, 0.006, -0.011, 0.009, 0.014, -0.004],
    [0.007, 0.005, -0.003, 0.009, 0.004, 0.006, -0.002, 0.008],
    [-0.018, 0.012, -0.014, 0.021, -0.009, 0.016, -0.020, 0.011],
    [0.010, -0.006, 0.008, -0.012, 0.014, -0.003, 0.007, 0.005]
])

funds = np.array(["Fund_X", "Fund_B", "Fund_C", "Fund_D"]) # Wait, funds array is Fund_A, Fund_B, Fund_C, Fund_D
funds = np.array(["Fund_A", "Fund_B", "Fund_C", "Fund_D"])

# -------------------------------------------------------------
# Task 1: Mean and Standard Deviation of Daily Returns
# -------------------------------------------------------------
mean_returns = np.mean(returns, axis=1)
std_returns = np.std(returns, axis=1, ddof=1)  # Sample standard deviation

highest_avg_idx = np.argmax(mean_returns)
highest_avg_fund = funds[highest_avg_idx]

print("--- Task 1: Mean & Standard Deviation ---")
for i, fund in enumerate(funds):
    print(f"{fund}: Mean = {mean_returns[i]:.5f}, Std Dev = {std_returns[i]:.5f}")
print(f"Fund with the highest average return: {highest_avg_fund} ({mean_returns[highest_avg_idx]:.5f})\n")

# -------------------------------------------------------------
# Task 2: Cumulative Growth of ₹10,000 Investment
# -------------------------------------------------------------
initial_investment = 10000
# Calculate daily growth factor (1 + return), then cumulative product
growth_factors = 1 + returns
wealth_indices = initial_investment * np.cumprod(growth_factors, axis=1)
final_values = wealth_indices[:, -1]

print("--- Task 2: Cumulative Growth (₹10,000 Initial) ---")
for i, fund in enumerate(funds):
    print(f"{fund} Final Value: ₹{final_values[i]:,.2f}")
print()

# -------------------------------------------------------------
# Task 3: Negative Return Percentage and Most Frequent Losses
# -------------------------------------------------------------
negative_counts = np.sum(returns < 0, axis=1)
total_days = returns.shape[1]
negative_percentages = (negative_counts / total_days) * 100

most_frequent_loss_idx = np.argmax(negative_percentages)
most_frequent_loss_fund = funds[most_frequent_loss_idx]

print("--- Task 3: Negative Return Frequency ---")
for i, fund in enumerate(funds):
    print(f"{fund}: {negative_counts[i]} negative days ({negative_percentages[i]:.1f}%)")
print(f"Fund with the most frequent daily losses: {most_frequent_loss_fund}\n")

# -------------------------------------------------------------
# Task 4: Maximum Drawdown Calculation
# -------------------------------------------------------------
max_drawdowns = []
for i in range(len(funds)):
    wealth = wealth_indices[i]
    # Running maximum of the wealth index to track peaks
    running_peak = np.maximum.accumulate(wealth)
    # Drawdown percentage at each point
    drawdowns = (wealth - running_peak) / running_peak
    # Maximum drawdown is the minimum value (most negative) of the drawdown series
    max_drawdowns.append(np.min(drawdowns))

max_drawdowns = np.array(max_drawdowns)
largest_dd_idx = np.argmin(max_drawdowns)
largest_dd_fund = funds[largest_dd_idx]

print("--- Task 4: Maximum Drawdowns ---")
for i, fund in enumerate(funds):
    print(f"{fund}: Max Drawdown = {max_drawdowns[i]*100:.2f}%")
print(f"Fund with the largest peak-to-trough decline: {largest_dd_fund} ({max_drawdowns[largest_dd_idx]*100:.2f}%)\n")

# -------------------------------------------------------------
# Task 5: Summary Comparison
# -------------------------------------------------------------
print("--- Task 5: Summary Comparison Table ---")
print(f"{'Fund':<10} | {'Avg Return':<12} | {'Volatility':<12} | {'Max Drawdown':<12}")
print("-" * 52)
for i, fund in enumerate(funds):
    print(f"{fund:<10} | {mean_returns[i]*100:10.2f}% | {std_returns[i]*100:10.2f}% | {max_drawdowns[i]*100:10.2f}%")