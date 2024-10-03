sentence = "hello world python is fun"
word_lengths = {}
for word in sentence.split():
    word_lengths[word] = len(word)
print(word_lengths)