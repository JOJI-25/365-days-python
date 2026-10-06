import matplotlib.pyplot as plt
import pandas as pd

data = {
    "booking_id": range(2001, 2013),
    "destination": [
        "Goa",
        "Kerala",
        "Goa",
        "Rajasthan",
        "Kerala",
        "Goa",
        "Rajasthan",
        "Kerala",
        "Goa",
        "Rajasthan",
        "Kerala",
        "Goa",
    ],
    "room_nights": [3, 5, 2, 6, 4, 7, 3, 5, 2, 8, 4, 6],
    "room_rate": [
        4200,
        3800,
        5200,
        3500,
        4500,
        4800,
        3900,
        4100,
        5600,
        3600,
        4700,
        5000,
    ],
    "guests": [2, 3, 2, 4, 2, 5, 2, 3, 2, 4, 3, 4],
    "discount_pct": [5, 10, 0, 15, 8, 12, 5, 10, 0, 18, 7, 10],
    "rating": [4.5, 4.2, 4.7, 4.0, 4.6, 4.3, 4.1, 4.4, 4.8, 3.9, 4.5, 4.6],
}
df = pd.DataFrame(data)

df["gross_value"] = df["room_nights"] * df["room_rate"]
df["net_value"] = df["gross_value"] * (1 - df["discount_pct"] / 100.0)

dest_summary = (
    df.groupby("destination")
    .agg(
        total_net_revenue=("net_value", "sum"),
        avg_booking_value=("net_value", "mean"),
        avg_guests=("guests", "mean"),
        avg_rating=("rating", "mean"),
    )
    .reset_index()
)

print("=== 2. Destination Comparison ===")
print(dest_summary.to_string(index=False))
print("\n")

df["revenue_per_guest_night"] = df["net_value"] / (
    df["room_nights"] * df["guests"]
)
highest_vpgn_idx = df["revenue_per_guest_night"].idxmax()
best_booking = df.loc[highest_vpgn_idx]

print("=== 3. Revenue per Guest Night ===")
print(
    f"Highest Value Booking ID: {best_booking['booking_id']} ({best_booking['destination']})"
)
print(f"Revenue per Guest-Night: ₹{best_booking['revenue_per_guest_night']:.2f}")
print("\n")

correlation = df["rating"].corr(df["net_value"])
print("=== 4. Rating vs. Net Booking Value Correlation ===")
print(f"Correlation Coefficient: {correlation:.4f}\n")

plt.figure(figsize=(8, 5))
plt.scatter(
    df["rating"],
    df["net_value"],
    color="royalblue",
    edgecolor="black",
    s=80,
)
plt.title("Customer Rating vs. Net Booking Value", fontsize=12, fontweight="bold")
plt.xlabel("Customer Rating", fontsize=10)
plt.ylabel("Net Booking Value (₹)", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

print("=== 5. Destination Recommendation Summary ===")
print(
    "Goa stands out as the most attractive destination from a revenue"
    " perspective."
)
print(
    "Justification: Goa leads in total net revenue (₹90,138.00) and average"
    " booking value (₹18,027.60),"
)
print(
    "while simultaneously maintaining the highest average customer rating"
    " (4.58/5.0), proving strong"
)
print("monetization combined with superior customer satisfaction.")