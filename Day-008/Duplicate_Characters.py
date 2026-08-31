dup = str(input("Enter the string: "))

counts = {}

for ch in dup:
    counts[ch] = counts.get(ch, 0) + 1

result = []
seen = set()

for ch in dup:
    if counts[ch] > 1 and ch not in seen:
        result.append(ch)
        seen.add(ch)


if len(result) == 0:
    print("No duplicate characters found")
else:
    print(f"The duplicate characters are: {result}")
