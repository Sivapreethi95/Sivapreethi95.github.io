sentence = ["apple","banana","pear","grape"]
dictionary = {}
evenList = []
oddList = []

for word in sentence:
    if len(word)% 2 == 0:
        evenList.append(word)
    else:
        oddList.append(word)
print(evenList)
print(oddList)
dictionary["even"] = evenList
dictionary["odd"] = oddList
print(dictionary)