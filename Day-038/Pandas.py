import pandas as pd

data = {
    "booking_id": range(201, 213),
    "city": [
        "Kochi", "Kochi", "Trivandrum", "Kozhikode",
        "Kochi", "Trivandrum", "Kozhikode", "Kochi",
        "Trivandrum", "Kozhikode", "Kochi", "Trivandrum"
    ],
    "genre": [
        "Action", "Drama", "Comedy", "Action",
        "Comedy", "Drama", "Drama", "Action",
        "Comedy", "Action", "Drama", "Comedy"
    ],
    "customer_type": [
        "Regular", "Student", "Regular", "Student",
        "Family", "Regular", "Student", "Family",
        "Student", "Regular", "Family", "Regular"
    ],
    "tickets": [2, 1, 3, 2, 4, 2, 1, 5, 2, 3, 4, 2],
    "ticket_price": [220, 150, 200, 150, 180, 220, 150, 180, 150, 200, 180, 220]
}
df = pd.DataFrame(data)

# Task 1: Revenue column & total revenue
df["revenue"] = df["tickets"] * df["ticket_price"]
total_revenue = df["revenue"].sum()
print("Total Revenue:", total_revenue)

# Task 2: City comparison (total revenue and avg tickets per booking)
city_summary = df.groupby("city").agg(
    total_revenue=("revenue", "sum"),
    avg_tickets=("tickets", "mean")
)
print("\nCity Summary:\n", city_summary)

# Task 3: Genre highest revenue and percentage
genre_summary = df.groupby("genre")["revenue"].sum()
highest_genre = genre_summary.idxmax()
highest_genre_rev = genre_summary.max()
genre_percentage = (highest_genre_rev / total_revenue) * 100
print(f"\nGenre Summary:\n{genre_summary}")
print(f"Highest Genre: {highest_genre} with revenue {highest_genre_rev} ({genre_percentage:.2f}%)")

# Task 4: Pivot table city and customer_type for revenue
pivot_table = pd.pivot_table(df, values="revenue", index="city", columns="customer_type", aggfunc="sum", fill_value=0)
print("\nPivot Table (Revenue by City & Customer Type):\n", pivot_table)
# Find strongest combination
stacked = pivot_table.stack()
strongest_combo = stacked.idxmax()
print(f"Strongest combination: City={strongest_combo[0]}, Customer Type={strongest_combo[1]} with revenue {stacked.max()}")

# Task 5: High revenue, relatively few tickets
print("\nDetails of all bookings:")
print(df[["booking_id", "city", "genre", "customer_type", "tickets", "ticket_price", "revenue"]])