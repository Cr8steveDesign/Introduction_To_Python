# You use the def keyword when defining
# your function. This is followed with the
# name of the function and the parameter list and :

# this is a global variable
scholarship = True


def my_function(name, age, gender):
    # You can declare variables local to the function
    course = "ALX Software Engineering "
    cohort = "Cohort 16"
    year = 2023
    is_complete = False

    # To access global variables use "global varname"
    # Be careful as you can reassign the value of
    # the global variable from this function
    global scholarship

    # calling other functions inside your function
    print(name, age, gender, course, cohort, year)


# Defining a function and then calling it
# Python executes code sequentially, so if you attempt
# to call a function before it's defined, you'll
# encounter a "NameError" because Python doesn't
# recognize the function yet.

# Defining a function that concatenates two strings
# Take note this example, only receives the arguments
# and performs an operation with them. It doesn't
# return a value. We'll see an example of a function
# that returns a value shortly

def strConcat(str1, str2):
    newString = str1 + str2
    print(newString)


strConcat("Python", " is Awesome!")
# This will print out "Python is Awesome!"

# Note, you can't call a function with more arguments
# than you defined in the function definition, unless
# using *args or **kwargs. You also can't call it
# with less arguments unless there's a default argument.

# DEFAULT PARAMETERS
# This allows you to optionally pass certain values to
# the function, and the function assumes a default
# value if the positional parameter is not provided.
# Also, make sure that the arguments/parameters are
# separated with a comma. Naming conventions with
# variables also apply with functions.


def fullName(firstName, surName="False"):
    if surName == "False":
        print("Sorry, no surname was provided")
    else:
        print(f"Full Name is: {firstName} {surName}")


fullName("John")
fullName("Stephen", "Omoregie")
fullName("Freedom", "Talistalista")
# Yes you can use all programming constructs within
# a function. Also note that the parameters are treated
# as variables of the function. There's no need to define
# firstName and surName again. Just used directly

# FUNCTIONS THAT RETURNS SINGLE VALUES
# A function can return a value of any datatype. The
# value returned by a function depends on the logic
# or what you're trying to implement.

# A function that calculates the area of a rectangle
# or a square and returns the computed value


def calculateArea(shape, length, breadth):
    if shape.lower() == "rectangle":
        return length * breadth
    elif shape.lower() == "square":
        return length ** 2
    else:
        return 0


rectangle1 = calculateArea("rectangle", 17, 9)
rectangle2 = calculateArea("rectangle", 25, 56)
print(rectangle1, rectangle2)

square1 = calculateArea("square", 5, 5)
square2 = calculateArea("square", 5, 9)
print(square1, square2)

# A Function that returns multiple values
# In python, you can return more than one valuables
# separated by a comma (,). These variables will be
# returned as a Tuple, which can be unpacked when the
# function is called. This can be very helpful.

# A Function that squres any number passed into it
# and returns it.


def squarePeg(num1=1, num2=1, num3=1, num4=1):
    # Though there are better ways of creating
    # a function that receives a variable number
    # of arguments (*args and **kwargs)
    return num1**2, num2**2, num3**2, num4**2


# Upacking the return value
first, second, third, fourth = squarePeg(5, 9, 7, 10)
# calling it with less arguments
n1, n2, n3, _ = squarePeg(21, 8, 6)

# The position of the variables you're unpacking into
# will tally with the position of the value in your
# function definition

# USING THE RANGE FOR FIZZBUZZ

# The range function for getting a range between
# given arguments. # range(start, end, step)
# If the third argument is not given, it defaults
# to 1 - i.e one step at a time, 1, 2, 3, 4, 5

for num in range(1, 50):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")
print()

# Getting the length of a string, or number of
# elements in a list/dictionary/tuple
stringLen = len("The Zen of Python")
listLenght = len([6, 7, 8, 12, 34, 98, 66, 23])
dictioLength = len({"name": "Stephen"})

# PYTHON'S SUPPORT FOR RECURSIVE FUNCTION
# Using recursion to print even numbers from
# the given number  to 0 - in reverse.


def reverseEven(n: int) -> None:
    # A base case where the recursive function
    # Breaks and returns back to the caller
    if (n < 0):
        return
    if (n % 6 == 0):
        print()  # Print a new line
    if (n % 2 == 0):
        print(n, end=" ")  # Space separated
    reverseEven(n - 1)


print("Printing Recursively")
reverseEven(56)
print("============================")
reverseEven(100)
print("=============================")
