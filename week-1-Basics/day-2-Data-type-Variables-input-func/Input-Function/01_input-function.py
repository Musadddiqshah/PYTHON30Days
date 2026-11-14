# -------  Input Function  ------- #

# Basically, input() is a way to take input from the user.
# Let's do it practically.

name = input("Enter your name: ")   # takes input from user
print("Hello,", name)               # prints what user typed


# --- Input always returns a string ---
age = input("Enter your age: ")
print(age)
print(type(age))   # <class 'str'>  — even if user typed 18


# --- So we must cast it if we need a number ---
age = int(input("Enter your age: "))   # now it is an integer
print(age + 1)                          # works like math
print(type(age))                        # <class 'int'>


# --- Example: wrong vs right ---
# number = input("Enter a number: ")     # str
# print(number + 5)                       # ERROR: str + int
number = int(input("Enter a number: "))  # fixed
print(number + 5)                        # works


## ---- Smart Summary ---- ##
"""
input() is a function that takes input from the user.
It ALWAYS returns a string (str) — even if the user types numbers.
So before using it as a number, we must cast it:
    int(input(...))    -> whole number
    float(input(...))  -> decimal number
"""
