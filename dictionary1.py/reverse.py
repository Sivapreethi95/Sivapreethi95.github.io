sentence = "hello world python is fun"
dictionary = {}
for word in sentence.split():
    dictionary[word] = word[:: -1]
print(dictionary)