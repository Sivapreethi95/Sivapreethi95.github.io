sentence = ["try","my","fly","sky","ppel","app"]
dictionary = {}
for word in sentence:
    for i in word:
        if i not in "aeiouAEIOU":
            dictionary[word] = "TRUE"
        else:
            dictionary[word] = "FALSE"
            break
print(dictionary)