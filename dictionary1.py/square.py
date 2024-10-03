sentence = "hello world python is fun"
dictionary = {}
for word in sentence.split():
    dictionary[word] = len(word)**2
print(dictionary)