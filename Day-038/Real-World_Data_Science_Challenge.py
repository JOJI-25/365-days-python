import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

# 1. Dataset Setup
data = {
    "patient_id": range(501, 516),
    "age": [22, 45, 31, 67, 29, 54, 38, 72, 26, 61, 43, 35, 78, 49, 24],
    "days_waiting": [3, 14, 7, 21, 5, 18, 10, 25, 2, 16, 8, 12, 30, 20, 4],
    "previous_missed": [0, 1, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 4, 1, 0],
    "reminder_sent": [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    "distance_km": [4, 12, 6, 25, 3, 18, 7, 30, 5, 22, 9, 15, 28, 17, 4],
    "missed": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
}
df = pd.DataFrame(data)

# 2. Compare Summary Statistics (Attended vs. Missed)
summary = df.groupby("missed")[
    ["days_waiting", "previous_missed", "distance_km"]
].mean()
print("--- Mean Statistics by Attendance Status ---")
print(summary)
print("\n")

# 3. Feature Engineering
# Feature 1: Logistical friction interaction (days waiting * distance)
df["wait_distance_interaction"] = df["days_waiting"] * df["distance_km"]
# Feature 2: Unreminded wait time (days waiting without a reminder sent)
df["unreminded_wait"] = df["days_waiting"] * (1 - df["reminder_sent"])

# 4. Prepare Data for Modeling
features = [
    "days_waiting",
    "previous_missed",
    "reminder_sent",
    "distance_km",
    "wait_distance_interaction",
    "unreminded_wait",
]
X = df[features]
y = df["missed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# 5. Train Baseline Classifier
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 6. Predictions & Evaluation
y_pred = model.predict(X_test)

print("--- Model Evaluation Metrics ---")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, zero_division=0):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred, zero_division=0):.4f}")
print(f"F1-Score:  {f1_score(y_test, y_pred, zero_division=0):.4f}\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))