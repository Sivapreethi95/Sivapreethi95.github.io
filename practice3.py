count = 0
for i in range(1,10):
    if i%2 == 0:
        count = count + i
    elif i%3 == 0:
        count = count - i
print(count)