# ==========================================
#   Day 3 — Tasks (Operators) — SOLVED
# ==========================================

# ---------- Q1. Arithmetic ----------
a = 20
b = 6
print("Q1:")
print("sum       :", a + b)    # 26
print("difference:", a - b)    # 14
print("product   :", a * b)    # 120
print("division  :", a / b)    # 3.33
print("floor div :", a // b)   # 3
print("modulo    :", a % b)    # 2
print("power     :", a ** b)   # 64000000


# ---------- Q2. Predict the output ----------
# print(7 // 2)   -> 3
# print(7 % 2)    -> 1
# print(2 ** 3)   -> 8
# print(10 / 4)   -> 2.5
print("\nQ2:") # Dont think about /n tha Mean New Line 
print(7 // 2)
print(7 % 2)
print(2 ** 3)
print(10 / 4)


# ---------- Q3. Comparison ----------
x = 15
y = 25
print("\nQ3:")
print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= y)   # False
print(x <= y)   # True


# ---------- Q4. Assignment operators ----------
n = 5
print("\nQ4:")
n += 3
print(n)        # 8
n *= 2
print(n)        # 16
n -= 4
print(n)        # 12
n //= 2
print(n)        # 6


# ---------- Q5. Logical operators ----------
is_raining = True
have_umbrella = False
print("\nQ5:")
print(is_raining and have_umbrella)  # False — both must be True
print(is_raining or have_umbrella)   # True  — at least one is True
print(not is_raining)                # False — opposite of True


# ---------- Q6. Membership ----------
word = "python"
print("\nQ6:")
print("p" in word)       # True
print("P" in word)       # False — Python is case-sensitive
print("th" in word)      # True
print("z" not in word)   # True
# "P" is uppercase, "p" is lowercase.
# Python treats them as different characters.


# ---------- Q7. Identity — careful! ----------
a = 100
b = 100
print("\nQ7:")
print(a == b)   # True  — same value (correct way to compare)
print(a is b)   # True in file, False in interpreter (Python cache trick)

c = 1000
d = 1000
print(c == d)   # True  — same value
print(c is d)   # False (usually) — different objects

# Use == to compare values.
# Use is only for None.
