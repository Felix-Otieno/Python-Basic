age = 25
is_student = True

# Check if the person is both older than 18 and a student
if age > 18 and is_student:
    print("Eligible for student discount")  # Output: Eligible for student discount
else:
    print("Not eligible for discount")

age = 15
is_student = False

# Check if the person is either older than 18 or a student
if age > 18 or is_student:
    print("Eligible for discount")
else:
    print("Not eligible for discount")  # Output: Not eligible for discount

is_logged_in = False

# Negate the condition
if not is_logged_in:
    print("Please log in")  # Output: Please log in
else:
    print("Welcome back!")
