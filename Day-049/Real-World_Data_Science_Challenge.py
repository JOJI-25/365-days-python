import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Given Data
data = {
    "trial_id": range(1, 25),
    "rainfall_mm": [
        420, 510, 380, 620, 450, 700,
        560, 330, 480, 650, 390, 590,
        740, 460, 520, 350, 680, 610,
        430, 570, 720, 400, 630, 490
    ],
    "temperature_c": [
        24, 26, 23, 27, 25, 29,
        26, 22, 25, 28, 24, 27,
        30, 25, 26, 23, 29, 28,
        24, 27, 30, 23, 28, 25
    ],
    "fertilizer_kg_ha": [
        40, 60, 35, 80, 50, 90,
        70, 30, 55, 85, 45, 75,
        95, 50, 65, 35, 90, 80,
        45, 70, 100, 40, 85, 60
    ],
    "soil_moisture_pct": [
        42, 51, 38, 60, 46, 68,
        55, 35, 48, 64, 40, 58,
        72, 45, 53, 36, 66, 62,
        43, 57, 70, 39, 63, 49
    ],
    "yield_tonnes_ha": [
        3.2, 4.1, 2.8, 5.0, 3.6, 5.4,
        4.5, 2.5, 3.8, 5.2, 3.0, 4.7,
        5.6, 3.5, 4.2, 2.7, 5.3, 4.9,
        3.3, 4.6, 5.7, 2.9, 5.1, 3.9
    ]
}

df = pd.DataFrame(data)

# --- Task 1: Exploratory Data Analysis & Visualizations ---
print("--- Task 1: Descriptive Statistics ---")
print(df.describe())
print()

# Save correlation heatmap and pairplot
plt.figure(figsize=(8, 6))
sns.heatmap(df.drop(columns=["trial_id"]).corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Agricultural Features")
plt.tight_layout()
plt.savefig("crop_correlation_heatmap.png")
plt.show()
print("Saved correlation heatmap as 'crop_correlation_heatmap.png'.\n")


# --- Task 2: Feature Engineering ---
# Engineering an interaction feature: 'water_nutrient_index' multiplying rainfall by fertilizer
df["water_nutrient_index"] = df["rainfall_mm"] * df["fertilizer_kg_ha"] / 1000.0

"""
Why this helps:
Crop growth depends heavily on the synergistic relationship between water availability and nutrients. 
Fertilizer requires adequate moisture to dissolve and be absorbed by plant roots; multiplying them 
captures this non-linear interaction effect better than independent features alone.
"""


# --- Task 3: Train Baseline and Nonlinear Models ---
X = df.drop(columns=["trial_id", "yield_tonnes_ha"])
y = df["yield_tonnes_ha"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Baseline model: Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_preds)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_preds))

# Nonlinear model: Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_preds)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))

print("--- Task 3: Model Evaluation ---")
print(f"Linear Regression -> MAE: {lr_mae:.4f}, RMSE: {lr_rmse:.4f}")
print(f"Random Forest     -> MAE: {rf_mae:.4f}, RMSE: {rf_rmse:.4f}\n")


# --- Task 4: Examine Predictions and Residuals ---
results_df = pd.DataFrame({
    "Actual": y_test,
    "LR_Preds": lr_preds,
    "RF_Preds": rf_preds,
    "LR_Residual": y_test - lr_preds,
    "RF_Residual": y_test - rf_preds
})

print("--- Task 4: Prediction & Residual Analysis ---")
print(results_df.to_string(index=False))
print("\nResidual examination helps check for systematic bias under extreme high/low yield conditions.\n")


# --- Task 5: Recommendation & Limitations ---
"""
--- Task 5: Recommendations & Limitations ---
1. Dataset Limitation: 
   With only 24 samples, models are highly prone to overfitting and lack generalizability across 
   different soil types, seed varieties, pest pressures, and geographic regions. Broad validation 
   across multi-year trials is necessary before field deployment.

2. Strategic Use: 
   Use the model only as a preliminary decision-support tool to explore scenarios, rather than 
   making rigid operational resource commitments. Combine model outputs with local agronomic expertise.
"""
print("--- Task 5: Recommendation ---")
print("Recommendation: Use the model cautiously for exploratory scenario planning, and collect multi-season, multi-region data before practical deployment.")