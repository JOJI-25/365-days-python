import pandas as pd
import numpy as np

data = {    
    "user_id": range(1001, 1013),    
    "monthly_fee": [499, 699, 499, 999, 699, 499, 999, 699, 499, 999, 699, 499],    
    "sessions_30d": [18, 5, 22, 3, 14, 7, 2, 16, 25, 4, 9, 20],    
    "avg_session_min": [42, 25, 48, 18, 38, 29, 15, 41, 52, 20, 31, 45],    
    "support_tickets": [0, 3, 1, 4, 1, 2, 5, 0, 0, 3, 2, 1],    
    "days_since_login": [2, 18, 1, 25, 5, 14, 30, 3, 1, 21, 11, 4],    
    "cancelled": [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# 1. Compare cancelled vs retained groups (mean/median)
summary = df.groupby('cancelled')[['sessions_30d', 'avg_session_min', 'support_tickets', 'days_since_login']].agg(['mean', 'median'])
print("--- Summary Statistics ---")
print(summary)

# 2. Correlation with cancelled
corrs = df.corr()['cancelled'].sort_values()
print("\n--- Correlations with Cancelled ---")
print(corrs)

# 3. Feature engineering
# Feature 1: Total active time per month (sessions_30d * avg_session_min)
df['total_active_minutes_30d'] = df['sessions_30d'] * df['avg_session_min']
# Feature 2: Support ticket intensity relative to sessions (support_tickets / (sessions_30d + 1))
df['ticket_intensity'] = df['support_tickets'] / (df['sessions_30d'] + 1)

print("\n--- Engineered Features Sample ---")
print(df[['user_id', 'cancelled', 'total_active_minutes_30d', 'ticket_intensity']])

# 4. Simple baseline model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

X = df[['sessions_30d', 'avg_session_min', 'support_tickets', 'days_since_login']]
y = df['cancelled']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\n--- Model Evaluation ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))