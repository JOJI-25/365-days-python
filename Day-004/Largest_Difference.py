n = list(map(int, input("Enter the numbers : ").split()))

min_val = n[0]
max_diff = 0

for num in n[1:]:
    diff = num - min_val
    if diff > max_diff:
        max_diff = diff
    if num < min_val:
        min_val = num

print(max_diff)
