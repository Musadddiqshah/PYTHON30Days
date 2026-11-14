# Scope - where Variable live
# local variable - inside function - Global variable outside function

n = 20  # Global variable


def num():
    n = 10  # local variable
    print(n)


print(
    n
)  # return 20 beacuse that return value of global variable beacuse thats outside of function
# what happend when we call function
num()  # return 10 beacuse that print variable inside function.

# simple: Variable inside function is diffrent then Global variable


# we can't use variable inside function from outside function lets look
def check():
    x = 10
    print(x)


# let's  look
# print(x) # You will get this Error: NameError: name 'x' is not defined.  because we can't use variable from function. but we can use global variable from a function.
name = "Musaddiq"


def greet():
    print("Hello", name)  # can read a global variable


greet()
# But can't change a global variable
# count = 0 # that was a global variable
# def increment():
#     count += 2
# increment() # Output : UnboundLocalError: because we can't change a Global variable from inside of function.
# for changing a Global variable we use  global keyword inside function.
count = 0  # global varible


def increment():
    global count  # mean import global variable named count
    count += 2  # now we can change it


increment()  # Output: 2. On every run that add 2 to count variable
increment()  # add 2 more so 2 + 2 = 4
increment()  # add 2 more so 2 + 4 = 6
print(count)  # Output is: 6
