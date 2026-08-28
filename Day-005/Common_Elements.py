list_1 = list(map(int,input("Enter the 1st list: ").split()))
list_2 = list(map(int,input("Enter the 2nd list: ").split()))

set_2 = set(list_2)
seen = set()
result = []

for i in list_1:
    if i in set_2 and i not in seen:
        result.append(i)
        seen.add(i)

print(result)