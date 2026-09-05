numbers = list(map(int, input("Enter numbers separated by space: ").split()))

insert_pos = 0

for num in numbers:
    if num != 0:
        numbers[insert_pos] = num
        insert_pos += 1


while insert_pos < len(numbers):
    numbers[insert_pos] = 0
    insert_pos += 1

print(numbers)