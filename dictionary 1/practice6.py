words = ["apple","cat","banana","dog","fish"]
length_dict = {}
for word in words:
    length = len(word)
    if length not in length_dict:
        length_dict[length]=[word]
    else:
        length_dict[length].append(word)
print(length_dict)