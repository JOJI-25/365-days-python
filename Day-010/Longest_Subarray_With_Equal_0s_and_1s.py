numbers = list(map(int, input("Enter the numbers: ").split()))

balance = 0
first_seen = {0: -1}
max_length = 0

for i in range(len(numbers)):

    if numbers[i] == 0:
        balance -= 1
    else:
        balance += 1

    if balance in first_seen:
        length = i - first_seen[balance]

        if length > max_length:
            max_length = length

    else:
        first_seen[balance] = i

print("Length of longest subarray:", max_length)