import numpy as np

# Dataset of existing customers (6 customers, 4 features)
customers = np.array([
    [12, 850, 45, 0.20],
    [18, 920, 60, 0.15],
    [4,  450, 20, 0.70],
    [10, 780, 42, 0.25],
    [3,  420, 18, 0.80],
    [15, 880, 52, 0.18]
])

# New customer profile
new_customer = np.array([11, 800, 40, 0.30])

# 1. Feature differences
differences = customers - new_customer
print("Feature Differences:\n", differences)

# 2. Euclidean distance
distances = np.linalg.norm(differences, axis=1)
print("\nEuclidean Distances:", np.round(distances, 2))

# 3 & 4. Identify top 3 and most similar customers
top_3_indices = np.argsort(distances)[:3]
most_similar_index = np.argmin(distances)
print(f"\nMost Similar Customer Index: Customer {most_similar_index} (Distance: {distances[most_similar_index]:.2f})")
print(f"Top 3 Most Similar Customers Indices: {top_3_indices}")

# 5. Mean value of each feature across all customers
mean_features = np.mean(customers, axis=0)
print("\nMean Feature Values:", mean_features)

# 6. Feature numerical scale differences (Peak-to-peak range)
feature_ranges = np.ptp(customers, axis=0)
print("Feature Ranges (Max - Min):", feature_ranges)

# 8. Min-max scaling
min_val = np.min(customers, axis=0)
max_val = np.max(customers, axis=0)
customers_scaled = (customers - min_val) / (max_val - min_val)
new_customer_scaled = (new_customer - min_val) / (max_val - min_val)

# 9. Recalculate distances using normalized data
distances_scaled = np.linalg.norm(customers_scaled - new_customer_scaled, axis=1)
top_3_scaled = np.argsort(distances_scaled)[:3]
most_similar_scaled = np.argmin(distances_scaled)

print("\nScaled Distances:", np.round(distances_scaled, 2))
print(f"Most Similar Customer (Scaled): Customer {most_similar_scaled}")
print(f"Top 3 Customers (Scaled): {top_3_scaled}")