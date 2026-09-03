numbers = list(map(int, input("Enter the numbers: ").split()))

sum_map = {0:-1}
current_sum = 0
max_len = 0

for i,num in enumerate(numbers):
    current_sum += num
    if current_sum in sum_map:
        sub_array_length = i - sum_map[current_sum]
        max_len = max(max_len, sub_array_length)
    else:
        sum_map[current_sum] = i

print("Length of longest subarray with sum zero:", max_len)