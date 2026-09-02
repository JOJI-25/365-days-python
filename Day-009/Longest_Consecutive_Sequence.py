numbers = list(map(int, input("Enter numbers separated by space: ").split()))

num_set = set(numbers)
max_streak = 0

for num in num_set:
    # Check if 'num' is the start of a sequence
    if num - 1 not in num_set:
        current_num = num
        current_streak = 1

        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1

        if current_streak > max_streak:
            max_streak = current_streak

print("Length of longest consecutive sequence:", max_streak)
