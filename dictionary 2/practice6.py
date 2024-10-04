sentence = "Antelope ate apples under a banana tree, while cats chased dogs across the firld and eagles soared high above"
dictionary = {}
for i in "abcdefghijklmnopqrstuvwxyz":
    dictionary[i] = []
for word in sentence.split():
    #if word[0].lower() in dictionary:
    dictionary[word[0].lower()].append(word)
    #else:
        #dictionary[word[0].lower()] = [word]
    #dictionary[word[0].lower()]= word
    #print(word[0].lower())


print(dictionary)