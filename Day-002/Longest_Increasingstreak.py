a = list(map(int, input("Enter the numbers : ").split()))

max_length = 1
current_length = 1

for i in range(1, len(a)):
    if a[i] > a[i-1]:
        current_length += 1
    else:
        current_length = 1
    
    if current_length > max_length:
        max_length = current_length

print(max_length)