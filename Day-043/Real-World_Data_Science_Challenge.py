import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

data = {
    "order_id": range(1501, 1516),
    "order_value": [
        850, 1200, 450, 2200, 680,
        1750, 520, 3100, 390, 1450,
        980, 2600, 570, 1950, 720
    ],
    "items": [
        2, 4, 1, 6, 2,
        5, 1, 8, 1, 3,
        2, 7, 2, 5, 2
    ],
    "delivery_days": [
        3, 5, 2, 7, 3,
        6, 2, 9, 2, 4,
        3, 8, 3, 6, 4
    ],
    "customer_previous_returns": [
        0, 1, 0, 2, 0,
        1, 0, 3, 0, 1,
        0, 2, 0, 1, 0
    ],
    "discount_percent": [
        5, 20, 0, 30, 10,
        25, 0, 35, 5, 15,
        10, 30, 0, 20, 5
    ],
    "returned": [
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0
    ]
}
df = pd.DataFrame(data)

print("--- 1. Statistical Comparison (Returned vs Non-Returned) ---")
comparison = df.groupby("returned").mean()
print(comparison[['order_value', 'items', 'delivery_days', 'customer_previous_returns', 'discount_percent']])
print()

df['value_per_item'] = df['order_value'] / df['items']
df['delivery_days_per_item'] = df['delivery_days'] / df['items']

print("--- 2. Engineered Features Added ---")
print(df[['order_id', 'value_per_item', 'delivery_days_per_item']].head(3))
print()

X = df[['order_value', 'items', 'delivery_days', 'customer_previous_returns', 'discount_percent', 'value_per_item', 'delivery_days_per_item']]
y = df['returned']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("--- 3. Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print("--- 4. Feature Coefficients (Logistic Regression) ---")
print(coefficients.to_string(index=False))
print()

print("--- 5. Operational Recommendations ---")
print(
    "1. Risk Flagging: Use the model to flag high-risk orders prior to dispatch.\n"
    "2. Quality Assurance: Verify product descriptions, sizes, and images for high discount or high item-count orders to prevent expectation mismatches.\n"
    "3. Non-Penalising Approach: Avoid outright cancellations or harsh penalties for customers with previous returns; instead, offer clearer sizing guides, proactive customer support, or verified order confirmations."
)