from collections import Counter

string = input("Enter the string : ")

count = Counter(string)

maximum = max(dict.fromkeys(string), key=count.get)
print(maximum)

