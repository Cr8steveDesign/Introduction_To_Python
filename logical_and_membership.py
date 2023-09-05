# The "not in" Operator
# The not in operator returns True if a
# value is not found in a sequence, and
# False if it is found.

# Example: Checking if a Word is Not in a List:
banned_words = ["spam", "scam", "fraud"]
word = "spammy"

if word not in banned_words:
    print("The word is not banned.")
else:
    print("The word is banned.")

# Example 3: Using not in for Email Validation:
email = "user@example.com"

if ".com" not in email:
    print("Invalid email format.")
else:
    print("Email format is valid.")


# The "in" operator
# The in operator returns True if a value is
# found in a sequence, and False otherwise.

# Example: Checking if a Name is in a List:
friends = ["Alice", "Bob", "Charlie"]
name = "Bob"

if name in friends:
    print(name, "is your friend.")
else:
    print(name, "is not your friend.")

# Example 2: Checking if a String Contains
# Specific Characters:
password = "P@ssw0rd"

if "@" in password or "#" in password:
    print("Password contains special characters.")
else:
    print("Does not contain special characters.")


# The "not" operator
# The not operator returns the opposite of a
# condition. If a condition is True, not makes
# it False, and vice versa.

# Example: Checking if a user is not logged in:
is_logged_in = False

if not is_logged_in:
    print("Please log in to access the content.")
else:
    print("Welcome to the platform!")

# Using the and operator for a complex check
num = 9

if num % 2 == 1 and num % 3 == 0:
    print("The number is odd and divisible by 3.")
else:
    print("Doesn't meet both conditions.")


# The "and" operator
# The and operator returns True if both conditions
# on its left and right are True, otherwise, it
# returns False.
# Example: Checking if a number is between 10 and 20:
num = 15
if num >= 10 and num <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")

# The "or" operator
# The or operator returns True if at least one of
# the conditions on its left or right is True,
# otherwise, it returns False.
# Example: Checking if a person is either a student
# or an employee:
is_student = True
is_employee = False

if is_student or is_employee:
    print("A student or an employee.")
else:
    print("Neither a student nor an employee.")
