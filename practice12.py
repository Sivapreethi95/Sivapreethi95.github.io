numbers = [10,20,4,45,99]
largest = second_largest = float('-inf')
for num in numbers:
    if num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num
    elif num > second_largest:
        third_largest = second_largest
        second_largest = num
    elif num > third_largest:
        third_largest = num
print(second_largest)
