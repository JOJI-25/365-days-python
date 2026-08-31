numbers = list(map(int,input("Enter the numbers: ").split()))

counts = {}

for num in numbers:
    counts[num] = counts.get(num, 0) + 1

for num in numbers:
    if counts[num] == 1:
        print(f"The first non-repeating number is :{num}")
        break
else:
    print("No non-repeating number found")  