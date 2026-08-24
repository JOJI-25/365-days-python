number = list(map(int, input("Enter the numbers :").split()))

result = []
largest = number[0]

for num in number:
    if num > largest:
        largest = num

    result.append(largest)

print(result)