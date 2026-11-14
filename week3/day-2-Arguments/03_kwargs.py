# **kwargs = "keyword arguments" → collects named args into a DICT

def test(**kwargs):
    for key, value in kwargs.items():   # .items() gives (key, value) pairs
        print(f"{key}: {value}")

test(name="Musaddiq", age=18, marks=379)
# Output:
# name: Musaddiq
# age: 18
# marks: 379


# Proof it's a dict:
def show(**kwargs):
    print(kwargs, type(kwargs))

show(a=1, b=2)   # {'a': 1, 'b': 2} <class 'dict'>


# Compare with *args (tuple):
def show2(*args):
    print(args, type(args))

show2("a", "b")  # ('a', 'b') <class 'tuple'>


# Both together (order matters: *args first):
def both(*args, **kwargs):
    print("*args   =", args)
    print("**kwargs =", kwargs)

both(1, 2, 3, name="Musaddiq", age=19)
# *args    = (1, 2, 3)
# **kwargs = {'name': 'Musaddiq', 'age': 19}


# ---------------------------------------------------------
# Real Examples of **kwargs
# ---------------------------------------------------------

# Example 1 — User Profile
def user_profile(**user):
    # NOTE: use single quotes inside the f-string, not the same double quotes,
    # otherwise it raises a SyntaxError on Python < 3.12.
    print(f"\nCreating profile for {user['name']}")
    for key, value in user.items():
        print(f"  {key}: {value}")

user_profile(name="Musaddiq", age=18, city="Nushki")
# Output:
# Creating profile for Musaddiq
#   name: Musaddiq
#   age: 18
#   city: Nushki


# Example 2 — Sending data to an API (very common!)
def send_request(url, **params):
    print(f"\nGET {url}")
    for key, value in params.items():
        print(f"  ?{key}={value}")

send_request("com.google", q="python", page=2, limit=10)


# ---------------------------------------------------------
# Rules & Gotchas
# ---------------------------------------------------------
# def f(**kwargs, *args):  # ❌ SyntaxError
# def f(*args, **kwargs):  # ✅ correct order

# f(**{1: "a"})   # ❌ TypeError — keyword keys must be strings
# f(**{"a": 1})   # ✅


# ---------------------------------------------------------
# One-line summary
# ---------------------------------------------------------
"""
**kwargs collects any number of named arguments into a dictionary.
kwargs is just a convention name — you can call it **options, **data, or anything.
"""

"""
*args    → tuple → "give me any number of unnamed things"
**kwargs → dict  → "give me any number of named things"
"""
# Combining Full
print("Full")
def full(a,b=3,*args,c=2,**kwargs):
    print(a,b,args,c,kwargs)
full(1,2,3,4,c=4,d=6)
print("Focus on Tuple are *args and Dicts are *kwargs")

#### Combining All  #####
# Order matters Full Signature
#   def function_name(required,default=value,*args,**kwargs):
#* Example:
print("\nCombinig Everything")
def everything(a,b=6,*args,**kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"*args: {args}")
    print(f"**kwargs: {kwargs}")
# Calling func
everything(1)
everything(1,4)
everything(1,4,13,14,15,16,name="Musaddiq",age=19)
everything(1,name="Yaseen")


# This is Advance But Rarely needed at Beginner Level -- But Good To Know


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
# Why These matters. Real Python users use It constantly.
# •  Defaults. Clean Simple Common cases
# • *args variable number of items.
# • Flexible Option.
"""
when you read a Python Library you will see them everywhere Understanding Them makes you better Python reader
"""




