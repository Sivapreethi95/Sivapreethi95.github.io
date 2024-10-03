sentence = "apple banana orange"
#Method 1
# def uniquelen(word):
#     seen_list = []
#     for i in word:
#         if i not in seen_list:
#             seen_list.append(i)

#     return len(seen_list)
        
# word_lengths = {}
# for word in sentence.split():
#     word_lengths[word] = uniquelen(word)
# print(word_lengths)
    
sentence = "apple banana orange"
        
word_lengths = {}
for word in sentence.split():
    seen_list = []
    for i in word:
        if i not in seen_list:
            seen_list.append(i)

    word_lengths[word] = len(seen_list)
print(word_lengths)
    
        
#print(dictionary)

        
#print(dictionary)
