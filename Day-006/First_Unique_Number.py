unique = list(map(int,input("Enter the integers in the list ").split()))

count={}

for num in unique:
    count[num] = count.get(num, 0) + 1

for num in unique:
    if count[num]== 1:
        u_num = num

print(u_num)
