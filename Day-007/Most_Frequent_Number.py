num = list(map(int, input("Enter the numbers: ").split()))

counts ={}
max_count = 0
result = None

for num in num:
    counts[num] = counts.get(num, 0) + 1
    if counts[num] > max_count:
        max_count = counts[num]
        result = num
    
print(result)