numbers = [1,2,2,3,4,1,2]
count_dict ={}
for num in numbers:
    if num in count_dict:
        count_dict[num] = count_dict[num]+1
    else:
        count_dict[num] = 1
print(count_dict)