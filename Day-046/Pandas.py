import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset initialization
data = {
    "student_id": range(301, 313),
    "department": [
        "CSE", "ECE", "CSE", "ME",
        "ECE", "CSE", "ME", "ECE",
        "CSE", "ME", "ECE", "CSE"
    ],
    "attendance_pct": [
        92, 78, 88, 65, 81, 95,
        72, 84, 69, 76, 90, 97
    ],
    "assignment_score": [
        86, 72, 91, 58, 75, 94,
        64, 82, 61, 70, 88, 96
    ],
    "exam_score": [
        89, 68, 93, 55, 74, 97,
        61, 79, 58, 67, 91, 98
    ],
    "projects_completed": [
        4, 3, 5, 2, 3, 5,
        2, 4, 2, 3, 4, 5
    ]
}

df = pd.DataFrame(data)

# 1. Calculate final_score and status classification
df['final_score'] = (0.3 * df['assignment_score']) + (0.7 * df['exam_score'])
df['status'] = np.where(df['final_score'] >= 50, 'Pass', 'Fail')

print("--- Student Dataset with Final Scores & Status ---")
print(df[['student_id', 'department', 'attendance_pct', 'final_score', 'status']])
print()

# 2. Compare departments
dept_summary = df.groupby('department').agg(
    avg_attendance=('attendance_pct', 'mean'),
    avg_final_score=('final_score', 'mean'),
    avg_projects=('projects_completed', 'mean')
).reset_index()

print("--- Department Comparison ---")
print(dept_summary.to_string(index=False))
print()

# 3. Correlation between attendance percentage and final score
correlation = df['attendance_pct'].corr(df['final_score'])
print(f"--- Correlation Analysis ---")
print(f"Correlation coefficient: {correlation:.4f}\n")

# Visualization: Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x='attendance_pct', y='final_score', color='b', marker='o')
plt.title('Attendance Percentage vs. Final Score')
plt.xlabel('Attendance Percentage (%)')
plt.ylabel('Final Score')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('attendance_vs_score.png')
plt.show()

# 4. Identify students with attendance < 75% but final score > overall average
overall_avg_score = df['final_score'].mean()
interesting_group = df[(df['attendance_pct'] < 75) & (df['final_score'] > overall_avg_score)]

print("--- Low Attendance & High Performance Analysis ---")
print(f"Overall Average Final Score: {overall_avg_score:.2f}")
print(f"Number of students with < 75% attendance AND > overall average score: {len(interesting_group)}")
if len(interesting_group) > 0:
    print(interesting_group[['student_id', 'department', 'attendance_pct', 'final_score']])
else:
    print("None found in this dataset. All students with attendance below 75% also scored below the overall average.")