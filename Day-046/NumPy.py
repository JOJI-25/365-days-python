import numpy as np

defects = np.array([
    [12, 15, 11, 14, 18, 13, 16, 15],
    [7,  9,  8,  10, 6,  11, 9,  8],
    [21, 18, 25, 23, 27, 20, 29, 24],
    [4,  6, 5, 7, 4, 8, 6, 5]
])

lines = np.array(["Line_A", "Line_B", "Line_C", "Line_D"])

# Calculate the total and average number of defects for each production line and identify the line with the highest defect rate.

total_defects = defects.sum(axis=1)
avg_defects = defects.mean(axis=1)
max_defect = total_defects.max()
max_defect_line = lines[np.argmax(total_defects)]

print("=== 1. Total & Average Defects ===")
for i in range(len(lines)):
    print(f"{lines[i]}: Total = {total_defects[i]}, Average = {avg_defects[i]:.2f}")
print(f"Line with highest defect rate: {max_defect_line} ({max_defect} defects)")
print()

# 

# 