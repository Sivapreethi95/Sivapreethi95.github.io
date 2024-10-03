numbers = [1,2,3,4,5]
for i in range(len(numbers) -1, -1,-1):
    if numbers[i] % 2 == 0:
        numbers.insert(i+1,10)
        numbers.insert(i+2,20)
print(numbers)