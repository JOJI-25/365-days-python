numbers = list(map(int, input("Enter the numbers : ").split()))

if len(numbers) < 2:
    print("No pair found")
else:
    pair_counts = {}
        
    for i in range(len(numbers) - 1):
        current_pair = (numbers[i], numbers[i+1])
        pair_counts[current_pair] = pair_counts.get(current_pair, 0) + 1
            
    most_frequent = max(pair_counts, key=pair_counts.get)

    print("Most frequent consecutive pair: ", most_frequent)