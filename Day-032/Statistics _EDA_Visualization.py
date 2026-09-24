import numpy as np
import matplotlib.pyplot as plt

# Daily Active Users dataset
dau = np.array([
    820, 850, 870, 910, 940, 960, 980,
    1020, 1050, 1080, 1100, 1140, 1180, 1210
])

days = np.arange(1, len(dau) + 1)

# 1. Statistical Calculations
mean_dau = np.mean(dau)
median_dau = np.median(dau)
std_dau = np.std(dau)  # Population standard deviation
sample_std_dau = np.std(dau, ddof=1)  # Sample standard deviation
pct_increase_total = ((dau[-1] - dau[0]) / dau[0]) * 100
avg_daily_change = np.mean(np.diff(dau))
consecutive_pct_changes = (np.diff(dau) / dau[:-1]) * 100
max_single_day_increase = np.max(np.diff(dau))
any_decreases = np.any(np.diff(dau) < 0)
correlation = np.corrcoef(days, dau)[0, 1]

# Print key statistics
print(f"Mean DAU: {mean_dau:.2f}")
print(f"Median DAU: {median_dau}")
print(f"Standard Deviation (Population): {std_dau:.2f}")
print(f"Total % Increase (Day 1 to 14): {pct_increase_total:.2f}%")
print(f"Average Daily Change: {avg_daily_change:.2f}")
print(f"Largest Single-Day Increase: {max_single_day_increase}")
print(f"Any Decreases: {any_decreases}")
print(f"Correlation (Day vs DAU): {correlation:.4f}")

# 2. Visualization (Line Chart)
plt.figure(figsize=(9, 5))
plt.plot(days, dau, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5, markersize=6)
plt.title('Daily Active Users (DAU) Over 14 Days', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Day', fontsize=12)
plt.ylabel('Daily Active Users (DAU)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(days)
plt.tight_layout()

# Save the visualization
plt.savefig('dau_trend.png', dpi=300)
plt.show()