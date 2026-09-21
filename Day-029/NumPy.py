import numpy as np

probabilities = np.array([
    [0.70, 0.20, 0.10],
    [0.15, 0.65, 0.20],
    [0.40, 0.35, 0.25],
    [0.10, 0.25, 0.65],
    [0.55, 0.30, 0.15]
])

# Segment name mapping
segment_names = ["Low Value", "Medium Value", "High Value"]

# 1. Determine the predicted segment for each customer
predicted_indices = np.argmax(probabilities, axis=1)
predicted_segments = [segment_names[i] for i in predicted_indices]

# 2. Extract the highest probability for every customer
highest_probabilities = np.max(probabilities, axis=1)

# 3. Calculate the average probability assigned to each segment across all customers
average_probabilities = np.mean(probabilities, axis=0)

# 4. Identify customers whose highest prediction probability is below 0.60
low_confidence_mask = highest_probabilities < 0.60
low_confidence_customers = np.where(low_confidence_mask)[0]

# 5. Calculate prediction confidence (difference between highest and second-highest)
sorted_probs = np.sort(probabilities, axis=1)
confidences = sorted_probs[:, -1] - sorted_probs[:, -2]

# 6. Identify the customer with the lowest prediction confidence
lowest_confidence_customer = np.argmin(confidences)

# --- Output Results ---
print("Predicted Segments:", predicted_segments)
print("Highest Probabilities:", highest_probabilities)
print("Average Segment Probabilities:", dict(zip(segment_names, average_probabilities)))
print("Customers with Max Probability < 0.60 (0-indexed):", low_confidence_customers.tolist())
print("Prediction Confidences:", confidences)
print("Customer with Lowest Confidence (0-indexed):", lowest_confidence_customer)