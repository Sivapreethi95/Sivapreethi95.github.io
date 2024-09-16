def sum_numbers():
    total = 0
    i = 1
    
    while i <= 100:
        total += i
        i += 1
        
    return total

# Call the function and print the result
result = sum_numbers()
print("Sum of numbers from 1 to 100:", result)