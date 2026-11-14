# Task1: Print Your Name
# create a Variable Called name that contain you name then print it
name = "AM Musaddiq"
print(name)
# Task2: Add Two numbers
# create a variabls called num1 and num2 then print there sum
num1 = 10
num2 = 50
print(num1 + num2)

# Task3: Create a three diffrent variables then print there type.
a = "AM"
b = 10
c = 4.7
print(type(a))
print(type(b))
print(type(c))

# Task4: You have a number = "50" convert  Variable to integer Then add 25 to it Answer expacted = 75
number = "50"
print(int(number) + 25)
# print(number + 25) # Not work because number variable is str not int after convert then we can add it.
# Tasks:5 Convert int to string num = 99
# then join to Apple Expected sectentce = 99 apples
num = 99 # we have a integer variable.
print("We Have " + str(num) + " apples") # We are convert int to str then Join to str then Print

# task:6  Convert float to int  we Have price = 99.99
# convert to int and Print also Say Wy Answere is 99 wy Not 100
price = 99.99
print(int(price)) # we will Get a Answere 99 becsuce afterCnvert to int integer ignore all digits after  dot (.).

# Task:7 Fix This Code
# # Look at this code:
# ```python
# age = "18"
# print(age + 2)
age = "18"
print(int(age) + 2) # Now thats work because we converted the age to int then sum it to Num

#      Extra Hard   Task
#  Take input From User Name and Age Then print it Like this Your Name is [name] your age is [age]
name = input("Enter Your Name: ")
age = int(input("Enter your age: ")) # We use int here because are Get Input int not str
print("Your Name is " + name + " Your age is", age)
