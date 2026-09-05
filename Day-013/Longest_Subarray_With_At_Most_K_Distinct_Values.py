numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter k: "))

freq = {}
left = 0
max_len = 0

for right in range(len(numbers)):
    num = numbers[right]
    freq[num] = freq.get(num, 0) + 1

    while len(freq) > k:
        left_num = numbers[left]
        freq[left_num] -= 1
        if freq[left_num] == 0:
            del freq[left_num]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)