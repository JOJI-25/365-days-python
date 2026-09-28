# Restaurant dataset
restaurants = [
    {"name": "Spice Hub", "ratings": [4.5, 4.2, 4.8, 4.1, 4.6]},
    {"name": "Burger Point", "ratings": [3.8, 4.0, 3.5, 4.1, 3.9]},
    {"name": "Curry House", "ratings": [4.7, 4.9, 4.8, 4.6, 4.9]},
    {"name": "Pizza Corner", "ratings": [4.0, 3.9, 4.2, 4.1, 3.8]},
    {"name": "Dosa Palace", "ratings": [4.3, 4.5, 4.1, 4.4, 4.6]},
]


# Task 1 & 3: Calculate average and classify each restaurant
def process_restaurants(data):
  processed = []
  for r in data:
    avg = sum(r["ratings"]) / len(r["ratings"])

    # Classification logic
    if avg >= 4.5:
      category = "Excellent"
    elif avg >= 4.0:
      category = "Good"
    else:
      category = "Needs Improvement"

    processed.append(
        {"name": r["name"], "average_rating": round(avg, 2), "category": category}
    )
  return processed


# Task 4: Reusable function to return restaurants sorted by average rating descending
def sort_restaurants_by_rating(data):
  processed = process_restaurants(data)
  return sorted(processed, key=lambda x: x["average_rating"], reverse=True)


# Task 5: Identify restaurants whose ratings have a range greater than 0.8
def analyze_rating_ranges(data):
  high_range_restaurants = []
  for r in data:
    rating_range = max(r["ratings"]) - min(r["ratings"])
    if rating_range > 0.8:
      high_range_restaurants.append(
          {"name": r["name"], "range": round(rating_range, 2)}
      )
  return high_range_restaurants


# --- Execution and Output ---
if __name__ == "__main__":
  # 1. Averages and Classifications
  print("--- 1. Averages and Classifications ---")
  processed_data = process_restaurants(restaurants)
  for item in processed_data:
    print(
        f"Restaurant: {item['name']} | Average: {item['average_rating']} |"
        f" Status: {item['category']}"
    )

  # 2. Highest and Lowest Average Rating
  sorted_list = sort_restaurants_by_rating(restaurants)
  print("\n--- 2. Highest and Lowest ---")
  print(
      f"Highest: {sorted_list[0]['name']} ({sorted_list[0]['average_rating']})"
  )
  print(
      f"Lowest: {sorted_list[-1]['name']} ({sorted_list[-1]['average_rating']})"
  )

  # 3. Sorted List (Descending)
  print("\n--- 3. Sorted Restaurants (Descending) ---")
  for item in sorted_list:
    print(f"{item['name']}: {item['average_rating']}")

  # 4. Range Analysis (> 0.8)
  print("\n--- 4. Rating Range Consistency Analysis ---")
  wide_ranges = analyze_rating_ranges(restaurants)
  if wide_ranges:
    print(f"Restaurants with range > 0.8: {wide_ranges}")
  else:
    print(
        "None of the restaurants have a rating range greater than 0.8. A"
        " smaller range indicates that the service and customer experiences"
        " remain consistently steady over time without sharp fluctuations."
    )