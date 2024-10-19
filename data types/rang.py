# Generate integer numbers from 10 to 14
numbers = range(10, 15, 1)
print(type(numbers))  # class 'range'

# iterate range using for loop
for i in range(10, 15, 1):
    print(i, end=" ")
# Output 10 11 12 13 14