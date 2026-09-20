transactions = [
    ("C101", 1250),
    ("C102", 450),
    ("C101", 800),
    ("C103", 2100),
    ("C102", 750),
    ("C104", 300),
    ("C103", 900),
    ("C101", 1500),
    ("C104", 650),
]

# Calculates the total spending for each customer.

customer_total = {}

for customer_id, amount in transactions:
    if customer_id in customer_total:
        customer_total[customer_id] += amount
    else:
        customer_total[customer_id] = amount

print(customer_total)

# 2. Find the highest-spending customer

highest_customer = max(customer_total,key=customer_total.get)
highest_amount = customer_total[highest_customer]

print("Highest Spending Customer:",highest_customer)
print("Highest Spending Amount:", highest_amount)

# 3. Find the average transaction value

total_revenue = sum(amount for _,amount in transactions)
total_transaction = len(transactions)
average_transaction = total_revenue // total_transaction
print("Average transaction value:",average_transaction)


# 4. Create a list containing only customers whose total spending is greater than 2,000

high_spender = [(customer,total) for customer, total in customer_total.items() if total > 2000]
print("High spender:",high_spender)


# 5. Sort the customers from highest total spending to lowest

sorted_customers = sorted(customer_total.items(), key=lambda item:item[1], reverse=True )
print("Sorted customers:",sorted_customers)