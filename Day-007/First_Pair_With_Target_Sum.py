nums = list(map(int,input("Enter the numbers: ").split()))


target = int(input("enter the target number: "))


for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Index pairs are: {i} and {j}, and the Values are {nums[i]} and {nums[j]} ")
            break
    else:
        continue
    break

else:
    print("no pair found")

    