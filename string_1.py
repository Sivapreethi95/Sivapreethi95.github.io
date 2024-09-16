def say_hello(x):
    i=0
    vowels=["a","e","i","o","u"]
    count=0
    while i<len(x):
        if x[i] in vowels:
            count=count+1
        i=i+1
    return count

print(say_hello("sivapreethi"))

