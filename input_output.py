# More examples of user input and printing
# You can equally use the .format() method
# or f-strings to build the output of print

name = "John"
country = "Egypt"
age = 75
profession = "Engineer"
GPA = 4.99

print(f"My name is {name}. I live in {country}")
print(f"I have a GPA of {GPA}")
print("I am currently {}years old".format(age))
print("I am an {} by profession".format(profession))

# You see how we can combine everything we've learnt
# so far, about numbers, strings, input and output
# To create really interactive programs.
greeting = "Hello"
print(greeting * 5)  # Try this out!

print(f"{60 * 5 + ( 100 // 25) - 12 * ( 2 + 9)}")

# The print function is more dynamic
# You can pass 0 to any number of variables
# To be printed

# To print an empty new line simply call print
print()

name = "Stephen"
age = 127
height = 6.2

# Printing multiple variables
print(name, age, height)

# By default each of the variables will be
# separated by a space. You can change that using
# a keyword-argument called sep
print(name, age, height, sep="....")

# You can also override the default newline
# Which is inserted whenever you print
# You can use a space or any character
print(name, height, end=" ")


# The response is returned as a string
# You can enter a prompt for the user.
name = input("Please Enter your name: ")
print(name)
# If you want the user to enter an integer
# You have to type cast the return of the
# input function as the an int.
year = int(input("What year is this? "))
print(year)
# The same for floats
total_cost = float(input("Price: $ "))
discount = float(input("Discount: "))
coupon = int(input("Enter code: "))
print(f"Cost: {total_cost} Discount: {discount}")

# Inserting data into a list
mylist = []  # We'll learn about lists soon
mylist.append(int(input("Enter first number: ")))
mylist.append(int(input("Enter second number: ")))
print(mylist)
