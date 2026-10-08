import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Dataset initialization
data = {
    "listing_id": range(4001, 4016),
    "nightly_price": [
        1800, 3200, 2400, 4500, 2100,
        3800, 1600, 5200, 2700, 3500,
        1900, 4100, 5800, 2300, 3000
    ],
    "rating": [
        4.7, 4.3, 4.8, 4.1, 4.6,
        4.4, 4.9, 4.0, 4.5, 4.2,
        4.8, 4.3, 3.9, 4.6, 4.4
    ],
    "reviews": [
        125, 82, 210, 45, 160,
        95, 280, 38, 145, 70,
        190, 110, 31, 175, 88
    ],
    "photos": [
        18, 9, 22, 7, 15,
        12, 28, 6, 17, 10,
        21, 14, 5, 20, 11
    ],
    "response_time_hours": [
        2, 8, 1, 14, 3,
        6, 1, 18, 4, 10,
        2, 7, 20, 3, 9
    ],
    "booking_requests": [
        32, 18, 41, 9, 29,
        21, 52, 6, 35, 15,
        38, 24, 5, 34, 20
    ],
    "high_demand_next_month": [
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 0, 1, 0
    ]
}

df = pd.DataFrame(data)

# 1. Compare High-Demand vs. Normal-Demand Listings
print("--- 1. Group Comparison (High Demand vs. Normal Demand) ---")
group_summary = df.groupby('high_demand_next_month').mean()
print(group_summary[['nightly_price', 'rating', 'reviews', 'photos', 'response_time_hours', 'booking_requests']])
print()

# 2. Feature Engineering
# Feature 1: value_score = Rating per unit of nightly price (scaled for readability)
df['value_score'] = (df['rating'] / df['nightly_price']) * 10000

# Feature 2: engagement_score = Interaction volume combining review history and visual appeal (reviews * photos)
df['engagement_score'] = df['reviews'] * df['photos']

print("--- 2. Engineered Features Sample ---")
print(df[['listing_id', 'value_score', 'engagement_score']].head())
print()

# 3. Build a Baseline Classification Model
features = ['nightly_price', 'rating', 'reviews', 'photos', 'response_time_hours', 'booking_requests', 'value_score', 'engagement_score']
X = df[features]
y = df['high_demand_next_month']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("--- 3. Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))

# 4. Analyze Feature Coefficients/Importance
coefficients = pd.Series(model.coef_[0], index=features).sort_values(ascending=False)
print("--- 4. Feature Coefficients (Logistic Regression) ---")
print(coefficients)