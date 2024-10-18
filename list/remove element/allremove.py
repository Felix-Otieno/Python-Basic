# occurence = [1, 2, 3, 4, 7, 8, 7, 7, 9, 0, 7]

# for item in occurence:
#     occurence.remove(7)
# print(occurence)

my_list = [6, 4, 6, 6, 8, 12]

for item in my_list:
    my_list.remove(6)

print(my_list)
# Output [4, 8, 12]

occurence = [1, 2, 3, 4, 7, 8, 7, 7, 9, 0, 7]

for item in occurence[:]:  # Iterate over a copy of the list
    if item == 7:
        occurence.remove(7)

print(occurence)
