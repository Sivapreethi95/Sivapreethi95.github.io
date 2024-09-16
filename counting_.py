def count_consonants(x):
    i=0
    vowels=["a","e","i","o","u"]
    count=0
    while i<len(x):
        if x[i] not in vowels:
            count=count+1
        i=i+1
    return count

print(count_consonants("sivapreethi"))

