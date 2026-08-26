number = list(map(int,input("Enter the numbers : ").split()))

current = 0
longest = 0

for i in range(len(number)):
    if number[i] > 0:
        current += 1
    else:
        current = 0
    
    if current > longest:
        longest = current

print(longest)
    