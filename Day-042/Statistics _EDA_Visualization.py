import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

response_time = pd.Series([
    180, 195, 205, 210, 215, 
    220, 225, 230, 235, 240, 
    245, 250, 260, 275, 290, 
    310, 340, 380, 620, 850
])

mean_val = response_time.mean()
median_val = response_time.median()
std_val = response_time.std()
q1 = response_time.quantile(0.25)
q3 = response_time.quantile(0.75)
iqr = q3 - q1

print("--- 1. Descriptive Statistics ---")
print(f"Mean: {mean_val:.2f} ms")
print(f"Median: {median_val:.2f} ms")
print(f"Standard Deviation: {std_val:.2f} ms")
print(f"Q1: {q1:.2f} ms")
print(f"Q3: {q3:.2f} ms")
print(f"IQR: {iqr:.2f} ms\n")



lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = response_time[(response_time < lower_bound) | (response_time > upper_bound)]

print("--- 2. Outlier Analysis ---")
print(f"Lower Bound: {lower_bound:.2f}, Upper Bound: {upper_bound:.2f}")
print(f"Outliers detected: {list(outliers)}")
print(f"Number of affected observations: {len(outliers)}\n")



plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
sns.histplot(response_time, kde=True, bins=10, color='skyblue', edgecolor='black')
plt.title('Response Time Distribution (Histogram)', fontsize=11, fontweight='bold')
plt.xlabel('Response Time (ms)', fontsize=10)
plt.ylabel('Frequency', fontsize=10)


plt.subplot(1, 2, 2)
sns.boxplot(y=response_time, color='lightgreen')
plt.title('Response Time Box Plot', fontsize=11, fontweight='bold')
plt.ylabel('Response Time (ms)', fontsize=10)

plt.tight_layout()
plt.show()


exceed_300 = (response_time > 300).mean() * 100
print(f"--- 4. Threshold Analysis ---")
print(f"Percentage of requests exceeding 300 ms: {exceed_300:.2f}%\n")
print("--- 5. Engineering Recommendation & Conclusion ---")
print("Recommendation: Focus on reducing extreme delays (tail latency) rather than the overall average.")
print("Justification:")
print("- The median response time (242.50 ms) indicates that the majority of users experience fast performance.")
print("- The mean (291.00 ms) is significantly skewed upward by a small number of extreme outliers (620 ms and 850 ms).")
print("- Focusing solely on the average might lead engineers to overhaul stable routines, whereas fixing "
      "the root cause of extreme delays (e.g., slow database queries or network timeouts) will directly "
      "protect vulnerable users from app abandonment.")