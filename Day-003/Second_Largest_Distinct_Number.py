a = list(input("Enter the numbers : ").split())

set = list(set(a))

if len(set) < 2:
    print(False)
else:
    set.sort(reverse = True)
    print(set[1])