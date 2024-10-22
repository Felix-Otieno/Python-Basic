# range from 'a' to 'z
def character_range(char1, char2):
    for char in range(ord(char1), ord(char2) + 1):
        yield (char)


for letter in character_range('a', 'z'):
    print(chr(letter), end=', ')
