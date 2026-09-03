numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
k = int(input("Enter the target k: "))

min_length = float('inf')
n = len(numbers)

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += numbers[j]
        
        if current_sum >= k:
            length = j - i + 1
            if length < min_length:
                min_length = length

if min_length == float('inf'):
    print(0)
else:
    print(min_length)