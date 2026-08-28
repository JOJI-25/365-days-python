import string

sentence = input("Enter the sentence: ")

clean_sen = sentence.translate(str.maketrans('', '', string.punctuation))
words = clean_sen.split()

max_len = 0
longest_word = None

for word in words:
    if len(word) > max_len:
        max_len = len(word)
        longest_word = word

print(longest_word)