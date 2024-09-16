def sum_of_list(numbers):
    i = 0
    a = 0
    
    while i<len(numbers):
        a = a+numbers[i]
        #print(numbers[i])
        i+=1
        #a = a+numbers[i]
    
    return a

# Call the function and print the result
result = sum_of_list([10,20,30,40,50])
print("Sum of list is ", result)