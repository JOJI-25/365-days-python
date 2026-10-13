import numpy as np

latency = np.array([
    [112, 118, 115, 121, 119, 124, 117, 122, 126, 120, 123, 125],
    [85,  88,  86,  90,  87,  89,  91,  88,  92,  90,  89,  91],
    [145, 150, 148, 152, 155, 149, 151, 158, 210, 225, 218, 230],
    [65,  68,  67,  66,  70,  69,  68,  71,  67,  69,  70,  68]
])
services = np.array([
    "Authentication",
    "Search",
    "Checkout",
    "Notifications"
])

# 1. Calculate mean, median, and standard deviation
means = np.mean(latency, axis=1)
medians = np.median(latency, axis=1)
stds = np.std(latency, axis=1)

print("--- 1. Descriptive Statistics ---")
for s, m, med, st in zip(services, means, medians, stds):
    print(f"Service: {s} | Mean: {m:.2f} ms | Median: {med:.2f} ms | Std Dev: {st:.2f} ms")

max_std_service = services[np.argmax(stds)]
print(f"Service with greatest overall response-time variability: {max_std_service}\n")

# 2. Three-window moving average using np.convolve
weights = np.ones(3) / 3.0
print("--- 2. Three-Window Moving Average ---")
for i, s in enumerate(services):
    ma = np.convolve(latency[i], weights, mode='valid')
    print(f"{s}: {[round(x, 2) for x in ma]}")
print()

# 3. Median Absolute Deviation (MAD) anomaly detection
print("--- 3. Anomaly Detection (Values > Median + 3 * MAD) ---")
anomalies = []
for i, s in enumerate(services):
    med = medians[i]
    mad = np.median(np.abs(latency[i] - med))
    threshold = med + 3 * mad
    for j, val in enumerate(latency[i]):
        if val > threshold:
            anomalies.append((s, j + 1, val, med, mad))
            print(f"Anomaly detected in {s} at Window {j + 1}: Latency = {val} ms (Median = {med}, MAD = {mad})")

if not anomalies:
    print("No anomalies detected based on the threshold.")
print()

# 4. Percentage increase between first 6 and last 6 windows
print("--- 4. Percentage Increase (First 6 vs Last 6 Windows) ---")
first_six_means = np.mean(latency[:, :6], axis=1)
last_six_means = np.mean(latency[:, 6:], axis=1)
pct_increases = ((last_six_means - first_six_means) / first_six_means) * 100

for s, f_mean, l_mean, pct in zip(services, first_six_means, last_six_means, pct_increases):
    print(f"{s} | First 6 Mean: {f_mean:.2f} ms | Last 6 Mean: {l_mean:.2f} ms | Increase: {pct:.2f}%")
print()

# 5. Priority Recommendation
print("--- 5. Priority Recommendation ---")
print(f"Recommendation: '{max_std_service}' should receive the highest investigation priority.")