for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to skip current iteration
        if j == 5:
            continue
        print(i * j, end=' ')
    print('')