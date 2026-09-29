import numpy as np

temperature = np.array([
    71.2, 72.1, 71.8, 72.5, 73.0, 73.4,
    74.2, 75.1, 76.0, 77.2, 78.5, 79.1,
    80.3, 81.0, 82.5, 84.8, 86.2, 88.0,
    91.5, 93.2, 89.8, 86.5, 82.1, 78.4
])

mean = temperature.mean()
median = np.median(temperature)
minimum = temperature.min()
maximum = temperature.max()
standard_deviation = temperature.std()

print("mean", mean)
print("median", median)
print("minimum", minimum)
print("maximum", maximum)
print("standard_deviation", standard_deviation)


indices_above_85 = np.where(temperature>85)[0]
print("Indices above 85:", indices_above_85)


deviations = temperature - mean
top_3_indices = np.argsort(deviations)[-3:][::-1]
top_3_values = deviations[top_3_indices]

print(f"All deviations from mean: {deviations}")
print(f"Top 3 positive deviation indices: {top_3_indices}")
print(f"Top 3 positive deviation values: {top_3_values}")


percentage_above_85 = (np.sum(temperature > 85) / len(temperature)) * 100
print(f"Percentage above 85°C: {percentage_above_85}%")


classification = np.select(
    [
        temperature < 80,
        (temperature >= 80) & (temperature <= 85),
        temperature > 85,
    ],
    ["Normal", "Warning", "Critical"],
    default="Unknown",
)
print(f"Classification array: {classification}")

