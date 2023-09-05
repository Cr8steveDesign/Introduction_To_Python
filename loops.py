# Number Guessing Game
# Importing the python random module
import random

# Get a random number from 1 to 100
secret_number = random.randint(1, 100)
guess = -1
exit_game = ""


while guess != secret_number:
    if exit_game.upper() == "N":
        break
    guess = int(input("Guess the secret number: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it.")

    exit_game = input("Continue game? Y / N")


# THE WHILE LOOP IN PYTHON
# General Syntax

# while condition:
# Code to be executed while the
# condition is True

# Countdown Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Example: Calculating Factorial
number = int(input("Enter a positive integer: "))
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print("Factorial of", number, "is", factorial)


#  Creating Patterns with Nested Loops:
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# The enumerate function receives a sequence
# and returns a key-value pair you can unpack
# and use in a loop to access the value and
# index of the sequence you're looping through
# Don't worry about the lists. We'll cover
# other data structures soon.
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print("Fruit", index + 1, ":", fruit)

# Summing Numbers Using a Loop
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print("Sum:", sum)


# Try these examples out to understand better
# Iterating Through Characters in a String
word = "Python"
for char in word:
    print(char)

# Using the range function to carry out
# actions a number of times. The above
# will print num from 1 to 5 (except 6)
for num in range(1, 6):
    print(num)

# Loops on a list (kindda like an array)
numbers = [1, 2, 3, 4, 5]
sum = 0

for num in numbers:
    sum += num

print("Sum:", sum)
