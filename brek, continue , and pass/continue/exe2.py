name = 'Je sa a'

size = len(name)
i = -1
# iterate loop till the last character
while i < size - 1:
    i = i + 1
    # skip loop body if current character is space
    if name[i].isspace():
        continue
    # print current character
    print(name[i], end=' ')