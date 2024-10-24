try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a/b
    print("The answer of a divide by b:", c)
except ZeroDivisionError as e:
    raise ValueError("Division failed") from e

# Output: Enter value of a:10
# Enter value of b:0
# ValueError: Division failed