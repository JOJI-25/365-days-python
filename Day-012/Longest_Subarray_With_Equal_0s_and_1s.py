numbers = list(map(int, input("Enter the numbers (0s and 1s): ").split()))

sum_index = {0: -1}
prefix_sum = 0
max_len = 0

for i, num in enumerate(numbers):
    prefix_sum += 1 if num == 1 else -1
    
    if prefix_sum in sum_index:
        length = i - sum_index[prefix_sum]
        if length > max_len:
            max_len = length
    else:
        sum_index[prefix_sum] = i

print("Length of longest subarray with equal 0s and 1s:", max_len)