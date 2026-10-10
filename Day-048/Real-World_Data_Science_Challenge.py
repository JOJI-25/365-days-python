import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Given Data
customers = pd.DataFrame({
    "customer_id": range(2001, 2017),
    "annual_spend": [
        4200, 18500, 7200, 32000,
        5600, 27500, 9800, 41000,
        3800, 22500, 11500, 35000,
        6800, 29500, 8500, 46000
    ],
    "visits_per_month": [
        2, 8, 3, 12,
        2, 10, 4, 14,
        1, 9, 5, 11,
        3, 12, 4, 15
    ],
    "avg_basket_value": [
        350, 780, 420, 950,
        390, 850, 510, 1100,
        320, 820, 560, 980,
        430, 900, 480, 1200
    ],
    "days_since_last_purchase": [
        45, 8, 32, 3,
        60, 5, 25, 2,
        75, 7, 18, 4,
        38, 6, 21, 1
    ]
})

# -------------------------------------------------------------
# Task 1: Descriptive Statistics & Feature Scale Explanation
# -------------------------------------------------------------
print("--- Task 1: Descriptive Statistics ---")
print(customers.describe())
print()
print("Explanation of Feature Scales:")
print("- Annual spend ranges in the tens of thousands, while visits per month are single digits.")
print("- Without scaling, distance-based algorithms (like KMeans) would disproportionately weight features with larger numeric ranges (annual spend) over smaller ones (visits per month).\n")

# -------------------------------------------------------------
# Task 2: Feature Engineering
# -------------------------------------------------------------
# Engineer 'spend_per_visit_est' to capture shopping efficiency/basket density relative to frequency
customers['spend_per_visit_est'] = customers['annual_spend'] / (customers['visits_per_month'] * 12)

print("--- Task 2: Engineered Feature Sample ---")
print(customers[['customer_id', 'annual_spend', 'visits_per_month', 'spend_per_visit_est']].head(3))
print()

# -------------------------------------------------------------
# Task 3 & 4: Standardization, KMeans, and Silhouette Scores
# -------------------------------------------------------------
features = ['annual_spend', 'visits_per_month', 'avg_basket_value', 'days_since_last_purchase', 'spend_per_visit_est']
X = customers[features]

# Standardize features (mean=0, variance=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("--- Task 4: Evaluating Candidate K using Silhouette Scores ---")
best_k = 2
best_score = -1

for k in range(2, 6):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    print(f"K = {k}: Silhouette Score = {score:.4f}")
    if score > best_score:
        best_score = score
        best_k = k

print(f"\nOptimal K chosen based on highest silhouette score: {best_k}\n")

# Fit final model with optimal K
final_kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
customers['cluster'] = final_kmeans.fit_predict(X_scaled)

# Cluster Profiles Summary
cluster_summary = customers.groupby('cluster')[features].mean().reset_index()
print("--- Cluster Profiles (Averages per Cluster) ---")
print(cluster_summary.to_string(index=False))
print()

# -------------------------------------------------------------
# Task 5: Strategic Recommendations Summary
# -------------------------------------------------------------
print("--- Task 5: Strategic Recommendations ---")
print("1. High-Value / Frequent Segment: Offer exclusive loyalty perks, early access to sales, and premium product recommendations to retain them.")
print("2. Low-Engagement / Inactive Segment: Send targeted re-engagement campaigns, win-back discounts, or reminders based on their days since last purchase.")
print("3. Caveat: Clusters represent behavioral groupings, not permanent customer types; customers can transition between segments based on recent shopping habits.")