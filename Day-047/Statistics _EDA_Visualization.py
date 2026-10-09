import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

experiment = pd.DataFrame({
    "group": ["Control", "New_Design"],
    "visitors": [2400, 2450],
    "enrollments": [288, 343]
})

# ---------------------------------------------------------
# Task 1: Conversion rates and absolute difference
# ---------------------------------------------------------
experiment["conversion_rate"] = experiment["enrollments"] / experiment["visitors"]
ctrl_rate = experiment.loc[experiment["group"] == "Control", "conversion_rate"].values[0]
new_rate = experiment.loc[experiment["group"] == "New_Design", "conversion_rate"].values[0]

abs_diff_pp = (new_rate - ctrl_rate) * 100

print("=== TASK 1: Conversion Rates ===")
for idx, row in experiment.iterrows():
    print(f"{row['group']}: {row['conversion_rate']*100:.2f}%")
print(f"Absolute Difference: {abs_diff_pp:.2f} percentage points")


# ---------------------------------------------------------
# Task 2: Relative conversion-rate improvement
# ---------------------------------------------------------
rel_improvement = ((new_rate - ctrl_rate) / ctrl_rate) * 100

print("\n=== TASK 2: Relative Improvement ===")
print(f"Relative Improvement of New Design: {rel_improvement:.2f}%")


# ---------------------------------------------------------
# Task 3: 95% Confidence Interval for the difference
# ---------------------------------------------------------
p1 = new_rate
n1 = experiment.loc[experiment["group"] == "New_Design", "visitors"].values[0]
p2 = ctrl_rate
n2 = experiment.loc[experiment["group"] == "Control", "visitors"].values[0]

diff = p1 - p2
se_diff = np.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
ci_low = diff - 1.96 * se_diff
ci_high = diff + 1.96 * se_diff

print("\n=== TASK 3: 95% Confidence Interval ===")
print(f"95% CI for the difference: ({ci_low*100:.2f}%, {ci_high*100:.2f}%)")


# ---------------------------------------------------------
# Task 4: Statistical Significance Test (Two-proportion Z-test)
# ---------------------------------------------------------
successes = np.array([343, 288]) # New_Design, Control
nobs = np.array([2450, 2400])

z_stat, p_value = proportions_ztest(successes, nobs)

print("\n=== TASK 4: Hypothesis Test ===")
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")
if p_value < 0.05:
    print("Result: Statistically significant (Reject the null hypothesis at alpha = 0.05)")
else:
    print("Result: Not statistically significant")


# ---------------------------------------------------------
# Task 5: Business Recommendation & Interpretation
# ---------------------------------------------------------
print("\n=== TASK 5: Recommendation & Interpretation ===")
print("""
1. Statistical Significance: With a p-value of approx 0.0385 (less than 0.05), the improvement is statistically significant, meaning it is unlikely to have occurred purely by random chance.
2. Practical Business Value: A 16.67% relative lift (or 2 percentage point increase) translates to meaningful additional enrollments at scale, confirming practical value.
3. Recommendation: Roll out the new design. The evidence shows that the performance boost is reliable and not a fluke of random variation.
""")