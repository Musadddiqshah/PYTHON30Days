# Funtion with parameter.
"""
Parameter let you pass value inside funtion
"""


def greet(name):
    print(f"Hello {name}")


greet("Musaddiq")  # that mean Hello Musaddiq
"""
name = parameter (variable in funtion).
"Musaddiq" = argument (value you pass in funtion).
"""


# Two parameters
def add(num1, num2):
    print(f"Result: {num1 + num2}")


add(2, 4)  # mean 2 + 4  So Output is Result: 6
add(7, 7)


# Three Paramenters
def introduce(name, age, city):
    print(f"{name} is {age} year old from {city}")


introduce("Musaddiq", 18, "Nushki")  # Output is: Musaddiq 18 year old from Nushki


#
# default parameter. Give a parameter a Default value. Used if caller does not proved it.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("Musaddiq")
greet("Musaddiq", "Hey")
greet("Yaseen", "How are you")


# Common Error: SyntaxError. Missing comma , on defining functions paramaterd and calling function parameters.
#
# keyword argument
def introduce(name, age, city):
    print(f"My name is {name}, i am {age} years old, from {city}")


introduce(
    "Musaddiq", 18, "Nushki"
)  # that give default given so out put is: My name is Musaddiq, i am 18 years old, from Nushki
# We can use this
introduce(
    name="Yaseen", age=16, city="Ahmed wal"
)  # output is: My name is Yaseen, i am 16 years old, from Ahmed wal
#
# we can do this Order does not matter
introduce(
    city="Quetta", age=20, name="Mutee"
)  # Output: My name is Mutee, i am 20 years old, from Quetta
# Good For Function with many parameter and Readablity


# Positional vs Argument
def greet(first, last):
    print(f"Hello {first} {last}")


greet("Musaddiq", "Shah")  # This is Positional
greet(first="AM", last="Musaddiq")  # this is keyword.
greet("Musaddiq", last="Shah")  # Mixed (Positional first)
# Rule: Positional argument must before keyword argument
