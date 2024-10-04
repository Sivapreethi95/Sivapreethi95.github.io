sentence = ["apple123","banana","456","cherry"]
dictionary = {}
containsDigits = []
noDigits = []
# Method 1
# Using True or False
# for word in sentence:
#     have_I_added = False
#     for i in word:
#         if i.isdigit():
#             containsDigits.append(word)
#             have_I_added = True
#             break
#     if have_I_added == False:
#         noDigits.append(word)

#Method 2
for word in sentence:
    for i in word:
        if i.isdigit():
            containsDigits.append(word)
            break
    if word not in containsDigits:
        noDigits.append(word)
                    
print(containsDigits)
print(noDigits)
dictionary ["contains_digits"] = containsDigits
dictionary["no_digits"] = noDigits
print(dictionary)