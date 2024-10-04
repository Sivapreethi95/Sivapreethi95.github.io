string1 = ["Alagappan","Preethi","Sivapreethi","Alpha","Beta","Theta"]
longest = string1[0]
for i in string1:
    if len(i)>len(longest):
        longest = i
print(longest)