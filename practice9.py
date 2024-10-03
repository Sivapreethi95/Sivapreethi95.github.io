numbers = []
for i in range (1,11):
    if i % 2 == 0:
        numbers.append(i)
    else:
        numbers.extend([i,0])
print(numbers)