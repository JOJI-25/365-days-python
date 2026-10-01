import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load Data
data = {
    "customer_id": range(701, 716),
    "age": [24, 31, 45, 52, 29, 63, 38, 47, 26, 58, 34, 41, 69, 36, 55],
    "transactions_30d": [14, 8, 3, 2, 11, 1, 7, 4, 16, 2, 9, 6, 0, 10, 3],
    "avg_balance": [
        42000,
        28000,
        76000,
        91000,
        35000,
        120000,
        47000,
        68000,
        24000,
        105000,
        39000,
        52000,
        150000,
        44000,
        82000,
    ],
    "login_days_30d": [18, 12, 5, 3, 15, 2, 10, 6, 21, 4, 14, 8, 1, 16, 5],
    "support_contacts": [0, 1, 2, 3, 0, 4, 1, 2, 0, 3, 1, 1, 5, 0, 2],
    "inactive_next_month": [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
}
df = pd.DataFrame(data)

# 2. Feature Engineering
# Engagement intensity: transactions per login day
df["engagement_intensity"] = df["transactions_30d"] / (
    df["login_days_30d"] + 1
)
# Frustration index: support contacts relative to transactions
df["frustration_index"] = df["support_contacts"] / (
    df["transactions_30d"] + 1
)

# 3. Model Training & Evaluation
features = [
    "age",
    "transactions_30d",
    "avg_balance",
    "login_days_30d",
    "support_contacts",
    "engagement_intensity",
    "frustration_index",
]
X = df[features]
y = df["inactive_next_month"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale features and train Logistic Regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Predictions & Probabilities
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

print("--- Model Evaluation ---")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 4. Practical Tiered Risk Strategy Implementation
df["predicted_churn_prob"] = model.predict_proba(
    scaler.transform(X[features])
)[:, 1]


def assign_retention_tier(row):
    if (
        row["predicted_churn_prob"] > 0.5
        and row["avg_balance"] > 50000
        and row["support_contacts"] >= 2
    ):
        return "Tier 1: High-Value Human Outreach"
    elif row["predicted_churn_prob"] > 0.5:
        return "Tier 2: Automated Digital Nudge & Incentive"
    else:
        return "Tier 3: Monitor / No Action"


df["retention_strategy"] = df.apply(assign_retention_tier, axis=1)

print("\n--- Customer Retention Action Plan ---")
print(
    df[["customer_id", "avg_balance", "predicted_churn_prob", "retention_strategy"]]
)