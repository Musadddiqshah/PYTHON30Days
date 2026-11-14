# If you get bored and don't understand this, please don't ignore it.
# This is an important chapter. Let's learn it in an easy way.

# What are default arguments?
# A default argument is a "parameter" that already has a value set.
# If the caller does not provide it, Python uses the default value.

# Simple explanation:
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")

greet(name="Musaddiq", greeting="Hello")
# We gave it a default greeting "Hello", so the output is: Hello Musaddiq.
# But we can also call it without passing the greeting, because a default is already set. Look here:
greet("Musaddiq")
# Now Python uses our default argument. Output: Hello Musaddiq

# We can also pass the greeting like we learned before:
greet(name="Yaseen", greeting="Hi")
# Output: Hi Yaseen

# More examples:
# print() uses a default argument for a new line. That's why:
print("Hi")
print("Musaddiq")
# This prints Musaddiq on a new line because it's like print("Musaddiq", end="\n").
# end="\n" means "new line". What happens if we change it to a space?
print("Hi", end=" ")   # Don't create a new line; use a space instead.
print("Musaddiq")      # Output: Hi Musaddiq

# We can do this too:
print("Hi", end=",")
print("Musaddiq")      # Output: Hi,Musaddiq

# Another use:
for i in range(1, 6):
    print(i, end=" ")  # Output: 1 2 3 4 5
print("I hope you understand")

# I hope you understand now.
# So default arguments are values Python already provides.
# If you don't pass them, Python uses them automatically.

# Rules for default arguments:
def greet(name, greet="Hello"):   # default arguments must come last
    print(f"{greet} {name}")

# greet("Musaddiq", "Hi")   # works

# def greet(greet="Hello", name):
#     print(f"{greet} {name}")
# greet("Hello", "Musaddiq")
# This raises SyntaxError because default arguments must come last.

# More examples:
print("Musaddiq", end=" ")   # valid, because we used the default argument at the end
print("Shah")                # Output: Musaddiq Shah

# Invalid:
# print(end="", "Musaddiq")  # Error: argument must be at the end, not first

# Defaults are evaluated only once.
# This is a famous trap in Python:
def add_items(item, items=[]):
    items.append(item)
    return items

# We have a function with two parameters: item and items (an empty list).
print(add_items("A"))   # Output: ['A']
print(add_items("B"))   # Output: ['A', 'B']
# Why didn't it create a new list? Because the default list is created only once,
# so every call keeps adding to the same list.

# The fix: use None as the default.
# If you want a new list on every call, use None as the default, like this:
def add_items(item, items=None):
    if items is None:
        items = []   # now we create a new one
    items.append(item)
    return items

print(add_items("A"))
print(add_items("B"))

# Rule: Don't use mutable objects like [], {}, set() as defaults. Use None instead.

# Examples of using defaults:
# 1. Power
def power(base, exponent):
    return base ** exponent

print(power(2, 3))    # 2 to the power 3 = 8
print(power(2, 10))   # 1024

# 2. Connect message
def connect(host="127.0.0.1", port=8080):
    print(f"Connected to {host}:{port}")

connect()
connect(port=3333)


# Real World Uses
# print()  uses sep, and end
print(1,2,3,sep="-") # sep="-" mean seprate by - we use , insted Output is 1-2-3
print("Musaddiq",end=" ") # Dont creat a new line just use space on end
print("Shah") # Output is Musaddiq Shah
# dict.get uses default
student = {"name":"Musaddiq","age":18,"marks":481}
print(student.get("name"))
print(student.get("rank","Not Found")) # return Not found if no key name rank in student. We can use anything Like:
print(student.get("rank","No Key name accociated by rank")) # Output is: No Key name accociated by rank


# All code written by AM Musaddiq. Date: 13 Nov 2026
