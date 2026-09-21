import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
data = {
    "student_id": [
        "S01", "S02", "S03", "S04", "S05",
        "S06", "S07", "S08", "S09", "S10",
        "S11", "S12"
    ],
    "age": [21, 25, 19, 32, 28, 24, 35, 22, 27, 30, 20, 26],
    "weekly_study_hours": [8, 14, 5, 3, 12, 18, 4, 10, 6, 15, 7, 11],
    "assignments_completed": [8, 12, 4, 3, 10, 15, 5, 9, 6, 13, 5, 10],
    "avg_quiz_score": [72, 85, 61, 48, 79, 91, 52, 76, 64, 88, 58, 81],
    "login_days": [18, 25, 10, 7, 22, 28, 9, 20, 13, 26, 11, 21],
    "forum_posts": [4, 8, 1, 0, 5, 9, 1, 6, 2, 7, 2, 5],
    "final_status": [
        "Completed", "Completed", "Dropped", "Dropped",
        "Completed", "Completed", "Dropped", "Completed",
        "Dropped", "Completed", "Dropped", "Completed"
    ]
}

students = pd.DataFrame(data)

# A. Data preparation
students["target"] = students["final_status"].map({"Dropped": 1, "Completed": 0})
missing_values = students.isnull().sum().sum()
print(f"Total Missing Values: {missing_values}")

# B. Compare behavior by group
numeric_cols = ["age", "weekly_study_hours", "assignments_completed", "avg_quiz_score", "login_days", "forum_posts"]
comparison = students.groupby("final_status")[numeric_cols].mean()
print("\n--- Mean Metrics by Status ---")
print(comparison)

# C. Correlation with target
correlations = students[numeric_cols + ["target"]].corr()["target"].sort_values(ascending=False)
print("\n--- Correlation with Target (Dropped = 1) ---")
print(correlations)

# D. Risk Score Logic
def calculate_risk(row):
    score = 0
    if row["weekly_study_hours"] < 8: score += 1
    if row["avg_quiz_score"] < 65: score += 1
    if row["login_days"] < 15: score += 1
    if row["assignments_completed"] < 7: score += 1
    return score

students["risk_score"] = students.apply(calculate_risk, axis=1)
print("\n--- Student Risk Scores ---")
print(students[["student_id", "final_status", "risk_score", "weekly_study_hours", "avg_quiz_score", "login_days"]])

# E. Visualizations
plt.figure(figsize=(12, 5))

# Plot 1: Scatter plot of Login Days vs. Average Quiz Score
plt.subplot(1, 2, 1)
sns.scatterplot(
    data=students, 
    x="login_days", 
    y="avg_quiz_score", 
    hue="final_status", 
    palette={"Completed": "green", "Dropped": "red"}, 
    s=100
)
plt.title("Login Days vs. Average Quiz Score")
plt.xlabel("Total Login Days")
plt.ylabel("Average Quiz Score (%)")
plt.grid(True, linestyle="--", alpha=0.5)

# Plot 2: Bar chart of Weekly Study Hours by Student ID
plt.subplot(1, 2, 2)
sns.barplot(
    data=students, 
    x="student_id", 
    y="weekly_study_hours", 
    hue="final_status", 
    dodge=False,
    palette={"Completed": "skyblue", "Dropped": "salmon"}
)
plt.title("Weekly Study Hours by Student")
plt.xlabel("Student ID")
plt.ylabel("Weekly Study Hours")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()