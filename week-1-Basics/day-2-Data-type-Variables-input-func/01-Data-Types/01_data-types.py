## -:-:  Values & Data Types :-:- ##

'''
Values are the basic building blocks of almost every programming language.
You have already seen values like 'Hello World!', 12, and 6.1.
These values belong to different data types:
    - 'Hello World!' is a string   (str)
    - 12             is an integer (int)
    - 6.1            is a float
'''

# string  (str)   -> text, sentences, names, etc.        e.g. "Hello", 'AM'
# integer (int)   -> whole numbers                       e.g. 100, 6, 2, -7
# float   (float) -> decimal / floating-point numbers    e.g. 8.2, 77.1, -7.2
# boolean (bool)  -> True or False, used in conditions   (explained later)
# NoneType(None)  -> represents "no value"

name = "AM Musaddiq"   # str  -> because it is inside quotes " "
print(name)            # Output: AM Musaddiq

age = 18               # int  -> a whole number
print(age)             # Output: 18

height = 5.6           # float -> has a decimal point
print(height)          # Output: 5.6

is_student = True      # bool -> True or False
print(is_student)      # Output: True

# Empty value
result = None          # NoneType -> means "nothing here yet"
print(result)          # Output: None


# How to find the type of a value:
# Python provides a built-in function called `type()`.

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(result))      # <class 'NoneType'>


##--- Summary ---##
"""
Data types describe what kind of value something is.
Python automatically infers the type from the value you assign —
you don't have to declare it yourself.
"""
