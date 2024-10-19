# create a bytearray
list1 = [9, 17, 11, 78]
b_array = bytearray(list1)
print(b_array)
print(type(b_array))  # class 'bytearray'

# modifying bytearray
b_array[1] = 99
print(b_array[1])  # 99

# iterate bytearray
for i in b_array:
    print(i, end=" ")  # 9 99 11 78