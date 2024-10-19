b_array = b'PYnative'
b_array_view = memoryview(b_array)  # creating memory view for bytes objects
print("view object: ", b_array_view)

byte_array = b'PYnative'      # creating bytes array object
byte_array_view = memoryview(byte_array)  # creating memory view for bytes array objects
container = tuple(byte_array_view)   # Storing it in container of iterating
for char in container:
    print(char, end=" ")