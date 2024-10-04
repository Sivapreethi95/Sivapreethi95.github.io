string1 = ["Alagappan","Preethi","Sivapreethi","Alpha","Beta","Theta"]
count =0
for i in string1:
    count = 0
    for j in i:
        if j not in 'aeiouAEIOU':
            count = count + 1
    print(count)