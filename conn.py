from itertools import chain

# Concatenate ranges
new_range = chain(range(5), range(5, 10))
for num in new_range:
    print(num, end=' ')
# Output 0 1 2 3 4 5 6 7 8 9