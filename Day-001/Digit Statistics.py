##------------- Digit Statistics ---------------

#Using the String conversion Method

a = str(input("Enter the number :"))

number = len(a)
sum = sum(int(ch) for ch in a)
largest = max(int(ch) for ch in a)
smallest = min(int(ch) for ch in a)

print(number)
print(sum)
print(largest)
print(smallest)

#Using the Mathematical Operation 

a = int(input("Enter the number :"))

num = 0
sum = 0
max = 0
min = 0

if a == 0:
    print(1)
    print(0)
    print(0)
    print(0)

while a > 0:
    digit = a % 10
    num += 1
    sum += digit
    max = max(max,digit)
    min = min(max,digit)
    a // 10

print(num)
print(sum)
print(max)
print(min)

# using functional programming

a = str(input("Enter the number :"))

digit = list(map(int, str(a)))

print(len(digit))
print(sum(digit))
print(max(digit))
print(min(digit))