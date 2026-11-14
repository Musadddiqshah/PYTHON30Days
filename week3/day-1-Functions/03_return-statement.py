# return statement. Return sends a value back to caller.


def add(num1, num2):
    return num1 + num2


result = add(3, 3)
print(result)  # Output is 6  ← FIXED (was wrongly saying None)


# Without return function Gives None like this
def add_no_return(num1, num2):
    num1 + num2  # no return


result = add_no_return(3, 3)
print(result)  # Output: None


# Why return matters
# table
"""
print()              |   return
---------------------|----------------------------------
show on screen       | send values back
For humans           | For further use
can't store result   | can store, add, compare
"""


def square(n):
    return n * n


print(square(5))  # 25
x = square(5) + square(5)  # 25 + 25
print(x)  # 50

# Rule: if a function should give back a value, use return


# print() vs return
def add_print(num1, num2):
    print(num1 + num2)


def add_return(num1, num2):
    return num1 + num2


add_print(3, 4)  # prints 7, but result is None
print(add_return(4, 5))  # prints 9


# More Examples of return.
def check_age(age):
    if age >= 18:
        return "Adults"
    elif age <= 0:
        return "Enter valid age"
    else:
        return "Minor"


print(check_age(18))  # Adults
print(check_age(0))  # Enter valid age
print(check_age(17))  # Minor


# A function can return several values as a TUPLE.
def min_max(nums):
    return min(nums), max(nums)  # returns a tuple


lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)  # 1 5

# Or keep the tuple:
result = min_max([3, 1, 4, 1, 5])
print(result)  # (1, 5)
print(result[0])  # 1


# return exits the function immediately — nothing after it runs.
def check(x):
    if x < 0:
        return "negative"  # exits here
    return "positive"  # only runs if x >= 0


print(check(-5))  # negative
print(check(5))  # positive


# Proof that return stops execution:
def test():
    print("A")
    return "done"  # function ends here
    print("B")  # never runs (unreachable)


print(test())  # prints A, returns "done"


# A function WITHOUT return → returns None automatically.
def greet(name):
    print(f"Hello {name}")
    # no return


result = greet("Ali")  # prints Hello Ali
print(result)  # None
