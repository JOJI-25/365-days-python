a = list(map(int, input("Enter the numbers : ").split()))

a.sort()
current_count = 0
maximum_count = 0
previous_num = None
 
most_frequent_num = a[0]

for num in a:
    if num == previous_num:
       current_count += 1
    else:
        current_count = 1
        previous_num = num

    if current_count > maximum_count:
        maximum_count = current_count
        most_frequent_num = num

print(most_frequent_num)
