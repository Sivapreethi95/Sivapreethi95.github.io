text = "A1b2c3@#d4e"
for character in text:
    if character.lower() not in "abcdefghijklmnopqrstuvwxyz":
        continue
    else:
        print(character)