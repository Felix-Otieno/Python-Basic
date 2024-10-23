numbers = [2, 3, 11, 7]
for i in numbers:
    print('Current Number is', i)
    # skip below statement if number is greater than 10
    if i > 10:
        continue
    square = i * i
    print('Square of a current number is', square)