

"""
if-elif-else Statement:
The if-elif-else statement allows you to check 
multiple conditions sequentially and execute the 
block corresponding to the first True condition.

if condition1:
    # Code to execute if condition1 is True
    # These can be multiple lines - indented
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
else:
    # Code to execute if none of the conditions 
    are True

"""
# These are the general syntax for if-elif-else
# Now let's look at them in code action. Take
# note of the indentations under each one.


"""
if Statement:
The if statement is used to execute a block 
of code only if a specific condition is True.

if condition:
    # Code to execute if condition is True

    
if-else Statement:
The if-else statement allows you to execute 
one block of code when a condition is True, 
and a different block when the condition 
is False.

if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
"""

# Example of if-elif-else statement
# Checking a Student's grade
score = int(input("Enter Score: "))
status = " "

if score >= 90:
    status = "Grade A Student"
    print("Excellent!")
elif score >= 80:
    status = "Grade B Student"
    print("Good job!")
elif score >= 70:
    status = "Still picking up"
    print("Fair.")
else:
    status = "Dropping grades"
    print("Needs improvement.")

print(status)
# Pay attention to how the statements
# under each condition is indented.


# Example of if statement
# The code is only executed if age is greater
# than or equal 18.
age = 18
if age >= 18:
    print("You are an adult.")

# Example of if-else statement
# Check if a number # is ODD or EVEN
num = int(input("Enter your number"))
if num % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

# If-else statement for input validation
user_guess = int(input("Enter number: "))

if user_guess == 777:
    print("Congratulations! You won!")
else:
    print("Sorry, you guessed wrong!")
