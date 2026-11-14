#   Operators

# After Hello World, the next step is operators.
# Operators are special symbols used for computation
# like + (addition), - (subtraction), * (multiplication), and / (division).

#   Types of Operators
# There are SIX main types of operators in Python:

# 1. Arithmetic  :  +, -, *, /, //, %, **
# 2. Comparison  :  ==, !=, >, <, >=, <=
# 3. Assignment  :  =, +=, -=, *=, /=, //=, %=, **=
# 4. Logical     :  and, or, not
# 5. Membership  :  in, not in
# 6. Identity    :  is, is not


# ---------- 1. Arithmetic Operators  ----------
# Do math.
a = 10
b = 3
print("     Arithmetic Operators: +,-,*,/,//,%,**")
print(a + b)    # 13   Addition
print(a - b)    # 7    Subtraction
print(a * b)    # 30   Multiplication
print(a / b)    # 3.33 Division (always float)
print(a // b)   # 3    Floor Division (whole part)
print(a % b)    # 1    Modulo (remainder)
print(a ** b)   # 1000 Power (10 to the power 3)


# ---------- 2. Comparison Operators  ----------
# Compare two values. Answer is always True or False.
a = 10
b = 3
print("        Comparison Operators: ==, !=, >, <, >=, <=")
print(a == b)   # False  (a is equal to b?)
print(a != b)   # True   (a is not equal to b?)
print(a > b)    # True   (a is greater than b?)
print(a < b)    # False  (a is less than b?)
print(a >= b)   # True   (a is greater or equal to b?)
print(a <= b)   # False  (a is less or equal to b?)


# ---------- 3. Assignment Operators  ----------
print("  Assignment Operators: +=,-=,*=,/=,//=,**=,%=")
x = 10
x += 1        # x = x + 1  -> 11
print(x)      # 11
x -= 2        # x = x - 2  -> 9
print(x)      # 9
x *= 2        # x = x * 2  -> 18
print(x)      # 18
x /= 3        # x = x / 3  -> 6.0  (always float)
print(x)      # 6.0
x //= 3       # x = x // 3 -> 2.0  (whole part, but float because x was float)
print(x)      # 2.0

n = 10
n %= 3        # n = n % 3  -> 1
print(n)      # 1

n1 = 10
n1 **= 3      # n1 = n1 ** 3 -> 1000
print(n1)     # 1000


# ---------- 4. Logical Operators  ----------
# and : both must be True
# or  : at least one must be True
# not : opposite
print("     Logical Operators: and, or, not")
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
print(not False)        # True


# ---------- 5. Membership Operators  ----------
# Check if something is inside a string or list.
print("     Membership Operators: in, not in")
first_name = "AM"
print("A" in first_name)      # True   (A is in "AM")
print("a" in first_name)      # False  (Python is case-sensitive)
print(" A" in first_name)     # False  (we added a space, not in "AM")
print("a" not in first_name)  # True   (a is not in "AM")


# ---------- 6. Identity Operators  ----------
# 'is' checks if two names point to the SAME object — NOT the same value.
# For comparing values, always use ==.
print("     Identity Operators: is, is not")
price1 = 50
price2 = 50
print(price1 == price2)       # True   (same value — this is the right check)
print(price1 is price2)       # True in a file, False in interpreter (Python cache trick)
print(price1 is not price2)   # the opposite of above

# Rule: use == for values, use is only for None.
