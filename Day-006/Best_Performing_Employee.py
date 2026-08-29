def best_performing_employee(sales_data):
    best_employee = -1
    max_sales = -1
    
    for entry in sales_data:
        name = entry["name"]
        sales = entry["sales"]
        
        if sales > max_sales:
            max_sales = sales
            best_employee = name
            
    return best_employee

sales = [
    {"name": "John", "sales": 45000},
    {"name": "Sara", "sales": 52000},
    {"name": "Mike", "sales": 48000},
    {"name": "Anna", "sales": 52000}
]

print(best_performing_employee(sales))  