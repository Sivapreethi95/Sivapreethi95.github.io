prices = {"apple":1.2,"banana":0.5,"cherry":2.5}
quantities = {"banana":5,"apple":3,"cherry":2}
total_price = 0
for i  in quantities:
    #i = prices[i] * quantities[i]
    #total_price = total_price + i
    total_price = total_price + (prices[i]*quantities[i])
print(total_price)