import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load the dataset
housing = pd.DataFrame({
    "area_sqft": [
        850, 1000, 1200, 1350, 1500,
        1650, 1800, 2000, 2200, 2500,
        900, 1100, 1400, 1750, 2100
    ],
    "bedrooms": [
        2, 2, 3, 3, 3,
        3, 4, 4, 4, 5,
        2, 3, 3, 4, 4
    ],
    "age_years": [
        15, 10, 8, 12, 6,
        5, 4, 3, 2, 1,
        18, 11, 7, 6, 3
    ],
    "distance_to_city_km": [
        12, 10, 8, 9, 7,
        6, 5, 4, 3, 2,
        14, 11, 8, 5, 3
    ],
    "parking": [
        0, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        0, 1, 1, 1, 1
    ],
    "price_lakh": [
        48, 55, 72, 78, 92,
        105, 125, 145, 168, 205,
        50, 64, 82, 132, 175
    ]
})

# 2. Inspect Correlations
print("Correlation with Price:")
print(housing.corr()['price_lakh'].sort_values(ascending=False))
print("-" * 40)

# 3. Feature Preparation
features = ["area_sqft", "bedrooms", "age_years", "distance_to_city_km", "parking"]
X = housing[features]
y = housing["price_lakh"]

# 4. Train/Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Model Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Evaluation Metrics:")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")
print("-" * 40)

# 7. Predict Price for a New House
new_house = pd.DataFrame([{
    "area_sqft": 1600,
    "bedrooms": 3,
    "age_years": 5,
    "distance_to_city_km": 6,
    "parking": 1
}])

predicted_price = model.predict(new_house)[0]
print(f"Predicted Price for New House: ₹{predicted_price:.2f} lakhs")