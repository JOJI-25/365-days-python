import pandas as pd
import numpy as np

jobs = pd.DataFrame({
    "job_id": [
        "J01", "J02", "J03", "J04", "J05",
        "J06", "J07", "J08", "J09", "J10",
        "J11", "J12", "J13", "J14", "J15"
    ],
    "role": [
        "Data Analyst", "Data Scientist", "BI Analyst",
        "Data Analyst", "ML Engineer", "Data Scientist",
        "BI Analyst", "Data Analyst", "ML Engineer",
        "Data Scientist",
        "Data Analyst", "BI Analyst", "ML Engineer",
        "Data Scientist", "Data Analyst"
    ],
    "city": [
        "Bengaluru", "Bengaluru", "Hyderabad", "Pune", "Bengaluru",
        "Hyderabad", "Pune", "Chennai", "Hyderabad", "Bengaluru",
        "Chennai", "Hyderabad", "Pune", "Pune", "Bengaluru"
    ],
    "experience_years": [
        1, 3, 2, 1, 4,
        5, 2, 3, 4, 6,
        2, 1, 5, 7, 0
    ],
    "salary_lpa": [
        5.2, 11.5, 6.8, 5.8, 14.2,
        15.5, 7.1, 6.2, 12.8, 17.5,
        5.9, 6.5, 13.4, 19.2, 4.8
    ],
    "remote": [
        True, False, True, False, False,
        True, False, True, True, False,
        True, False, False, True, True
    ],
    "python_required": [
        True, True, False, True, True,
        True, False, True, True, True,
        True, False, True, True, True
    ],
    "sql_required": [
        True, True, True, True, False,
        True, True, True, False, True,
        True, True, False, True, True
    ]
})

# A. Salary Exploration
median_sal = jobs["salary_lpa"].median()
mean_sal = jobs["salary_lpa"].mean()
min_sal = jobs["salary_lpa"].min()
max_sal = jobs["salary_lpa"].max()

salary_by_role = jobs.groupby("role")["salary_lpa"].agg(["count", "mean", "median", "min", "max"])
salary_by_city = jobs.groupby("city")["salary_lpa"].agg(["count", "mean", "median", "min", "max"])

print("--- A. Salary Exploration ---")
print(f"Overall Median: {median_sal} LPA | Mean: {mean_sal:.2f} LPA | Min: {min_sal} LPA | Max: {max_sal} LPA\n")
print("Salary by Role:\n", salary_by_role, "\n")
print("Salary by City:\n", salary_by_city, "\n")

# B. Experience Relationship
exp_corr = jobs["experience_years"].corr(jobs["salary_lpa"])
print("--- B. Experience Relationship ---")
print(f"Pearson Correlation (Experience vs Salary): {exp_corr:.3f}\n")

# C. Skill Requirements Analysis
def get_skill_group(row):
    if row["python_required"] and row["sql_required"]:
        return "Both"
    elif row["python_required"]:
        return "Python Only"
    elif row["sql_required"]:
        return "SQL Only"
    else:
        return "Neither"

jobs["skill_group"] = jobs.apply(get_skill_group, axis=1)
salary_by_skill = jobs.groupby("skill_group")["salary_lpa"].agg(["count", "mean", "median"])

print("--- C. Skill Requirements Analysis ---")
print(salary_by_skill, "\n")

# D. Remote-Work Analysis
salary_by_remote = jobs.groupby("remote")["salary_lpa"].agg(["count", "mean", "median"])
print("--- D. Remote-Work Analysis ---")
print(salary_by_remote)