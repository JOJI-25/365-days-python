nums = list(map(int, input("Enter list of integers separated by space: ").split()))

if not nums:
    print("List is empty.")
else:
    max_current = nums[0]
    max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        
        if max_current > max_global:
            max_global = max_current

    print("Maximum Subarray Sum:", max_global)