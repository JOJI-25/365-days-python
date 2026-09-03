numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
k = int(input("Enter window size k: "))

result = []
n = len(numbers)

for i in range(n - k + 1):
    window = numbers[i : i + k]
    
    distinct_count = len(set(window))
    result.append(distinct_count)

print(result)