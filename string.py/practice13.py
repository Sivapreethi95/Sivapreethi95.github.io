string1 = ["Alagappan","Preethi","Sivapreethi","Alpha","Beta","Theta"]
shortest = string1[0]
for i in string1:
    if len(i)<len(shortest):
        shortest = i
print(shortest)