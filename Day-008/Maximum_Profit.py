stock = list(map(int,input("Enter the stock prices: ").split()))

min_price = stock[0]
max_prof = 0

for price in stock:
    if price < min_price:
        min_price = price
    else:
        current_prof = price - min_price
        if current_prof > max_prof:
            max_prof = current_prof
            
print(f"Maximum profit is: {max_prof}")