import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.preprocessing import StandardScaler

# -------------------------------------------------------------------------
# Dataset Initialization
# -------------------------------------------------------------------------
data = {
    "seller_id": list(range(1001, 1016)),
    "products_listed": [42, 18, 75, 9, 51, 63, 14, 37, 82, 11, 29, 56, 7, 68, 24],
    "orders_30d": [31, 8, 54, 3, 27, 46, 5, 19, 61, 4, 13, 38, 2, 49, 11],
    "avg_rating": [
        4.6, 4.1, 4.8, 3.7, 4.5, 4.7, 3.9, 4.2, 4.9, 3.6, 4.0, 4.6, 3.5, 4.8, 4.1
    ],
    "returns_30d": [1, 2, 0, 3, 1, 0, 2, 1, 0, 3, 2, 1, 4, 0, 2],
    "days_since_last_order": [2, 9, 1, 24, 4, 3, 18, 7, 1, 27, 12, 5, 30, 2, 14],
    "support_tickets": [0, 1, 0, 3, 1, 0, 2, 1, 0, 4, 2, 1, 5, 0, 2],
    "inactive_next_month": [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
}

df = pd.DataFrame(data)

# -------------------------------------------------------------------------
# Task 1: Statistical Comparison & Risk Signal Identification
# -------------------------------------------------------------------------
base_features = [
    "products_listed",
    "orders_30d",
    "avg_rating",
    "returns_30d",
    "days_since_last_order",
    "support_tickets",
]

comparison = df.groupby("inactive_next_month")[base_features].mean().T
comparison.columns = ["Active (0)", "Inactive (1)"]
comparison["Absolute Difference"] = (
    comparison["Inactive (1)"] - comparison["Active (0)"]
).abs()

print("=== Task 1: Mean Comparison Across Features ===")
print(comparison.round(2))
print()

# -------------------------------------------------------------------------
# Task 2: Feature Engineering
# -------------------------------------------------------------------------
# 1. Return Rate: Operational friction & product quality issues
df["return_rate"] = df["returns_30d"] / (df["orders_30d"] + 1e-5)

# 2. Support-to-Order Ratio: Seller distress and dissatisfaction
df["support_to_order_ratio"] = df["support_tickets"] / (df["orders_30d"] + 1e-5)

# 3. Catalog Turn Ratio: Demand velocity relative to inventory
df["catalog_velocity"] = df["orders_30d"] / (df["products_listed"] + 1e-5)

print("=== Task 2: Engineered Features (Sample) ===")
print(
    df[
        [
            "seller_id",
            "return_rate",
            "support_to_order_ratio",
            "catalog_velocity",
            "inactive_next_month",
        ]
    ].head()
)
print()

# -------------------------------------------------------------------------
# Task 3: Baseline Logistic Regression with Stratified K-Fold
# -------------------------------------------------------------------------
feature_cols = base_features + [
    "return_rate",
    "support_to_order_ratio",
    "catalog_velocity",
]
X = df[feature_cols]
y = df["inactive_next_month"]

# Standardizing for coefficient interpretability
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=feature_cols)

model = LogisticRegression(random_state=42)

# Using Stratified K-Fold due to small sample size (n=15, 4 positives)
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
y_pred = cross_val_predict(model, X_scaled, y, cv=cv)
y_prob = cross_val_predict(model, X_scaled, y, cv=cv, method="predict_proba")[:, 1]

print("=== Task 3: Classification Performance Metrics ===")
print("Confusion Matrix:")
print(confusion_matrix(y, y_pred))
print("\nClassification Report:")
print(classification_report(y, y_pred, target_names=["Active", "Inactive"]))
print(f"ROC-AUC Score: {roc_auc_score(y, y_prob):.3f}\n")

# -------------------------------------------------------------------------
# Task 4: Feature Importance / Correlation Analysis
# -------------------------------------------------------------------------
# Train on full dataset to inspect feature weights
model.fit(X_scaled, y)
importance = pd.DataFrame({
    "Feature": feature_cols,
    "Coefficient": model.coef_[0],
    "Correlation_with_Inactive": [df[col].corr(df["inactive_next_month"]) for col in feature_cols],
}).sort_values(by="Coefficient", ascending=False)

print("=== Task 4: Feature Importance & Correlation ===")
print(importance.to_string(index=False))
print()

# -------------------------------------------------------------------------
# Task 5: Risk Scoring & Retention Prioritisation Framework
# -------------------------------------------------------------------------
df["inactivity_risk_score"] = model.predict_proba(X_scaled)[:, 1]


def assign_retention_tier(score):
    if score >= 0.70:
        return "High Risk (Direct Outreach + Tech Support)"
    elif score >= 0.35:
        return "Medium Risk (Automated Prompt + Ad Credits)"
    else:
        return "Low Risk (No Incentive Needed)"


df["retention_tier"] = df["inactivity_risk_score"].apply(assign_retention_tier)

print("=== Task 5: Retention Prioritisation Table ===")
retention_summary = df[[
    "seller_id",
    "days_since_last_order",
    "orders_30d",
    "inactivity_risk_score",
    "retention_tier",
]].sort_values(by="inactivity_risk_score", ascending=False)

print(retention_summary.to_string(index=False))