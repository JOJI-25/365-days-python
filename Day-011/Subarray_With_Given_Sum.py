def has_subarray_with_sum(numbers, k):
    seen = {0}
    current_sum = 0
    
    for num in numbers:
        current_sum += num
        if (current_sum - k) in seen:
            return True
        seen.add(current_sum)
        
    return False


if __name__ == "__main__":
    numbers = list(map(int, input("Enter the numbers: ").split()))
    k = int(input("Enter the Target: "))
    
    result = has_subarray_with_sum(numbers, k)
    print("Subarray with given sum exists:" if result else "No subarray with given sum found:")
    print(result)
