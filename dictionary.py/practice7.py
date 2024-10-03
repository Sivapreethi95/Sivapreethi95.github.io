words = "hello world"
dict = {}
for word in words:
    if word in dict :
        dict[word]=dict[word]+1
    else:
        dict[word] = 1
print(dict)