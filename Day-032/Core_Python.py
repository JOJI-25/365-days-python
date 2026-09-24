from collections import defaultdict

tickets = [
    ("C101", "Payment", 18),
    ("C102", "Login", 12),
    ("C101", "Delivery", 35),
    ("C103", "Payment", 22),
    ("C104", "Login", 8),
    ("C102", "Payment", 25),
    ("C103", "Delivery", 40),
    ("C101", "Login", 15),
    ("C104", "Payment", 30),
    ("C105", "Delivery", 28),
    ("C102", "Login", 10),
    ("C105", "Payment", 20),
]

# --- Reusable Function ---
def customer_support_summary(tickets):
    """Calculates ticket count and average resolution time per customer."""
    customer_data = defaultdict(lambda: {"total_time": 0, "count": 0})
    
    for customer_id, _, resolution_time in tickets:
        customer_data[customer_id]["total_time"] += resolution_time
        customer_data[customer_id]["count"] += 1
        
    summary = {}
    for customer_id, data in customer_data.items():
        summary[customer_id] = {
            "ticket_count": data["count"],
            "avg_resolution_time": data["total_time"] / data["count"]
        }
    return summary

# Execute the function
customer_summary = customer_support_summary(tickets)

# --- 1 & 2. Tickets & Average Resolution Time per Customer ---
print("--- Customer Summaries ---")
for cid, stats in customer_summary.items():
    print(f"Customer {cid}: {stats['ticket_count']} tickets, Avg Time: {stats['avg_resolution_time']:.1f} mins")

# --- 3. Number of Tickets for Each Issue Category ---
category_counts = defaultdict(int)
for _, category, _ in tickets:
    category_counts[category] += 1

print("\n--- Tickets by Issue Category ---")
for cat, count in category_counts.items():
    print(f"{cat}: {count} tickets")

# --- 4. Issue Category with the Highest Number of Tickets ---
highest_category = max(category_counts, key=category_counts.get)
print(f"\nCategory with highest tickets: {highest_category} ({category_counts[highest_category]} tickets)")

# --- 5. Customer with the Highest Average Resolution Time ---
highest_avg_customer = max(customer_summary, key=lambda k: customer_summary[k]["avg_resolution_time"])
print(f"Customer with highest avg resolution time: {highest_avg_customer} ({customer_summary[highest_avg_customer]['avg_resolution_time']:.1f} mins)")

# --- 6. Customers with Average Resolution Time > 25 Minutes ---
slow_customers = [cid for cid, stats in customer_summary.items() if stats["avg_resolution_time"] > 25]
print(f"Customers with avg resolution time > 25 mins: {slow_customers}")

# --- 7. Ranking of Customers by Ticket Count (Descending) ---
ranked_customers = sorted(customer_summary.items(), key=lambda x: x[1]["ticket_count"], reverse=True)
print("\n--- Customer Ranking by Ticket Count ---")
for rank, (cid, stats) in enumerate(ranked_customers, 1):
    print(f"{rank}. Customer {cid} - {stats['ticket_count']} tickets")