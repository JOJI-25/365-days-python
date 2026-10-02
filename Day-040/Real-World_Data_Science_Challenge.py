import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Input data
data = {
    "customer_id": range(901, 916),
    "monthly_usage_gb": [18, 42, 65, 12, 55, 73, 21, 48, 81, 15, 37, 69, 90, 28, 60],
    "monthly_calls": [85, 140, 190, 60, 155, 210, 95, 130, 225, 70, 120, 180, 240, 105, 165],
    "streaming_hours": [4, 15, 28, 2, 21, 35, 7, 18, 42, 3, 12, 31, 50, 8, 25],
    "support_tickets": [0, 1, 2, 0, 1, 3, 0, 1, 2, 0, 1, 2, 3, 0, 1],
    "current_plan_price": [399, 399, 499, 299, 499, 499, 299, 399, 599, 299, 399, 499, 599, 299, 499],
    "upgraded_next_month": [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# 1. Compare customers who upgraded vs those who did not
print("--- 1. Behavioural Comparison ---")
comparison = df.groupby('upgraded_next_month')[
    ['monthly_usage_gb', 'monthly_calls', 'streaming_hours', 'support_tickets', 'current_plan_price']
].mean()
print(comparison)
print()

# 2. Engineer features
# Feature 1: Total Digital Activity (combining usage and streaming)
# Feature 2: Usage-to-Price Ratio (measuring value extraction relative to plan price)
df['total_digital_activity'] = df['monthly_usage_gb'] + df['streaming_hours']
df['usage_to_price_ratio'] = df['monthly_usage_gb'] / df['current_plan_price']

print("--- 2. Engineered Features (Sample) ---")
print(df[['customer_id', 'total_digital_activity', 'usage_to_price_ratio', 'upgraded_next_month']].head())
print()

# 3. Build baseline classification model using scikit-learn
X = df[[
    'monthly_usage_gb', 'monthly_calls', 'streaming_hours', 
    'support_tickets', 'current_plan_price', 
    'total_digital_activity', 'usage_to_price_ratio'
]]
y = df['upgraded_next_month']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Using a pipeline with StandardScaler and Logistic Regression
from sklearn.pipeline import make_pipeline
model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42))
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("--- 3. Model Performance Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 4. Examine model coefficients / feature importance
log_reg = model.named_steps['logisticregression']
coefficients = pd.Series(log_reg.coef_[0], index=X.columns)

print("--- 4. Feature Importance (Standardised Coefficients) ---")
print(coefficients.sort_values(ascending=False))
print()

# 5. Targeted strategy summary
print("--- 5. Targeted Marketing Strategy Summary ---")
print("Target customers with high usage-to-price ratios and high data/streaming activity.")
print("Avoid blanket marketing to prevent wasted spend and customer fatigue.")