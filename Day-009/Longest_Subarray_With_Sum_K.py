numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
k = int(input("Enter the value of k: "))

prefix_sum = 0
max_len = 0
seen_sums = {}

for i in range(len(numbers)):
    prefix_sum += numbers[i]
    
    if prefix_sum == k:
        max_len = i + 1
    
    if (prefix_sum - k) in seen_sums:
        current_len = i - seen_sums[prefix_sum - k]
        if current_len > max_len:
            max_len = current_len
            
    if prefix_sum not in seen_sums:
        seen_sums[prefix_sum] = i

print("Length of longest subarray with sum K:", max_len)