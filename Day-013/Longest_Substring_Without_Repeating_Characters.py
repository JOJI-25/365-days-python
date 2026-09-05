s = input("Enter a string: ")

char_index = {}
left = 0
max_len = 0

for right in range(len(s)):
    char = s[right]
    
    if char in char_index and char_index[char] >= left:
        left = char_index[char] + 1
        
    char_index[char] = right
    
    max_len = max(max_len, right - left + 1)

print(max_len)