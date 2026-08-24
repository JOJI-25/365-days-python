# Second Largest Distinct Number
numbers = list(input("Enter the number :"))

num = list(set(numbers))

if len(num) < 2:
    print(-1)
else:
    num.sort()
    print(num[-2])