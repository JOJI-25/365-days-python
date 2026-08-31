long = list(map(int, input("Enter the numbers: ").split()))

if not long:
    print("No increasing subarray found")
else:
    current_len = 1
    current_elements = [long[0]]

    long_len = 1
    long_element = [long[0]]

    for i in range(1, len(long)):
        if long[i] > long[i - 1]:
            current_len += 1
            current_elements.append(long[i])
        else:
            if current_len > long_len:
                long_len = current_len
                long_element = list(current_elements)
            current_len = 1
            current_elements = [long[i]]

    # Final check for the last sequence
    if current_len > long_len:
        long_len = current_len
        long_element = list(current_elements)

    print("Length of longest increasing subarray:", long_len)
    print("Elements of longest increasing subarray:", long_element)