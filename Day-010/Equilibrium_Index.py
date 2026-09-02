numbers = list(map(int, input("Enter numbers: ").split()))
total_sum = sum(numbers)
left_sum = 0

for i in range(len(numbers)):
    right_sum = total_sum - left_sum - numbers[i]

    if left_sum == right_sum:
        print(i)

    left_sum += numbers[i]

