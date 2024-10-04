sentence = "hello world python is fun"
dictionary = {}
for word in sentence.split():
    count = 0
    for j in word:
        if j in "aeiouAEIOU":
            count=count+1
    #print(count)
    dictionary[word] = count
print(dictionary)