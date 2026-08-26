a = list(map(int,input("Enter the numbers : ").split()))

n = len(a)

if n == 1:
    print("no missing values")
else:
    expected_sum = (n*(n+1)//2)
    actual_sum = sum(a)

    if expected_sum == actual_sum:
        print("No missing values")
    else:
        missing = expected_sum - actual_sum
        print("The missing values are:", missing)
