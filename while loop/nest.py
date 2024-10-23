i = 1
# outer while loop
# 4 rows in pattern
while i < 5:
    j = 0
    # nested while loop
    while j < i:
        print('*', end=' ')
        j = j + 1
    # end of nested while loop
    # new line after each row
    print('')
    i = i + 1
