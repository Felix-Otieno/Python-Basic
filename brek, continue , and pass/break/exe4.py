for i in range(1, 11):
    # condition to break outer loop
    if i > 5:
        break
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')
