numbers = [10,15,30,45,20,50,25,5]
sum = 0
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        continue
    else:
        sum = sum + number
        if sum > 100:
            break
        print(sum)
#print(sum)