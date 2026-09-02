def subarraySum(numbers, k):
    count = 0
    current_sum = 0
    sum_freq = {0: 1}
    
    for num in numbers:
        current_sum += num
        
        if current_sum - k in sum_freq:
            count += sum_freq[current_sum - k]
            
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1
        
    return count

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter target sum: "))
    result = subarraySum(numbers, target)
    print("Total subarrays with target sum:", result)
