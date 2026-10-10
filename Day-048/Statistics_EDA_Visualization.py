import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Given Data
payments = pd.DataFrame({
    "device": ["Android", "iOS"],
    "successful_payments": [864, 936],
    "failed_payments": [136, 64]
})

# Total attempts per device
payments["total_attempts"] = payments["successful_payments"] + payments["failed_payments"]

# -------------------------------------------------------------
# Task 1: Success and Failure Rates & Difference
# -------------------------------------------------------------
payments["success_rate"] = payments["successful_payments"] / payments["total_attempts"]
payments["failure_rate"] = payments["failed_payments"] / payments["total_attempts"]

print("--- Task 1: Rates ---")
for idx, row in payments.iterrows():
    print(f"{row['device']}: Success Rate = {row['success_rate']*100:.2f}%, Failure Rate = {row['failure_rate']*100:.2f}%")

ios_success = payments.loc[payments['device'] == 'iOS', 'success_rate'].values[0]
android_success = payments.loc[payments['device'] == 'Android', 'success_rate'].values[0]
diff_pp = (ios_success - android_success) * 100
print(f"Difference in success rates (iOS - Android): {diff_pp:.2f} percentage points\n")

# -------------------------------------------------------------
# Task 2: 95% Confidence Interval for Difference in Proportions
# -------------------------------------------------------------
n_ios = payments.loc[payments['device'] == 'iOS', 'total_attempts'].values[0]
n_android = payments.loc[payments['device'] == 'Android', 'total_attempts'].values[0]

# Standard error of the difference between two proportions
p_diff = ios_success - android_success
se = np.sqrt((ios_success * (1 - ios_success) / n_ios) + (android_success * (1 - android_success) / n_android))

# Z-score for 95% confidence
z_score = stats.norm.ppf(0.975)
ci_lower = p_diff - z_score * se
ci_upper = p_diff + z_score * se

print("--- Task 2: 95% Confidence Interval ---")
print(f"95% CI for difference (iOS - Android): [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%]\n")

# -------------------------------------------------------------
# Task 3: Chi-Square Test of Independence
# -------------------------------------------------------------
# Contingency table: Rows = Devices (Android, iOS), Columns = [Success, Failed]
contingency_table = np.array([
    [864, 136],  # Android
    [936, 64]    # iOS
])

chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)

print("--- Task 3: Chi-Square Test ---")
print(f"Chi2 Statistic: {chi2:.4f}")
print(f"p-value: {p_val:.5e}")
print(f"Interpretation: Since the p-value is extremely small (< 0.05), we reject the null hypothesis.")
print(f"There is a statistically significant association between device type and payment success outcome.\n")

# -------------------------------------------------------------
# Task 4: Visualization Comparison
# -------------------------------------------------------------
devices = payments['device']
success_pcts = payments['success_rate'] * 100
failure_pcts = payments['failure_rate'] * 100

x = np.arange(len(devices))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, success_pcts, width, label='Success Rate (%)', color='#2ca02c')
ax.bar(x + width/2, failure_pcts, width, label='Failure Rate (%)', color='#d62728')

ax.set_ylabel('Percentage (%)')
ax.set_title('Payment Success vs. Failure Rates by Device')
ax.set_xticks(x)
ax.set_xticklabels(devices)
ax.legend()
plt.tight_layout()
plt.show()  # Uncomment to display locally

print("--- Task 4: Visualization Script Executed ---")
print("Pattern revealed: iOS users show a notably higher success rate (93.6%) compared to Android users (86.4%).\n")

# -------------------------------------------------------------
# Task 5: Recommendation & Distinction (Correlation vs Causation)
# -------------------------------------------------------------
print("--- Task 5: Recommendation Summary ---")
print("1. Investigation: The company should investigate Android payment flows due to the higher failure rate (13.6% vs 6.4%).")
print("2. Distinction: Statistical association proves that device type and payment outcome are related, but it does NOT prove that the device itself causes failures. Other confounding variables (e.g., app version, network quality, regional demographics, or payment gateway SDK differences across OS) could be driving the disparity.")