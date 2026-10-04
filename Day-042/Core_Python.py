sales = {
    "Store_A": [120, 135, 128, 142, 138, 150, 145],
    "Store_B": [95, 160, 102, 155, 110, 170, 108],
    "Store_C": [180, 175, 190, 185, 178, 192, 188],
    "Store_D": [130, 125, 140, 118, 135, 122, 145]
}

totals = {store: sum(daily_sales) for store, daily_sales in sales.items()}
highest_selling_store = max(totals, key=totals.get)

print("--- 1. Total Weekly Sales ---")
for store, total in totals.items():
    print(f"{store}: {total} items")
print(f"Highest-Selling Store: {highest_selling_store} ({totals[highest_selling_store]} items)\n")


averages = {store: sum(daily_sales) / len(daily_sales) for store, daily_sales in sales.items()}
ranked_stores = sorted(averages.items(), key=lambda x: x[1], reverse=True)

print("--- 2. Average Daily Sales Ranking ---")
for rank, (store, avg) in enumerate(ranked_stores, 1):
    print(f"{rank}. {store}: {avg:.2f} items/day")
print()

ranges = {store: max(daily_sales) - min(daily_sales) for store, daily_sales in sales.items()}
most_consistent_store = min(ranges, key=ranges.get)

print("--- 3. Sales Range (Max - Min) ---")
for store, rng in ranges.items():
    print(f"{store}: Range of {rng} (Max: {max(sales[store])}, Min: {min(sales[store])})")
print(f"Most Consistent Store: {most_consistent_store} (Lowest range of {ranges[most_consistent_store]})\n")


def classify_store(sales_range):
    if sales_range <= 25:
        return "Consistent"
    elif sales_range <= 50:
        return "Moderate"
    else:
        return "Unstable"

print("--- 4. Store Classifications ---")
for store, rng in ranges.items():
    status = classify_store(rng)
    print(f"{store}: {status} (Range: {rng})")
print()


print("--- 5. Conclusion & Business Implication ---")
is_same = (highest_selling_store == most_consistent_store)
print(f"Is the highest-selling store also the most consistent? {is_same}")
if is_same:
    print(f"Implication: {highest_selling_store} represents the ideal high-performance model. "
          "It delivers strong volume with predictable daily demand, making inventory management, "
          "staffing, and supply chain planning highly reliable and efficient.")
else:
    print("Implication: High volume does not guarantee stability.")