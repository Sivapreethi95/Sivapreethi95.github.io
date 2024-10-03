sentence = "The quick brown fox jumps over the lazy dog"
dictionary = {}
#length_dictionary = {}
#empty_list = []
#for word in sentence.split():
   # if len(word)
    #length = len(word)
    #dictionary[len(word)] = 
    
word_lengths = {}
for word in sentence.split():
    if len(word) in word_lengths:
        word_lengths[len(word)].append(word)
    else:
        word_lengths[len(word)] = [word]
print(word_lengths)



