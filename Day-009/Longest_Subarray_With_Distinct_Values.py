subarray = list(map(int, input("Enter the numbers : ").split()))

seen = {}
left = 0
long_len = 0
longest_sub = []

for right in range(len(subarray)):
    current = subarray[right]
    
    if current in seen and seen[current] >= left:
        left = seen[current] + 1
        
    seen[current] = right
    
    current_len = right - left + 1
    
    if current_len > long_len:
        long_len = current_len
        longest_sub = subarray[left:right + 1]

print("Length of longest subarray with distinct values: ", long_len)
print("Longest subarray with distinct values: ", longest_sub)