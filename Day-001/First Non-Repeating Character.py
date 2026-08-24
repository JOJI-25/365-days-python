a = input()

frequency = {}

for char in a:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

found = False

for char in a:
    if frequency[char] == 1:
        print(char)
        found = True
        break

if not found:
    print(-1)