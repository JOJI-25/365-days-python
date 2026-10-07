import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Data setup
data = {
    "ride_id": range(6001, 6016),
    "estimated_fare": [
        180, 420, 250, 680, 310,
        520, 160, 750, 290, 470,
        220, 610, 840, 330, 560
    ],
    "distance_km": [
        4.2, 12.5, 6.1, 18.2, 7.5,
        11.0, 3.1, 21.0, 5.8, 9.7,
        4.9, 14.8, 23.5, 7.2, 13.1
    ],
    "driver_eta_min": [
        4, 8, 5, 13, 6,
        11, 3, 15, 5, 9,
        4, 12, 18, 6, 10
    ],
    "surge_multiplier": [
        1.0, 1.2, 1.0, 1.5, 1.1,
        1.3, 1.0, 1.6, 1.0, 1.2,
        1.0, 1.4, 1.7, 1.1, 1.3
    ],
    "customer_previous_cancellations": [
        0, 1, 0, 2, 0,
        1, 0, 3, 0, 1,
        0, 2, 1, 0, 2
    ],
    "cancelled": [
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 1, 0, 1
    ]
}
df = pd.DataFrame(data)

# 1. Compare cancelled vs non-cancelled rides
print("--- 1. Feature Comparison (Cancelled vs. Non-Cancelled) ---")
comparison = df.groupby("cancelled")[["estimated_fare", "distance_km", "driver_eta_min", "surge_multiplier", "customer_previous_cancellations"]].mean()
print(comparison)
print("\nStrongest potential signals: Driver ETA, Surge Multiplier, and Previous Cancellations show significantly higher averages in cancelled rides.\n")

# 2. Feature Engineering
# Feature 1: 'fare_per_km' - Represents cost sensitivity / pricing efficiency per unit distance.
# Feature 2: 'wait_friction_score' - Interaction of driver ETA and surge multiplier (waiting longer under high pricing friction).
df["fare_per_km"] = df["estimated_fare"] / df["distance_km"]
df["wait_friction_score"] = df["driver_eta_min"] * df["surge_multiplier"]

print("--- 2. Engineered Features Sample ---")
print(df[["ride_id", "fare_per_km", "wait_friction_score", "cancelled"]].head())
print()

# 3. Build a baseline scikit-learn classification model
X = df[["estimated_fare", "distance_km", "driver_eta_min", "surge_multiplier", "customer_previous_cancellations", "fare_per_km", "wait_friction_score"]]
y = df["cancelled"]

# Split data (using a small test size or train-test split; note dataset has 15 rows)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("--- 3. Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 4. Analyze model coefficients / feature importance
print("--- 4. Feature Importance (Logistic Regression Coefficients) ---")
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
}).sort_values(by="Coefficient", ascending=False)
print(coefficients.to_string(index=False))
print()

# 5. Practical Intervention Strategy
print("--- 5. Practical Intervention Strategy ---")
print("""
Strategy to Reduce Cancellations Efficiently:
1. Risk Thresholding: Score incoming ride requests in real-time using the trained model to assign a cancellation probability.
2. Targeted Interventions (High-Risk Only):
   - For customers predicted to be at **high risk** of cancellation due to high driver ETA, dispatch nearby alternative drivers or display live driver-movement tracking to reduce perceived wait time.
   - For high price-friction risk, provide minor dynamic time-bound incentives or clearer fare breakdowns *only* when the risk score exceeds a strict threshold.
3. Cost Optimization: Avoid blanket discounts or incentives to all users. Reserve interventions exclusively for high-propensity cancellation segments to protect profit margins while saving driver time and fuel.
""")