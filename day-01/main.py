# Python is simple
# Python is Open Source
# Python is Case Sensitive
# Python is Dynamically typed language - Type decided while running the program

# Print() -- built-in function (Python standard library)
print("Hello World")
# To run - python3 ./day-01/main.py

# print() wasn’t always a function!
# In Python 2, it was a statement (like print "Hello").
# But in Python 3, it became a proper function — which means now you can do things like:

print("A", "B", "C", sep="-", end="!!\n")
# Output: A-B-C!!

print("My name is")
print("Gagan Chauhan")
# Output:
# My name is
# Gagan Chauhan

print("My name is", "Gagan Chauhan")
# Output: My name is Gagan Chauhan

print(99)
# Output: 99

# Variable -- A name given to a memory location in a program.
# variable = value
name = "Gagan Chauhan"
age = 23
price = 100.99

print(price)
print("Hello, My age is", age)
print(f"My name is {name} and I am {age} years old.") # f-string

# "=" - Assignment Operator

# type() - It checks the datatype of variable
print(type(name)) # <str>
print(type(age)) # <int>
print(type(price)) # <float>

# Datatype - Integer, String, Float, Boolean, None
var1 = True
var2 = None
print(type(var1)) # <bool>
print(type(var2)) # <NoneType>

# Keywords - They are reserved words in python - and, else, if, elif, def, in, is, True, etc.

# Quetion - Print sum of two numbers.
x = 20
y = 34
print(x+y) # 54

"""
Multiple line
comment
"""

# Operators - Arithmetic Operator, Relational/Comparison Operator, Assignment Operator, Logical Operator
# Arithmetic Operator:
a = 4
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a%b) # Remainder
print(a**b) # Power

# Relational/Comparison Operator:
print(a == b) # False
print(a != b) # True
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

# Assignment Operator:
num = 10
num += 10 # num = num + 10
print(num)

# Logical Operator: not, and, or
print(not True)
print(not (a > b))

var1 = True
var2 = False
print(var1 and var2) # Both should be true for output: true
print(var1 or var2) # Any one can be true for output: true

# Type Conversion - Done automatically
# Type Casting - Done manually

var3 = 2
var4 = 4.35
print(var3 + var4)

var5 = int(var4) # Type Casting
print(var5)

# We can type cast string as number e.x - "2", "19" to int, float but we can't type cast int, float to string

# Input in python: This statement is used to accept a value from user.
# input() - Always convert to String
# input("Enter your name: ")
# int(input()) - For Integer value use this
# float(input())

surname = input("Enter your surname: ")
print(surname)

# Question - Write a program to input 2 number and print them sum?
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print(num1 + num2)

# Question - Write a program to input a number and print them square?
num3 = int(input("Enter a number: "))
print(num3 ** 2)