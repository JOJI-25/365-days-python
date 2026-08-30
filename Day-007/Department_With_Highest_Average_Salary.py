employees = [
    {"name": "John", "department": "IT", "salary": 50000},
    {"name": "Sara", "department": "HR", "salary": 45000},
    {"name": "Mike", "department": "IT", "salary": 70000},
    {"name": "Anna", "department": "HR", "salary": 55000},
    {"name": "David", "department": "Sales", "salary": 60000}
]

dept_data = {}

for emp in employees:
    dept = emp["department"]
    salary = emp["salary"]
    
    if dept not in dept_data:
        dept_data[dept] = {"total": 0, "count": 0}
        
    dept_data[dept]["total"] += salary
    dept_data[dept]["count"] += 1

highest_avg = 0
best_dept = None

for dept, data in dept_data.items():
    avg_salary = data["total"] / data["count"]
    
    if avg_salary > highest_avg:
        highest_avg = avg_salary
        best_dept = dept

print(best_dept) 