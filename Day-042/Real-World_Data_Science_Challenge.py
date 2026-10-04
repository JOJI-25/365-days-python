import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

data = {
    "policy_id": range(1201, 1216),
    "age": [23, 35, 47, 61, 29, 52, 38, 68, 26, 44, 57, 32, 71, 41, 50],
    "annual_premium": [18000, 24000, 32000, 41000, 21000, 35000, 27000, 46000, 19000, 30000, 38000, 23000, 49000, 28000, 34000],
    "previous_claims": [0, 1, 2, 3, 0, 2, 1, 4, 0, 1, 2, 0, 5, 1, 2],
    "vehicle_age": [2, 5, 8, 11, 3, 7, 4, 13, 1, 6, 9, 2, 15, 5, 8],
    "annual_km": [8000, 14000, 19000, 22000, 9500, 17000, 12000, 25000, 7000, 16000, 21000, 9000, 28000, 13000, 18000],
    "claim_next_year": [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

# 1. Compare policyholders who filed claims vs those who did not
comparison = df.groupby('claim_next_year')[['previous_claims', 'vehicle_age', 'annual_km', 'age', 'annual_premium']].mean()
print("--- 1. Feature Means by Claim Status (0: No Claim, 1: Claim) ---")
print(comparison)
print()


# 2. Feature Engineering
# Feature 1: Driving intensity relative to vehicle age (annual km per year of vehicle age)
df['km_per_vehicle_age'] = df['annual_km'] / (df['vehicle_age'] + 1)
# Feature 2: Claim history density relative to age
df['claim_density'] = df['previous_claims'] / (df['age'] - 18 + 1)

print("--- 2. Engineered Features Sample ---")
print(df[['policy_id', 'km_per_vehicle_age', 'claim_density']].head())
print()


# 3. Build a baseline scikit-learn classification model
features = ['age', 'annual_premium', 'previous_claims', 'vehicle_age', 'annual_km', 'km_per_vehicle_age', 'claim_density']
X = df[features]
y = df['claim_next_year']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

print("--- 3. Model Evaluation ---")
print(classification_report(y_test, y_pred, zero_division=0))
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_prob):.2f}\n")


# 4. Analyze feature coefficients
coefficients = pd.Series(model.coef_[0], index=features).sort_values(ascending=False)
print("--- 4. Logistic Regression Coefficients ---")
print(coefficients)
print()


# 5. Strategic Recommendation Summary
print("--- 5. Practical Recommendation & Business Implication ---")
print("Recommendation:")
print("- Use the model's predicted risk probabilities rather than a strict cutoff.")
print("- Balance precision and recall by tuning the classification threshold: lower the threshold "
      "if the goal is to capture all potential high-risk claims for manual review, or raise it to "
      "avoid alienating low-risk customers with unnecessary investigative overhead.")