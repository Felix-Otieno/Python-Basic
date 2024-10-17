# calculate the square of each even number from a list and store in dict
numbers = [1, 3, 5, 2, 8]
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print(even_squares)

# output {2: 4, 8: 64}