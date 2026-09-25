import pandas as pd

# ----------------- 1. Setup Datasets -----------------
rides = pd.DataFrame(
    {
        "ride_id": [
            "R01",
            "R02",
            "R03",
            "R04",
            "R05",
            "R06",
            "R07",
            "R08",
            "R09",
            "R10",
            "R11",
            "R12",
        ],
        "driver_id": [
            "D01",
            "D02",
            "D01",
            "D03",
            "D02",
            "D04",
            "D03",
            "D01",
            "D04",
            "D02",
            "D03",
            "D04",
        ],
        "city": [
            "Kochi",
            "Kochi",
            "Kochi",
            "Bengaluru",
            "Bengaluru",
            "Bengaluru",
            "Kochi",
            "Bengaluru",
            "Kochi",
            "Bengaluru",
            "Kochi",
            "Bengaluru",
        ],
        "distance_km": [
            5.2,
            8.1,
            3.4,
            12.5,
            7.3,
            10.2,
            4.8,
            15.1,
            6.2,
            9.4,
            3.7,
            11.6,
        ],
        "fare": [210, 320, 160, 520, 310, 430, 190, 610, 250, 390, 175, 470],
        "rating": [
            4.7,
            4.2,
            4.8,
            4.1,
            4.4,
            4.6,
            4.5,
            4.0,
            4.7,
            4.3,
            4.8,
            4.5,
        ],
    }
)

drivers = pd.DataFrame(
    {
        "driver_id": ["D01", "D02", "D03", "D04"],
        "experience_years": [3, 5, 2, 7],
        "vehicle_type": ["Sedan", "SUV", "Sedan", "SUV"],
    }
)

# ----------------- 2. Analysis -----------------

# Task 1: Merge ride and driver datasets
df = pd.merge(rides, drivers, on="driver_id", how="left")

# Tasks 2 - 6: Driver-level metrics
driver_summary = (
    df.groupby("driver_id")
    .agg(
        total_revenue=("fare", "sum"),
        total_distance=("distance_km", "sum"),
        avg_rating=("rating", "mean"),
        total_rides=("ride_id", "count"),
        experience_years=("experience_years", "first"),
        vehicle_type=("vehicle_type", "first"),
    )
    .reset_index()
)

# Average fare per kilometre
driver_summary["fare_per_km"] = (
    driver_summary["total_revenue"] / driver_summary["total_distance"]
).round(2)
driver_summary["avg_revenue_per_ride"] = (
    driver_summary["total_revenue"] / driver_summary["total_rides"]
).round(2)

# Rank drivers based on total revenue
driver_summary["revenue_rank"] = driver_summary["total_revenue"].rank(
    ascending=False, method="min"
)
driver_summary = driver_summary.sort_values(by="total_revenue", ascending=False)

# Task 8: Vehicle Type comparison
vehicle_comparison = (
    df.groupby("vehicle_type")
    .agg(
        avg_fare=("fare", "mean"),
        avg_distance=("distance_km", "mean"),
        avg_rating=("rating", "mean"),
    )
    .round(2)
)

# Task 9: City-level statistics
city_summary = (
    df.groupby("city")
    .agg(
        total_rides=("ride_id", "count"),
        total_revenue=("fare", "sum"),
        avg_fare=("fare", "mean"),
        avg_rating=("rating", "mean"),
    )
    .round(2)
)

# ----------------- 3. Display Results -----------------
print("--- DRIVER PERFORMANCE SUMMARY ---")
print(
    driver_summary[
        [
            "driver_id",
            "experience_years",
            "total_rides",
            "total_revenue",
            "total_distance",
            "fare_per_km",
            "avg_rating",
            "avg_revenue_per_ride",
            "revenue_rank",
        ]
    ].to_string(index=False)
)

print("\n--- VEHICLE TYPE COMPARISON ---")
print(vehicle_comparison)

print("\n--- CITY-LEVEL METRICS ---")
print(city_summary)