# Type Casting
# Type casting is a way to convert one data type into another.
# Let's do it practically.

# --- Starting values ---
a = 'Musaddiq Shah'   # a is a string (str)
print(type(a))        # <class 'str'>   — because the value is text inside quotes

b = 12                # b is an integer (int)
print(type(b))        # <class 'int'>   — because 12 is a whole number

A = "12"              # looks like a number, but it is INSIDE quotes -> str
print(type(A))        # <class 'str'>

# print(A + 20)        # TypeError!  str + int is not allowed.


# --- Casting a string to an integer ---
num = int(A)          # convert "12" (str) into 12 (int)
print(type(num))      # <class 'int'>
print(10 + num)       # 22   — now we can do math

# --- Casting a string that is not numeric ---
# print(int("Musaddiq"))   # ValueError: invalid literal for int() with base 10
# print(int("12.5"))       # ValueError: "12.5" is not a whole number string
print(int(float("12.5")))  # 12   — must go through float first


# --- Other useful casts ---
print(int(7.9))        # 7         float -> int (truncates, does NOT round)
print(float(5))        # 5.0       int   -> float
print(str(50))         # '50'      int   -> str
print(str(50) + "50")  # 5050      (string concatenation, not math!)
print(bool(0))         # False
print(bool(1))         # True
print(bool(""))        # False     empty string is falsy
print(bool("hello"))   # True


## ---- Smart Summary ---- ##
"""
Type casting converts a value from one data type to another.
Common functions:
    int(x)    -> convert to integer
    float(x)  -> convert to float
    str(x)    -> convert to string
    bool(x)   -> convert to boolean

Important rules:
  - int("12")   works        (digits only) not on int('AM')
  - int("12.5") fails        (ValueError)
  - int(7.9)    -> 7         (truncates, does not round)
  - str(x) + str(y) concatenates, it does NOT add numbers
"""
