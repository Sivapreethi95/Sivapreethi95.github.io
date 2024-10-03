def is_vowel(char):
    if char in "aeiou":
        return True
    else:
        return False

characters = ["a","b","o","c"]
for char in characters:
    print(is_vowel(char))