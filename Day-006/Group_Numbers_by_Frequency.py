number = list(map(int,input("Enter the integers in the list ").split()))

count =  {}

for num in number:
    count[num] = count.get(num ,0) + 1

result = []

seen = set()

for num in number:
    if count[num] > 1 and num not in seen:
        result.append(num)
        seen.add(num)

print(result)