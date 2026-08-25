a = int(input("Enter the number: "))

even = 0
odd = 0

while a > 0:
    digit = a % 10
    if digit % 2 == 0:
        even += digit
    else:
        odd += digit
    a //= 10

if even == odd:
    print(True)
else:
    print(False)