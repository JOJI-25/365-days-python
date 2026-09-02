numbers = list(map(int, input("Enter the numbers: ").split()))
k = int(input("Enter k: "))

window_sum = sum(numbers[:k])
max_sum = window_sum

for i in range(k, len(numbers)):
    window_sum = window_sum - numbers[i - k] + numbers[i]

    if window_sum > max_sum:
        max_sum = window_sum

max_average = max_sum / k

print("Maximum average:", max_average)