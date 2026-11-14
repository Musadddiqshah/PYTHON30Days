number1 = 10
number2 = 5

print("Sum      :", number1 + number2)   # 15
print("Subtract :", number1 - number2)   # 5
print("Multiply :", number1 * number2)   # 50
print("Divide   :", number1 / number2)   # 2.0  (always a float)
print("Floor div:", number1 // number2)  # 2    (integer result)
print("Modulo   :", number1 % number2)   # 0    (remainder)
print("Power    :", number1 ** number2)  # 100000

# --- Type error example ---
name = "50"        # this is a STRING, not an integer
number3 = 50       # this is an INTEGER
# print(name + number3)   # TypeError: can only concatenate str (not "int") to str
print(type(name))  # <class 'str'>  — quotes make it a string even if it looks like a number
print(type(number3))  # <class 'int'>

# --- String repetition ---
print("Mutee " * 5)  # Mutee Mutee Mutee Mutee Mutee

# --- Floats ---
print(7.9 * 7.9)       # 62.41
print(type(6.7))       # <class 'float'>

# --- Bonus ---
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
