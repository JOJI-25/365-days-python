from collections import Counter

string = input("Enter the string: ")

if len(string) <= 1:
    print(None)
else:
    count = Counter(string)
    set = sorted(set(count.values()), reverse=True)
    print(set[1])