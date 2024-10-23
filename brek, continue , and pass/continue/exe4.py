for i in range(1, 11):
    # condition to skip iteration
    # Don't print multiplication table of even numbers
    if i % 2 == 0:
        continue
    print('Multiplication table of', i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')