n = list(map(int,input("Enter the numbers : ").split()))

seen = set()


for i in range(len(n)):
    if n[i] in seen:
        print(n[i])
        break
    seen.add(n[i])

