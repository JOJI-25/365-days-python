import pandas as pd

# 1. Load the dataset
data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "city": [
        "Kochi", "Kochi", "Alappuzha", "Kochi", "Kollam",
        "Alappuzha", "Kollam", "Kochi", "Kollam", "Alappuzha"
    ],
    "restaurant_type": [
        "Fast Food", "Cafe", "Fast Food", "Restaurant", "Cafe",
        "Restaurant", "Fast Food", "Cafe", "Restaurant", "Fast Food"
    ],
    "delivery_minutes": [32, 41, 28, 55, 37, 48, 31, 39, 52, 29],
    "order_value": [450, 320, 280, 750, 390, 620, 350, 410, 680, 300],
    "customer_rating": [4.5, 4.1, 4.7, 3.5, 4.2, 3.9, 4.6, 4.0, 3.6, 4.8]
}

orders = pd.DataFrame(data)

# 2. Create delivery_status column
def get_delivery_status(minutes):
    if minutes < 35:
        return "Fast"
    elif minutes <= 45:
        return "Normal"
    else:
        return "Delayed"

orders["delivery_status"] = orders["delivery_minutes"].apply(get_delivery_status)

# 3. Number of orders in each delivery-status category
status_counts = orders["delivery_status"].value_counts()

# 4. Average delivery time for each city
avg_delivery_by_city = orders.groupby("city")["delivery_minutes"].mean()

# 5. Average customer rating for each city
avg_rating_by_city = orders.groupby("city")["customer_rating"].mean()

# 6. City with the highest proportion of delayed orders
delayed_proportions = orders.groupby("city")["delivery_status"].apply(lambda x: (x == "Delayed").mean())
highest_delayed_city = delayed_proportions.idxmax()

# 7. Summary using groupby() by city and restaurant_type
summary_group = orders.groupby(["city", "restaurant_type"]).agg(
    order_count=("order_id", "count"),
    avg_delivery_time=("delivery_minutes", "mean"),
    avg_order_value=("order_value", "mean"),
    avg_customer_rating=("customer_rating", "mean")
).reset_index()

# 8. Identify city + restaurant type combination with the lowest average customer rating
lowest_rating_combination = summary_group.loc[summary_group["avg_customer_rating"].idxmin()]

# --- Display Results ---
print("--- Delivery Status Counts ---")
print(status_counts, "\n")

print("--- Average Delivery Time by City ---")
print(avg_delivery_by_city, "\n")

print("--- Average Customer Rating by City ---")
print(avg_rating_by_city, "\n")

print("--- Proportion of Delayed Orders by City ---")
print(delayed_proportions, "\n")
print(f"City with highest delayed proportion: {highest_delayed_city}\n")

print("--- Groupby Summary (City & Restaurant Type) ---")
print(summary_group, "\n")

print("--- Lowest Average Customer Rating Combination ---")
print(lowest_rating_combination)