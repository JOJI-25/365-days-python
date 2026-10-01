import pandas as pd

data = {
    "trip_id": range(301, 313),
    "vehicle_type": [
        "Mini", "Sedan", "SUV", "Mini",
        "Sedan", "SUV", "Mini", "Sedan",
        "SUV", "Mini", "Sedan", "SUV"
    ],
    "city": [
        "Kochi", "Kochi", "Kochi", "Trivandrum",
        "Trivandrum", "Trivandrum", "Kozhikode", "Kozhikode",
        "Kozhikode", "Kochi", "Trivandrum", "Kozhikode"
    ],
    "distance_km": [8, 14, 22, 6, 18, 25, 9, 15, 21, 11, 20, 24],
    "fare": [180, 320, 520, 150, 390, 610, 210, 340, 500, 240, 430, 570],
    "fuel_cost": [55, 85, 145, 42, 110, 170, 60, 95, 140, 68, 125, 160]
}
df = pd.DataFrame(data)

# Task 1: Profit and average profit by vehicle type
df["profit"] = df["fare"] - df["fuel_cost"]
avg_profit_vehicle = df.groupby("vehicle_type")["profit"].mean()
print("1. Avg Profit by Vehicle Type:\n", avg_profit_vehicle)

# Task 2: Profit margin and most profitable trip by margin
df["profit_margin"] = (df["profit"] / df["fare"]) * 100
most_profitable_trip = df.loc[df["profit_margin"].idxmax()]
print("\n2. Most Profitable Trip by Margin:\n", most_profitable_trip)

# Task 3: Compare three cities using total fare, total profit, and average profit per trip
city_summary = df.groupby("city").agg(
    total_fare=("fare", "sum"),
    total_profit=("profit", "sum"),
    avg_profit_per_trip=("profit", "mean")
)
print("\n3. City Summary:\n", city_summary)

# Task 4: Grouped summary showing average distance, fare, fuel cost, and profit for each vehicle type
vehicle_summary = df.groupby("vehicle_type").agg(
    avg_distance=("distance_km", "mean"),
    avg_fare=("fare", "mean"),
    avg_fuel_cost=("fuel_cost", "mean"),
    avg_profit=("profit", "mean")
)
print("\n4. Vehicle Type Summary:\n", vehicle_summary)