numbers = list(map(int, input("Enter the numbers: ").split()))
k = int(input("Enter the value of k: "))

current_sum = sum(numbers[:k])
max_sum = current_sum

for i in range(k, len(numbers)):
    current_sum = current_sum - numbers[i - k] + numbers[i]
    
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)