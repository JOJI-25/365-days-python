import numpy as np

accuracy = np.array([
    [0.91, 0.93, 0.95],
    [0.82, 0.85, 0.89],
    [0.76, 0.80, 0.83],
    [0.88, 0.87, 0.91],
    [0.94, 0.95, 0.96]
])

# 1. Average accuracy of each model across all classes
model_avg = np.mean(accuracy, axis=0)
print("1. Average accuracy of each model:")
print(f"   - Model A: {model_avg[0]:.3f}")
print(f"   - Model B: {model_avg[1]:.3f}")
print(f"   - Model C: {model_avg[2]:.3f}")

# 2. Best-performing model overall
models = ['Model A', 'Model B', 'Model C']
best_model = models[np.argmax(model_avg)]
print(f"\n2. Best-performing model overall: {best_model}")

# 3. Improvement from Model A to Model C for each class
improvement = accuracy[:, 2] - accuracy[:, 0]
print("\n3. Improvement from Model A to Model C per class:")
for i, imp in enumerate(improvement, 1):
    print(f"   - Class {i}: +{imp:.2f}")

# 4. Class that improved the most
best_improved_class = np.argmax(improvement) + 1
print(f"\n4. Class that improved the most: Class {best_improved_class} (+{np.max(improvement):.2f})")

# 5. Classes where Model C achieved at least 90% accuracy
class_c_90 = np.where(accuracy[:, 2] >= 0.90)[0] + 1
print(f"\n5. Classes where Model C achieved >= 90% accuracy: {list(class_c_90)}")

# 6. Standard deviation of accuracy across classes for each model
model_std = np.std(accuracy, axis=0)
print("\n6. Standard deviation across classes:")
print(f"   - Model A: {model_std[0]:.4f}")
print(f"   - Model B: {model_std[1]:.4f}")
print(f"   - Model C: {model_std[2]:.4f}")

# 7. Model with the most consistent performance
most_consistent = models[np.argmin(model_std)]
print(f"\n7. Most consistent model (lowest std dev): {most_consistent}")

# 8. Average accuracy improvement from Model A to Model C
avg_improvement = np.mean(improvement)
print(f"\n8. Average accuracy improvement from Model A to Model C: {avg_improvement:.3f}")

# 9. Identify whether every class improved between Model A and Model C
every_improved = np.all(accuracy[:, 2] > accuracy[:, 0])
print(f"\n9. Did every class improve from Model A to Model C? {every_improved}")