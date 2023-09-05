# String Interpolation (f-strings, Python 3.6+):
name = "Bob"
height = 175
info = f"{name}'s height is {height} cm."
print(info)

# Expressions inside f-strings
x = 10
y = 20
result = f"The sum of {x} and {y} is {x + y}."
print(result)

# Caling methods inside f-strings
text = "python programming"
capitalized_text = f"Capitalized: {text.capitalize()}"
print(capitalized_text)

# Number formating inside f-strings
price = 49.99
discount = 0.2
final = f"Final price: ${price * (1 - discount):.2f}"
print(final)


# String Methods: Using built-in methods
text = "python programming"
uppercase_text = text.upper()
capitalized_text = text.capitalize()
replace_text = text.replace("python", "Python")
print("Uppercase:", uppercase_text)
print("Capitalized:", capitalized_text)
print("Replaced:", replace_text)

# String Formatting for dynamic strings
num1 = 5.6789
num2 = 12.3456
formatted_nums = "Numbers: {:.1f}, \
{:.2f}".format(num1, num2)
print(formatted_nums)

info = "Name: {name}, Age: {age}"\
    .format(name="Charlie", age=28)
print(info)

name = "Alice"
age = 30
greeting = "Hello, {}! You're {} \
  years old.".format(name, age)
print(greeting)


"""
Slicing is a way to extract a portion of a string
in Python. It allows you to "slice" a string into 
smaller parts based on the indices of the characters 
within the string. The syntax for slicing is 
[start:end], where start is the index of the first 
character you want to include, and end is the index 
of the character just after the last one you want 
to include.
"""

# Slicing '[:]': Extracting a portio of a string
# Syntax: [start:end] or [start:end:step]

phrase = "Hello, world!"
substring = phrase[7:12]
# Starting at index 7, up to index 12 (exclusive)
print("Substring:", substring)

substring_omit_start = phrase[:5]
# Omitting the start index starts at the
# beginning of the string # Result: "Hello"

substring_omit_end = phrase[7:]
# Omitting the end index continues
# until the end of the string # Result: "world!"
# Slicing with a step

substring_step = phrase[0:12:2]
# Starting at index 0, ending at index 12
# (exclusive), with a step of 2 # Result: "Hlo o"


# Concatenation of Strings using + operator
string1 = "Hello, "
string2 = "world!"
result = string1 + string2
print(result)  # output = Hello World!

# Repetition '*': Repeating a string multiple times
word = "Python "
repeated_word = word * 3
print(repeated_word)

# Indexing '[ ]': Accessing by index
text = "Python"
first_char = text[0]  # Index starts at 0
last_char = text[-1]  # Negative index counts from end
print("First:", first_char, "Last:", last_char)

# Length 'len( )': Finding the number of characters
message = "Hello, world!"
length = len(message)
print("Length of the string:", length)
