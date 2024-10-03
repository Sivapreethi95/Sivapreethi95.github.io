numbers = [10,20,4,45,99]
smallest = second_smallest = third_smallest = float('+inf')
for num in numbers:
    if num < smallest:
        third_smallest = second_smallest
        second_smallest = smallest
        smallest = num
    elif num < second_smallest:
        third_smallest = second_smallest
        second_smallest = num
    elif num < third_smallest:
        third_smallest = num
print(second_smallest)
