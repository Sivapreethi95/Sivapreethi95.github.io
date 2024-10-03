numbers =[1,2,3,4,5]
n=3
for i in range(n):
    last_elemnet = numbers.pop()
    numbers.insert(0,last_elemnet)
print(numbers)