from collections import defaultdict

orders = [
    {"order_id": 101, "category": "Pizza", "quantity": 2, "price": 280},
    {"order_id": 102, "category": "Burger", "quantity": 3, "price": 180},
    {"order_id": 103, "category": "Pizza", "quantity": 1, "price": 320},
    {"order_id": 104, "category": "Drinks", "quantity": 4, "price": 90},
    {"order_id": 105, "category": "Burger", "quantity": 2, "price": 220},
    {"order_id": 106, "category": "Dessert", "quantity": 3, "price": 150},
    {"order_id": 107, "category": "Pizza", "quantity": 3, "price": 250},
    {"order_id": 108, "category": "Drinks", "quantity": 5, "price": 80},
    {"order_id": 109, "category": "Dessert", "quantity": 2, "price": 180},
    {"order_id": 110, "category": "Burger", "quantity": 4, "price": 190}
]

# Task 1: Calculate total revenue per order
for order in orders:
    order["revenue"] = order["quantity"] * order["price"]

print("--- Task 1: Revenue Per Order ---")
for order in orders:
    print(f"Order {order['order_id']} ({order['category']}): {order['revenue']}")


# Task 2 & 3: Aggregate revenue and calculate average per category
category_data = defaultdict(lambda: {"total_revenue": 0, "order_count": 0})

for order in orders:
    cat = order["category"]
    category_data[cat]["total_revenue"] += order["revenue"]
    category_data[cat]["order_count"] += 1

print("\n--- Task 2 & 3: Category Aggregation & Averages ---")
highest_revenue_category = None
max_revenue = -1

for cat, stats in category_data.items():
    stats["avg_revenue"] = stats["total_revenue"] / stats["order_count"]
    print(f"Category: {cat:<8} | Total Revenue: {stats['total_revenue']:<6} | Avg Revenue: {stats['avg_revenue']:.2f}")
    
    if stats["total_revenue"] > max_revenue:
        max_revenue = stats["total_revenue"]
        highest_revenue_category = cat

print(f"\nHighest Total Revenue Category: {highest_revenue_category} ({max_revenue})")


# Task 4: Reusable order size classifier function
def classify_order_size(revenue: float) -> str:
    """Classifies order size into Small, Medium, or Large based on revenue thresholds."""
    if revenue <= 400:
        return "Small"
    elif revenue <= 550:
        return "Medium"
    else:
        return "Large"


# Task 5: Determine category with largest proportion of 'Large' orders
large_counts = defaultdict(int)

for order in orders:
    order["size"] = classify_order_size(order["revenue"])
    if order["size"] == "Large":
        large_counts[order["category"]] += 1

print("\n--- Task 5: Proportion of Large Orders ---")
highest_prop_category = None
max_proportion = -1.0

for cat, stats in category_data.items():
    total_orders = stats["order_count"]
    large_orders = large_counts[cat]
    proportion = large_orders / total_orders
    print(f"Category: {cat:<8} | Large Orders: {large_orders}/{total_orders} ({proportion:.1%})")
    
    if proportion > max_proportion:
        max_proportion = proportion
        highest_prop_category = cat

print(f"\nCategory with Largest Proportion of Large Orders: {highest_prop_category} ({max_proportion:.1%})")