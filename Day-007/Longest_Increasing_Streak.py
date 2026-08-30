num = list(map(int,input("Enter the number: ").split()))

max_streak= 0
current_streak = 0

for i in range(len(num)):
    if num[i] > num[i-1]:
        current_streak += 1
    else:
        current_streak = 1

    if current_streak > max_streak:
        max_streak = current_streak

print(max_streak)