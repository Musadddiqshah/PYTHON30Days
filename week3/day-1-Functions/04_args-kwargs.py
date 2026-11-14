# *args — Variable number of arguments
# Use when you don't know how many arguments will be passed.


def add(*nums):
    total = 0
    for n in nums:
        total = total + n
    return total


print(add(1, 2))  # 3
print(add(1, 2, 3, 4, 5))  # 15
print(add())  # 0

# *nums collects all arguments into a TUPLE.
# Name is a convention (args), you can name it anything:
#   def add(*nums), def add(*numbers), def add(*items)  ← all valid


# **kwargs — keyword arguments as DICT
# Use when you don't know how many named arguments will be passed.


def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


show_info(name="Musaddiq", age=19, city="Nushki")
# name: Musaddiq
# age: 19
# city: Nushki

# **details collects named arguments into a DICT.
# Name is convention (kwargs), you can name it anything:
#   def show_info(**details), def show_info(**data), def show_info(**info)


# You can use both in the same function.
# Rule: *args comes BEFORE **kwargs.
def show(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


show(1, 2, 3, name="Ali", age=18)
# args: (1, 2, 3)
# kwargs: {'name': 'Ali', 'age': 18}


# Don't worry about these — just know they exist.
# You'll use them when building flexible functions later.
