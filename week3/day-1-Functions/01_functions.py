# A function is a reusable block of code that does one job.
"""
Think of it as a recipe:
You write it once.
Use it many times.
It gives the same result on every use.
"""

# Without function
print("Hello Musaddiq")
print("Hello Naseem")
print("Hello Yaseen")


# With function
def greet(name):
    print(f"Hello {name}")


greet("Musaddiq")
greet("Naseem")
greet("Yaseen")
greet("Farhan")  # reusable


# Another example
def add(num1, num2):
    print(f"Results: {num1 + num2}")


add(5, 4)  # Results: 9
add(288, 206)  # Results: 494

"""
Why use functions:
Reusable | write once, call many times
Readable | add(298, 198) is clearer than 2 lines of math
"""

# Basic syntax.
"""
def function_name():
    # body

- def means "define a function" — e.g. def greet():, def subtract():
- function_name is your chosen name (letters, digits, underscores).
- round () brackets contain parameters.
- : is the colon at the end.
- 4 spaces indent inside block (same as loop / if statements).
"""


# Defining a function
def hello():
    print("Hello World")


# Calling a function
hello()
hello()

# Output:
"""
Hello World
Hello World
"""

# Rule: def only DEFINES a function — it does not run it.
# You must call it by name: hello()


# The first triple-quoted string inside a function = docstring.
# It documents what the function does. Not required, but a good habit.


def add_doc(a, b):
    """Return the sum of a and b."""
    return a + b


print(add_doc(2, 3))  # 5
print(add_doc.__doc__)  # Return the sum of a and b.


# Small functions can call each other — this is how real programs work.


def square(n):
    return n * n


def sum_squares(nums):
    total = 0
    for n in nums:
        total += square(n)  # calls square() for each item
    return total


print(sum_squares([1, 2, 3]))  # 1 + 4 + 9 = 14


# Function as value — you can store the returned value in a variable.


def add_return(num1, num2):
    return num1 + num2


result = add_return(2, 3)
print(result)  # 5


# More example
def say_hi(name):
    return f"Hi {name}"


hi = say_hi("Musaddiq")
print(hi)  # Hi Musaddiq


# Variable naming — same rules as variables:
"""
Start with letter or underscore ( _ )
No spaces in name
No special characters like +$@?! etc.
"""


# Written by Musaddiq Shah.
