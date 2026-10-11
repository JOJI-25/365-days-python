from collections import Counter

string = input("Enter the string: ")

count = Counter(string)

if len(count) < 2:
    print(-1)
else:
    unique_freqs = sorted(list(set(count.values())), reverse=True)
    
    if len(unique_freqs) < 2:
        print(-1)
    else:
        second_freq = unique_freqs[1]
        candidates = [char for char, freq in count.items() if freq == second_freq]
        result = min(candidates, key=string.index)
        print(result)