a = list(map(int, input("Enter the numbers : ").split()))

if len(a) < 3:
    is_mountain = False
else:
    i = 0
    n = len(a)

    while i + 1 < n and a[i] < a[i + 1]:
        i += 1
    
    if i == 0 or i == n - 1:
        is_mountain = False
    else:
        while i + 1 < n and a[i] > a[i + 1]:
            i += 1
        
        if i == n - 1:
            is_mountain = True
        else:
            is_mountain = False

print(is_mountain)
