# Transaction dataset
transactions = [
    {"id": 101, "category": "Food", "amount": 450, "status": "Success"},
    {"id": 102, "category": "Travel", "amount": 1200, "status": "Success"},
    {"id": 103, "category": "Food", "amount": 780, "status": "Failed"},
    {"id": 104, "category": "Shopping", "amount": 2500, "status": "Success"},
    {"id": 105, "category": "Bills", "amount": 1800, "status": "Success"},
    {"id": 106, "category": "Travel", "amount": 650, "status": "Failed"},
    {"id": 107, "category": "Shopping", "amount": 900, "status": "Success"},
    {"id": 108, "category": "Food", "amount": 320, "status": "Success"},
    {"id": 109, "category": "Bills", "amount": 950, "status": "Failed"},
    {"id": 110, "category": "Travel", "amount": 2100, "status": "Success"}
]

# 1. Calculate the total value of successful transactions for each category
successful_totals = {}
category_counts = {}
category_success_counts = {}

for tx in transactions:
    cat = tx["category"]
    status = tx["status"]
    amount = tx["amount"]
    
    # Track overall and successful counts for success rate calculation
    category_counts[cat] = category_counts.get(cat, 0) + 1
    if status == "Success":
        category_success_counts[cat] = category_success_counts.get(cat, 0) + 1
        successful_totals[cat] = successful_totals.get(cat, 0) + amount

print("--- 1. Total Successful Value by Category ---")
for cat, total in successful_totals.items():
    print(f"- {cat}: {total}")
print()

# 2. Determine category with highest successful value and its percentage of overall total
overall_success_total = sum(successful_totals.values())
highest_category = max(successful_totals, key=successful_totals.get)
highest_value = successful_totals[highest_category]
highest_percentage = (highest_value / overall_success_total) * 100

print("--- 2. Highest Successful Category & Share ---")
print(f"Highest Category: {highest_category} ({highest_value})")
print(f"Percentage of Overall Successful Value: {highest_percentage:.2f}%")
print()

# 3. Calculate the success rate for each category
success_rates = {}
print("--- 3. Category Success Rates ---")
for cat, total_count in category_counts.items():
    success_count = category_success_counts.get(cat, 0)
    rate = (success_count / total_count) * 100
    success_rates[cat] = rate
    print(f"- {cat}: {rate:.2f}% ({success_count}/{total_count} successful)")
print()

# 4. Reusable function to classify successful transactions by amount
def classify_transaction_amount(amount):
    """Classifies a transaction amount into Low, Medium, or High."""
    if amount < 1000:
        return "Low"
    elif 1000 <= amount <= 2000:
        return "Medium"
    else:
        return "High"

print("--- 4. Transaction Amount Classification (Successful Only) ---")
for tx in transactions:
    if tx["status"] == "Success":
        classification = classify_transaction_amount(tx["amount"])
        print(f"ID {tx['id']} ({tx['category']}): Amount {tx['amount']} -> {classification}")
print()

# 5. Comparison and Business Implication
highest_success_rate_category = max(success_rates, key=success_rates.get)
matches_highest = (highest_category == highest_success_rate_category)

print("--- 5. Comparison & Business Implication ---")
print(f"Category with highest spending: {highest_category}")
print(f"Category with highest success rate: {highest_success_rate_category}")
print(f"Do they match? {'Yes' if matches_highest else 'No'}")
print()
print("Business Implication:")
print(
    "Since the highest spending category ('Shopping') also has the highest success rate (100%), "
    "it indicates strong reliability and user trust in high-value purchases. "
    "The digital wallet company can focus on expanding partnerships or offering rewards in "
    "this category, while investigating other categories with lower success rates (like Bills) "
    "to fix technical or payment gateway bottlenecks."
)