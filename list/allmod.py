list = [2, 4, 6, 8]

for i in range(len(list)):
    square = list[i] * list[i]
    list[i] = square
print(list)