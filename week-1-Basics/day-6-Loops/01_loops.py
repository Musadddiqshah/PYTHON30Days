# What is loops in Python.
# A Loops Repeats Code Many times.
# Instead of typing print("Hello") 100 times use loop like this for i in range(101):
#  print("Hello World")
# Two Loops In Python
# 1. for. Repeats for known Number.
# 2. while. Repeats untill conditions in True
# for Loops basic

for i in range(5):
    print(i)
# Thats print from 0 to 4. end is Not Encluded. Remember in Python count start from zero.

# for = Keyword of loop
# i = take it like variable
# range = keyword for numbers range
# : colon at the end.

# Another Example
for i in range(11):
    print("I Love Coding")
# Loop Variable name ( i ) is common but you can use any name like
for a in range(8):
    print("Hello")

for num in range(21):
    print(num)

for x in range(0,6):
    print(x)
# You can use any name

#  Indention Must be needed Like 4 spaces

for i in range(20):
    print("Hello")
#^^^ i mean these spaces.

for num in range(6):
    print("I am running 6 times") # this will run 6 times because that inside of loop.
# Outside of loop
print("I am running one time") # run one time because outside of loop
# While loop
# Run untill condition is True stop when condition is False.
i = 1
while i < 6:
    print(i)
    i = i + 1 # Very Very Important !! without this loop never end. i + i = 1mean add and assign 1 to i untill loop is finished. Output is

#
# 1
# 2
# 3
# 4
# 5
#   (6 is not encluded because that was last in number count start from 0 and last is not encluded.)

'''
Common Loop Errors

Error                     Why                            Fix
Forget colon :        SyntaxError                Add : colon at the end
Wrong Indent          IndentationError            4 spaces
Forget i+=1           Infinite Loop(never end)   Add i+=1 or i = i +1

'''
