numbers = list(map(int, input("Enter the numbers: ").split()))
k = int(input("Enter the value of k: "))

prefix_sum=0
sum_count={0:1}

count=0
for num in numbers:
    prefix_sum += num
    
    diff = prefix_sum - k
    if diff in sum_count:
        count+=sum_count[diff]
    
    sum_count[prefix_sum]=sum_count.get(prefix_sum,0)+1

print(count)