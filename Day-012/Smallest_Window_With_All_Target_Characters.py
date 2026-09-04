s = input("Enter string s: ")
target = input("Enter target string: ")

target_count = {}
for char in target:
    target_count[char] = target_count.get(char, 0) + 1

required = len(target_count)
formed = 0
window_counts = {}

l = 0
min_len = float("inf")
min_left = 0

for r in range(len(s)):
    char = s[r]
    window_counts[char] = window_counts.get(char, 0) + 1

    if char in target_count and window_counts[char] == target_count[char]:
        formed += 1

    while l <= r and formed == required:
        char = s[l]

        if r - l + 1 < min_len:
            min_len = r - l + 1
            min_left = l

        window_counts[char] -= 1
        if char in target_count and window_counts[char] < target_count[char]:
            formed -= 1

        l += 1

if min_len == float("inf"):
    print("")
else:
    print(s[min_left : min_left + min_len])