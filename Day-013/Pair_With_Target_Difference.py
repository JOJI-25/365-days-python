numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter k: "))


seen = set()
found = False

for num in numbers:
    if (num - k) in seen or (num + k) in seen:
        found = True
        break
    seen.add(num)

print(found)