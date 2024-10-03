sentence = "Alligators always swim, but birds fly above the trees while elephants march slowly"
dictionary = {}
for i in "abcdefghijklmnopqrstuvwxyz":
    dictionary[i] = []
#count = 0
for word in sentence.split():
    dictionary[word[0].lower()].append(word)
    #if dictionary[word[0].lower()] in dictionary:
       # count = count + 1
#print(count)
    


print(dictionary)

for i in dictionary:
   # print(i)
    # print(len(dictionary[i]))
    dictionary[i] = len(dictionary[i])

print(dictionary)