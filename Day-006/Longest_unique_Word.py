word = input("Enter the list of words: ").split()

unique_ch = -1
word_len = -1

for word in word:
    if len(word) == len(set(word)):
        if len(word) > word_len:
            word_len = len(word)
            unique_ch = word

print(unique_ch)