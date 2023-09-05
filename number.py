# NUMBER OPERATIONS IN PYTHON
import math  # This is only needed to use the math functions

# Addition of numbers
num1 = 1 + 2 + 56  # output = 59
# Multiplication
num2 = 2.5 * 2  # output = 5
# Division
num3 = 50.54 / 3  # output = 16.8466666666...
# Floor Division (Without a remainder)
num4 = 10 / 3  # output = 3
# Exponetiation (Raise to power)
num5 = 5 ** 2  # output = 25
# Modulus (Remainder)
num6 = 30 % 3  # output = 0

# You can use parenthesis to direct the order
# Of calculation, else they'll be evaluated
# using the operator precedence (Learn more)
result = (10 + 5) * (2 ** 3) / (4 + 2)
print(result)  # output = 20

# Comparison Operations on
# Floating-Point Numbers
float1 = 3.14
float2 = 2.71

# Equal to
print(float1 == float2)  # False
# Not equal to
print(float1 != float2)  # True
# Greater than
print(float1 > float2)   # True
# Less than
print(float1 < float2)   # False
# Greater than or equal to
print(float1 >= float2)  # True
# Less than or equal to
print(float1 <= float2)  # False

# Type Conversions in Python
# Integer to Float
int_value = 42
float_value = float(int_value)
print("Float value:", float_value)

# Float to Integer (with truncation)
float_num = 3.8
int_num = int(float_num)
print("Integer value:", int_num)

# String to Integer
str_num = "123"
int_from_str = int(str_num)
print("Integer from string:", int_from_str)

# String to Float
str_float = "3.14"
float_from_str = float(str_float)
print("Float from string:", float_from_str)

# Comparison Operations on Integers
num1 = 10
num2 = 20

# Equal to
print(num1 == num2)       # False
# Not equal to
print(num1 != num2)       # True
# Greater than
print(num1 > num2)        # False
# Less than
print(num1 < num2)        # True
# Greater than or equal to
print(num1 >= num2)       # False
# Less than or equal to
print(num1 <= num2)       # True


# Calculate the square root of a number
number = 25
square_root = math.sqrt(number)

# Calculate the exponential value
base = 2
exponent = 3
result = math.pow(base, exponent)

# Round a floating-point number up and down
float_num = 3.8
rounded_up = math.ceil(float_num)
rounded_down = math.floor(float_num)

# Calculate trigonometric values
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)
sine_value = math.sin(angle_in_radians)
cosine_value = math.cos(angle_in_radians)

# Print constants
pi_value = math.pi
euler_constant = math.e
print("The value of pi:", pi_value)
print("Euler's constant:", euler_constant)
