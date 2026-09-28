import pandas as pd
import numpy as np

watch_time = pd.DataFrame({
    "session_minutes": [
        12, 18, 21, 25, 27, 30, 32, 35, 38, 41,
        44, 47, 50, 53, 56, 60, 65, 72, 80, 140
    ]
})

s = watch_time["session_minutes"]
mean_val = s.mean()
median_val = s.median()
std_val = s.std(ddof=1) # sample std
q1 = s.quantile(0.25)
q3 = s.quantile(0.75)
iqr = q3 - q1

# Outlier bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Std: {std_val}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Lower Bound: {lower_bound}")
print(f"Upper Bound: {upper_bound}")
print(f"Is 140 an outlier? {140 > upper_bound}")