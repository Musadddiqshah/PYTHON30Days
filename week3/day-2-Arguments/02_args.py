# *args → Variable Positional Arguments
# ---------------------------------------------------------
# The Problem: you don't know how many arguments will be passed.

# In this example you know two arguments will be passed:
def add(a, b):
    return a + b

print(add(3, 4))   # 7


# But what happens when you don't know how many arguments will be passed?
# In that situation we use *args:
def add(*nums):
    total = 0                    # adding sums of numbers
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5))        # 1 + 2 + 3 + 4 + 5 = 15


# *nums collects all positional arguments into a tuple.
# The name *nums is your choice — *args is just a convention name;
# you can give it any name you like.

# *args is a tuple — let's see:
def args(*nums):
    print(type(nums), nums)      # <class 'tuple'>
    return nums

print(args(3))
# Output: (3,)
# Remember: (3) is an int, but (3,) is a tuple because of the comma.

# Output from the type print:
# <class 'tuple'> (3,)


# *args with a regular parameter:
def greet(greeting, *names):
    for name in names:
        print(f"{greeting} {name}")

greet("Hello", "Musaddiq", "Yaseen", "Mutee", "Faheem")
# Output:
# Hello Musaddiq
# Hello Yaseen
# Hello Mutee
# Hello Faheem

# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------
"""
args is a tuple of arguments.
When you don't know how many arguments will be passed, use *args.
You can use any name — *nums, *names, anything.
*args packs all given positional arguments into a tuple.
"""

# Written by AM Musaddiq. Date: 13 Nov 2026
