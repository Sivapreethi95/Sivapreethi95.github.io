sentence = ["banana","Alpha","peep","dad","moM"]
dictionary = {}
for word in sentence:
    if word[0].lower() == word[-1].lower():
        dictionary[word] = "YES"
print(dictionary)
