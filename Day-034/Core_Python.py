def analyse_transactions(transactions):
    # Dictionaries to track customer metrics
    totals = {}
    counts = {}
    max_amounts = {}
    
    large_transactions = []
    
    # Process each transaction
    for transaction_id, customer_id, amount, transaction_type in transactions:
        # 1. Total transaction amount per customer
        totals[customer_id] = totals.get(customer_id, 0) + amount
        
        # 2. Number of transactions per customer
        counts[customer_id] = counts.get(customer_id, 0) + 1
        
        # 3. Highest transaction per customer
        if customer_id not in max_amounts or amount > max_amounts[customer_id]:
            max_amounts[customer_id] = amount
            
        # 4. Identify transactions greater than ₹10,000
        if amount > 10000:
            large_transactions.append({
                "transaction_id": transaction_id,
                "customer_id": customer_id,
                "amount": amount,
                "transaction_type": transaction_type
            })
            
    customer_summary = []
    
    for customer_id in totals:
        total_val = totals[customer_id]
        max_val = max_amounts[customer_id]
        
        # 6. Customer risk classification
        if max_val <= 10000:
            risk = "Low"
        elif total_val > 30000 and max_val > 10000:
            risk = "High"
        else:
            risk = "Medium"
            
        # 5. Identify customers whose total > ₹20,000 AND at least one > ₹10,000
        meets_criteria = (total_val > 20000) and (max_val > 10000)
        
        customer_summary.append({
            "customer_id": customer_id,
            "total_amount": total_val,
            "transaction_count": counts[customer_id],
            "highest_transaction": max_val,
            "risk_level": risk,
            "flagged_for_review": meets_criteria
        })
        
    # 7. Sort customers by total transaction value in descending order
    customer_summary.sort(key=lambda x: x["total_amount"], reverse=True)
    
    return {
        "large_transactions": large_transactions,
        "customer_summary": customer_summary,
        "totals": totals,
        "counts": counts,
        "max_amounts": max_amounts
    }


# --- Execution Example ---
transactions = [
    ("T001", "C101", 1200, "UPI"),
    ("T002", "C102", 4500, "CARD"),
    ("T003", "C101", 800, "UPI"),
    ("T004", "C103", 15000, "CARD"),
    ("T005", "C102", 700, "UPI"),
    ("T006", "C104", 25000, "BANK"),
    ("T007", "C103", 900, "UPI"),
    ("T008", "C101", 18000, "CARD"),
    ("T009", "C104", 1200, "UPI"),
    ("T010", "C102", 9500, "CARD"),
    ("T011", "C105", 600, "UPI"),
    ("T012", "C105", 22000, "BANK")
]

results = analyse_transactions(transactions)
totals = results["totals"]
counts = results["counts"]
max_amounts = results["max_amounts"]

print("4. Transactions > ₹10,000:")
for t in results["large_transactions"]:
    print(f"   {t}")

print("\n5. Customer Summary:")
for c in results["customer_summary"]:
    print(c)

print("\n6. High-Risk Customers:")
high_risk = [c for c in results["customer_summary"] if c["risk_level"] == "High"]
for c in high_risk:
    print(f"   {c['customer_id']} (Total: {c['total_amount']}, Highest: {c['highest_transaction']})")

print("\n7. Flagged Customers:")
flagged = [c for c in results["customer_summary"] if c["flagged_for_review"]]
for c in flagged:
    print(f"   {c['customer_id']} (Total: {c['total_amount']}, Highest: {c['highest_transaction']})")

print("\n1. Total Transaction Amount per Customer:")
for customer_id, total in totals.items():
    print(f"   {customer_id}: ₹{total:,.2f}")

print("\n2. Number of Transactions per Customer:")
for customer_id, count in counts.items():
    print(f"   {customer_id}: {count} transaction(s)")

print("\n3. Highest Transaction Amount per Customer:")
for customer_id, max_amount in max_amounts.items():
    print(f"   {customer_id}: ₹{max_amount:,.2f}")