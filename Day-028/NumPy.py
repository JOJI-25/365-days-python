import numpy as np

sales = np.array([
    [120, 135, 150, 142, 160, 175, 190],
    [90,  105, 98,  115, 120, 130, 145],
    [200, 220, 210, 230, 250, 270, 290],
    [75,  82,  95,  88,  100, 110, 120],
    [150, 160, 155, 170, 180, 195, 205]
])

# calculate the total weekly sales for each stores

total_weekly_sales = sales.sum(axis=1)
print("Total weekly sales for each stores: ",total_weekly_sales)

# Calculate the average daily sales across all stores.
average_sales = sales.mean(axis=1)
print("Average daily sales across all stores: ",average_sales)

# Identify the store with the highest weekly sales.
highest_store_index = np.argmax(total_weekly_sales)
highest_store_sales = total_weekly_sales[highest_store_index]
print("Store with the highest weekly sales:", highest_store_index)
print("Highest weekly sales:", highest_store_sales)

# Find the day with the highest combined sales across all stores.

daily_combined_sales = sales.sum(axis=0)
best_day = np.argmax(daily_combined_sales)
best_day_sales = daily_combined_sales[best_day]

days_of_week =[
    "Monday",
    "Tuesday",
    "Wednesdsy",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print(f"Best day with highest combined sales: {days_of_week[best_day]}")
print(f"Highest combined sales: {best_day_sales}")

# Calculate the percentage contribution of each store to the overall weekly sales.
total_overall_sales = np.sum(total_weekly_sales)
store_percentage = (total_weekly_sales/total_overall_sales)*100
print("Percentage contribution of each store: ",store_percentage)

# Identify every individual daily sales value that is above the overall daily-sales mean.

overall_mean = np.mean(sales)
above_mean_values = sales[sales>overall_mean]
print("Above mean values: ",above_mean_values)