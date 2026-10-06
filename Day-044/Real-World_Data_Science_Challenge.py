import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

data = {
    "order_id": range(3001, 3016),
    "distance_km": [
        2.5,
        6.2,
        3.1,
        9.5,
        4.0,
        12.0,
        2.8,
        7.4,
        5.1,
        10.5,
        3.6,
        8.2,
        14.0,
        4.7,
        11.3,
    ],
    "prep_time_min": [18, 25, 20, 31, 22, 35, 17, 28, 24, 33, 19, 29, 38, 23, 34],
    "driver_experience_years": [
        4.2,
        1.1,
        3.5,
        0.8,
        5.0,
        0.5,
        4.8,
        1.7,
        3.2,
        1.0,
        6.0,
        2.1,
        0.4,
        4.0,
        0.9,
    ],
    "traffic_score": [2, 7, 3, 8, 4, 9, 2, 6, 5, 8, 3, 7, 10, 4, 9],
    "restaurant_rating": [
        4.6,
        4.2,
        4.7,
        3.9,
        4.5,
        4.0,
        4.8,
        4.1,
        4.4,
        3.8,
        4.7,
        4.0,
        3.7,
        4.5,
        3.9,
    ],
    "late": [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
}
df = pd.DataFrame(data)

print("=== 1. Statistical Comparison (Means) ===")
comparison = df.groupby("late").mean()
print(comparison[["distance_km", "prep_time_min", "driver_experience_years", "traffic_score", "restaurant_rating"]])
print("\n")

df["traffic_distance_load"] = df["distance_km"] * df["traffic_score"]

df["prep_to_experience_ratio"] = df["prep_time_min"] / (df["driver_experience_years"] + 0.1)

features = [
    "distance_km",
    "prep_time_min",
    "driver_experience_years",
    "traffic_score",
    "restaurant_rating",
    "traffic_distance_load",
]
X = df[features]
y = df["late"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("=== 3. Model Evaluation ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("=== 4. Model Coefficients ===")
for feat, coef in zip(features, model.coef_[0]):
  print(f"{feat}: {coef:.4f}")