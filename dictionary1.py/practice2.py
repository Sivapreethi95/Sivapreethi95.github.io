sentence = ["aPple","BaNaNa","cherry"]
dictionary = {}
for word in sentence:
    for i in word:
        if i.isupper():
            dictionary[word] = "TRUE"
            break
        else:
            dictionary[word] = "FALSE"
print(dictionary)