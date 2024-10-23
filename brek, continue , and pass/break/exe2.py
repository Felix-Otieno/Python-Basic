name = 'Jesaa29 Roy'

size = len(name)
i = 0
# iterate loop till the last character
while i < size:
    # break loop if current character is space
    if name[i].isspace():
        break
    # print current character
    print(name[i], end=' ')
    i = i + 1