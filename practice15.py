numbers = [1,2,3,4,5,6,7,8]
filtered_numbers =[]
for num in numbers:
    if num % 2 !=0:
        filtered_numbers.append(num)
print(filtered_numbers)