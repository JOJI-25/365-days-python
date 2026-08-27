def longest_alternating_streak(numbers):
    if not numbers:
        return 0
    
    max_len = 1
    curr_len = 1
    
    for i in range(1, len(numbers)):
        # Check if values are equal (breaks the pattern)
        if numbers[i] == numbers[i - 1]:
            curr_len = 1
        # Check if the current step alternates direction from the previous step
        elif i == 1 or (numbers[i] > numbers[i - 1]) != (numbers[i - 1] > numbers[i - 2]):
            curr_len += 1
        else:
            # If direction repeats, start a new streak with the current pair
            curr_len = 2
            
        max_len = max(max_len, curr_len)
        
    return max_len

n = list(map(int, input("Enter the numbers : ").split()))
print(longest_alternating_streak(n))